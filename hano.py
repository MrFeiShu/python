level = 0

def hano(n, a, b, c):
    '''
    汉诺塔移动
    n:第几个盘子
    a:第一个塔，起始塔
    b:第二个塔，中间塔
    c:第三个塔，目标塔
    '''
    global level
    level += 1
    print("---{0}--------enter---".format(level))
    if n == 1:
        print(a, "-->", c)
        print("---{0}--------levae-1--".format(level))
        return None

    if n == 2:
        print(a, "-->", b)
        print(a, "-->", c)
        print(b, "-->", c)
        print("---{0}--------levae-2--".format(level))
        return None

    hano(n-1, a, c, b)
    print(a, "-->", c)
    hano(n-1, b, a, c)

# 关于vscode提交GitHub演示
n = 4
a = "A"
b = "B"
c = "C"
hano(n, a, b, c)