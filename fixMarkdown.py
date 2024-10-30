import os
import sys
import re
import argparse

def fix_image_paths(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 处理 HTML <img> 标签中的 src 属性
    img_tag_pattern = r'<img\s+[^>]*src=["\']([^"\']+)["\']'
    def replace_img_tag(match):
        src = match.group(1)
        if not src.startswith('http') and not src.startswith('./') and not src.startswith('/'):
            return match.group(0).replace(src, './' + src)
        return match.group(0)
    
    content = re.sub(img_tag_pattern, replace_img_tag, content)

    # 处理 Markdown 图片插入语法 ![](src)
    markdown_img_pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    def replace_markdown_img(match):
        src = match.group(1)
        if not src.startswith('http') and not src.startswith('./') and not src.startswith('/'):
            return match.group(0).replace(src, './' + src)
        return match.group(0)

    content = re.sub(markdown_img_pattern, replace_markdown_img, content)

    # 保存修改后的文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_folder(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                print(f'Processing file: {file_path}')
                fix_image_paths(file_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fix image paths in markdown files.')
    parser.add_argument('root', type=str, help='The folder path to process')
    args = parser.parse_args()


    root = args.root 

    # 检查 config.list 文件是否存在
    config_file = os.path.join(root, 'config.list')
    if not os.path.isfile(config_file):
        print(f"Error: {config_file} does not exist.")
        sys.exit(1)

    # 读取 config.list 文件并提取第一个字符串
    all_dir = []
    with open(config_file, 'r') as file:
        for line in file:
            # 去除行末的换行符并分割字符串
            parts = line.strip().split(' ')
            if len(parts) >= 1:
                all_dir.append(parts[0])

    for folder in all_dir:
       process_folder(os.path.join(root, folder))
 
