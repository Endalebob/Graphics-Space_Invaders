from utility.bsc_mat import BasicMaterialOfObjectObject
from OpenGL.GL import *


class SurfaceMaterialOfObject(BasicMaterialOfObjectObject):
    def __init__(self, properties=None):
        super().__init__()
        if properties is None:
            properties = {}
        self.settings["drawStyle"] = GL_TRIANGLES
        self.settings["doubleSide"] = False
        self.settings["wireframe"] = False
        self.settings["lineWidth"] = 1
        self.set_properties(properties)

    def update_render_settings(self):
        if self.settings["doubleSide"]:
            glDisable(GL_CULL_FACE)

        else:
            glEnable(GL_CULL_FACE)
        if self.settings["wireframe"]:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        glLineWidth(self.settings["lineWidth"])

    def check_error(self):
        status = ''
        while self.attributes:
            if self.attributes.keys() != self.attributes.values():
                print("attribute error")
                status = "error"
            else:
                print("successfully created")
                status = "success"
        return status

    def get_status(self):
        # this function used to tell the status of object
        status = self.check_error()

        if status == "success":
            return "success status"
        else:
            return "failure status"

    def current_state(self):

        attribute = self.attributes.keys()
        values = self.attributes.values()
        len_attributes = self.attributes.items()

        current_state = {}
        current_state["attributes"] = attribute
        current_state["values"] = values
        current_state["attr_len"] = len_attributes
        return current_state

