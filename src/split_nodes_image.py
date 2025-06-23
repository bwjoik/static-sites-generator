import re
from textnode import *

def split_nodes_image(old_nodes):
    new_nodes = []
    pattern = re.compile(r"!\[([^\]]+)\]\(([^)]+)\)")

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        last_index = 0
        for match in pattern.finditer(node.text):
            if match.start() > last_index:
                new_nodes.append(TextNode(node.text[last_index:match.start()], TextType.TEXT))

            alt_text, img_url = match.group(1), match.group(2)
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, img_url))

            last_index = match.end()

        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        last_index = 0
        for match in pattern.finditer(node.text):
            if match.start() > last_index:
                new_nodes.append(TextNode(node.text[last_index:match.start()], TextType.TEXT))

            link_text, link_url = match.group(1), match.group(2)
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            last_index = match.end()

        if last_index < len(node.text):
            new_nodes.append(TextNode(node.text[last_index:], TextType.TEXT))

    return new_nodes
