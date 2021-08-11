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
background_color = (10, 10, 10)
screen = pygame.display.set_mode((x, y))
surface = pygame.display.get_surface()
start_time = datetime.now()
clock = pygame.time.Clock()

noise_gens = noise_gens.ParticleNoise(surface=surface)
world_mechanics = WorldMechanics(surface=surface)
mouse_monitor = MouseMonitor(world_mechanics)

while True:
    surface.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    dt = clock.tick(60)
    mouse_monitor.update()
    world_mechanics.update(time_step=dt)

    pygame.display.flip()



