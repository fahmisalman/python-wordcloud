from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class wordclouds():

    def __init__(self, text, font, mask, background_color, color, color_generator=False, show=False, save=True):
        self.text = text
        self.font = font
        self.mask = mask
        self.background_color = background_color
        self.color = color
        self.wordcloud = None
        self.color_generator = color_generator
        self.show = show
        self.save = save

    def random_color_func(self, word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
        h = int(self.color)
        s = int(100.0 * 255.0 / 255.0)
        l = int(100.0 * float(random_state.randint(60, 120)) / 255.0)

        return "hsl({}, {}%, {}%)".format(h, s, l)

    def simple_wordcloud(self):
        wc = WordCloud(background_color="white", max_words=2000, stopwords=STOPWORDS, max_font_size=256, random_state=42).generate(self.text)
        return wc

    def show_wordcloud(self, show=False, save=True, color_generator=False, mask=None):
        if self.color_generator:
            mask_colors = ImageColorGenerator(self.mask)
            plt.imshow(self.wordcloud.recolor(color_func=mask_colors), interpolation="bilinear")
        else:
            plt.imshow(self.wordcloud)

        plt.axis('off')

        if save:
            plt.savefig('Result/{}.png'.format(datetime.timestamp(datetime.now())), dpi=300, pad_inches=0, bbox_inches='tight')

        if show:
            plt.show()

    def masking_wordcloud(self):
        stopwords = set(STOPWORDS)
        if self.color != None:
            self.wordcloud = WordCloud(stopwords=stopwords, font_path=self.font, background_color=self.background_color, width=self.mask.shape[1], height=self.mask.shape[0], mask=self.mask, max_words=2000, max_font_size=256, random_state=42, color_func=self.random_color_func).generate(self.text)
        else:
            self.wordcloud = WordCloud(stopwords=stopwords, font_path=self.font, background_color=self.background_color, width=self.mask.shape[1], height=self.mask.shape[0], mask=self.mask, max_words=2000, max_font_size=256).generate(self.text)
