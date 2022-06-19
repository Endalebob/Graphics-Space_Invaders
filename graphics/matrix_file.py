import numpy
from math import sin, cos, tan, pi


# matrix is two dimensional array of numbers used to perform transformation easily
class MatrixFile(object):

    # Identity matrix is a matrix which results the matrix after multiplication
    @staticmethod
    def make_identity():
        return MatrixFile.unique("hello")

    # used to make identity matrix
    @staticmethod
    def unique(data_type):
        return numpy.array([[1, 0, 0, 0],
                            [0, 1, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]).astype(float)

    # translation is linear movement in different direction
    # the following two functions are used to apply translation
    @staticmethod
    def make_translation(x, y, z):
        return MatrixFile.translateMatrix(x, y, z)

    @staticmethod
    def translateMatrix(x, y, z):
        return numpy.array([[1, 0, 0, x],
                            [0, 1, 0, y],
                            [0, 0, 1, z],
                            [0, 0, 0, 1]]).astype(float)

    # rotation is one of the linear transforamtion in order to along a specified axis
    # we need to apply different formulas for X, Y, Z
    @staticmethod
    def make_rotation_X(angle):
        return MatrixFile.x_rotate(angle)

    # ROTATION along x-axis
    @staticmethod
    def x_rotate(data_type):
        c = cos(data_type)
        s = sin(data_type)
        return numpy.array([[1, 0, 0, 0],
                            [0, c, -s, 0],
                            [0, s, c, 0],
                            [0, 0, 0, 1]]).astype(float)

    # rotation along y-axis
    @staticmethod
    def make_rotation_Y(angle):
        return MatrixFile.y_rotate(angle)

    @staticmethod
    def y_rotate(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c, 0, s, 0],
                            [0, 1, 0, 0],
                            [-s, 0, c, 0],
                            [0, 0, 0, 1]]).astype(float)

    # rotation along z-axis
    @staticmethod
    def make_rotation_Z(angle):
        return MatrixFile.z_rotate(angle)

    @staticmethod
    def z_rotate(angle):
        c = cos(angle)
        s = sin(angle)
        return numpy.array([[c, -s, 0, 0],
                            [s, c, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def make_scale(s):
        return MatrixFile.scaler(s)

    @staticmethod
    def scaler(s):
        return numpy.array([[s, 0, 0, 0],
                            [0, s, 0, 0],
                            [0, 0, s, 0],
                            [0, 0, 0, 1]]).astype(float)

    # to make perspective view we need angle of view aspect ratio near and far distance
    @staticmethod
    def make_perspective(angle_of_view_of_scene=60,
                         aspect_ration_of_scene=1, near=0.1, far=1000):
        a = angle_of_view_of_scene * pi / 180.0
        d = 1.0 / tan(a / 2)
        r = aspect_ration_of_scene
        b = (far + near) / (near - far)
        c = 2 * far * near / (near - far)
        return numpy.array([[d / r, 0, 0, 0],
                            [0, d, 0, 0],
                            [0, 0, b, c],
                            [0, 0, -1, 0]]).astype(float)
