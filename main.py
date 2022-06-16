from graphics.home import Home
from graphics.rendering import ObjectRenderer
from graphics.scene_file import SceneOfObjectObject
from graphics.camera_file import CameraView
from graphics.mesh_file import MeshObjectObject
from graphics.texture_file import TextureFile
from utility.textu_mat import TextureMaterialOfObject
from utility.rect_geo import RectangleGeometryOfObject
from utility.sphere_geo import SphereGeometryOfObject
from utility.movtRig import MovementRigObject


# render a basic scene
class Test(Home):
    def __init__(self, sizeOfScreen=None):
        super().__init__(sizeOfScreen)
        self.current = 0
        self.picture_list = [
            ["images/sky.webp", "images/grass.jpg"],
            ["images/space1.jpg", "images/space2.jpg"],
            ["images/space6.png", "images/space7.png"],
            ["images/space5.png", "images/space4.jpg"],
            ["images/water.jpeg", "images/water.jpeg"],
        ]
        self.rig = MovementRigObject()
        self.camera = CameraView(aspectRatio=800 / 600)
        self.scene = SceneOfObjectObject()
        self.renderer = ObjectRenderer()

    def init(self):
        print("Initializing program...")

        self.camera.setPosition([0, 0, 4])
        self.rig.add(self.camera)
        self.scene.add(self.rig)
        self.rig.setPosition([0, 1, 4])
        self.picture_changer()

    def picture_changer(self, idx=0):
        skyGeometry = SphereGeometryOfObject(radius=50)
        skyMaterial = TextureMaterialOfObject(TextureFile(self.picture_list[idx][0]))
        sky = MeshObjectObject(skyGeometry, skyMaterial)
        self.scene.add(sky)
        grassGeometry = RectangleGeometryOfObject(width=100, height=100)
        grassMaterial = TextureMaterialOfObject(TextureFile(self.picture_list[idx][1]),
                                                {"repeatUV": [50, 50]})
        grass = MeshObjectObject(grassGeometry, grassMaterial)
        grass.rotateX(-3.14 / 2)
        self.scene.add(grass)

    def draw(self):
        self.rig.update(self.keyboard, self.delta_time)
        self.renderer.render_object(self.scene, self.camera)
        if self.keyboard.is_key_pressed("j") and self.current != 0:
            self.current = 0
            self.scene = SceneOfObjectObject()
            self.scene.add(self.rig)
            self.picture_changer(self.current)
        if self.keyboard.is_key_pressed("u") and self.current != 1:
            self.current = 1
            self.scene = SceneOfObjectObject()
            self.scene.add(self.rig)
            self.picture_changer(self.current)
        if self.keyboard.is_key_pressed("i") and self.current != 2:
            self.current = 2
            self.scene = SceneOfObjectObject()
            self.scene.add(self.rig)
            self.picture_changer(self.current)
        if self.keyboard.is_key_pressed("k") and self.current != 3:
            self.current = 3
            self.scene = SceneOfObjectObject()
            self.scene.add(self.rig)
            self.picture_changer(self.current)
        if self.keyboard.is_key_pressed("l") and self.current != 4:
            self.current = 4
            self.scene = SceneOfObjectObject()
            self.scene.add(self.rig)
            self.picture_changer(self.current)


Test().run()
