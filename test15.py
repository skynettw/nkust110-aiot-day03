import sqlite3
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import jieba
from collections import Counter

db = sqlite3.connect("nkustnews.db")
data = list()
sql = "select title from news;"
rows = db.execute(sql)
for row in rows:
    data.append(row[0])
data = ";".join(data)
jieba.load_userdict("dict.txt")
with open('stopwords.txt', 'rt', encoding='utf-8') as fp:
    stopwords = [word.strip() for word in fp.readlines()]

keyterms = [keyterm for keyterm in jieba.cut(data) 
            if keyterm not in stopwords 
                and keyterm.strip()!=""
                and keyterm.strip()!=","]
text = ",".join(keyterms)
mask = np.array(Image.open('cloud.jpg'))
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, 
                      margin=2, font_path="simhei.ttf", 
                      mask=mask).generate(text)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud)
plt.axis("off")
plt.show()