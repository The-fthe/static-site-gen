
class HTMLNode:
    def __init__(self, tag="", value="", children=None, props=[]):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        count = len(self.props.keys())
        if count == 0:
            return ""

        s = ""
        i = 0
        for key, value in self.props.items():
            if i != 0:
                s += f" {key}=\"{value}\""
                i += 1
                continue
            s += f"{key}=\"{value}\""
            i += 1

        return s

    def __repr__(self):
        if self.children is not None:
            s = self.children.__repr__

        return f"{self.tag},{self.value}, {s},{self.props_to_html()}"
