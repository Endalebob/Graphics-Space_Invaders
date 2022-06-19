from utility.para_geo import ParametricGeometryOfObject
from math import sin, cos, pi


class EllipsoidGeometryOfObject(ParametricGeometryOfObject):
    def __init__(self, width=1, height=1, depth=1,
                 radius_segments=32, height_segments=16):
        def S(u, v):
            return [width / 2 * sin(u) * cos(v),
                    height / 2 * sin(v),
                    depth / 2 * cos(u) * cos(v)]

        super().__init__(0, 2 * pi, radius_segments,
                         -pi / 2, pi / 2, height_segments, S)

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
        len_attributes = self.count_vertices()

        current_state = {}
        current_state["attributes"] = attribute
        current_state["values"] = values
        current_state["attr_len"] = len_attributes
        return current_state
