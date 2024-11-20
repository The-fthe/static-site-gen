
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
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
        return f"{self.tag},{self.value}, {self.children},{self.props_to_html()}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value is None")
            return ""

        if self.tag == None:
            return self.value

        match self.tag:
            case "p":
                return f'<p>{self.value}</p>'
            case "a":
                return f'<a {self.props_to_html()}>{self.value}</a>'

    def __repr__(self):
        return f"{self.tag},{self.value}, {self.props_to_html()}"
