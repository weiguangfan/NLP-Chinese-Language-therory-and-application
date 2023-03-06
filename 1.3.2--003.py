# -*- coding:utf-8 -*-
import sys
import os
from importlib import reload

# 导入ltp库
from pyltp import Segmentor
reload(sys)

# 设置utf-8输出环境
# sys.setdefaultencoding('utf-8')

# 分词模型库
model_path = "D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\cws.model"
# 外部专有名词词典路径
user_dict = ""
# 实例化分词模块
segmentor = Segmentor()
segmentor.load_with_lexicon(model_path,user_dict)
sent = "在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树"
words = segmentor.segment(sent)
print(" | ".join(words))















