from OpenGL.GL import *


# this class used to send data directly from cpu to gpu.
class UniformProvider(object):
    def __init__(self, type_of_data, data):
        self.type_of_data = type_of_data
        self.data = data
        # this variable reference the location variable in program
        self.variable_reference = None

    # this function get the required variable
    def locate_variable(self, programRef, variableName):
        self.variable_reference = glGetUniformLocation(programRef, variableName)

    def up_load_data(self):

        # if the program does not reference the variable, then exit
        if self.variable_reference == -1:
            return
        if self.type_of_data == "int":
            glUniform1i(self.variable_reference, self.data)
        elif self.type_of_data == "bool":
            glUniform1i(self.variable_reference, self.data)
        elif self.type_of_data == "float":
            glUniform1f(self.variable_reference, self.data)
        elif self.type_of_data == "vec2":
            glUniform2f(self.variable_reference, self.data[0], self.data[1])
        elif self.type_of_data == "vec3":
            glUniform3f(self.variable_reference, self.data[0], self.data[1], self.data[2])
        elif self.type_of_data == "vec4":
            glUniform4f(self.variable_reference, self.data[0], self.data[1], self.data[2], self.data[3])
        elif self.type_of_data == "mat4":
            glUniformMatrix4fv(self.variable_reference, 1, GL_TRUE, self.data)
        elif self.type_of_data == "sampler2D":
            textureObjectRef, textureUnitRef = self.data
            # activate texture unit
            glActiveTexture(GL_TEXTURE0 + textureUnitRef)
            glBindTexture(GL_TEXTURE_2D, textureObjectRef)
            glUniform1i(self.variable_reference, textureUnitRef)
