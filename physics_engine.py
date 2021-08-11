from pygame import Surface
from particles import ParticleCollection
from utility import Position, Velocity


class WorldMechanics:
    def __init__(self, surface: Surface):
        self.surface = surface
        self.display_size = surface.get_size()

        self.particle_collection = ParticleCollection()
        self.creating_particle = False

        self.gravity_constant = 2

    def add_particle(self, pos: Position, velocity: Velocity):
        self.particle_collection.add_particle(pos=pos, velocity=velocity)

    def update(self):
        self.particle_collection.draw_particles(self.surface)




