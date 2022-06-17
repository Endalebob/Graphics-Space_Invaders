from utility.mat import MaterialOfObject
from graphics.unifor_file import UniformProvider


class BasicMaterialOfObjectObject(MaterialOfObject):
    def __init__(self):
        vertex_shader_code = """
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        in vec3 vertexColor;
        out vec3 color;
        void main()
        {
        gl_Position = projectionMatrix *
        viewMatrix * modelMatrix 
        * vec4(vertexPosition, 1.0);
        color = vertexColor;
        }
        """

        fragment_shader_code = """
        uniform vec3 baseColor;
        uniform bool useVertexColors;
        in vec3 color;
        out vec4 fragColor;
        void main()
        {
        vec4 tempColor = vec4(baseColor, 1.0);
        if ( useVertexColors )
        tempColor *= vec4(color, 1.0);
        fragColor = tempColor;
        }
        """

        super().__init__(vertex_shader_code, fragment_shader_code)
        self.add_uniform("vec3", "baseColor", [1.0, 1.0, 1.0])
        self.add_uniform("bool", "useVertexColors", False)
        self.locate_uniforms()
