import tensorflow as tf
import os
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from io import BytesIO

def read_img(image):


img = ''

MODEL = load_model()