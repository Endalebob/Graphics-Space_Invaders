import pygame
from graphics.keyboard import KeyBoard


class Home(object):
    def __init__(self, sizeOfScreen=None):
        if sizeOfScreen is None:
            sizeOfScreen = [600, 600]
        pygame.init()
        display_flags = pygame.DOUBLEBUF | pygame.OPENGL
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLESAMPLES, 4)
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_CORE)
        self.screen = pygame.display.set_mode(sizeOfScreen, display_flags)
        pygame.display.set_caption("Space Invader")
        self.running_state = True
        self.clock = pygame.time.Clock()
        self.keyboard = KeyBoard()
        self.time_pass = 0

    def init(self):
        pass

    def draw(self):
        pass

    def run(self):
        self.init()
        while self.running_state:
            self.keyboard.update()
            if self.keyboard.quit:
                self.running_state = False
            self.delta_time = self.clock.get_time() / 1000
            self.time_pass += self.delta_time
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
