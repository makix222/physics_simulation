from math import sqrt


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


def midway_point(start: Position, end: Position, scale) -> Position:
    output = Position()
    output.x = start.x - int((start.x - end.x) / (1 + scale))
    output.y = start.y - int((start.y - end.y) / (1 + scale))
    return output


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



