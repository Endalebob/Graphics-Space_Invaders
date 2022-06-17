from utility.ellips_geo import EllipsoidGeometryOfObject
from math import sin, cos, pi


class SphereGeometryOfObject(EllipsoidGeometryOfObject):
    def __init__(self, radius=1,
                 radius_segments=32, height_segments=16):
        super().__init__(2 * radius, 2 * radius, 2 * radius,
                         radius_segments,
                         height_segments)
