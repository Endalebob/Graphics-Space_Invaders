import numpy
from math import sin, cos, tan, pi


class MatrixFile(object):
    @staticmethod
    def make_identity():
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def make_translation(x, y, z):
        return numpy.array([[1, 0, 0, x],
                            [0, 1, 0, y],
                            [0, 0, 1, z],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def make_rotation_X(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[1, 0, 0, 0],
                            [0, c, -s, 0],
                            [0, s, c, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def make_rotation_Y(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c, 0, s, 0],
                            [0, 1, 0, 0],
                            [-s, 0, c, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def make_rotation_Z(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c, -s, 0, 0],
                            [s, c, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def make_scale(s):
        return numpy.array([[s, 0, 0, 0],
                            [0, s, 0, 0],
                            [0, 0, s, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def make_perspective(angleOfView=60,
                         aspectRatio=1, near=0.1, far=1000):
        a = angleOfView * pi / 180.0
        d = 1.0 / tan(a / 2)
        r = aspectRatio
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)
        return numpy.array([[d / r, 0, 0, 0],
                            [0, d, 0, 0],
                            [0, 0, b, c],
                            [0, 0, -1, 0]]).astype(float)



