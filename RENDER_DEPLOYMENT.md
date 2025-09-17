# 🚀 Render部署指南

## 部署步骤

### 1. 注册Render账户
- 访问 [https://render.com](https://render.com)
- 使用GitHub账户登录

### 2. 连接GitHub仓库
- 点击 "New +" → "Web Service"
- 选择仓库：`coolkidhugh/picwork`
- 选择分支：`master`

### 3. 配置部署设置
- **Name**: `maoloujiji`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
- **Plan**: `Free`

### 4. 环境变量（可选）
- `PYTHON_VERSION`: `3.11.0`

### 5. 部署
- 点击 "Create Web Service"
- 等待部署完成（约5-10分钟）

## 部署后访问
- 应用URL: `https://maoloujiji.onrender.com`
- 首次访问可能需要等待几秒钟启动

## 注意事项
- Render免费版有休眠机制，首次访问可能较慢
- 如果应用休眠，访问时会自动唤醒
- 建议升级到付费版以获得更好的性能

## 故障排除
1. **部署失败**: 检查requirements.txt中的依赖
2. **应用无法启动**: 检查start.sh脚本权限
3. **访问超时**: 等待应用完全启动后再访问
