from pygame import Surface, Rect, draw, error
from particles import ParticleCollection, Particle
from utility import Position, Velocity
import random
from typing import List


class WorldMechanics:
    def __init__(self, surface: Surface):
        self.surface = surface
        self.display_size = surface.get_size()

        self.particle_collection = ParticleCollection()
        self.creating_particle = False

        self.gravity_constant = 2
        self.walls = Walls(surface=surface,
                           x_world_size=self.display_size[0],
                           y_world_size=self.display_size[1])

    def add_particle(self, pos: Position, velocity: Velocity):
        self.particle_collection.add_particle(pos=pos,
                                              velocity=velocity,
                                              radius=random.randint(1, 10),
                                              density=random.randint(1, 100))

    def update(self, time_step):
        for particle in self.particle_collection.particle_collection.values():
            new_particle = Particle(pos=particle.calculate_new_position(time_step=time_step),
                                    velocity=particle.velocity,
                                    radius=particle.radius,
                                    density=particle.density)
            new_particle.id = particle.id
            self.particle_collection.update_particle_position(particle_id=new_particle.id,
                                                              particle=new_particle)

        self.draw()

    def draw(self):
        self.particle_collection.draw_particles(self.surface)
        self.particle_collection.draw_center_of_mass(self.surface)
        self.walls.draw_world_walls()


class Walls:
    def __init__(self, surface: Surface, x_world_size, y_world_size):
        self.surface = surface
        self.wall_thickness = 2
        self.world_x = x_world_size - self.wall_thickness
        self.world_y = y_world_size - self.wall_thickness
        self.walls: List[Wall] = self._generate_borders()

    def _generate_borders(self) -> list:
        top_left = Position(x_pos=self.wall_thickness - 1, y_pos=self.wall_thickness - 1)
        top_right = Position(x_pos=self.world_x, y_pos=self.wall_thickness - 1)
        btm_left = Position(x_pos=self.wall_thickness - 1, y_pos=self.world_y)
        btm_right = Position(x_pos=self.world_x, y_pos=self.world_y)
        return [Wall(surface=self.surface, start=top_left, end=top_right, wall_thickness=self.wall_thickness),
                Wall(surface=self.surface, start=top_left, end=btm_left, wall_thickness=self.wall_thickness),
                Wall(surface=self.surface, start=btm_left, end=btm_right, wall_thickness=self.wall_thickness),
                Wall(surface=self.surface, start=top_right, end=btm_right, wall_thickness=self.wall_thickness),]

    def draw_world_walls(self):
        for each_wall in self.walls:
            each_wall.draw_wall()

    def custom_walls(self):
        pass


class Wall:
    def __init__(self, surface: Surface, start: Position, end: Position, wall_thickness: int = 1):
        """Currently just Horizontal or Vertical walls."""
        self.surface = surface
        self.start = (start.x, start.y)
        if start.x == end.x:
            self.end = (end.x, end.y + wall_thickness)
        elif start.y == end.y:
            self.end = (end.x + wall_thickness, end.y)
        else:
            self.end = (end.x, end.y)
        self.wall_color = (0, 0, 255)
        self.rect: Rect = Rect(self.start, self.end)
        self.thickness = wall_thickness

    def draw_wall(self):
        draw.rect(surface=self.surface,
                  rect=self.rect,
                  color=self.wall_color,
                  width=self.thickness)

    def __repr__(self):
        return f"start: {self.start} end: {self.end}"
