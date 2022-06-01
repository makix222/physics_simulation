import random
from pygame import Surface
from particles import ParticleCollection
from utility import Position, Vector


class ParticleNoise:
    def __init__(self, surface: Surface):
        self.surface = surface
        self.size = surface.get_size()
        self.x = self.size[0]
        self.y = self.size[1]

        self.particle_collection = ParticleCollection()

    def create_random_particle(self):
        random_x = random.randint(0, self.x - 1)
        random_y = random.randint(0, self.y - 1)
        random_pos = Position(x_pos=random_x,
                              y_pos=random_y)
        random_velocity = Vector(target=Position((random.randint(0, self.x - 1), random.randint(0, self.y - 1))))
        self.particle_collection.add_particle(random_pos, random_velocity)

    def draw_particles(self):
        self.particle_collection.draw_particles(self.surface)

