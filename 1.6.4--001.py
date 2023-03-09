# -*- coding:utf-8 -*-
import sys
import os
from nltk.tree import Tree
from stanford import *


root = "D:\\stanford-corenlp\\"
modelpath = root + "modles\\lexparser\\chinesePCFG.ser.gz"
# penn,typedDependencies
opttype = 'typedDependencies'
parser = StanfordParser(modelpath,root,opttype)
result = parser.parse("罗马尼亚 的 首都 是 布加勒斯特 。")
print(result)


