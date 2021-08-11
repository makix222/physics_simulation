from pygame import mouse
from physics_engine import WorldMechanics
from particles import Particle
from utility import Position, Velocity


class MouseMonitor:
    def __init__(self, world_mechanics: WorldMechanics):
        self.previous_mouse_state = (0, 0, 0)
        self.mouse_state = (0, 0, 0)
        self.world_mechanics = world_mechanics
        self.ghost_particle: Particle = None

    def update(self):
        self.mouse_state = mouse.get_pressed(num_buttons=3)

        # Mouse creates a particle, but does not add it to the particle list until MOUSEUP
        if self.mouse_state[0] and not self.previous_mouse_state[0]:
            # New Mouse left click.
            mouse_pos = Position(mouse.get_pos())
            self.ghost_particle = Particle(pos=mouse_pos,
                                           velocity=Velocity())

        elif self.mouse_state[0] and self.previous_mouse_state[0]:
            # Left click still being held.
            mouse_pos = Position(mouse.get_pos())
            new_velocity = Velocity(target=mouse_pos,
                                    start=self.ghost_particle.pos)
            self.ghost_particle.update(velocty=new_velocity)


        self.world_mechanics.update_mouse_input(self.mouse_state[0], mouse.get_pos())


