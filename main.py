from preprocessing import preprocessing
from word_cloud import *
from PIL import Image
import pandas as pd
import numpy as np
import argparse

text = preprocessing(open('Assets/Text/sample.txt').read())
mask = np.array(Image.open('Assets/Mask/twitter.png'))
font = 'Assets/Font/Ignazio.ttf'
background = 'white'
color_generator = True
color = None
show = False
save = True

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--text", required=False,
	help="Path of textfile that will be use")
ap.add_argument("-m", "--mask", required=False,
	help="Path of image that will be use as a mask"),
ap.add_argument("-f", "--font", required=False,
	help="Path of font that will be use"),
ap.add_argument("-b", "--background", required=False,
	help="Background color that will be use in the wordcloud (e.g. white, black, blue, etc.)"),
ap.add_argument("-c", "--colorgenerator", required=False,
	help="true/false, if true this will be generating color of the image mask"),
ap.add_argument("-s", "--show", required=False,
	help="Show image when process in completed")
ap.add_argument("--color", required=False,
    help="Dominant color that will be use in the wordcloud (e.g. white, black, blue, etc.)")
args = vars(ap.parse_args())

if args['text']:
    text = preprocessing(open(args['text']).read())
if args['mask']:
    mask = np.array(Image.open(args['mask']))
if args['font']:
    font = args['font']
if args['background']:
    background = args['background']
if args['colorgenerator']:
    if args['colorgenerator'].lower() == 'false':
        color_generator = False
if args['color']:
    if args['color'].lower() == 'red':
        color = 0
    elif args['color'].lower() == 'orange':
        color = 30
    elif args['color'].lower() == 'yellow':
        color = 60
    elif args['color'].lower() == 'green':
        color = 120
    elif args['color'].lower() == 'sky':
        color = 180
    elif args['color'].lower() == 'blue':
        color = 240
    elif args['color'].lower() == 'magenta':
        color = 300
    print(color)
    if type(color) == int:
        color_generator = False
if args['show']:
    show = args['show']

print(args)
wc = wordclouds(text, font, mask, background, color, color_generator=color_generator, show=show, save=save)
wc.masking_wordcloud()
wc.show_wordcloud()
# wc = masking_wordcloud(text, font, mask, background)
# show_wordcloud(wc, show=show, save=True, color_generator=color_generator, mask=mask)

