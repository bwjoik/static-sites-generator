from blocks_to_html import *
import os
def extract_title(markdown):
    for line in markdown.splitlines():
        if line.strip().startswith("# "):
            return line.strip()[2:].strip()
    raise Exception("No h1 header found in markdown")

def generate_page(from_path, template_path, dest_path, basepath = "/"):
    print(f"Generating page from {from_path} using {template_path} to {dest_path}")
    # 讀取 markdown 檔案
    with open(from_path, "r") as f:
        markdown = f.read()
    # 讀取 template 檔案
    with open(template_path, "r") as f:
        template = f.read()
    # 產生 HTML 內容
    html_string = markdown_to_html_node(markdown).to_html()
    # 取得標題
    title = extract_title(markdown)
    # 替換 template 變數
    html_with_placeholders = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    # 這裡進行 href 與 src 的替換
    html_with_placeholders = html_with_placeholders.replace('href="/', f'href="{basepath}')
    html_with_placeholders = html_with_placeholders.replace('src="/', f'src="{basepath}')
    print(f"Generated page: {dest_path}")
    with open(dest_path, "w") as f:
        f.write(html_with_placeholders)
        
def generate_pages_recursive(dir_path, template_path, dest_dir, basepath = "/"):
    for filename in os.listdir(dir_path):
        src_path = os.path.join(dir_path, filename)
        dest_path = os.path.join(dest_dir, filename)
        if os.path.isdir(src_path):
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            generate_pages_recursive(src_path, template_path, dest_path)
        elif filename.endswith(".md"):
            dest_html = os.path.splitext(dest_path)[0] + ".html"
            generate_page(src_path, template_path, dest_html)