# -*- encoding:utf-8 -*-

"""
    web UI
"""

import streamlit as st


# 文件上传
def build_upload():
    return st.file_uploader('选择需要检测的图片')


# 创建侧边栏
def build_aside():
    return st.sidebar


class UI:
    def __init__(self, args):
        self.args = args
