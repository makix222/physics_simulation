from math import sqrt, atan, degrees
import numpy as np


class Position:
    def __init__(self, pos: tuple = (0, 0), x_pos=0, y_pos=0):
        if pos != (0, 0):
            self.x = pos[0]
            self.y = pos[1]
        else:
            self.x = x_pos
            self.y = y_pos

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"


def midway_point(start: Position, end: Position, scale=1) -> Position:
    output = Position()
    output.x = start.x - int((start.x - end.x) / (1 + scale))
    output.y = start.y - int((start.y - end.y) / (1 + scale))
    return output


def bearing(start: Position, end: Position) -> float:
    """Returns a degree from 0-360 where 0 is on the top of the screen"""
    return degrees(atan((end.x - start.x) / (end.y - start.y)))


def point_from_bearing(start_pos: Position, bearing_angle: float, length: int = 1) -> Position:
    bearing_rad = np.radians(bearing_angle)
    cos = np.cos(bearing_rad)
    sin = np.sin(bearing_rad)
    return Position(x_pos=int(cos * length) + start_pos.x,
                    y_pos=int(sin * length) + start_pos.y)


def rotation_from_point(point_to_rotate: Position, center_of_rotation: Position, rotation_angle: float) -> Position:
    rotation_rad = np.radians(rotation_angle)
    cos = np.cos(rotation_rad)
    sin = np.sin(rotation_rad)
    rotation_matrix = np.array(((cos, -sin), (sin, cos)))
    new_point = np.array([[point_to_rotate.x - center_of_rotation.x], [point_to_rotate.y - center_of_rotation.y]])
    delta_rotation = rotation_matrix * new_point
    final_pos = Position(x_pos=int(delta_rotation[0][1] + center_of_rotation.x),
                         y_pos=int(delta_rotation[1][0] + center_of_rotation.y))
    return final_pos


def generate_normal_point(start_pos: Position, bearing_angle: float, length: int = 1) -> Position:
    point_ahead = point_from_bearing(start_pos, bearing_angle, length)

    if length > 0:
        rotation_angle = 90
    else:
        rotation_angle = -90
    normal_point = rotation_from_point(point_to_rotate=point_ahead,
                                       center_of_rotation=start_pos,
                                       rotation_angle=rotation_angle)
    return normal_point


def distance(start: Position, end: Position) -> float:
    return sqrt((start.x - end.x) ** 2 + (start.y - end.y) ** 2)


class Velocity:
    def __init__(self, start: Position = Position(), target: Position = Position(), reverse=False):
        self.magnitude = distance(start, target)
        self.direction = Position(x_pos=target.x - start.x,
                                  y_pos=target.y - start.y)
        if reverse:
            self.direction = Position(x_pos=-(target.x - start.x),
                                      y_pos=-(target.y - start.y))

    def __str__(self):
        return f"Magnitude: {self.magnitude}, direction: {self.direction}"


class CenterOfMass:
    def __init__(self):
        self.pos = Position()
        self.eq_mass = 0

    def update(self, new_pos: Position, new_mass):
        if not self.eq_mass:
            self.pos = new_pos
            self.eq_mass = new_mass
        else:
            mass_diff = self.eq_mass / new_mass
            self.pos = midway_point(start=self.pos,
                                    end=new_pos,
                                    scale=mass_diff)
            self.eq_mass += new_mass
