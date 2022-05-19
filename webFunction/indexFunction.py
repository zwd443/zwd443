# -*- encoding:utf-8 -*-

"""
    web function
"""

import streamlit as st
from yolo import detect
from io import StringIO, BytesIO
import cv2
import numpy as np
from PIL import Image
import time
import os
import shutil


# 检测事件
def click_detect(img):
    weightPath = 'yolo/weights/yolov5s.pt'
    opt = detect.my_parse_opt(sourcePath=img)
    return detect.main(opt)


# 获得图片 bytes => [[list]]
def get_upload_img(upload_file):
    bytes_stream = BytesIO(upload_file.getvalue())
    capture_img = Image.open(bytes_stream)
    return cv2.cvtColor(np.asarray(capture_img), cv2.COLOR_RGB2BGR)


# 图片储存
def save_img(img_list):
    now = str(time.time()).split(".")[1]
    name = r'E:\file\PyCharm_workspace\yoloV5ToStreamlit\out\image_{now}.jpg'
    cv2.imwrite(filename=name, img=img_list)
    return name


# 视频储存
def save_video(video):
    now = str(time.time()).split(".")[1]
    name = r'E:\file\PyCharm_workspace\yoloV5ToStreamlit\out\video_{now}.mp4'
    with open(name, 'wb+')as f:
        f.write(video.getvalue())
    st.write('视频存储成功')
    return name


# 资源删除
def remove_file(path):
    if os.path.exists(path):
        # remove
        os.remove(path)


def remove_dir(path):
    if os.path.exists(path):
        # remove
        shutil.rmtree(path)


# 处理视频
def video_deal(upload_file):
    vs_name = save_video(upload_file)
    st.write(vs_name)
    if st.button(label='开始检测'):
        st.write("开始处理")
        st.write("处理中。。。")
        r_name = click_detect(vs_name)
        st.write("处理完毕!")
        de_dir = os.getcwd() + "\\" + r_name
        st.video(r_name)
        remove_file(vs_name)
        remove_dir(os.path.dirname(de_dir))


# 图片处理
def image_deal(upload_file):
    st.image(upload_file)
    if st.button(label='开始检测'):
        st.write('开始检测')
        res = get_upload_img(upload_file)
        name = save_img(res)
        st.write('资源路径', name)
        # 处理
        st.write('检测中。。。')
        detect_res = click_detect(name)
        st.write('检测完毕')
        de_dir = os.getcwd() + "\\" + detect_res
        st.image(detect_res)
        # 删除资源路径
        remove_file(name)
        remove_dir(os.path.dirname(de_dir))
