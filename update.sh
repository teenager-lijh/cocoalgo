#!/bin/bash

export PATH=/root/.nvm/versions/node/v16.20.2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$PATH

# 检查是否提供了路径参数
if [ -z "$1" ]; then
    echo "请提供一个 Git 仓库目录路径作为参数。"
    exit 1
fi

# 获取传入的 Git 仓库路径
REPO_DIR=$1

# 检查目录是否存在
if [ ! -d "$REPO_DIR" ]; then
    echo "指定的目录不存在。"
    exit 1
fi

# 进入 Git 仓库目录
cd "$REPO_DIR" || exit

# 检查是否是一个 Git 仓库
if [ ! -d ".git" ]; then
    echo "指定的目录不是一个 Git 仓库。"
    exit 1
fi

# 拉取远程 main 分支的最新代码
echo "正在拉取远程 main 分支的代码..."
git fetch origin main
# 检查是否有新的代码需要拉取
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/main)

if [ "$LOCAL" = "$REMOTE" ]; then
    echo "本地仓库已经是最新，无需更新。"
else
    echo "发现新的代码，开始拉取..."
    git pull origin main
    if [ $? -ne 0 ]; then
        echo "拉取失败，请检查问题。"
        exit 1
    fi

    # 拉取成功后，执行 npm run docs:build 命令
    echo "代码拉取成功，开始构建文档..."
    echo "switch to main"
    git switch main 
    
    echo "fix markdown"
    python3 fixMarkdown.py $1
    
    echo "generatePermalink"
    python3 generatePermalink.py $1
    
    echo "generateConfig"
    python3 generateConfig.py $1 
    
    echo "build dist"
    npm run docs:build
    
    echo "resize image files"
    python3 resizeImageFiles.py $1 
    
    echo "checkout files which are modified"
    git checkout .
    
    echo "clean files in git workspace"
    git clean -fd
    
    if [ $? -ne 0 ]; then
        echo "文档构建失败。"
        exit 1
    fi
    echo "1 -> 9 OK!"
fi

echo "脚本执行完毕。"
exit 0
