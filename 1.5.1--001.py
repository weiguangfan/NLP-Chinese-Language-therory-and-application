# -*- coding:utf-8 -*-
import sys
import os
from pyltp import *
sent = "欧洲 东部 的 罗马尼亚 , 首都 是 布加勒斯特 , 也 是 一 座 世界性 的 城市 。"
words = sent.split(" ")
print(words)
postagger = Postagger()
print(postagger)
# 导入词性标注模块
postagger.load("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\pos.model")
postags = postagger.postag(words)
print(postags)
recognizer = NamedEntityRecognizer()
print(recognizer)
# 导入命名实体识别模块
recognizer.load("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\ner.model")
netags = recognizer.recognize(words,postags)
print(netags)
for word,postag,netag in zip(words,postags,netags):
    print(word + "/" + postag + "/" + netag)
















