from utility.geometry_file import GeometryOfObject


class RectangleGeometryOfObject(GeometryOfObject):
    def __init__(self, width=1, height=1):
        super().__init__()
        P0 = [-width/2, -height/2, 0]
        P1 = [ width/2, -height/2, 0]
        P2 = [-width/2, height/2, 0]
        P3 = [ width/2, height/2, 0]
        C0, C1, C2, C3 = [1,1,1], [1,0,0], [0,1,0],[0,0,1]
        positionData = [ P0,P1,P3, P0,P3,P2 ]
        colorData = [ C0,C1,C3, C0,C3,C2 ]
        self.add_attribute("vec3", "vertexPosition",
                           positionData)
        self.add_attribute("vec3", "vertexColor",
                           colorData)
        self.count_vertices()
        # texture coordinates
        T0, T1, T2, T3 = [0, 0], [1, 0], [0, 1], [1, 1]
        uvData = [T0, T1, T3, T0, T3, T2]
        self.add_attribute("vec2", "vertexUV", uvData)
