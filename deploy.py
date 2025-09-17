#!/usr/bin/env python3
"""
快速部署脚本
帮助用户快速将应用部署到GitHub和Streamlit Cloud
"""

import os
import subprocess
import sys

def run_command(command):
    """运行命令并返回结果"""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ 成功: {command}")
            return True
        else:
            print(f"❌ 失败: {command}")
            print(f"错误: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ 执行失败: {command}")
        print(f"错误: {str(e)}")
        return False

def check_git():
    """检查Git是否已安装"""
    return run_command("git --version")

def check_files():
    """检查必要文件是否存在"""
    required_files = [
        "app.py",
        "data_extractor.py", 
        "requirements.txt",
        ".streamlit/config.toml",
        "README.md"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ 缺少必要文件:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print("✅ 所有必要文件都存在")
        return True

def init_git():
    """初始化Git仓库"""
    if not os.path.exists(".git"):
        print("🔧 初始化Git仓库...")
        return run_command("git init")
    else:
        print("✅ Git仓库已存在")
        return True

def add_files():
    """添加文件到Git"""
    print("📁 添加文件到Git...")
    return run_command("git add .")

def commit_changes():
    """提交更改"""
    print("💾 提交更改...")
    return run_command('git commit -m "Deploy: Hotel booking data analysis tool"')

def setup_remote():
    """设置远程仓库"""
    print("🌐 设置远程仓库...")
    print("请输入您的GitHub仓库URL (例如: https://github.com/username/repo-name.git)")
    repo_url = input("仓库URL: ").strip()
    
    if repo_url:
        return run_command(f"git remote add origin {repo_url}")
    else:
        print("❌ 未提供仓库URL")
        return False

def push_to_github():
    """推送到GitHub"""
    print("🚀 推送到GitHub...")
    return run_command("git branch -M main") and run_command("git push -u origin main")

def main():
    """主函数"""
    print("🏨 酒店预订数据分析工具 - 部署助手")
    print("=" * 50)
    
    # 检查环境
    if not check_git():
        print("❌ 请先安装Git")
        sys.exit(1)
    
    if not check_files():
        print("❌ 请确保所有必要文件都存在")
        sys.exit(1)
    
    # 部署流程
    steps = [
        ("初始化Git仓库", init_git),
        ("添加文件", add_files),
        ("提交更改", commit_changes),
        ("设置远程仓库", setup_remote),
        ("推送到GitHub", push_to_github)
    ]
    
    for step_name, step_func in steps:
        print(f"\n📋 {step_name}...")
        if not step_func():
            print(f"❌ {step_name}失败，部署中止")
            sys.exit(1)
    
    print("\n🎉 部署完成！")
    print("\n📝 下一步:")
    print("1. 访问 https://share.streamlit.io/")
    print("2. 点击 'New app'")
    print("3. 连接您的GitHub账户")
    print("4. 选择刚创建的仓库")
    print("5. 设置Main file path为: app.py")
    print("6. 点击 'Deploy!'")
    print("\n🔗 部署完成后，您将获得一个在线应用链接")

if __name__ == "__main__":
    main()
