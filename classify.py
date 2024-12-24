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
