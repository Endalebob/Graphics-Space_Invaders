from utility.ellips_geo import EllipsoidGeometryOfObject
from math import sin, cos, pi


class SphereGeometryOfObject(EllipsoidGeometryOfObject):
    def __init__(self, radius=1,
                 radius_segments=32, height_segments=16):
        super().__init__(2 * radius, 2 * radius, 2 * radius,
                         radius_segments,
                         height_segments)

    def check_error(self):
        status = ''
        while self.add_attribute:
            if self.attributes.keys() != self.attributes.values():
                print("attribute error")
                status = "error"
            else:
                print("successfully created")
                status = "success"
        return status

    def get_status_of_objects(self):
        # this function used to tell the status of object
        status = self.check_errors()

        if status == "success":
            return "success status"
        else:
            return "failure status"

    def current_state_of_objects(self):

        attribute = self.attributes.keys()
        values = self.attributes.values()
        len_attributes = self.count_vertices()

        current_state = {}
        current_state["attributes"] = attribute
        current_state["values"] = values
        current_state["attr_len"] = len_attributes
        return current_state

