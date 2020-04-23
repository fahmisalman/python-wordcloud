from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np


def simple_wordcloud(text):
    wc = WordCloud(background_color="white", max_words=2000, stopwords=STOPWORDS, max_font_size=256, random_state=42).generate(text)
    return wc

def show_wordcloud(wc, show=False, save=True, color_generator=False, mask=None):
    if color_generator:
        mask_colors = ImageColorGenerator(mask)
        plt.imshow(wc.recolor(color_func=mask_colors), interpolation="bilinear")
    else:
        plt.imshow(wc)

    plt.axis('off')

    if save:
        plt.savefig('Result/Wordcloud.png', dpi=300, pad_inches=0, bbox_inches='tight')

    if show:
        plt.show()

def masking_wordcloud(text, font, mask, background_color):
    wc = WordCloud(stopwords=STOPWORDS, font_path=font, background_color=background_color, width=mask.shape[1], height=mask.shape[0], mask=mask, max_words=2000, max_font_size=256, random_state=42).generate(text)
    return wc