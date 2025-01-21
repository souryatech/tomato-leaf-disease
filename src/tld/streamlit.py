import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
import os
from keras.preprocessing import image
from tensorflow.keras.models import load_model

MODEL = load_model(os.path.join("models", "T1"))

classes = [
    "Early Blight",
    "Late Blight",
    "Leaf Mold",
    "Yellowleaf Curl Virus",
    "Mosaic Virus",
    "Healthy",
]
st.title("Tomato Leaf Disease")
img = None

img = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if img is not None:
    st.image(img)
    img = Image.open(img)
    img = np.array(img)
    # img = tf.image.resize(image_process, (256, 256))

    st.write(img.shape)
# st.write(img.shape())
# st.write(img)
# st.write(type(img))
st.write("Use a test image")

one = st.button("Early Blight")
two = st.button("Late Blight")
three = st.button("Leaf Mold")
four = st.button("Yellowleaf Curl Virus")
five = st.button("Mosaic Virus")
six = st.button("Healthy")
# 1: Early Blight, 2: Late Blight, 3: Leaf Mold, 4: Yellowleaf Curl Virus, 5: Mosaic Virus, 6: Healthy
button_clicked = False;
if one:
    img = Image.open("test_images/1.jpg")
    button_clicked = True
elif two:
    img = Image.open("test_images/2.jpg")
    button_clicked = True
elif three:
    img = Image.open("test_images/3.jpg")
    button_clicked = True
elif four:
    img = Image.open("test_images/4.jpg")
    button_clicked = True
elif five:
    img = Image.open("test_images/5.jpg")
    button_clicked = True
elif six:
    img = Image.open("test_images/6.jpg")
    button_clicked = True

if img is not None and button_clicked:
    st.image(img)
    st.write(np.array(img).shape)


if img is not None:
    image_process = image.img_to_array(img)

    image_process = tf.image.resize(image_process, (256, 256))

    prediction = MODEL.predict(np.expand_dims(image_process, 0))

    st.write(f"Prediction: {classes[np.argmax(prediction)]}")
    st.write(f"Confidence: {round(np.max(prediction)*100,2)}%")