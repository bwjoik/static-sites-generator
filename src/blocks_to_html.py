from parentnode import ParentNode
from leafnode import LeafNode
from blocktype import BlockType, block_to_blocktype
from markdown_to_blocks import *
from text_to_textnodes import text_to_textnodes
from text_node_to_html_node import text_node_to_html_node

def text_to_children(text):
    """將一行文字轉換為 HTMLNode 子節點（支援 inline markdown）"""
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []

    for block in blocks:
        block_type = block_to_blocktype(block)

        if block_type == BlockType.PARAGRAPH:
            # 合併多行為單行，並去除每行前後空白
            lines = [line.strip() for line in block.split('\n')]
            paragraph_text = ' '.join([line for line in lines if line])
            children = text_to_children(paragraph_text)
            block_nodes.append(ParentNode("p", children))
        elif block_type == BlockType.HEADING:
            # 計算 heading 等級
            level = 0
            while level < len(block) and block[level] == "#":
                level += 1
            content = block[level:].strip()
            tag = f"h{level}"
            children = text_to_children(content)
            block_nodes.append(ParentNode(tag, children))
        elif block_type == BlockType.CODE:
            code_content = block.strip()
            if code_content.startswith("```"):
                code_content = code_content[3:]
            if code_content.endswith("```"):
                code_content = code_content[:-3]
            # 去除每行開頭的多餘空白
            code_content = "\n".join([line.lstrip() for line in code_content.strip("\n").splitlines()])
            code_node = LeafNode("code", code_content)
            block_nodes.append(ParentNode("pre", [code_node]))
        elif block_type == BlockType.QUOTE:
            # 去除每行開頭的 "> "
            lines = [line.lstrip("> ").rstrip() for line in block.split("\n")]
            quote_text = " ".join(lines)
            children = text_to_children(quote_text)
            block_nodes.append(ParentNode("blockquote", children))
        elif block_type == BlockType.UNORDER_LIST:
            items = [item.lstrip("- ").strip() for item in block.split("\n") if item.strip()]
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            block_nodes.append(ParentNode("ul", li_nodes))
        elif block_type == BlockType.ORDERED_LIST:
            items = [item[item.find('.')+1:].strip() for item in block.split("\n") if item.strip()]
            li_nodes = [ParentNode("li", text_to_children(item)) for item in items]
            block_nodes.append(ParentNode("ol", li_nodes))
        else:
            # fallback: 原樣輸出
            block_nodes.append(LeafNode(None, block))

    return ParentNode("div", block_nodes)