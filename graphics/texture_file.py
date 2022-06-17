import pygame
from OpenGL.GL import *


class TextureFile(object):
    def __init__(self, fileName=None, properties=None):
        if properties is None:
            properties = {}
        self.surface = None
        self.textureRef = glGenTextures(1)
        self.properties = {
            "magFilter": GL_LINEAR,
            "minFilter": GL_LINEAR_MIPMAP_LINEAR,
            "wrap": GL_REPEAT
        }
        self.set_properties(properties)
        if fileName is not None:
            self.load_image(fileName)
            self.upload_data()

    def load_image(self, fileName):
        self.surface = pygame.image.load(fileName)

    def set_properties(self, props):
        for _name, data in props.items():
            if _name in self.properties.keys():
                self.properties[_name] = data

            else:  # unknown property type
                raise Exception("Texture has no property with name: " + _name)

    def upload_data(self):
        width = self.surface.get_width()
        height = self.surface.get_height()
        pixel_data = pygame.image.tostring(self.
                                          surface, "RGBA", 1)
        glBindTexture(GL_TEXTURE_2D, self.textureRef)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA,
                     width, height, 0, GL_RGBA,
                     GL_UNSIGNED_BYTE, pixel_data)
        glGenerateMipmap(GL_TEXTURE_2D)
        glTexParameteri(GL_TEXTURE_2D,
                        GL_TEXTURE_MAG_FILTER,
                        self.properties["magFilter"])
        glTexParameteri(GL_TEXTURE_2D,
                        GL_TEXTURE_MIN_FILTER,
                        self.properties["minFilter"])
        glTexParameteri(GL_TEXTURE_2D,
                        GL_TEXTURE_WRAP_S,
                        self.properties["wrap"])
        glTexParameteri(GL_TEXTURE_2D,
                        GL_TEXTURE_WRAP_T,
                        self.properties["wrap"])
        glTexParameterfv(GL_TEXTURE_2D,
                         GL_TEXTURE_BORDER_COLOR, [1, 1, 1, 1])
