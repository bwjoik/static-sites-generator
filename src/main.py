from textnode import *
from htmlnode import *
import shutil
import os
from copytree import copytree
from gen_page import *
print("hello world")

def main():
    #delete file in public folder
    for filename in os.listdir('public'):
        filepath = os.path.join('public', filename)
    #copy static files to public folder
    copytree("static","public")
    #generate pages from markdown files
    generate_pages_recursive("content", "template.html", "public")
    
    
    
    
    
if __name__ == "__main__":
    main()
    

