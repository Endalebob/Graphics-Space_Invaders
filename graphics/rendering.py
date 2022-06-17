from OpenGL.GL import *
from graphics.mesh_file import MeshObjectObject


class ObjectRenderer(object):
    def __init__(self, clear_color=None):
        if clear_color is None:
            clear_color = [0, 0, 0]
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_MULTISAMPLE)
        glClearColor(clear_color[0], clear_color[1], clear_color[2], 1)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def render_object(self, scene, camera):
        glClear(GL_COLOR_BUFFER_BIT |
                GL_DEPTH_BUFFER_BIT)
        camera.updateViewMatrix()
        descendant_list = scene.getDescendantList()
        mesh_filter = lambda x: isinstance(x, MeshObjectObject)
        mesh_list = list(filter(mesh_filter,
                               descendant_list))
        for mesh in mesh_list:
            if not mesh.visible:
                continue
            glUseProgram(mesh.material_object.program_ref)
            # bind VAO
            glBindVertexArray(mesh.vaoRef)
            mesh.material_object.uniforms["modelMatrix"].data = mesh.getWorldMatrix()
            mesh.material_object.uniforms["viewMatrix"].data = camera.view_matrix
            mesh.material_object.uniforms["projectionMatrix"].data = camera.projection_matrix

            for variable_name, uniform_object in mesh.material_object.uniforms.items():
                uniform_object.up_load_data()
            mesh.material_object.update_render_settings()
            glDrawArrays(mesh.material_object.
                         settings["drawStyle"], 0,
                         mesh.geometrical_shape.vertex_count)
