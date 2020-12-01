''' Plot the dots to plan palm tree plantation. '''
import os
import tkinter

import matplotlib
import matplotlib.pyplot as plt
from PIL import Image


matplotlib.use('TkAgg')

MAP_COLOR = 'bcbec0'
MAP_COLOR_RGB = (188,190,192)
DESIRED_COLOR = (255, 0, 0)
IMAGE_PATH = 'worldmap.png'

os.chdir(os.getcwd())

def get_shape(path):
    ''' Return the shape of the image '''

    im = Image.open(path)
    pix = im.load()

    # Get the width and hight of the image for iterating over
    width, height = im.size

    return (
        width,
        height
    )

def colorize_image(path):
    ''' Colorize the image with the desired color. '''

    # Can be many different formats.
    im = Image.open(path)
    pix = im.load()

    # Get the width and hight of the image for iterating over
    width, height = im.size

    for w in range(width):
        for h in range(height):

            # Get the RGBA Value of the a pixel of an image
            red, green, blue, alpha = pix[w,h]
            rgb = (
                red,
                green,
                blue
            )
            if rgb == MAP_COLOR_RGB:
                # Set the RGBA Value of the image (tuple)
                pix[w,h] = DESIRED_COLOR

    # Save the modified pixels as .png
    im.save('desired.png')

    return im



# colorize_image('worldmap.png')

def scatter_image(path):
    ''' Scatterize the image '''
    im = plt.imread(path)
    implot = plt.imshow(im)
    im_ = Image.open(path)
    pix = im_.load()
    width, height = get_shape(path)
    for w in range(0, width, 15):
        for h in range(0, height, 15):

            # Get the RGBA Value of the a pixel of an image
            red, green, blue, alpha = pix[w,h]
            rgb = (
                red,
                green,
                blue
            )
            if rgb == MAP_COLOR_RGB:
                # put a red dot at (w, h)
                plt.scatter(x=[w], y=[h], c='g', marker='.')

    plt.title('Image with ScatterPlot')
    plt.savefig('desired.png')
    plt.show()

scatter_image(IMAGE_PATH)
