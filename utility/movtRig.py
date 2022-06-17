from graphics.ThreeDObject import Three_D_Object


class MovementRigObject(Three_D_Object):
    def __init__(self, units_per_second=1, degrees_per_second=60):
        super().__init__()
        self.look_attachment = Three_D_Object()
        self.children = [self.look_attachment]
        self.look_attachment.parent = self
        self.units_per_seconds = units_per_second
        self.degrees_per_seconds = degrees_per_second
        # customizable key mappings
        #  defaults: WASDRF (move), QE (turn), TG (look)
        self.KEY_MOVE_FORWARDS = "w"
        self.KEY_MOVE_BACKWARDS = "s"
        self.KEY_MOVE_LEFT = "a"
        self.KEY_MOVE_RIGHT = "d"
        self.KEY_MOVE_UP = "r"
        self.KEY_MOVE_DOWN = "f"
        self.KEY_TURN_LEFT = "q"
        self.KEY_TURN_RIGHT = "e"
        self.KEY_LOOK_UP = "t"
        self.KEY_LOOK_DOWN = "g"

    def update(self, input_objects, delta_times):
        moveAmount = self.units_per_seconds * delta_times
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

    def add(self, child):
        self.look_attachment.add(child)

    def remove(self, child):
        self.look_attachment.remove(child)
