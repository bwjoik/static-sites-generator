from enum import Enum
import re
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDER_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_blocktype(markdown):
    if markdown.startswith("#"):
        return BlockType.HEADING
    elif markdown.startswith('```'):
        return BlockType.CODE
    elif markdown.startswith('> '): 
        return BlockType.QUOTE
    elif markdown.startswith('- '):
        return BlockType.UNORDER_LIST
    elif markdown.startswith('1. '):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    