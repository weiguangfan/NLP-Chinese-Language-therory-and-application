# -*- coding:utf-8 -*-
import sys
import os
from importlib import reload

from pyltp import *
reload(sys)
# sys.setdefaultending('utf-8')

sent = "在 包含 问题 的 所有 解 的 解空间树 中 , 按照 深度优先 搜索 的 策略 , 从 根节点 出发 深度 探索 解空间树 。"
words = sent.split(' ')
# 实例化词性标注类
postagger = Postagger()
# 导入词性标注模型
postagger.load("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\pos.model")
postags = postagger.postag(words)
for word,postag in zip(words,postags):
    print(word + '/' + postag)








