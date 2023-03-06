# -*- coding:utf-8 -*-
import sys
import os
# 导入结巴分词库
from importlib import reload

import jieba
# 设置utf-8输出环境
reload(sys)
# sys.setdefaultencoding('utf-8')
# 加载外部用户词典
jieba.load_userdict("userdict.txt")
# 结巴分词--全模式
sent = "在包含问题的所有解的解空间树中，按照深度优先搜索的策略，从根节点出发深度探索解空间树"
wordlist = jieba.cut(sent)
print(" | ".join(wordlist))
