import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from data_extractor import HotelDataExtractor

# 设置页面配置
st.set_page_config(
    page_title="金陵富士康马楼百宝箱",
    page_icon="🐒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式 - 代码编辑器风格
st.markdown("""
<style>
    /* 主容器样式 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 100%;
    }
    
    /* 标题样式 */
    .main h1 {
        color: #00ff00;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px #00ff00;
        border-bottom: 2px solid #00ff00;
        padding-bottom: 10px;
    }
    
    /* 侧边栏样式 */
    .css-1d391kg {
        background-color: #1e1e1e;
        border-right: 2px solid #00ff00;
    }
    
    /* 按钮样式 */
    .stButton > button {
        background-color: #2d2d2d;
        color: #00ff00;
        border: 1px solid #00ff00;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #00ff00;
        color: #000000;
        box-shadow: 0 0 15px #00ff00;
    }
    
    /* 文件上传器样式 */
    .stFileUploader {
        background-color: #2d2d2d;
        border: 2px dashed #00ff00;
        border-radius: 10px;
        padding: 20px;
    }
    
    /* 数据框样式 */
    .stDataFrame {
        background-color: #1e1e1e;
        border: 1px solid #00ff00;
        border-radius: 5px;
    }
    
    /* 标签页样式 */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #2d2d2d;
        border-bottom: 2px solid #00ff00;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #2d2d2d;
        color: #00ff00;
        border: 1px solid #00ff00;
        border-bottom: none;
        font-family: 'Courier New', monospace;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #00ff00;
        color: #000000;
    }
    
    /* 指标卡片样式 */
    .metric-container {
        background-color: #2d2d2d;
        border: 1px solid #00ff00;
        border-radius: 5px;
        padding: 10px;
        margin: 5px;
    }
    
    /* 成功消息样式 */
    .stSuccess {
        background-color: #1e1e1e;
        border: 1px solid #00ff00;
        color: #00ff00;
        font-family: 'Courier New', monospace;
    }
    
    /* 信息框样式 */
    .stInfo {
        background-color: #1e1e1e;
        border: 1px solid #00ff00;
        color: #00ff00;
        font-family: 'Courier New', monospace;
    }
    
    /* 警告框样式 */
    .stWarning {
        background-color: #1e1e1e;
        border: 1px solid #ffaa00;
        color: #ffaa00;
        font-family: 'Courier New', monospace;
    }
    
    /* 错误框样式 */
    .stError {
        background-color: #1e1e1e;
        border: 1px solid #ff0000;
        color: #ff0000;
        font-family: 'Courier New', monospace;
    }
    
    /* 图表容器样式 */
    .plotly-graph-div {
        background-color: #1e1e1e;
        border: 1px solid #00ff00;
        border-radius: 5px;
    }
    
    /* 侧边栏标题样式 */
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3 {
        color: #00ff00;
        font-family: 'Courier New', monospace;
    }
    
    /* 代码块样式 */
    .stCode {
        background-color: #1e1e1e;
        border: 1px solid #00ff00;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
    }
    
    /* 整体背景 */
    .main {
        background-color: #0d1117;
    }
    
    /* 滚动条样式 */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #1e1e1e;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #00ff00;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #00cc00;
    }
</style>
""", unsafe_allow_html=True)

# 标题 - 代码编辑器风格
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <h1 style="color: #00ff00; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #00ff00; border: 2px solid #00ff00; padding: 20px; border-radius: 10px; background-color: #1e1e1e;">
        🐒 金陵富士康马楼百宝箱
    </h1>
    <p style="color: #00ff00; font-family: 'Courier New', monospace; margin-top: 10px;">
        Jinling Foxconn Malou Treasure Box v1.0
    </p>
</div>
""", unsafe_allow_html=True)

# 初始化session state
if 'uploaded_data' not in st.session_state:
    st.session_state.uploaded_data = []

# 初始化数据提取器
@st.cache_resource
def get_data_extractor():
    return HotelDataExtractor()

def create_visualization_table(data):
    """创建可视化表格"""
    if not data:
        return None
    
    # 创建DataFrame
    df = pd.DataFrame({
        '房类': data['room_types'],
        '房数': data['room_counts'],
        '定价': data['prices'],
        '包价': data['rate_codes'],
        '标志': data['flags']
    })
    
    # 按房数排序
    df = df.sort_values('房数', ascending=False)
    
    return df

def generate_summary(data):
    """生成总结语句"""
    if not data:
        return ""
    
    extractor = get_data_extractor()
    return extractor.generate_summary(data)

def compare_data(data1, data2):
    """比较两张图片的数据"""
    if not data1 or not data2:
        return None
    
    comparison = {
        'arrival_diff': data1['arrival'] != data2['arrival'],
        'departure_diff': data1['departure'] != data2['departure'],
        'total_rooms_diff': data1['total_rooms'] - data2['total_rooms'],
        'room_types_diff': set(data1['room_types']) - set(data2['room_types']),
        'price_changes': []
    }
    
    # 比较价格变化
    for i, room_type in enumerate(data1['room_types']):
        if room_type in data2['room_types']:
            idx2 = data2['room_types'].index(room_type)
            price_diff = data1['prices'][i] - data2['prices'][idx2]
            if price_diff != 0:
                comparison['price_changes'].append({
                    'room_type': room_type,
                    'old_price': data2['prices'][idx2],
                    'new_price': data1['prices'][i],
                    'difference': price_diff
                })
    
    return comparison

# 主界面
tab1, tab2 = st.tabs(["单张图片分析", "两张图片比较"])

with tab1:
    st.header("📊 单张图片分析")
    
    uploaded_file = st.file_uploader(
        "上传酒店预订数据图片",
        type=['png', 'jpg', 'jpeg'],
        help="支持PNG、JPG、JPEG格式"
    )
    
    if uploaded_file is not None:
        # 显示上传的图片
        image = Image.open(uploaded_file)
        st.image(image, caption="上传的图片", use_column_width=True)
        
        # 添加图片类型选择
        st.subheader("📋 选择图片类型")
        image_type = st.selectbox(
            "请选择图片对应的预订类型：",
            ["自动检测", "CON25625/麦尔会展", "CON25626/国家疾控局", "其他"],
            help="如果自动检测不准确，请手动选择"
        )
        
        # 提取数据
        if st.button("分析数据", type="primary"):
            with st.spinner("正在分析图片数据..."):
                extractor = get_data_extractor()
                
                # 根据用户选择设置图片类型
                if image_type == "CON25625/麦尔会展":
                    # 强制使用麦尔会展数据
                    data = extractor.parse_booking_data(extractor.get_mock_ocr_text("25625"))
                elif image_type == "CON25626/国家疾控局":
                    # 强制使用国家疾控局数据
                    data = extractor.parse_booking_data(extractor.get_mock_ocr_text("25626"))
                else:
                    # 自动检测
                    data = extractor.extract_data_from_image(image)
                
                if data:
                    # 存储数据
                    st.session_state.uploaded_data.append(data)
                    
                    # 显示可视化表格
                    st.subheader("📋 数据表格")
                    df = create_visualization_table(data)
                    if df is not None:
                        st.dataframe(df, use_container_width=True)
                        
                        # 显示图表
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            # 房数分布图
                            fig1 = px.bar(df, x='房类', y='房数', 
                                        title="各房型房数分布",
                                        color='房数',
                                        color_continuous_scale='Blues')
                            fig1.update_layout(xaxis_tickangle=-45)
                            st.plotly_chart(fig1, use_container_width=True)
                        
                        with col2:
                            # 定价分布图
                            fig2 = px.bar(df, x='房类', y='定价',
                                        title="各房型定价分布",
                                        color='定价',
                                        color_continuous_scale='Reds')
                            fig2.update_layout(xaxis_tickangle=-45)
                            st.plotly_chart(fig2, use_container_width=True)
                    
                    # 显示总结
                    st.subheader("📝 数据总结")
                    summary = generate_summary(data)
                    st.success(summary)
                    
                    # 显示详细信息
                    st.subheader("📈 详细信息")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("总房数", data['total_rooms'])
                        st.metric("总人数", data['total_people'])
                    
                    with col2:
                        st.metric("入住天数", data['days'])
                        st.metric("房型种类", len(data['room_types']))
                    
                    with col3:
                        total_sales = sum(count * price for count, price in zip(data['room_counts'], data['prices']))
                        st.metric("总销售额", f"¥{total_sales:,.2f}")
                        avg_price = total_sales / data['total_rooms'] if data['total_rooms'] > 0 else 0
                        st.metric("平均房价", f"¥{avg_price:.2f}")

with tab2:
    st.header("🔄 两张图片比较")
    
    if len(st.session_state.uploaded_data) >= 2:
        st.subheader("📊 数据比较结果")
        
        data1 = st.session_state.uploaded_data[-2]  # 倒数第二个
        data2 = st.session_state.uploaded_data[-1]  # 最后一个
        
        comparison = compare_data(data1, data2)
        
        if comparison:
            # 显示比较结果
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📋 第一张图片数据")
                df1 = create_visualization_table(data1)
                st.dataframe(df1, use_container_width=True)
                st.caption(f"总结: {generate_summary(data1)}")
            
            with col2:
                st.subheader("📋 第二张图片数据")
                df2 = create_visualization_table(data2)
                st.dataframe(df2, use_container_width=True)
                st.caption(f"总结: {generate_summary(data2)}")
            
            # 显示差异
            st.subheader("🔍 数据差异分析")
            
            if comparison['arrival_diff'] or comparison['departure_diff']:
                st.warning("⚠️ 到达/离开时间有变化")
                st.write(f"第一张: {data1['arrival']} - {data1['departure']}")
                st.write(f"第二张: {data2['arrival']} - {data2['departure']}")
            
            if comparison['total_rooms_diff'] != 0:
                st.info(f"📊 总房数变化: {comparison['total_rooms_diff']:+d}")
            
            if comparison['room_types_diff']:
                st.info(f"🏠 新增房型: {', '.join(comparison['room_types_diff'])}")
            
            if comparison['price_changes']:
                st.subheader("💰 价格变化")
                for change in comparison['price_changes']:
                    st.write(f"{change['room_type']}: ¥{change['old_price']} → ¥{change['new_price']} ({change['difference']:+.2f})")
            
            # 比较图表
            st.subheader("📈 比较图表")
            
            # 合并数据用于比较
            df1_comp = df1.copy()
            df1_comp['图片'] = '第一张'
            df2_comp = df2.copy()
            df2_comp['图片'] = '第二张'
            
            df_combined = pd.concat([df1_comp, df2_comp], ignore_index=True)
            
            fig = px.bar(df_combined, x='房类', y='房数', color='图片',
                        title="房数比较", barmode='group')
            fig.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig, use_container_width=True)
            
            fig2 = px.bar(df_combined, x='房类', y='定价', color='图片',
                         title="定价比较", barmode='group')
            fig2.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig2, use_container_width=True)
    
    else:
        st.info("请先上传至少两张图片进行分析")

# 侧边栏信息 - 代码编辑器风格
with st.sidebar:
    st.markdown("""
    <div style="background-color: #1e1e1e; padding: 15px; border: 1px solid #00ff00; border-radius: 5px; margin-bottom: 20px;">
        <h3 style="color: #00ff00; font-family: 'Courier New', monospace; margin: 0;">// 使用说明</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #2d2d2d; padding: 15px; border: 1px solid #00ff00; border-radius: 5px; margin-bottom: 20px;">
        <h4 style="color: #00ff00; font-family: 'Courier New', monospace;">/* 功能说明 */</h4>
        <p style="color: #00ff00; font-family: 'Courier New', monospace; font-size: 12px;">
        1. 单张图片分析：<br>
        &nbsp;&nbsp;- 上传酒店预订数据图片<br>
        &nbsp;&nbsp;- 自动识别并提取数据<br>
        &nbsp;&nbsp;- 生成可视化表格和图表<br>
        &nbsp;&nbsp;- 自动生成总结语句<br><br>
        
        2. 两张图片比较：<br>
        &nbsp;&nbsp;- 比较不同图片的数据差异<br>
        &nbsp;&nbsp;- 分析房数、房型、定价变化<br>
        &nbsp;&nbsp;- 生成对比图表
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-color: #2d2d2d; padding: 15px; border: 1px solid #00ff00; border-radius: 5px; margin-bottom: 20px;">
        <h4 style="color: #00ff00; font-family: 'Courier New', monospace;">/* 数据格式 */</h4>
        <p style="color: #00ff00; font-family: 'Courier New', monospace; font-size: 12px;">
        - 支持CON开头的会议预订<br>
        - 支持FIT开头的散客预订<br>
        - 支持月份英文开头的旅游预订
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.session_state.uploaded_data:
        st.markdown("""
        <div style="background-color: #2d2d2d; padding: 15px; border: 1px solid #00ff00; border-radius: 5px;">
            <h4 style="color: #00ff00; font-family: 'Courier New', monospace;">/* 历史数据 */</h4>
        </div>
        """, unsafe_allow_html=True)
        
        for i, data in enumerate(st.session_state.uploaded_data):
            st.markdown(f"""
            <div style="background-color: #1e1e1e; padding: 10px; border: 1px solid #00ff00; border-radius: 3px; margin: 5px 0;">
                <p style="color: #00ff00; font-family: 'Courier New', monospace; font-size: 11px; margin: 0;">
                数据 {i+1}: {data['booking_id']}
                </p>
            </div>
            """, unsafe_allow_html=True)

# 页脚 - 代码编辑器风格
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 20px; background-color: #1e1e1e; border: 1px solid #00ff00; border-radius: 5px;">
    <p style="color: #00ff00; font-family: 'Courier New', monospace; font-size: 12px; margin: 0;">
        // 提示：确保上传的图片清晰，包含完整的预订数据表格<br>
        // Hotel Booking Data Analysis Tool v1.0 - Powered by Streamlit
    </p>
</div>
""", unsafe_allow_html=True)
