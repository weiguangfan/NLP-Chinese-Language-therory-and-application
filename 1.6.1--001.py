# -*- coding:utf-8 -*-
import sys
import os

import nltk
# 导入nltk tree 结构
from nltk.tree import Tree

# 导入依存句法包
from nltk.grammar import DependencyGrammar

from nltk.parse import *

# 导入ltp应用包
from pyltp import *

# 例句
words = "罗马尼亚 的 首都 是 布加勒斯特 。".split(" ")

# 首先对句子进行词性标注
postagger = Postagger()
postagger.load("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\pos.model")
postags = postagger.postag(words)

# 将词性标注和分词结果都加入分析器中进行句法解析
parser = Parser()
parser.load("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\parser.model")
arcs = parser.parse(words,postags)
print(arcs)
arclen = len(arcs)
print(arclen)

conll = ""
# 构建Coll标准的数据结构
for i in range(arclen):
    if arcs[i].head == 0:
        arcs[i].relation = "ROOT"
    conll += "\t"+words[i]+"("+postags[i]+")"+"\t"+postags[i]+"\t"+str(arcs[i].head)+"\t"+arcs[i].relation+"\n"
print(conll)


# 转换为依存句法图
colltree = DependencyGraph(conll)
# 构建树结构
tree = colltree.tree()
# 显示输出的树
tree.draw()









