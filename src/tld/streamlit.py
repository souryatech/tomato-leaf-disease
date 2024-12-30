import streamlit as st
from PIL import Image
import numpy as np

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

one = st.button("1.jpg")
two = st.button("2.jpg")
three = st.button("3.jpg")
four = st.button("4.jpg")
five = st.button("5.jpg")
six = st.button("6.jpg")
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