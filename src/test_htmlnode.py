import unittest
from htmlnode import HTMLNode

class test_htmlnode(unittest.TestCase):
    def test_htmlnode_eq(self):
        node = HTMLNode("p", "This is a html node", [1,2,3], {"href": "https://example.com", "target": "_blank"})
        node2 = HTMLNode("p", "This is a html node", [1,2,3], {"href": "https://example.com", "target": "_blank"})
        assert node == node2

    def test_htmlnode_not_eq(self):

        node = HTMLNode("p", "This is a html node", [1,2,3], {"href": "https://example.com", "target": "_blank"})
        node2 = HTMLNode("div", "This is a different html node", [4,5,6], {"href": "https://example.com", "target": "_blank"})
        assert node != node2

    def test_htmlnode_no_url(self):
        
        node = HTMLNode("p", "This is a html node", [1,2,3])
        assert node.props is None