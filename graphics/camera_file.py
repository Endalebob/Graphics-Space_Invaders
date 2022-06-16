from graphics.ThreeDObject import Three_D_Object
from graphics.matrix_file import MatrixFile
from numpy.linalg import inv


class CameraView(Three_D_Object):
    def __init__(self, angle_of_view=60, aspectRatio=1, near=0.1, far=1000):
        super().__init__()
        self.projection_matrix = MatrixFile.make_perspective(angle_of_view, aspectRatio, near, far)
        self.view_matrix = MatrixFile.make_identity()

    def updateViewMatrix(self):
        self.view_matrix = inv(self.getWorldMatrix())


