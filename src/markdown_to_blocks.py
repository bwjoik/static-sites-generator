def markdown_to_blocks(markdown):
    res = markdown.split("\n\n")
    res = [block.strip() for block in res]
    return [block for block in res if block]
