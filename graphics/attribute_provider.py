from OpenGL.GL import *
import numpy


class AttributeProvider:
    def __init__(self, data_type, value):
        #  int | float | vec2 | vec3 | vec4
        self.data_type = data_type
        self.data = value
        self.buffer_ref = glGenBuffers(1)
        self.upload_data()

    def upload_data(self):
        data = numpy.array(self.data).astype(numpy.float32)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_ref)
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    def associate_variable(self, programRef, variableName):
        variable_ref = glGetAttribLocation(programRef, variableName)
        if variable_ref == -1:
            return
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_ref)
        if self.data_type == "int":
            glVertexAttribPointer(variable_ref, 1, GL_INT, False, 0, None)
        elif self.data_type == "float":
            glVertexAttribPointer(variable_ref, 1, GL_FLOAT, False, 0, None)
        elif self.data_type == "vec2":
            glVertexAttribPointer(variable_ref, 2, GL_FLOAT, False, 0, None)
        elif self.data_type == "vec3":
            glVertexAttribPointer(variable_ref, 3, GL_FLOAT, False, 0, None)
        elif self.data_type == "vec4":
            glVertexAttribPointer(variable_ref, 4, GL_FLOAT, False, 0, None)

        else:
            raise Exception("Attribute " + variableName + " has unknown type " + self.data_type)
        # indicate that data will be streamed to this variable
        glEnableVertexAttribArray(variable_ref)
