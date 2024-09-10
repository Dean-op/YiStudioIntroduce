import time
import streamlit as st
from datetime import datetime


def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


st.sidebar.image("images/工作室logo.png", use_column_width=True)

page = st.sidebar.radio("选择页面", ("部门介绍", "算法赛事介绍", "逸工作室训练手册"))
st.sidebar.image("images/QRcode02.png", caption="2024届逸工作室招募群")

st.markdown(
    """
    <style>
    .title-container {
        text-align: center;
        font-size: 34px;
        font-weight: bold;
        margin-top: 20px;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: right;
        font-size: 18px;
        font-style: italic;
        color: #87CEFA;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title-container">逸工作室</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">——与编码爱好者同台竞技！</div>', unsafe_allow_html=True)

# 获取当前时间
current_time = datetime.now()
# 训练手册开放时间
open_time = datetime(2024, 10, 1)

if page == "部门介绍":
    department_intro = read_markdown_file("pages/introduce.md")
    time.sleep(2)
    st.markdown(department_intro, unsafe_allow_html=True)

elif page == "算法赛事介绍":
    time.sleep(2)
    event_intro = read_markdown_file("pages/AlgorithmIntro.md")
    st.markdown(event_intro, unsafe_allow_html=True)

elif page == "逸工作室训练手册":
    with st.spinner("文档加载中..."):
        time.sleep(3)
        if current_time >= open_time:
            other_info = read_markdown_file("pages/train.md")
            st.markdown(other_info, unsafe_allow_html=True)
        else:
            # st.warning(f"逸工作室训练手册将在 {open_time.strftime('%Y年%m月%d日')} 开放，请耐心等待！")
            st.warning(f"此文档为逸工作室社员训练手册，请联系相关人员获取权限")
