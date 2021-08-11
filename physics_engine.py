from pygame import Surface
from particles import ParticleCollection, Particle
from utility import Position, Velocity
import random


class WorldMechanics:
    def __init__(self, surface: Surface):
        self.surface = surface
        self.display_size = surface.get_size()

        self.particle_collection = ParticleCollection()
        self.creating_particle = False

        self.gravity_constant = 2

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




