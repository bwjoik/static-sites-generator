import unittest
from blocktype  import BlockType, block_to_blocktype

class TestBlockType(unittest.TestCase):
    def test_paragraph(self):
        markdown = "This is a paragraph."
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_blocktype(markdown), expected)
    
    def test_heading(self):
        markdown = "# This is a heading"
        expected = BlockType.HEADING
        self.assertEqual(block_to_blocktype(markdown), expected)

    def test_code(self):
        markdown = "```python\nprint('Hello, World!')\n"
        expected = BlockType.CODE
        self.assertEqual(block_to_blocktype(markdown), expected)
        
    def test_quote(self):
        markdown = "> This is a quote."
        expected = BlockType.QUOTE
        
    def test_ordered_list(self):
        markdown = "1. This is an ordered list item /n 2. Another ordered list item"
        expected = BlockType.ORDERED_LIST
        self.assertEqual(block_to_blocktype(markdown), expected)
        
    def test_unordered_list(self): 
        markdown = "- This is an unordered list item\n- Another unordered list item"
        expected = BlockType.UNORDER_LIST
        self.assertEqual(block_to_blocktype(markdown), expected)