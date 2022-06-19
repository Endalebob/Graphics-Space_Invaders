from graphics.ThreeDObject import Three_D_Object

# this class used to represent a node that do not correspond to visible objects in
# the scene. It represents the root of the tree.
class SceneOfObjectObject(Three_D_Object):
    def __init__(self):
        super().__init__()
