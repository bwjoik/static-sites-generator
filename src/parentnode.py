from htmlnode import HTMLNode

# ...existing code...

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag is None:
            raise ValueError("ParentNode 必須有 tag")
        if children is None:
            raise ValueError("ParentNode 必須有 children")
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode 必須有 tag")
        if self.children is None:
            raise ValueError("ParentNode 必須有 children")
        props_str = ""
        if self.props:
            props_list = [f'{key}="{value}"' for key, value in self.props.items()]
            props_str = " " + " ".join(props_list)
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}>{children_html}</{self.tag}>"

# ...existing code...