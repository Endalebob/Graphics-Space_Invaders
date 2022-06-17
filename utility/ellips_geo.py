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
