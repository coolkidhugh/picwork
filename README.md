# 🏨 酒店预订数据分析工具

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)

这是一个基于Streamlit的酒店预订数据分析工具，可以自动识别和分析酒店预订数据图片，生成可视化表格和比较分析。

## 🚀 在线演示

[点击这里访问在线应用](https://your-app-name.streamlit.app)

## 📸 界面预览

应用采用代码编辑器风格的深色主题，提供专业的用户体验。

## 功能特点

### 1. 单张图片分析
- 📸 上传酒店预订数据图片
- 🔍 自动OCR识别和数据提取
- 📊 生成可视化表格和图表
- 📝 自动生成总结语句
- 📈 显示详细统计信息

### 2. 两张图片比较
- 🔄 比较不同图片的数据差异
- 📊 分析房数、房型、定价变化
- 📈 生成对比图表
- 💰 显示价格变化详情

### 3. 智能数据识别
- 🏢 自动识别预订类型：
  - CON开头：会议预订
  - FIT开头：散客预订
  - 月份英文开头：旅游预订
- 📋 按房数大小自动排序
- 💡 智能生成业务总结

## 安装和运行

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 安装Tesseract OCR
- **Windows**: 下载并安装 [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)
- **macOS**: `brew install tesseract tesseract-lang`
- **Linux**: `sudo apt-get install tesseract-ocr tesseract-ocr-chi-sim`

### 3. 运行应用
```bash
streamlit run app.py
```

## 使用说明

### 单张图片分析
1. 在"单张图片分析"标签页上传图片
2. 点击"分析数据"按钮
3. 查看生成的可视化表格和图表
4. 阅读自动生成的总结语句

### 两张图片比较
1. 先上传第一张图片并分析
2. 再上传第二张图片并分析
3. 切换到"两张图片比较"标签页
4. 查看数据差异和对比图表

## 支持的数据格式

应用支持识别包含以下信息的酒店预订数据表格：
- 预订ID（CON/FIT/月份英文开头）
- 房型代码（支持以下所有房型）：
  - **D系列**: DKN, DKS, DQN, DQS, DSKN, DSTN, DTN, DETN
  - **E系列**: EKN, EKS, ETN, ETS, ESN, ESS
  - **J系列**: JKN, JDKN, JDKS, JEKN, JETN, JETS, JTN, JTS, JLKN, JESN, JESS, JDEN
  - **S系列**: SKN, SQS, SQN, STN, STS, OTN, SSN, SSS
  - **VC系列**: VCKD, VCKN
  - **F系列**: FSB, FSC, FSN
  - **R系列**: RSN
  - **PS系列**: PSA, PSB, PSC, PSD
- 房数统计
- 价格信息
- 到达/离开时间
- 包价代码
- 标志信息

## 技术栈

- **前端**: Streamlit
- **数据处理**: Pandas, NumPy
- **图像处理**: OpenCV, Pillow
- **OCR识别**: Tesseract
- **可视化**: Plotly
- **语言支持**: 中文简体 + 英文

## 文件结构

```
├── app.py                 # 主应用文件
├── data_extractor.py      # 数据提取模块
├── requirements.txt       # 依赖包列表
└── README.md             # 说明文档
```

## 注意事项

1. 确保上传的图片清晰，包含完整的预订数据表格
2. 支持PNG、JPG、JPEG格式的图片
3. OCR识别效果取决于图片质量和清晰度
4. 建议图片中的文字大小适中，对比度良好

## 示例数据

应用可以处理类似以下格式的酒店预订数据：

| 状态 | 姓名 | 房类 | 房数 | 定价 | 到达 | 离开 | 天 |
|------|------|------|------|------|------|------|-----|
| R | CON25625/麦尔会展 | DKN | 25 | 520.00 | 12/19 18:00 | 12/21 12:00 | 2 |
| R | CON25625/麦尔会展 | EKN | 20 | 580.00 | 12/19 18:00 | 12/21 12:00 | 2 |
| R | CON25625/麦尔会展 | JKN | 30 | 650.00 | 12/19 18:00 | 12/21 12:00 | 2 |
| R | CON25625/麦尔会展 | VCKN | 10 | 750.00 | 12/19 18:00 | 12/21 12:00 | 2 |
| R | CON25625/麦尔会展 | PSA | 12 | 600.00 | 12/19 18:00 | 12/21 12:00 | 2 |

## 故障排除

### OCR识别不准确
- 检查图片清晰度
- 确保文字对比度良好
- 尝试调整图片大小

### 数据提取失败
- 确认图片包含完整的表格数据
- 检查图片格式是否支持
- 查看控制台错误信息

### 依赖安装问题
- 确保Python版本 >= 3.8
- 检查Tesseract是否正确安装
- 验证所有依赖包版本兼容性
