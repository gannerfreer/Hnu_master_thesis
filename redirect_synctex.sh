#!/bin/bash
sleep 0.5
# 获取当前工作目录
current_dir=$(pwd)

# 解压缩 synctex 文件
gzip -d *.synctex.gz

# 使用 sed 替换所有的 workspace 字段
escaped_dir=$(echo "$current_dir" | sed 's/\//\\\//g')
sed -i "s/\/workspace/${escaped_dir}/g" *.synctex

# 压缩回 synctex 文件
gzip *.synctex