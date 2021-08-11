import random

from pygame import PixelArray, draw, Surface
from typing import Dict
from utility import Position, Velocity, CenterOfMass
from math import pi


class Particle:
    def __init__(self,
                 pos: Position,
                 velocity,
                 radius: int = random.randint(1, 10),
                 density: int = random.randint(1, 100)):
        self.id: int = 0
        self.pos: Position = pos
        self.velocity: Velocity = velocity
        self.radius: int = radius
        self.density: float = density
        self.surface_area: float = self._calc_surface_area()
        self.mass: float = self._calc_mass()
        self.momentum: Velocity = self._calc_momentum()

    def _calc_surface_area(self) -> float:
        return pi * self.radius ** 2

    def _calc_mass(self) -> float:
        return self.density * self.surface_area

    def _calc_momentum(self) -> Velocity:
        output: Velocity = self.velocity
        output.magnitude = output.magnitude * self.mass
        return output

    def draw(self, surface: Surface):
        draw.circle(surface=surface,
                    center=(self.pos.x, self.pos.y),
                    radius=self.radius,
                    width=int(1 + round(self.density / 10, 1)),
                    color=(255, 0, 255))

    def draw_velocity(self, surface: Surface):
        end_location = (self.velocity.direction.x - self.pos.x,
                        self.velocity.direction.y - self.pos.y)
        draw.line(surface=surface,
                  start_pos=(self.pos.x, self.pos.y),
                  end_pos=end_location,
                  width=self.velocity.magnitude,
                  color=(0, 255, 0))

    def update(self, **kwargs):
        self.__dict__.update(kwargs)


class ParticleCollection:
    def __init__(self):
        """Collection of Particles"""
        self.particle_collection: Dict[int: Particle] = {}  # Contains the particle ID and the particle
        self.center_of_mass = CenterOfMass()

        self.count = 0  # Used in color cycling. Can be removed later.

    def add_particle(self, pos: Position, velocity: Velocity):
        new_particle: Particle = Particle(pos=pos, velocity=velocity)
        new_particle.id = len(self.particle_collection)
        self.particle_collection[new_particle.id] = new_particle
        self._update_center_of_mass(new_particle)

    def _update_center_of_mass(self, new_particle: Particle):
        self.center_of_mass.update(new_pos=new_particle.pos,
                                   new_mass=new_particle.mass)

    def update_single_particle(self, particle):
        self.particle_collection[particle.id] = particle

    def draw_particles(self, surface: Surface):
        for each_particle in self.particle_collection.values():
            each_particle.draw(surface)

    def particle_centers_to_pixel_array(self, pixel_array: PixelArray):
        for each_particle in self.particle_collection.values():
            pixel_array[each_particle.x_pos, each_particle.y_pos] = each_particle.color

    def draw_center_of_mass(self, surface: Surface):
        self.count += 4
        if self.count > 255:
            self.count = 0

        draw.circle(surface=surface,
                    center=(self.center_of_mass.pos.x, self.center_of_mass.pos.y),
                    color=(255, 0 + self.count, 255 - self.count),
                    radius=self.center_of_mass.eq_mass)



