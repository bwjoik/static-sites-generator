from enum import Enum
from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode 必須有 value")
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode 必須有 value")
        if self.tag is None:
            return str(self.value)
        props_str = ""
        if self.props:
            props_list = [f'{key}="{value}"' for key, value in self.props.items()]
            props_str = " " + " ".join(props_list)
        return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"