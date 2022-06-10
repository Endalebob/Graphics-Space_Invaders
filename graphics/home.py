import pygame





class missile:
    def __init__(self, x, y):
        self.x = x
        self.y = y        

    playerImg = pygame.image.load('images/photo1.jpeg')
class enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y        

    enemyImg = pygame.image.load('images/photo2.jpeg')
class bullet:
        def __init__(self, x, y):
            self.x = x
            self.y = y        

class Home(object):
    def __init__(self, screenSize=None):
        if screenSize is None:
            screenSize = [600, 600]
        pygame.init()
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        # initialize buffers to perform antialiasing
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(
            pygame.GL_MULTISAMPLESAMPLES, 4)
        # use a core OpenGL profile for cross-platform compatibility
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_CORE)
        self.screen = pygame.display.set_mode(screenSize, displayFlags)
        pygame.display.set_caption("Graphics Window")
        self.running = True
        self.clock = pygame.time.Clock()
        #here next time we include input file
        self.time = 0

    def initialize(self):
        pass
    def update(self):
        pass

    def run(self):
        self.initialize()
        while self.running:
            self.input.update()
            if self.input.quit:
                self.running = False
            self.deltaTime = self.clock.get_time() / 1000
            self.time += self.deltaTime
            self.update()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
