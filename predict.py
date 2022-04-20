from tensorflow import keras
from PIL import Image
import PIL.ImageOps
import numpy as np
import matplotlib.pyplot as plt
from canvas import DRAWN_IMAGE_NAME


BAR_NAME = "media/bar.png"


def save_as_image():
    try:
        img = Image.open(DRAWN_IMAGE_NAME)
    except FileNotFoundError:
        return None
    img = img.resize((28, 28), Image.ANTIALIAS)
    img = img.convert('L')
    img = PIL.ImageOps.invert(img)
    arr = np.asarray(img) / 255
    return np.reshape([arr], (1, 28, 28))


def predict():
    model = keras.models.load_model('model')
    im = save_as_image()
    return model.predict(im)[0]


def visualization(predictions, norm=True):
    figure = plt.figure(figsize=(3, 3))
    max_element = max(predictions)
    max_element_index = list(predictions).index(max_element)
    if norm:
        predictions = 1/(1 + np.exp(-predictions * 0.5))
    x = list(range(10))
    colors = ["crimson"] * 10
    colors[max_element_index] = "darkgreen"
    plt.bar(x, predictions, color=colors)
    plt.xticks(x)
    plt.savefig(BAR_NAME)
    return figure
