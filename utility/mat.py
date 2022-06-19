from graphics.openGlUtilClass import OpenGLUtilClass
from graphics.unifor_file import UniformProvider
from OpenGL.GL import *


# store data related to rendering
# shader program references, uniform data, opengl render settings
class MaterialOfObject(object):
    def __init__(self, vertexShaderCode, fragmentShaderCode):
        self.program_ref = OpenGLUtilClass.initialize_program(vertexShaderCode, fragmentShaderCode)
        # this dictionary used to store uniform data
        self.uniforms = {"modelMatrix": UniformProvider("mat4", None), "viewMatrix": UniformProvider("mat4", None),
                         "projectionMatrix": UniformProvider("mat4", None)}
        # this dictionary used to rendering
        self.settings = {"drawStyle": GL_TRIANGLES}
        self.attributes = {}

    def add_uniform(self, dataType, variableName, data):
        self.uniforms[variableName] = UniformProvider(dataType, data)

    def locate_uniforms(self):
        for variableName, uniformObject in self.uniforms.items():
            uniformObject.locate_variable(self.program_ref, variableName)

    # this function implemented in other class
    def update_render_settings(self):
        pass

    # used to update uniforms
    def set_properties(self, properties):
        for name, data in properties.items():

            # change or update uniform variables
            if name in self.uniforms.keys():
                self.uniforms[name].data = data
            # update render settings
            elif name in self.settings.keys():
                self.settings[name] = data
            # unknown property type
            else:
                raise Exception("Material has no property named: " + name)

    def check_errors(self):
        status = ''
        while self.attributes:
            if self.attributes.keys() != self.attributes.values():
                print("attribute error")
                status = "error"
            else:
                print("successfully created")
                status = "success"
        return status

    def get_status_of_object(self):
        # this function used to tell the status of object
        status = self.check_errors()

        if status == "success":
            return "success status"
        else:
            return "failure status"

    def current_state_of_object(self):

        attribute = self.attributes.keys()
        values = self.attributes.values()
        len_attributes = self.attributes.items()

        current_state = {}
        current_state["attributes"] = attribute
        current_state["values"] = values
        current_state["attr_len"] = len_attributes
        return current_state

