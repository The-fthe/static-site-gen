class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

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
            props_html += f' {key}="{value}"'
            i += 1

        return props_html

    def __repr__(self):
        return f"{self.tag},{self.value}, {self.children},{self.props_to_html()}"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid value")

        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"{self.tag},{self.value}, {self.props_to_html()}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid tag")
        if self.children is None:
            raise ValueError("Invalid children")
        sb = ""
        for leaf in self.children:
            sb += leaf.to_html()
        return f"<{self.tag}{self.props_to_html()}>{sb}</{self.tag}>"

    def __repr__(self):
        return f"{self.tag},{self.value}, {self.children},{self.props_to_html()}"
