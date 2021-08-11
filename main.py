from datetime import datetime
from sys import exit
import pygame
import noise_gens
from mouse_tracking import MouseMonitor
from physics_engine import WorldMechanics

pygame.init()
x = 300
y = 300
pixel_count = x * y
screen = pygame.display.set_mode((x, y))
start_time = datetime.now()

noise_gens = noise_gens.ParticleNoise(surface=pygame.display.get_surface())
world_generator = WorldMechanics(surface=pygame.display.get_surface())
mouse_monitor = MouseMonitor(world_generator)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    mouse_monitor.update()

    noise_gens.draw_particles()
    pygame.display.flip()



