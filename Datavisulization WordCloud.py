import sys
import wikipedia
from wordcloud import WordCloud,STOPWORDS
import os
from os import path
from PIL import Image
import numpy as np

currdir = os.path.dirname(__file__)

def get_wiki(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

def create_wc(text):
    mask = np.array(Image.open(os.path.join(currdir, "gokka.png")))

    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="rgba(255, 255, 255, 0)",
                   mask = mask,
                   max_words=10000,
                   stopwords=STOPWORDS)
    wc.generate(text)
    wc.to_file(os.path.join(currdir, "vish.png"))

create_wc(get_wiki("Google"))