# -*- coding:utf-8 -*-
import sys
import os
from importlib import reload

# 导入ltp库
from pyltp import Segmentor
reload(sys)

# 设置utf-8输出环境
# sys.setdefaultencoding('utf-8')

postdict = {"解 | 空间":"解空间","深度 | 优先":"深度优先"}
# 分词后处理--矫正一些错误的结果
model_path = "D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\cws.model"
segmentor = Segmentor()
segmentor.load(model_path)
words = segmentor.segment("在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树")
seg_sent = " | ".join(words)
for key in postdict:
    seg_sent = seg_sent.replace(key,postdict[key])
print(seg_sent)






