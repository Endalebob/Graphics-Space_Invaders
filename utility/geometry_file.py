from graphics.attribute_provider import AttributeProvider


class GeometryOfObject(object):
    def __init__(self):
        self.attributes = {}
        self.vertex_count = None

    def add_attribute(self, dataType, variableName, data):
        self.attributes[variableName] = AttributeProvider(dataType, data)

    def count_vertices(self):
        attrib = list(self.attributes.values())[0]
        self.vertex_count = len(attrib.data)
