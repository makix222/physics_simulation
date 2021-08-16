from pygame import draw, Surface, Rect
from typing import Dict
from utility import Position, Velocity, CenterOfMass
from math import pi


class Particle:
    def __init__(self,
                 pos: Position = Position(),
                 velocity: Velocity = Velocity(),
                 radius: int = 1,
                 density: int = 1):
        self.id: int = 0

        self.pos: Position = pos
        self._velocity: Velocity = velocity
        self._radius: int = radius
        self._density: float = density

        self.surface_area: float = self._calc_surface_area()
        self.mass: float = self._calc_mass()
        self.momentum: Velocity = self._calc_momentum()

        self.color = (0, 255, 0)

    def __str__(self):
        return f"Particle({self.pos}, {self.velocity}, {self.radius}, {self.density})"

    def __repr__(self):
        return f"{self.pos}"

    def _calc_surface_area(self) -> float:
        return pi * self._radius ** 2

    def _calc_mass(self) -> float:
        return self._density * self.surface_area

    def _calc_momentum(self) -> Velocity:
        output: Velocity = self._velocity
        output.magnitude = output.magnitude * self.mass
        return output

    def draw(self, surface: Surface):
        draw.circle(surface=surface,
                    center=(self.pos.x, self.pos.y),
                    radius=self._radius,
                    width=int(1 + round(self._density / 10, 1)),
                    color=self.color)

    def draw_velocity(self, surface: Surface):
        end_location = (self._velocity.direction.x + self.pos.x,
                        self._velocity.direction.y + self.pos.y)
        draw.line(surface=surface,
                  start_pos=(self.pos.x, self.pos.y),
                  end_pos=end_location,
                  width=1,
                  color=(255, 255, 0))
        draw.circle(surface=surface,
                    center=end_location,
                    color=(0, 255, 255),
                    radius=self._radius - 1)

    def calculate_new_position(self, time_step: float):
        x_add = int(self.velocity.direction.x / time_step)
        y_add = int(self.velocity.direction.y / time_step)
        new_pos = Position(x_pos=self.pos.x + x_add,
                           y_pos=self.pos.y + y_add)
        return new_pos

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, new_radius: int):
        self._radius = new_radius
        self._calc_surface_area()
        self._calc_mass()
        self._calc_momentum()

    @property
    def density(self):
        return self._density

    @density.setter
    def density(self, new_density: int):
        self._density = new_density
        self._calc_mass()
        self._calc_momentum()

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, new_velocity: Velocity):
        self._velocity = new_velocity
        self._calc_momentum()


class ParticleCollection:
    def __init__(self):
        """Collection of Particles"""
        self.particle_collection: Dict[int: Particle] = {}  # Contains the particle ID and the particle
        self.center_of_mass = CenterOfMass()

        self.count = 0  # Used in color cycling. Can be removed later.

    def add_particle(self,
                     pos: Position,
                     velocity: Velocity,
                     radius: int = 1,
                     density: int = 1):
        new_particle: Particle = Particle(pos=pos,
                                          velocity=velocity,
                                          radius=radius,
                                          density=density)
        new_particle.id = len(self.particle_collection)
        self.particle_collection[new_particle.id] = new_particle
        self._update_center_of_mass(new_particle)

    def _update_center_of_mass(self, new_particle: Particle):
        # ToDo: why does center of mass not update correctly with a single particle?
        self.center_of_mass.update(new_pos=new_particle.pos,
                                   new_mass=new_particle.mass)

    def update_particle_position(self, particle_id, particle):
        self.particle_collection[particle_id] = particle
        self._update_center_of_mass(particle)

    def draw_particles(self, surface: Surface):
        for each_particle in self.particle_collection.values():
            each_particle.draw(surface)

    def draw_center_of_mass(self, surface: Surface):
        self.count += 4
        if self.count > 255:
            self.count = 0

        draw.circle(surface=surface,
                    center=(self.center_of_mass.pos.x, self.center_of_mass.pos.y),
                    color=(255, 0 + self.count, 255 - self.count),
                    radius=1)



