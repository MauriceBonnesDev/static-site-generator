from os.path import isfile
from markdown_blocks import markdown_to_html_node
from textnode import TextNode, TextType
import os
import shutil
import sys

def main():
    basepath = sys.argv[1] if sys.argv[1] != "" else "/"
    src= "static"
    dst = "docs"

    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.mkdir(dst)

    copy_files(src, dst)
    dir_path_content = "content"

    generate_pages_recursive(dir_path_content, "template.html", dst, basepath)

def copy_files(src, dst):
    if os.path.isfile(src):
        return shutil.copy(src, dst)
    
    for sub_dir in os.listdir(src):
        path = os.path.join(src, sub_dir)
        out_dir = dst
        if not os.path.isfile(path):
            out_dir = os.path.join(dst, sub_dir)
            os.mkdir(out_dir)
        copy_files(path, out_dir)

def extract_title(markdown):
    lines = markdown.split("\n")
    heading = ""
    for line in lines:
        if line.startswith("# "):
            heading = line[2:].strip()
    if heading == "":
        raise Exception("h1 is missing")
    return heading

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown = ""
    template = ""
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", html).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    full_dest_path = os.path.join(dest_path, "index.html")
    os.makedirs(dest_path, exist_ok=True)
    with open(full_dest_path, "w") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if os.path.isfile(dir_path_content):
        return generate_page(dir_path_content, template_path, dest_dir_path, basepath)

    for sub_dir in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, sub_dir)
        out_dir = dest_dir_path
        if not os.path.isfile(path):
            out_dir = os.path.join(dest_dir_path, sub_dir)
            os.mkdir(out_dir)
        print(f"Recursively calling generate_pages_recursive with {path} at {out_dir} using {template_path}")
        generate_pages_recursive(path, template_path, out_dir, basepath)


main()
