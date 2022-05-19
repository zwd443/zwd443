# -*- encoding:utf-8 -*-

from io import StringIO, BytesIO
import cv2
import numpy as np
from PIL import Image
import os
from webUi import indexUI
from webFunction import indexFunction
import argparse
import streamlit as st


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--title', default='This is streamlit test!', help='title')
    return parser.parse_args()


args = parse_args()
print('Welcome!\nGo to streamlit!')

# aside
aside = indexUI.build_aside()
upload_file = aside.file_uploader(label='上传文件')

# 正文
st.header('Welcome!')

if upload_file is not None:
    st.write(upload_file.name)
    up_type = upload_file.type
    st.write(upload_file)
    if up_type.startswith('video'):
        res = indexFunction.video_deal(upload_file)
        # 条件删除

    elif up_type.startswith('image'):
        res = indexFunction.image_deal(upload_file)

