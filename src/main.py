from textnode import *
from htmlnode import *
import shutil
import os
from copytree import copytree
from gen_page import *
import sys
print("hello world")

def main():
    basepath = sys.argv[0]
    #delete file in docs folder
    for filename in os.listdir('docs'):
        filepath = os.path.join('docs', filename)
    #copy static files to docs folder
    copytree("static","docs")
    #generate pages from markdown files
    
    generate_pages_recursive("content", "template.html", "docs", basepath)
    
    
    
    
    
if __name__ == "__main__":
    main()
    

