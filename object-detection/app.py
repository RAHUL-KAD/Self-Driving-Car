import streamlit as st
import numpy as np
import cv2
import torch
import os
import shutil

st.title("Autonomous Vehicle Detection using YOLOv5")

upload_file = st.file_uploader("Choose an Image...", type=['jpg', 'png', 'jpeg', 'PNG'])

# loding custom trained model.
# model = torch.hub.load("ultralytics/yolov5",  'custom', path='/workspace/best.pt')

# loding the pretrained model by yolov5 team
model = torch.hub.load("ultralytics/yolov5", "yolov5n")

if upload_file is not None:
    # The image is in the from of IOBytes array
    file_bytes = np.asarray(bytearray(upload_file.read()), dtype=np.uint8)
    # decoding an image
    opencv_image = cv2.imdecode(file_bytes, 1)
    st.image(opencv_image, channels="BGR")

    if st.button("Show detected objects ..."):
        st.write("the output is ...")
        # model prediction
        results = model(opencv_image, size=640)
        print(results)
        file_path = results.save()
        print("predicted objects are : ",results)
        output_image = '/app/runs/detect/exp/image0.jpg'
        output_image = cv2.imread(output_image)
        st.image(output_image, channels="RGB")

        # removing the folder where an output image is saved
        location = "/app/runs/"
        shutil.rmtree(location)
