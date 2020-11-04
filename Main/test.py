#encoding=utf-8
import os
import docx
import subprocess
import xlrd

def FileFormatProcess(file):
    fileCopy = file + '_1'
    fpCopy = open(fileCopy, mode='a+', encoding='utf-8')
    tip = os.path.basename(file)
    with open(file, mode='r', encoding='utf-8') as fp:
        print(file)
        for line in fp.readlines():
            line = line.strip()
            if line == tip:
                continue
            if len(line):
                # print(line)
                if (len(line) < 5) and (line.find('《') < 0):  # 标签
                    line = '[' + line + ']'
                elif (line.find('《') > 0):
                    line = line + '\n'
                else:
                    line = line
                fpCopy.write(line)
    fpCopy.close()
    os.remove(file)
    os.rename(fileCopy, file)

def FileFormatProcessInPath(path):
    for file in os.listdir(path):
        if file.find('.') == -1:
            continue
        filePath = os.path.join(path, file)
        filePathCopy = filePath.split('.')[0]
        filePathCopy = filePathCopy.replace('＼','')
        tip = os.path.basename(filePathCopy)
        fpCopy = open(filePathCopy, mode='a+',encoding='utf-8')
        with open(filePath, mode='r',encoding='gbk') as fp:
            print(filePath)
            for line in fp.readlines():
                line = line.strip()
                if line == tip:
                    continue
                if len(line):
                    # print(line)
                    if (len(line) < 5) and (line.find('《') < 0): # 标签
                        line = '[' + line + ']'
                    elif (line.find('《') > 0):
                        line = line + '\n'
                    else:
                        line = line
                    fpCopy.write(line)
        fpCopy.close()
        # os.remove(filePathCopy)
        os.remove(filePath)
        # break

# 去除文件多余空格和空行
def SingleFileFormatProcess(file):
    fileCopy = file + '_1'
    fpCopy = open(fileCopy, mode='a+', encoding='utf-8')
    with open(file, mode='r', encoding='utf-8') as fp:
        print(file)
        for line in fp.readlines():
            # for num in range(48, 48+10):
            #     ch = chr(num)
            if 1:
                line = line.strip().replace(' ','\n').replace('\t','\n').replace('、', '\n')
                line = line.replace('：', '\n').replace('，', '\n').replace('；', '\n')
                line = line.replace('“', '').replace('。', '').replace('”', '')
                line = line.strip()
            else:
                line = line.strip().split('：')[0]
                line = line.strip().split('\t')[0]
                line = line.strip().split('。')[0]
                line = line.split('】')[0].replace('【','')
            if (len(line)):
                fpCopy.write(line + '\n')
    fpCopy.close()
    os.remove(file)
    # os.remove(fileCopy)
    os.rename(fileCopy, file)

def Docx2TxtInPath(path):
    for file in os.listdir(path):
        if (file.find('.') == -1) or (len(file.split('.')[0]) == 0):
            continue
        filePath = os.path.join(path, file)
        filePathCopy = filePath.split('.')[0]
        filePathCopy = filePathCopy.replace('＼','')
        tip = os.path.basename(filePathCopy)
        fpCopy = open(filePathCopy, mode='a+',encoding='utf-8')
        if (len(file.split('.')) < 2):
            continue
        if (file.split('.')[1] == 'doc'):
            output = subprocess.check_output(["antiword", filePath])
            docText = output.decode('utf-8')
        elif (file.split('.')[1] == 'docx'):
            doc = docx.Document(filePath)
            docText = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
        else:
            print(filePath)
        # print(docText)
        fpCopy.write(docText)
        fpCopy.close()
        SingleFileFormatProcess(filePathCopy)
        os.remove(filePath)
        # break

def RenameInPath(path):
    for file in os.listdir(path):
        # iList = file.split(' ')
        # if len(iList) > 2:
        #     newFile = iList[1] + '-' + iList[2]
        # elif len(iList) == 2:
        #     newFile = iList[1]
        # else:
        #     newFile = file
        # decFile = os.path.join(path, newFile)
        srcFile = os.path.join(path, file)
        if ((srcFile.find('(') != -1) and (srcFile.find(')') != -1)):
            os.remove(srcFile)
            continue
        # if (srcFile.find('章') != -1):
            # os.rename(srcFile, decFile)

if __name__ == "__main__":
    path = '/home/king/Documents/APL/TT'
    # path = '/media/king/A60E087C0E0847AF/我的小说/素材/食物'
    # FileFormatProcessInPath(path)
    # FileFormatProcess(path)
    SingleFileFormatProcess(path) # 去除文件多余空格和空行
    # RenameInPath(path) #修改文件夹中的文件名
    # Docx2TxtInPath(path) #将doc文档转化为txt格式

