from utility.geometry_file import GeometryOfObject


# by extending geometry of object class this class create rectangular
# shaped objects
class RectangleGeometryOfObject(GeometryOfObject):
    def __init__(self, width=1, height=1):
        super().__init__()
        P0 = [-width / 2, -height / 2, 0]
        P1 = [width / 2, -height / 2, 0]
        P2 = [-width / 2, height / 2, 0]
        P3 = [width / 2, height / 2, 0]
        # these are colors corresponding to the vertices
        C0, C1, C2, C3 = [1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]
        position_Data = [P0, P1, P3, P0, P3, P2]
        color_Data = [C0, C1, C3, C0, C3, C2]
        self.add_attribute("vec3", "vertexPosition",
                           position_Data)
        self.add_attribute("vec3", "vertexColor",
                           color_Data)
        # used to get the length of vertices
        self.count_vertices()
        # texture coordinates
        T0, T1, T2, T3 = [0, 0], [1, 0], [0, 1], [1, 1]
        uvData = [T0, T1, T3, T0, T3, T2]
        self.add_attribute("vec2", "vertexUV", uvData)

    def check_error(self):
        status = ''
        while self.add_attribute:
            if self.attributes.keys() == self.attributes.values():
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
