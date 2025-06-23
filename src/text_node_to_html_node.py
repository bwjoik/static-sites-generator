from leafnode import LeafNode
from textnode import TextType, TextNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node.text_type, TextType):
        raise ValueError(f"Invalid text type: {text_node.text_type}. Must be an instance of TextType Enum.")
    
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        if text_node.url is None:
            raise ValueError("Link text type requires a URL.")
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if text_node.url is None:
            raise ValueError("Image text type requires a URL.")
        return LeafNode(tag="img", value="", props={"alt": text_node.text, "src": text_node.url})