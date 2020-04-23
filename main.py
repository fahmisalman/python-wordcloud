from preprocessing import preprocessing
from word_cloud import *

import pandas as pd
import argparse
import cv2

mask = cv2.imread('/Volumes/Macbook HDD/MyProject/Python/Wordcloud/New Wordcloud/Assets/Mask/twitter_mask.png')
font = '/Volumes/Macbook HDD/MyProject/Python/Wordcloud/New Wordcloud/Assets/Font/Ignazio.ttf'
text = preprocessing(open('/Volumes/Macbook HDD/MyProject/Python/Wordcloud/New Wordcloud/Assets/Text/sample.txt').read())
background = 'white'
color_generator = True
show = False
save = True

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--text", required=False,
	help="Input sentence that will be classified")
ap.add_argument("-m", "--mask", required=False,
	help="Model that will be use in classification: model1 (without stemming and stopword), model2 (with stemming but without stopword), model3 (with stemming and stopword). If not defined, model1 will be used"),
ap.add_argument("-f", "--font", required=False,
	help=""),
ap.add_argument("-b", "--background", required=False,
	help=""),
ap.add_argument("-c", "--colorgenerator", required=False,
	help=""),
ap.add_argument("-s", "--show", required=False,
	help="")
args = vars(ap.parse_args())

if args['text']:
    text = preprocessing(open(args['text']).read())
if args['mask']:
    mask = cv2.imread(args['mask'])
if args['font']:
    font = args['font']
if args['background']:
    background = args['background']
if args['colorgenerator']:
    if args['colorgenerator'].lower() == 'false':
        color_generator = False
if args['show']:
    show = args['show']

wc = masking_wordcloud(text, font, mask, background)
show_wordcloud(wc, show=show, save=True, color_generator=color_generator, mask=mask)

