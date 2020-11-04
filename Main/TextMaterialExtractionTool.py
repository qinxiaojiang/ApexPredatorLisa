#encoding=utf-8
import sys
import os



predatorBrainPath = '/home/king/Documents/APL/PredatorBrain'
emotionKeywordsPath = predatorBrainPath + '/情绪'


def GetMaterial(fileName, keyWordFile):
    keyWordHandle = open(keyWordFile, mode='r', encoding='utf-8')
    keyWordsList = keyWordHandle.read().split('\n')
    keyWordHandle.close()
    with open(fileName, mode='r', encoding='utf-8') as fp:
        lines = fp.readlines()
        for i in range(0, len(lines)):
            line = lines[i].strip()
            # 写入章节名
            if (line.find('第') != -1) and (line.find('章') != -1) and (len(line) < 20):
                print(line)
                continue
            for keyword in keyWordsList:
                # keyword = keyword.strip()
                if (len(keyword) > 0 ) and (line.find(keyword) != -1):
                    print(line)
                    break

if __name__ == '__main__':
    print('begin!')
    fileName = '/home/king/Documents/zhetian.txt'

    for file in os.listdir(emotionKeywordsPath):
        keyWordFile = os.path.join(emotionKeywordsPath,file)
        # print(keyWordFile)
        GetMaterial(fileName, keyWordFile)
    print('end!')
