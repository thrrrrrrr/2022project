import csv
import wordcloud
from cv2 import imread
from PIL import Image
import matplotlib.pyplot as plt

mask = imread("background.png")#导入自定义词云图片

items = ""
with open('cluster2.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    for r in reader:
        items += r[0]

w = wordcloud.WordCloud(scale=2,font_path="msyh.ttc",width=1000,height=700,background_color="white",mask=mask)
w.generate(items)
w.to_file("output2.png")#输出词云
img = Image.open("output2.png")

plt.figure("Image") # 图像窗口名称
plt.imshow(img)
plt.axis('on') # 关掉坐标轴为 off
plt.title('image') # 图像题目
plt.show()

#对csv文件进行数据分析，生成词云

