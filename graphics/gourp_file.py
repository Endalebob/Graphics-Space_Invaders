from graphics.ThreeDObject import Three_D_Object


# Used to represent an iterior node to which other nodes are attached and enable
# easily transform them as a single unit.
class GroupObjectObject(Three_D_Object):
    def __init__(self):
        super().__init__()
