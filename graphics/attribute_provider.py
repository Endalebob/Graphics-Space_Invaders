from OpenGL.GL import *
import numpy


# vertex shader uses the data stored in vertex buffer
class AttributeProvider:
    def __init__(self, data_type_of_vertex, value):
        # store the type of data
        self.data_type_of_vertex = data_type_of_vertex
        # store the value
        self.data = value
        # this reference the buffer from the gpu for computation
        self.buffer_reference = glGenBuffers(1)
        self.up_load_data()

    def up_load_data(self):
        # change number format into numpy
        data = numpy.array(self.data).astype(numpy.float32)
        # here we select which buffer to use
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_reference)
        # this function put the data in the selected buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    # this function associate the variable in the program with the buffer
    # we created above

    def associate_variable(self, program_reference, variableName):
        # using this function we get program and we assign its location to this variable
        variable_ref = glGetAttribLocation(program_reference, variableName)
        if variable_ref == -1:
            return
        # here we select the buffer used in this program
        glBindBuffer(GL_ARRAY_BUFFER, self.buffer_reference)
        if self.data_type_of_vertex == "int":
            glVertexAttribPointer(variable_ref, 1, GL_INT, False, 0, None)
        elif self.data_type_of_vertex == "float":
            glVertexAttribPointer(variable_ref, 1, GL_FLOAT, False, 0, None)
        elif self.data_type_of_vertex == "vec2":
            glVertexAttribPointer(variable_ref, 2, GL_FLOAT, False, 0, None)
        elif self.data_type_of_vertex == "vec3":
            glVertexAttribPointer(variable_ref, 3, GL_FLOAT, False, 0, None)
        elif self.data_type_of_vertex == "vec4":
            glVertexAttribPointer(variable_ref, 4, GL_FLOAT, False, 0, None)

        else:
            raise Exception("Attribute " + variableName + " has unknown type " + self.data_type_of_vertex)
        # indicate that data will be streamed to this variable
        glEnableVertexAttribArray(variable_ref)
