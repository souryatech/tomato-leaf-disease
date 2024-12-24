import tensorflow as tf
import os
import numpy as np
from tensorflow.keras.models import load_model
from keras.preprocessing import image
import sys

img = sys.argv[2]

MODEL = load_model(os.path.join('models', 'T1'))

classes = ['Early Blight', 'Late Blight', 'Leaf Mold', 'Yellowleaf Curl Virus', 'Mosaic Virus', 'Healthy']

image_process = image.load_img(img)

image_process = image.img_to_array(image_process)

image_process = tf.image.resize(image_process, (256,256))

prediction = MODEL.predict(np.expand_dims(image_process, 0))

print(f"Prediction: {classes[np.argmax(prediction)]}")
print(f"Confidence: {round(np.max(prediction)*100,2)}%")
# [tool.uv.index]
# name = "tensorflow-index"
# url = "https://storage.googleapis.com/tensorflow/linux"  # Replace with TensorFlow's appropriate URL for your platform if needed.

# [tool.uv.dependencies]
# tensorflow = {
#     version = "2.15.0",  # Replace with the desired TensorFlow version, e.g., "2.12.0".
#     extra = "index"
# }