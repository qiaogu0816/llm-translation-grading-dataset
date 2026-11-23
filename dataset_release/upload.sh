#!/usr/bin/env bash
# 在 dataset_release 目录下运行；需先创建 GitHub 仓库并登录 git。
set -e
cd "$(dirname "$0")"
git init -b main
git add .
git commit -m "Add dataset for LLM-assisted translation grading research"
git remote add origin https://github.com/qiaogu0816/llm-translation-grading-dataset.git
git push -u origin main
