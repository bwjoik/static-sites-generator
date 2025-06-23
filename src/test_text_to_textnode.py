import unittest
from text_to_textnodes import text_to_textnodes
from split_nodes_image import split_nodes_image, split_nodes_link
from split_node_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        text = "Just some plain text."
        expected = [TextNode("Just some plain text.", TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_bold_text(self):
        text = "This is **bold**."
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_italic_text(self):
        text = "This is _italic_."
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_code_text(self):
        text = "Here is `code`."
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_image(self):
        text = "Here is an image ![alt](img.png)."
        expected = [
            TextNode("Here is an image ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "img.png"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)

    def test_link(self):
        text = "Check this [site](https://example.com)."
        expected = [
            TextNode("Check this ", TextType.TEXT),
            TextNode("site", TextType.LINK, "https://example.com"),
            TextNode(".", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected)
