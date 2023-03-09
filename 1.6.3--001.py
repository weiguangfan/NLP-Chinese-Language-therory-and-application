# -*- coding:utf-8 -*-
import sys
import os
from stanford import StanfordParser
# 导入nltk库
from nltk.tree import Tree
# 安装库
root = "D:\\stanford-corenlp\\"
modelpath = root + "modles\\lexparser\\chinesePCFG.ser.gz"
# 滨州树库格式
opttype = "penn"
parser = StanfordParser(modelpath,root,opttype)
# print(parser)
result = parser.parse("罗马尼亚 的 首都 是 布加勒斯特 。")
print(result)
tree = Tree.fromstring(result)
tree.draw()














