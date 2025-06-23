from enum import Enum
from leafnode import LeafNode
from textnode import TextType

def text_node_to_html_node(self):
    if not isinstance(self.text_type, TextType):
        raise ValueError(f"Invalid text type: {self.text_type}. Must be an instance of TextType Enum.")
    
    if self.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=self.text)
    elif self.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=self.text)
    elif self.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=self.text)
    elif self.tesxt_type == TextType.CODE:
        return LeafNode(tag="code", value = self.text)
    elif self.text_type == TextType.LINK:
        if self.url is None:
            raise ValueError("Link text type requires a URL.")
        return LeafNode(tag="a", value=self.text, props={"href": self.url})
    elif self.text_type == TextType.IMAGE:
        if self.url is None:
            raise ValueError("Image text type requires a URL.")
        return LeafNode(tag="img", value=str(), props={"alt": self.text,"src": self.url})
    
    