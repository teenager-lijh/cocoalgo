import os
import sys
import re
import argparse

def generate_file_permalink(file_path, permalink):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    content = f'---\npermalink: {permalink}\n---\n' + content

    # 保存修改后的文件
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_folder(folder_path, prefix):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file == 'README.md':
                print(f'Processing file: {file_path}')
                generate_file_permalink(file_path, f'/{prefix}/index.html')
            elif file.endswith('.md'):
                print(f'Processing file: {file_path}')
                timestamp = file_path.split('/')[-2]
                generate_file_permalink(file_path, f'/{prefix}/{timestamp}/index.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate permalink in markdown files.')
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
    all_prefix = []
    with open(config_file, 'r') as file:
        for line in file:
            # 去除行末的换行符并分割字符串
            parts = line.strip().split(' ')
            if len(parts) >= 2:
                all_dir.append(parts[0])
                all_prefix.append(parts[1].replace('SideBar.ts', '').strip())

    for folder, prefix in zip(all_dir, all_prefix):
       process_folder(os.path.join(root, folder), prefix)
 
