from OpenGL.GL import *


class OpenGLUtilClass(object):
    @staticmethod
    def initialize_shader(shader_code, shaderType):

        shader_code = '#version 330 \n ' + shader_code
        shaderRef = glCreateShader(shaderType)
        glShaderSource(shaderRef, shader_code)
        glCompileShader(shaderRef)
        compile_success = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)
        if not compile_success:
            error_message = glGetShaderInfoLog(shaderRef)
            glDeleteShader(shaderRef)
            error_message = '\n' + error_message.decode('utf-8')
            raise Exception(error_message)
        return shaderRef

    @staticmethod
    def initialize_program(vertexShaderCode, fragmentShaderCode):
        vertex_shader_ref = OpenGLUtilClass.initialize_shader(
            vertexShaderCode, GL_VERTEX_SHADER)
        fragment_shader_ref = OpenGLUtilClass.initialize_shader(
            fragmentShaderCode, GL_FRAGMENT_SHADER)
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
