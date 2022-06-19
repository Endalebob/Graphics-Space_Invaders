from graphics.matrix_file import MatrixFile


# in scene graph tree we represent anode using 3D objects
class Three_D_Object(object):
    def __init__(self):

        # this is a matrix used to store transform data
        self.transform = MatrixFile.make_identity()
        # it references the prent objects
        self.parent = None
        # this references child objects
        self.children = []

    # this function used to add a child for the node
    def add(self, child):
        self.children.append(child)
        child.parent = self

    # this function used to remove a child from the node
    def remove(self, child):
        self.children.remove(child)
        child.parent = None

    # used to calculate the transformation of 3D object relative to root scene
    def getWorldMatrix(self):
        if self.parent is None:
            return self.transform
        else:
            return self.parent.getWorldMatrix() @ self.transform

    def getDescendantList(self):
        descendants = []
        nodesToProcess = [self]
        while len(nodesToProcess) > 0:
            # remove the node at index 0
            node = nodesToProcess.pop(0)
            # add this node to descendants of children
            descendants.append(node)
            # add children with nodes to process
            nodesToProcess = node.children + nodesToProcess
        return descendants

    def applyMatrix(self, matrix, localCoord=True):
        if localCoord:
            self.transform = self.transform @ matrix
        else:
            self.transform = matrix @ self.transform

    def translate(self, x, y, z, localCoord=True):
        m = MatrixFile.make_translation(x, y, z)
        self.applyMatrix(m, localCoord)

    def rotateX(self, angle, localCoord=True):
        m = MatrixFile.make_rotation_X(angle)
        self.applyMatrix(m, localCoord)

    def rotateY(self, angle, localCoord=True):
        m = MatrixFile.make_rotation_Y(angle)
        self.applyMatrix(m, localCoord)

    def rotateZ(self, angle, localCoord=True):
        m = MatrixFile.make_rotation_Z(angle)
        self.applyMatrix(m, localCoord)

    def scale(self, s, localCoord=True):
        m = MatrixFile.make_scale(s)
        self.applyMatrix(m, localCoord)

    def getPosition(self):
        return [self.transform.item((0, 3)),
                self.transform.item((1, 3)),
                self.transform.item((2, 3))]

    def getWorldPosition(self):
        worldTransform = self.getWorldMatrix()
        return [worldTransform.item((0, 3)),
                worldTransform.item((1, 3)),
                worldTransform.item((2, 3))]

    def setPosition(self, position):
        self.transform.itemset((0, 3), position[0])
        self.transform.itemset((1, 3), position[1])
        self.transform.itemset((2, 3), position[2])
