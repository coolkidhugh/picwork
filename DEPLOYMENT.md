# 🚀 部署指南

## GitHub + Streamlit Cloud 部署步骤

### 1. 上传到GitHub

1. **创建GitHub仓库**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Hotel booking data analysis tool"
   git branch -M main
   git remote add origin https://github.com/your-username/your-repo-name.git
   git push -u origin main
   ```

2. **确保包含以下文件**：
   - `app.py` - 主应用文件
   - `data_extractor.py` - 数据提取模块
   - `requirements.txt` - 依赖包
   - `.streamlit/config.toml` - Streamlit配置
   - `README.md` - 说明文档

### 2. 部署到Streamlit Cloud

1. **访问 [Streamlit Cloud](https://share.streamlit.io/)**
2. **点击 "New app"**
3. **连接GitHub账户**
4. **选择仓库和分支**
5. **设置应用配置**：
   - **Main file path**: `app.py`
   - **App URL**: 自定义URL（可选）
6. **点击 "Deploy!"**

### 3. 配置说明

#### Streamlit配置 (`.streamlit/config.toml`)
```toml
[theme]
primaryColor = "#00ff00"
backgroundColor = "#0d1117"
secondaryBackgroundColor = "#1e1e1e"
textColor = "#00ff00"
font = "monospace"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = false

[browser]
gatherUsageStats = false
```

#### 依赖包 (requirements.txt)
```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.24.0
Pillow>=9.5.0
pytesseract>=0.3.10
opencv-python>=4.8.0
plotly>=5.15.0
python-dateutil>=2.8.0
```

### 4. 注意事项

#### OCR功能限制
- **Streamlit Cloud不支持Tesseract OCR**
- 需要修改代码以支持云端部署
- 建议使用在线OCR API替代

#### 替代方案
1. **使用Google Vision API**
2. **使用Azure Computer Vision**
3. **使用AWS Textract**
4. **使用在线OCR服务**

### 5. 本地运行

如果需要本地运行（支持OCR）：

```bash
# 安装依赖
pip install -r requirements.txt

# 安装Tesseract OCR
# Windows: 下载安装包
# macOS: brew install tesseract tesseract-lang
# Linux: sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim

# 运行应用
streamlit run app.py
```

### 6. 更新应用

每次更新代码后：
```bash
git add .
git commit -m "Update: description of changes"
git push origin main
```

Streamlit Cloud会自动重新部署应用。

## 🔧 故障排除

### 常见问题

1. **应用无法启动**
   - 检查 `requirements.txt` 中的依赖版本
   - 确保 `app.py` 文件路径正确

2. **OCR功能不工作**
   - Streamlit Cloud不支持本地OCR
   - 需要集成在线OCR服务

3. **样式不生效**
   - 检查 `.streamlit/config.toml` 配置
   - 确保CSS样式正确加载

### 联系支持

如果遇到问题，请：
1. 检查Streamlit Cloud的部署日志
2. 查看GitHub Issues
3. 联系技术支持
