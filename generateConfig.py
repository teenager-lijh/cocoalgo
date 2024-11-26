import os
import sys

def parse_config_list(config_file_path):
    config_data = []
    with open(config_file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                config_data.append({
                    'subdirectory': parts[0],  # 子目录名
                    'alias': parts[1],         # 别名
                    'title': parts[2],         # 标题
                })
    return config_data

def find_markdown_files(directory):
    markdown_files = []
    # 遍历目录下的所有子目录和文件
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md') and file != 'README.md':  # 排除 README.md 文件
                # 拼接相对路径，忽略顶层目录名，只保留子路径
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                markdown_files.append(relative_path)
    return markdown_files

def generate_sidebar_content(title, markdown_files):
    # 按照题目的格式生成 sidebar 文件内容
    children_entries = [f'"{md}"' for md in markdown_files]
    children_str = ',\n        '.join(children_entries)
    
    sidebar_template = f"""
export default [
    "",
    {{
      title: "{title}",
      collapsable: false,
      children: [
        {children_str}
      ],
    }},
  ];
"""
    return sidebar_template.strip()

def create_sidebar_files(root_dir, config_list):
    # 确保输出目录存在
    output_dir = os.path.join(root_dir, '.vuepress', 'sidebars')
    os.makedirs(output_dir, exist_ok=True)
    
    sidebar_imports = []
    sidebar_routes = []
    
    # 遍历 config.list 中的每一项
    for entry in config_list:
        subdirectory_path = os.path.join(root_dir, entry['subdirectory'])
        markdown_files = find_markdown_files(subdirectory_path)
        
        # 生成对应的文件内容
        sidebar_content = generate_sidebar_content(entry['title'], markdown_files)
        
        # 将内容写入对应别名命名的文件
        output_file_path = os.path.join(output_dir, entry['alias'])  # 直接使用别名命名文件，不加后缀
        with open(output_file_path, 'w') as output_file:
            output_file.write(sidebar_content)
        print(f"Generated sidebar file: {output_file_path}")
        
        # 准备生成 sidebar.ts 文件的导入和路由
        alias_without_extension = entry['alias'].split('.')[0]  # 别名就是我们生成的文件名（无后缀）
        sidebar_imports.append(f"import {alias_without_extension} from \"./sidebars/{alias_without_extension}\"")
        sidebar_routes.append(f'    "/{entry["subdirectory"]}/": {alias_without_extension}')

    # 生成 sidebar.ts 文件内容
    generate_sidebar_ts(root_dir, sidebar_imports, sidebar_routes)

def generate_sidebar_ts(root_dir, imports, routes):
    ts_content = """import { SidebarConfig4Multiple } from "vuepress/config";

""" + ";\n".join(imports) + ";\n" + """
// @ts-ignore
export default {
""" + ",\n".join(routes) + ",\n" + """
    "/": "auto",
} as SidebarConfig4Multiple;
"""

    ts_file_path = os.path.join(root_dir, '.vuepress', 'sidebar.ts')
    with open(ts_file_path, 'w') as ts_file:
        ts_file.write(ts_content)
    print(f"Generated sidebar.ts file: {ts_file_path}")

def generate_navbar(root_dir, config_list):
    navbar_items = []
    
    for entry in config_list:
        navbar_items.append(f"""
    {{
        text: "{entry['subdirectory']}",
        link: '/{entry['alias'].replace('SideBar.ts', '').strip()}/index.html'
    }}""")
    
    # 格式化 navbar.ts 文件的内容
    navbar_content = """import { NavItem } from "vuepress/config";

export default [
""" + ",\n".join(navbar_items) + "\n" """
] as NavItem[];
"""

    navbar_file_path = os.path.join(root_dir, '.vuepress', 'navbar.ts')
    with open(navbar_file_path, 'w') as navbar_file:
        navbar_file.write(navbar_content)
    print(f"Generated navbar.ts file: {navbar_file_path}")

if __name__ == "__main__":
    import sys

    # 检查命令行参数的数量
    if len(sys.argv) > 1:
        # 读取第一个参数并赋值给变量 root
        root = sys.argv[1]
        print("The root variable is set to:", root)
    else:
        print("No command line argument provided.")

    # config.list 文件路径
    config_list_path = os.path.join(root, 'config.list')
    
    # 解析 config.list 文件
    config_data = parse_config_list(config_list_path)

    # 创建 sidebar 文件
    create_sidebar_files(root, config_data)

    # 创建 navbar 文件
    generate_navbar(root, config_data)
