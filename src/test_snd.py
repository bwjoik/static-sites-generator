import unittest

from textnode import TextNode, TextType
from split_node_delimiter import split_nodes_delimiter
class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("some `code` here", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("some ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" here", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_bold_delimiter(self):
        node = TextNode("this is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("this is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
        ]
        self.assertEqual(result, expected)

    def test_italic_delimiter(self):
        node = TextNode("a _cat_ and a _dog_", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = [
            TextNode("a ", TextType.TEXT),
            TextNode("cat", TextType.ITALIC),
            TextNode(" and a ", TextType.TEXT),
            TextNode("dog", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter(self):
        node = TextNode("an `unclosed code", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)


