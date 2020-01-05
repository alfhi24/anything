import sys
import numpy as np 
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

x = str(input("enter keyword : "))
title = wikipedia.search(x)[0]
page = wikipedia.page(title)
text = page.content
print(text)
background = np.array(Image.open("cloud.png"))
stopwords = set(STOPWORDS)
wc = WordCloud(background_color="black",
                max_words = 300,
                mask = background,
                stopwords=stopwords)

wc.generate(text)
wc.to_file("wc.png")