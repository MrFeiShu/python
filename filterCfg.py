def formatCfg(line):
    '''
        格式化配置项
        "#define CFG_EXIT                                                0x0021001F  // 退出"，切分成下面结果
        [CFG_EXIT, 0x0021001F,// 退出]
        :param line:一行配置项
        :return:切分后的配置项list类型：[$(配置项宏名称), $(配置项宏值), $(配置项注释)]
    '''
    listCfg = []
    if "#define CFG_" in line:
        strCfg = "CFG_"
        str0x = "0x"
        strBackSlash = "// "

        posBegin = line.find(strCfg)
        posEnd = line.find(" ", posBegin)
        part1 = line[posBegin:posEnd]
        listCfg.append(part1)

        posBegin = line.find(str0x, posEnd)
        posEnd = line.find(" ", posBegin)
        part2 = line[posBegin:posEnd]
        listCfg.append(part2)

        posBegin = line.find(strBackSlash, posBegin)
        posEnd = len(line)
        part3 = line[posBegin:posEnd-1]
        listCfg.append(part3)

        return listCfg

def readCfgs(filePath):
    '''
    切分指定配置文件中的所有配置项
    :param filePath:配置头文件路径
    :return:所有配置项的切分结果，二维list类型
    '''
    listAllCfg = []
    fileCfg = open(filePath, "r")

    for line in fileCfg:
        listCfg = formatCfg(line)
        if None != listCfg:
            listAllCfg.append(listCfg)

    return listAllCfg

def funFilter(fileName, filterFileName, fileNameTarget):
    '''
    依据filterFileName中的配置，过滤fileName中的配置项，并保存到fileNameTarget中
    :param fileName:配置文件
    :param filterFileName:过滤配置文件
    :param fileNameTarget:保存切分后结果
    :return:None
    '''
    fileFilter = open(filterFileName, "r")
    fileTarget = open(fileNameTarget, "w+")

    strData = fileFilter.read()

    count = 0
    listCfgAll = readCfgs(fileName)
    for listCfg in listCfgAll:
        strItem = "({0},".format(listCfg[0])
        if strItem in strData:
            str = "{0}\t{1}\t{2}\n".format(listCfg[0], listCfg[1], listCfg[2])
            fileTarget.writelines(str)
            count += 1
    print("总共有{0}项配置".format(count))

filePath1 = "E:\\svn\\Software\\Projects\\EsStd\\Trunk\\Import\\Include\\EsConfig\\configAll.h"
filePath2 = "E:\\svn\\Software\\Projects\\EsStd\\Trunk\\Modules\\EsLocalCfgTool\\Sources\\ConfigProjectStd.cpp"
filePath3 = "E:\\svn\\Software\\Projects\\EsStd\\Trunk\\Import\\Include\\EsConfig\\Result.h"

# 我再试一次提交git
funFilter(filePath1, filePath2, filePath3)