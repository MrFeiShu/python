def readLines(line):
    listCfg = [] # create empty list
    line = line.expandtabs()
    if "#define CFG_" in line:
        strCfg = "CFG_"
        str0x = "0x"
        strBackSlash = "// "

        posBegin = 8
        posEnd = line.find(" ", posBegin)
        part1 = line[posBegin:posEnd]
        print("-------part1-1--------")
        print("-{0}-".format(part1))
        pos = part1.find(" ")
        part1.rstrip()
        part1.rstrip("\t")
        print("--{0}--".format(part1))
        print("-------part1-2-----------")
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

listCfg = []

listCfg1 = readLines("#define CFG_CERT_INFO_TYPE_SIGNATURE                            0x00210037  // 签名证书\n")
listCfg.append(listCfg1)

listCfg2 = readLines("#define CFG_CERT_INFO_TYPE_KEYEXCHANGE                          0x00210038  // 交换证书\n")
listCfg.append(listCfg2)

print(type(listCfg))
print(listCfg)

file = open("E:\\svn\\Software\\Projects\\EsStd\\Trunk\\Import\\Include\\EsConfig\\configAll.h", "r")
strData = file.read()
print("--file--{0}".format(type(strData)))
if listCfg1[0] in strData:
    print("fuck world")

#for lsitIndex in listCfg:
#    print("*" * 50)
#    print(type(lsitIndex[0]))
#    print("{0}\t{1}\t{2}".format(lsitIndex[0], lsitIndex[1], lsitIndex[2]))

