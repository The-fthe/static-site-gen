
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=[]):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method nto implemented")

    def props_to_html(self):
        if self.props is None:
            return ""

        props_html = ""
        count = len(self.props.keys())
        if count == 0:
            return ""

        props_html = ""
        i = 0
        for key, value in self.props.items():
            if i != 0:
                props_html += f" {key}=\"{value}\""
                i += 1
                continue
            props_html += f"{key}=\"{value}\""
            i += 1

        return props_html

    def __repr__(self):
        if self.children is not None:
            s = self.children.__repr__

        return f"{self.tag},{self.value}, {s},{self.props_to_html()}"
