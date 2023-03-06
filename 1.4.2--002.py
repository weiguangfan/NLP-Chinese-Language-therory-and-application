# -*- coding:utf-8 -*-
import sys
import os
class StanfordCoreNLP():
    """
    所有stanfordNLP的父类
    """
    def __init__(self,jarpath):
        self.root = jarpath
        # 输入临时文件路径
        self.tempsrcpath = 'tempsrc'
        self.jarlist = ["ejml-0.23.jar","javax.json.jar","jollyday.jar",
                        "joda-time.jar","protobuf.jar","slf4j-api.jar",
                        "slf4j-simple.jar","stanford-corenlp-3.6.0.har","xom.jar"
                        ]
        self.jarpath = ""
        self.buildjars()

    def buildjars(self):
        """
        根据root路径构建所有的jar包路径
        :return:
        """
        for jar in self.jarlist:
            self.jarpath += self.root + jar + ";"

    def savefile(self,path,sent):
        """
        创建临时文件存储路径
        :param path:
        :param sent:
        :return:
        """
        fp = open(path,'wb')
        fp.write(sent)
        fp.close()

    def delfile(self,path):
        os.remove(path)


class StanfordPOSTagger(StanfordCoreNLP):
    """
    词性标注子类
    """
    def __init__(self,jarpath,modelpath):
        StanfordCoreNLP.__init__(self,jarpath)
        # 模型文件路径
        self.modelpath = modelpath
        # 词性标注主类
        self.classifier = "edu.stanford.nlp.tagger.maxent.MaxenTagger"
        # 标签分隔符
        self.delimiter = "/"
        self.__buildcmd()

    def __buildcmd(self):
        pass



















