from textnode import *
from htmlnode import *
print("hello world")

def main():
    ntn = TextNode("This is some anchor text", "LINK", "https://www.boot.dev")
    print(f"TextNode(text: {ntn.text}, text_type: {ntn.text_type}, url: {ntn.url})")
    
    
    nhn = HTMLNode("a", "This is an anchor", None, {"href": "https://www.boot.dev", "target": "_blank"})
    print(f"HTMLNode(tag: {nhn.tag}, value: {nhn.value}, children: {nhn.children}, props: {nhn.props})")
    
if __name__ == "__main__":
    main()
    

