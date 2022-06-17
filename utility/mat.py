from graphics.openGlUtilClass import OpenGLUtilClass
from graphics.unifor_file import UniformProvider
from OpenGL.GL import *


class MaterialOfObject(object):
    def __init__(self, vertexShaderCode, fragmentShaderCode):
        self.program_ref = OpenGLUtilClass.initialize_program(vertexShaderCode, fragmentShaderCode)
        self.uniforms = {"modelMatrix": UniformProvider("mat4", None), "viewMatrix": UniformProvider("mat4", None),
                         "projectionMatrix": UniformProvider("mat4", None)}
        self.settings = {"drawStyle": GL_TRIANGLES}

    def add_uniform(self, dataType, variableName, data):
        self.uniforms[variableName] = UniformProvider(dataType, data)

    def locate_uniforms(self):
        for variableName, uniformObject in self.uniforms.items():
            uniformObject.locate_variable(self.program_ref, variableName)

    # configure OpenGL with render settings
    def update_render_settings(self):
        pass

    def set_properties(self, properties):
        for name, data in properties.items():

            # update uniforms
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            # update render settings
            elif name in self.settings.keys():
                self.settings[name] = data
            # unknown property type
            else:
                raise Exception("Material has no property named: " + name)
