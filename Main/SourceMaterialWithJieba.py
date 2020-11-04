#encoding=utf-8
import sys
import os
import jieba as jb
import jieba.posseg as pseg
import jieba.analyse
from optparse import OptionParser

jb.load_userdict("/home/king/code/ApexPredatorLisa/Main/MyDict.txt")

# KEYWORD_RATIO = 0.91
KEYWORD_COUNT_RATIO = 0.1

KEYWORD_RATIO = 0.91

#'n','v','vd','vn','a','ad','an','d'
def KeywordExtraction(content, topK=3):
    topK = int(len(content) * KEYWORD_COUNT_RATIO)
    print(topK)
    cutResult = GetCutResult(content)
    tags = jieba.analyse.extract_tags(cutResult, topK, withWeight=False, allowPOS=('n','v','vd','vn','a','ad','an','d'))
    return (",".join(tags))

def GetCutResult(text):
    result = jb.cut(text, cut_all=False)
    return ' '.join(result)

if __name__ == '__main__':
    # print('begain')
    # line = '他穿着一身大红直裰婚服，腰间扎条同色金丝蛛纹带，黑发束起以镶碧鎏金冠固定着，修长的身体挺的笔直，整个人丰神俊朗中又透着与生俱来的高贵，依旧如前世般让人觉得高不可攀、低至尘埃。'
    # line2 = '女生的校服是非常贴合身材，优雅中的小性感。男生的非常绅士和高贵。'
    # line3 = '锦茜红妆蟒暗花缂金丝双层广绫大袖衫，边缘尽绣鸳鸯石榴图案，胸前以一颗赤金嵌红宝石领扣扣住，外罩一件品红双孔雀绣云金缨络霞帔，那开屏孔雀有婉转温顺之态，好似要活过来一般，桃红缎彩绣成双花鸟纹腰封垂下云鹤销金描银十二幅留仙裙，裙上绣出百子百福花样，尾裙长摆曳地三尺许，边缘滚寸长的金丝缀，镶五色米珠，行走时簌簌有声，发鬓正中戴着联纹珠荷花鸳鸯满池娇分心，两侧各一株盛放的并蒂荷花，垂下绞成两股的珍珠珊瑚流苏和碧玉坠角，中心一对赤金鸳鸯左右合抱，明珠翠玉作底，更觉光彩耀目。'
    path = '/home/king/Documents/APL/PredatorBrain/renwu'
    for file in os.listdir(path):
        if (file.find('词汇') > 0):
            continue
        novelName = os.path.join(path, file)
        newName = novelName + '-词汇'
        fpCopy = open(newName, mode='w+', encoding='utf-8')
        with open(novelName, mode='r', encoding='utf-8') as fp:
            for line in fp.readlines():
                line = line.strip()
                if len(line):
                    result = KeywordExtraction(line).strip()
                    if len(result):
                        fpCopy.write(result + '\n')
                        print(result)
        fpCopy.close()
        # os.remove(novelName)
        # result = KeywordExtraction(fp.read())
        # print(result)