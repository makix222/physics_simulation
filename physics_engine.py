from pygame import Surface
from particles import ParticleCollection
from utility import Velocity


class WorldMechanics:
    def __init__(self, surface: Surface):
        self.surface = surface
        self.display_size = surface.get_size()

        self.particle_collection = ParticleCollection()
        self.creating_particle = False

        self.gravity_constant = 2

    def update_mouse_input(self, mouse_pressed, mouse_pos):
        if mouse_pressed and not self.creating_particle:
            self.particle_collection.add_particle(pos, )





