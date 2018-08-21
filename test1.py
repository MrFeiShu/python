#strspn(sStr1,sStr2)
sStr1 = '#define CFG_MANAGE_TOOL_CERT_INFO_CERTTYPE_CRYPT                0x00210104  // 证书信息-证书类型-加密证书'
sStr2 = 'CFG_'
#sStr1 and chars both in sStr1 and sStr2
pos = sStr1.find(sStr2)
print(type(pos))
print(pos)

#file = open("E:\\svn\\Software\\Projects\\EsStd\\Trunk\\Import\\Include\\EsConfig\\configAll.h", "r")
fileTarget = open("E:\\svn\\Software\\Projects\\EsStd\\Trunk\\Import\\Include\\EsConfig\\configAllTarget.h", "w+")
#str = file.read()
#print(str)
#fileTarget.write(str)
fileTarget.writelines(sStr1)
fileTarget.writelines(sStr2)
