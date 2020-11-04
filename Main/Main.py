#encoding=utf-8
import sys
import os
import pymysql
from TextProcessingSystem import TextProcessingSystem
import jieba as jb
import jieba.posseg as pseg
from LAC import LAC
import docx
import subprocess

jb.load_userdict(os.path.join(os.getcwd(), '/home/king/code/ApexPredatorLisa/Main/MyDict.txt'))
# 古诗词辞典/成语辞典

def IsChinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def cuttest(test_sent):
    result = jb.cut(test_sent)
    print(" ".join(result))



isHandleSymbolsInFiles = False
isReadNovel = False
if __name__ == "__main__":
    # cuttest("这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。")
    fileName = '/home/king/Documents/遮天-百度百科.txt'
    # HandleSymbolsInFiles(fileName)
    fileName = '/home/king/Documents/遮天-百度百科Tmp.txt'
    myDictFile = '/home/king/code/ApexPredatorLisa/Main/MyDict.txt'
    # GetDict2BaiduEncyclopedia(fileName, myDictFile)
    textProcessingSystem = TextProcessingSystem()
    if isHandleSymbolsInFiles:
        textProcessingSystem.HandleSymbolsInFiles(fileName, False)
    textProcessingSystem.GetDict2BaiduEncyclopedia(fileName, myDictFile)
    # 装载LAC模型
    lac = LAC(mode='lac')
    # 装载干预词典
    lac.load_customization('/home/king/code/ApexPredatorLisa/Main/MyDict.txt')
    # 读取小说
    novelName = '/home/king/Documents/zhetian.txt'
    if isReadNovel:
        novelList = []
        with open(novelName, mode='r', encoding='utf-8') as fp:
            for line in fp.readlines():
                # 批量样本输入, 输入为多个句子组成的list，平均速率更快
                if len(line):
                    # lac来划分词性
                    lac_result = lac.run(line)
                    # lac_result = pseg.cut(line, use_paddle=True)  # paddle模式
                    print(lac_result)

    # 连接数据库
    db = pymysql.connect("localhost", "root", "123123", "ApexPredatorLisaDB", charset='utf8' )
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()
    print("Database version : %s " % data)
    # 关闭数据库连接
    db.close()