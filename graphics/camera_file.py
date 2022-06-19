from graphics.ThreeDObject import Three_D_Object
from graphics.matrix_file import MatrixFile
from numpy.linalg import inv


# This class used to represent virtual camera used to view the scene
class CameraView(Three_D_Object):
    def __init__(self, angle_of_view=60, aspectRatio=1, near=0.1, far=1000):
        super().__init__()
        # the camera itself is not rendered like other node but it's transformation affects the
        # current placement of the objects in the scene
        self.projection_matrix = MatrixFile.make_perspective(angle_of_view, aspectRatio, near, far)
        self.view_matrix = MatrixFile.make_identity()

    def updateViewMatrix(self):
        self.view_matrix = inv(self.getWorldMatrix())


