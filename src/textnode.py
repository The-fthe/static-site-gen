
class TextNode:

    def __init__(self, text="", text_type="", url=None):
        self.TEXT = text
        self.TEXT_TYPE = text_type
        self.URL = url

    def __eq__(self, other):
        if self.TEXT is not other.TEXT:
            return False
        if self.TEXT_TYPE is not other.TEXT_TYPE:
            return False
        if self.URL is not other.URL:
            return False
        return True

    def __repr__(self):
        return f"TextNode({self.TEXT}, {self.TEXT_TYPE}, {self.URL})"
