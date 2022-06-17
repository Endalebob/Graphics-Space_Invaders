from utility.geometry_file import GeometryOfObject


class BoxGeometryOfObjectOfObject(GeometryOfObject):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()
        P0 = [-width / 2, -height / 2, -depth / 2]
        P1 = [width / 2, -height / 2, -depth / 2]
        P2 = [-width / 2, height / 2, -depth / 2]
        P3 = [width / 2, height / 2, -depth / 2]
        P4 = [-width / 2, -height / 2, depth / 2]
        P5 = [width / 2, -height / 2, depth / 2]
        P6 = [-width / 2, height / 2, depth / 2]
        P7 = [width / 2, height / 2, depth / 2]
        # colors for faces in order: x+, x-, y+, y-,z+, z
        C1, C2 = [1, 0.5, 0.5], [0.5, 0, 0]
        C3, C4 = [0.5, 1, 0.5], [0, 0.5, 0]
        C5, C6 = [0.5, 0.5, 1], [0, 0, 0.5]
        position_data = [P5, P1, P3, P5, P3, P7, P0, P4, P6, P0,
                        P6, P2, P6, P7, P3, P6, P3, P2,
                        P0, P1, P5, P0, P5, P4, P4, P5, P7,
                        P4, P7, P6, P1, P0, P2, P1, P2, P3]
        color_data = [C1] * 6 + [C2] * 6 + [C3] * 6 + [C4] * 6 + [C5] * 6 + [C6] * 6

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.count_vertices()
        # texture coordinates
        T0, T1, T2, T3 = [0, 0], [1, 0], [0, 1], [1, 1]
        uvData = [T0, T1, T3, T0, T3, T2] * 6
        self.add_attribute("vec2", "vertexUV", uvData)
