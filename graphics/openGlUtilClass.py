from OpenGL.GL import *


# we use this class for the purpose of compiling and linking
# the vertex and fragment shader to create gpu program
class OpenGLUtilClass(object):
    @staticmethod
    def initialize_shader(shader_code, type_of_shader):

        # this the code we put in shader
        shader_code = '#version 330 \n ' + shader_code
        # the first step is creating shader
        shader_reference = glCreateShader(type_of_shader)
        # then we add shader code
        glShaderSource(shader_reference, shader_code)
        # finally we compile shader code
        glCompileShader(shader_reference)
        # we check status
        compile_success = glGetShaderiv(shader_reference, GL_COMPILE_STATUS)
        if not compile_success:
            error_message = glGetShaderInfoLog(shader_reference)
            glDeleteShader(shader_reference)
            error_message = '\n' + error_message.decode('utf-8')
            raise Exception(error_message)
        return shader_reference

    # here create instance of object and link compiled shaders

    @staticmethod
    def initialize_program(vertex_shader_codes, fragment_shaders_codes):
        vertex_shader_ref = OpenGLUtilClass.initialize_shader(
            vertex_shader_codes, GL_VERTEX_SHADER)
        fragment_shader_ref = OpenGLUtilClass.initialize_shader(
            fragment_shaders_codes, GL_FRAGMENT_SHADER)
        # creating reference for the program
        programRef = glCreateProgram()
        glAttachShader(programRef, vertex_shader_ref)
        glAttachShader(programRef, fragment_shader_ref)
        glLinkProgram(programRef)
        link_success = glGetProgramiv(programRef,
                                     GL_LINK_STATUS)
        if not link_success:
            error_message = glGetProgramInfoLog(programRef)
            glDeleteProgram(programRef)
            error_message = '\n' + error_message.decode('utf-8')
            raise Exception(error_message)
        return programRef

    @staticmethod
    def print_system_info():
        print("  Vendor: " + glGetString(GL_VENDOR).
              decode('utf-8'))
        print("Renderer: " + glGetString(GL_RENDERER).
              decode('utf-8'))
        print("OpenGL version supported: " +
              glGetString(GL_VERSION).decode('utf-8'))
        print(" GLSL version supported: " +
              glGetString(GL_SHADING_LANGUAGE_VERSION).
              decode('utf-8'))
