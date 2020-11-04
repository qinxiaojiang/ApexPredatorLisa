#encoding=utf-8
import os
import docx
import subprocess

gSpecialSymbolsTup = ('：', '、', '（', '>', '》', '，', '；', '。') # 分割符号
gTruncationSymbolList = ['（', '《', '<', '▪', '/'] # 替换符号

class TextProcessingSystem:
    isRemoveSrcFile = False
    def __init__(self):
        pass
    def TextProcessingSystem(self):
        pass
    def HandleSymbolsInFiles(self, fileName, isRemoveSrcFile=False):
        srcFile = fileName
        path = os.path.split(srcFile)
        file = path[1].split('.')
        desFile = os.path.join(path[0], file[0] + 'Tmp.txt')
        # copyFile = os.path.join(path[0], file + 'Copy.txt')
        srcFileFp = open(srcFile, mode='r', encoding='utf-8');
        desFileFp = open(desFile, mode='w+', encoding='utf-8');
        # copyFileFp = open(desFile, mode='w+', encoding='utf-8');
        for line in srcFileFp.readlines():
            # 去除空格/制表符/
            line = line.strip().rstrip().replace('\t', '')
            if len(line):
                # 将英文字符全部替换为中文字符
                line = line.replace(',', '，').replace('.', '。').replace('!', '！').replace('!', '！')
                line = line.replace(' ', '').replace('(', '（').replace(')', '）').replace('[', '【').replace(']', '】')
                line = line.replace('?', '？') + line.replace('"', '') + '\n'
                desFileFp.write(line)
                # print(line)
        srcFileFp.close()
        desFileFp.close()
        if isRemoveSrcFile:
            os.remove(srcFile)
            os.rename(desFile, srcFile)

    def RemoveSpecialCharacter(self, str):
        for chr in str:
            if ((gTruncationSymbolList.count(chr) != 0) or (chr.isdigit())):
                str = str.replace(chr, '')
        return str

    def TruncationStringBySpecialSymbols(self, str):
        for ch in gSpecialSymbolsTup:
            if str.count(ch):
                str = str.split(ch)[0]
        return str

    def GetDict2BaiduEncyclopedia(self, filename, myDictFile):
        # 载入自定义字典
        with open(myDictFile, mode='r', encoding='utf-8') as fp:
            dictList = fp.readlines()
        # 移除dictList中的空字段
        while dictList.count('\n'):
            dictList.remove('\n')
        resultList = []
        srcFileFp = open(filename, mode='r', encoding='utf-8');
        desFileFp = open(myDictFile, mode='a+', encoding='utf-8');
        for line in srcFileFp.readlines():
            line = self.TruncationStringBySpecialSymbols(line)
            line = self.RemoveSpecialCharacter(line)
            line = line.replace('\n', '') + '\n'

            if ((dictList.count(line) == 0) and (resultList.count(line) == 0)):
                line = self.RemoveSpecialCharacter(line)
                if (len(line) > 8) or (line == '\n'):
                    continue
                resultList.append(line)
                # print(line)
        desFileFp.writelines(resultList)
        srcFileFp.close()
        desFileFp.close()


if __name__ == "__main__":
    doc = docx.Document('/media/king/A60E087C0E0847AF/我的小说/素材/创作手法资料/修真小说分类.docx')
    docText = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    print(docText)