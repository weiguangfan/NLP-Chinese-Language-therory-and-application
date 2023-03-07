# -*- coding:utf-8 -*-
import sys
import os
from importlib import reload

from stanford import StanfordPOSTagger
# 设置UTF-8输出环境
# reload(sys)
# sys.setdefaultencoding('utf-8')

root = "D:\\stanford-corenlp"
modelpath = root + "models\\pos-tagger\\chinese-distsim\\chinese-distsim.tagger"
st = StanfordPOSTagger(root,modelpath)
seg_sent = "在 包含 问题 的 所有 解 的 解空间 树 中 , 按照 深度优先 搜索 的 策略 , 从 根节点 出发 深度 探索 解空间 树 。"
taglist = st.tag(seg_sent)
print(taglist)








