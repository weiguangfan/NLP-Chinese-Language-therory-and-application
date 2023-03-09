# -*- coding:utf-8 -*-
import sys
import os


class StanfordCoreNLP(object):
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
        fp = open(path,'w')
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
        """
        构建命令行
        java -mx1g:调用java程序，以及设置的最大内存
        -cp "...jar":调用的jar包
        self.classifier:最大熵分类器
        -model self.modelpath:最大熵模型文件

        :return:
        """
        self.cmdline = 'java -mx1g -cp "'+self.jarpath+'" '+self.classifier+'-model "'+self.modelpath+'" -tagSeparator '+ self.delimiter

    def tag(self,sent):
        """
        标注句子
        -textFile self.tempsrcpath:最大熵输入文本文件
        :param sent:
        :return:
        """
        self.savefile(self.tempsrcpath,sent)
        # 结果输出到变量中
        tagtxt = os.popen(self.cmdline+"  -textFile  "+self.tempsrcpath, 'r').read()
        self.delfile(self.tempsrcpath)
        return tagtxt

    def tagfile(self,inputpath,outpath):
        """
        标注文件
        :param inputpath:
        :param outpath:
        :return:
        """
        os.system(self.cmdline + ' -textFile '+inputpath+' > '+outpath )


class StanfordNERTagger(StanfordCoreNLP):
    def __init__(self,modelpath,jarpath):
        StanfordCoreNLP.__init__(self,jarpath)
        # 模型文件路径
        self.modelpath = modelpath
        self.classifier = "edu.stanford.nlp.ie.crf.CRFClassifier"
        self.__buildcmd()

    def __buildcmd(self):
        self.cmdline = 'java -mx1g -cp "'+self.jarpath+'" '+self.classifier+'-loadClassifier "'+self.modelpath+'"'

    def tag(self,sent):
        self.savefile(self.tempsrcpath,sent)
        tagtxt = os.popen(self.cmdline+'  -textFile  '+self.tempsrcpath, 'r').read()
        self.delfile(self.tempsrcpath)
        return tagtxt

    def tagfile(self,sent,outpath):
        self.savefile(self.tempsrcpath,sent)
        os.system(self.cmdline+' -textFile '+self.tempsrcpath+' > '+outpath )
        self.delfile(self.tempsrcpath)


class StanfordParser(StanfordCoreNLP):
    def __init__(self,modelpath,jarpath,opttype):
        StanfordCoreNLP.__init__(self,jarpath)
        # 模型文件路径
        self.modelpath = modelpath
        self.classifier = "edu.stanford.nlp.parser.lexparser.LexicalizedParser"
        self.opttype = opttype
        self.__buildcmd()

    def __buildcmd(self):
        """构建命令行"""
        self.cmdline = 'java -mx500m -cp "'+self.jarpath+'" '+self.classifier+'-outputFormat "'+self.opttype+'" '+self.modelpath+' '

    # 解析句子
    def parse(self,sent):
        self.savefile(self.tempsrcpath,sent)
        # 输出到变量里
        tagtxt = os.popen(self.cmdline + self.tempsrcpath,"r").read()
        self.delfile(self.tempsrcpath)
        return tagtxt

    def tagfile(self,sent,outpath):
        self.savefile(self.tempsrcpath,sent)
        os.system(self.cmdline+self.tempsrcpath+' > '+outpath )
        self.delfile(self.tempsrcpath)











