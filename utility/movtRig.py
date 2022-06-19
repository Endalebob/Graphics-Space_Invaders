from graphics.ThreeDObject import Three_D_Object


class MovementRigObject(Three_D_Object):
    def __init__(self, units_per_second=1, degrees_per_second=60):
        super().__init__()
        self.look_attachment = Three_D_Object()
        self.children = [self.look_attachment]
        self.look_attachment.parent = self
        self.units_per_seconds = units_per_second
        self.degrees_per_seconds = degrees_per_second
        # this is mapping of keys to move the scene in space
        # to move in forward directions
        self.KEY_MOVE_FORWARDS = "w"
        # to move in backward directions
        self.KEY_MOVE_BACKWARDS = "s"
        # to move in left directions
        self.KEY_MOVE_LEFT = "a"
        # to move in right directions
        self.KEY_MOVE_RIGHT = "d"
        # to move in up directions
        self.KEY_MOVE_UP = "r"
        # to move in down directions
        self.KEY_MOVE_DOWN = "f"
        # to turn in left directions
        self.KEY_TURN_LEFT = "q"
        # to turn in right directions
        self.KEY_TURN_RIGHT = "e"
        # to move in up directions
        self.KEY_LOOK_UP = "t"
        # to move in down directions
        self.KEY_LOOK_DOWN = "g"

    # this function update the position of key pressed
    def update(self, input_objects, delta_times):
        # when the key pressed by how much amount the scene must move
        moveAmount = self.units_per_seconds * delta_times
        # when the key pressed by how much amount the scene must rotate
        rotateAmount = self.degrees_per_seconds * (3.1415926 / 180) * delta_times
        if input_objects.is_key_pressed(self.KEY_MOVE_FORWARDS):
            self.translate(0, 0, -moveAmount)
        if input_objects.is_key_pressed(self.KEY_MOVE_BACKWARDS):
            self.translate(0, 0, moveAmount)
        if input_objects.is_key_pressed(self.KEY_MOVE_LEFT):
            self.translate(-moveAmount, 0, 0)
        if input_objects.is_key_pressed(self.KEY_MOVE_RIGHT):
            self.translate(moveAmount, 0, 0)
        if input_objects.is_key_pressed(self.KEY_MOVE_UP):
            self.translate(0, moveAmount, 0)
        if input_objects.is_key_pressed(self.KEY_MOVE_DOWN):
            self.translate(0, -moveAmount, 0)
        if input_objects.is_key_pressed(self.KEY_TURN_RIGHT):
            self.rotateY(-rotateAmount)
        if input_objects.is_key_pressed(self.KEY_TURN_LEFT):
            self.rotateY(rotateAmount)
        if input_objects.is_key_pressed(self.KEY_LOOK_UP):
            self.look_attachment.rotateX(rotateAmount)
        if input_objects.is_key_pressed(self.KEY_LOOK_DOWN):
            self.look_attachment.rotateX(-rotateAmount)

    # used to add the child in the node
    def add(self, child):
        self.look_attachment.add(child)

    # used to remove the child from the node
    def remove(self, child):
        self.look_attachment.remove(child)
