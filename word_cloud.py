import csv
import wordcloud
from cv2 import imread

mask = imread("background.png")#导入自定义词云图片

items = ""
with open('cluster2.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for r in reader:
        items += r[0]

w = wordcloud.WordCloud(scale=2,font_path="msyh.ttc",width=1000,height=700,background_color="white",mask=mask)
w.generate(items)
w.to_file("output2.png")#输出词云