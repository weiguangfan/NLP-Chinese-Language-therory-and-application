# -*- coding:utf-8 -*-
import sys
import os
from pyltp import *


MODELDIR = "D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\"
sentence = "欧洲东部的罗马尼亚，首都是布加勒斯特，也是一座世界性的城市。"

# cws.model为中文分词模块所需的语言模型
# 实例化分词模块
segmentor = Segmentor()
# 加载分词库
# segmentor.load(os.path.join(MODELDIR, "cws.model"))
segmentor.load(os.path.join("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\cws.model"))
words = segmentor.segment(sentence)
print("words: ",words)
# 分割后的分词结果
wordlist = list(words)
print(wordlist)
# 释放模型
segmentor.release()


# 词性标注模块的文件名为pos.model
# 实例化词性标注类
postagger = Postagger()
# 导入词性标注模型
# postagger.load(os.path.join(MODELDIR,"pos.model"))
postagger.load(os.path.join("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\pos.model"))
# 使用分词结果进行标注
postags = postagger.postag(words)
print("postags: ",postags)
# 释放模型
postagger.release()


# 句法解析模块的文件名为parser.model
# 实例化句法解析类
parser = Parser()
# 导入句法解析模块
# parser.load(os.path.join(MODELDIR,"parser.model"))
parser.load(os.path.join("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\parser.model"))
# 使用分词结果、标注结果
# arc.head 表示依存弧的父节点词的索引，arc.relation 表示依存弧的关系。
arcs = parser.parse(words,postags)
print("arcs: ", arcs)
# 释放模型
parser.release()


# 命名实体识别模块的文件名为ner.model
# 实例化命名实体识别类
recognizer = NamedEntityRecognizer()
# 导入命名实体识别模块
# recognizer.load(os.path.join(MODELDIR,"ner.model"))
recognizer.load(os.path.join("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\ner.model"))
# 使用分词结果、标注结果
netags = recognizer.recognize(words,postags)
print("netags: ", netags)
# 释放模型
recognizer.release()


# 语义角色标注模块的文件名为srl
# 实例化语义角色标注类
labeller = SementicRoleLabeller()
# 导入语义角色标注模块
# labeller.load(os.path.join(MODELDIR,"srl/"))
labeller.load(os.path.join("D:\\ltp3.3\\3.4.0\\ltp_data_v3.4.0\\pisrl_win.model"))
# 使用分词结果、标注结果、命名实体识别结果、句法解析结果
# 报错，编译错误！！！
# 参数改为三个，分词结果、标注结果、句法解析结果，程序正常。
roles = labeller.label(words,postags,arcs)
print("roles: ", roles)
# 释放模型
labeller.release()

# arg.name 表示语义角色关系，
# arg.range.start 表示起始词位置，
# arg.range.end 表示结束位置。
# 输出标注结果
for role in roles:
    # print("role: ",role)
    # print("role.index",role.index)
    # print("role.arguments: ",[i for i in role.arguments])
    print('rel:',wordlist[role.index])  # 谓词
    for arg in role.arguments:
        # print("arg:",arg)
        # print("arg.name: ",arg.name)
        # print("arg.range.start:",arg.range.start)
        # print("arg.range.end:",arg.range.end)
        if arg.range.start != arg.range.end:
            print(arg.name,''.join(wordlist[arg.range.start:arg.range.end]))

        else:
            print(arg.name,wordlist[arg.range.start])














