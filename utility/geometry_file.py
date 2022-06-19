from graphics.attribute_provider import AttributeProvider


# Geometry objects will store attribute data and the total number of
# vertices.
# this class used to store attribute data and number of vertices
class GeometryOfObject(object):
    def __init__(self):

        # this dictionary used to store attributes
        self.attributes = {}
        # used to count vertex
        self.vertex_count = None

    def add_attribute(self, dataType, variableName, data):
        self.attributes[variableName] = AttributeProvider(dataType, data)

    def count_vertices(self):
        attrib = list(self.attributes.values())[0]
        self.vertex_count = len(attrib.data)
