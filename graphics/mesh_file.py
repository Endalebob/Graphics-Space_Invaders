from graphics.ThreeDObject import Three_D_Object
from OpenGL.GL import *


# this class represent visible object in the scene
# it uses different data to specifiy an object for v-related data it use
# geometric data and appearance material data
class MeshObjectObject(Three_D_Object):
    def __init__(self, geometry, material):
        super().__init__()
        self.geometrical_shape = geometry
        self.material_object = material
        self.visible = True
        self.vaoRef = glGenVertexArrays(1)
        glBindVertexArray(self.vaoRef)
        for variable_name, attribute_object in geometry.attributes.items():
            attribute_object.associate_variable(material.program_ref, variable_name)
        glBindVertexArray(0)
