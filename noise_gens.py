import random
from pygame import PixelArray
from pygame import Surface
from particles import ParticleCollection


class ParticleNoise:
    def __init__(self, surface: Surface):
        self.surface = surface
        self.size = surface.get_size()
        self.pixel_array = self._generate_pixel_array()
        self.x = self.size[0]
        self.y = self.size[1]

        self.particle_collection = ParticleCollection()

    def _generate_pixel_array(self) -> PixelArray:
        return PixelArray(self.surface)

    def create_random_particle(self):
        random_x = random.randint(0, self.x - 1)
        random_y = random.randint(0, self.y - 1)
        random_pos = random_x, random_y
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.particle_collection.add_particle(random_pos, random_color)

    def create_particle_with_pos(self, pos):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.particle_collection.add_particle(pos, random_color)

    def noise_gen_2(self, density):
        self.surface.fill((0, 0, 0))
        self.pixel_array = self._generate_pixel_array()

        distribution_density = int(density * (self.x * self.y))
        x_pixels = [random.randint(0, self.x-1) for foo in range(distribution_density)]
        y_pixels = [random.randint(0, self.y-1) for foo in range(distribution_density)]

        for index in range(distribution_density):
            self.pixel_array[x_pixels[index], y_pixels[index]] = (255, 255, 255)

    def draw_particles(self):
        self.particle_collection.particle_centers_to_pixel_array(self.pixel_array)


