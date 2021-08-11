from pygame import mouse
from physics_engine import WorldMechanics
from particles import Particle
from utility import Position, Velocity


class MouseMonitor:
    def __init__(self, world_mechanics: WorldMechanics):
        self.previous_mouse_state = (0, 0, 0)
        self.world_mechanics = world_mechanics
        self.surface = self.world_mechanics.surface
        self.ghost_particle: Particle = Particle()

    def update(self):
        mouse_state = mouse.get_pressed(num_buttons=3)

        # Mouse creates a particle, but does not add it to the particle list until MOUSEUP
        if mouse_state[0] and not self.previous_mouse_state[0]:
            # New Mouse left click.
            mouse_pos = Position(mouse.get_pos())
            self.ghost_particle.update(pos=mouse_pos,
                                       velocity=Velocity())

        elif mouse_state[0] and self.previous_mouse_state[0]:
            # Left click still being held.
            mouse_pos = Position(mouse.get_pos())
            new_velocity = Velocity(target=mouse_pos,
                                    start=self.ghost_particle.pos)
            self.ghost_particle.update(velocity=new_velocity)
            self.ghost_particle.draw(self.surface)
            self.ghost_particle.draw_velocity(self.surface)

        elif not mouse_state and self.previous_mouse_state[0]:
            # Left click has been let go.
            self.world_mechanics.add_particle(pos=self.ghost_particle.pos,
                                              velocity=self.ghost_particle.velocity)

        self.previous_mouse_state = mouse_state


