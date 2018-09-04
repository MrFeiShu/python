import time

count = 0
def hano(n, a, b, c):
    '''
    汉诺塔的递归实现
    n：代表几个盘子
    a:代表第一个塔，开始塔
    b:代表第二个塔，中间塔
    c:代表第三个塔，目标塔
    '''
    global count
    if n == 1:
 #       print(a, "-->", c)
        count += 1
        return None
        
    if n == 2:
 #       print(a, "-->", b)
 #       print(a, "-->", c)
 #       print(b, "-->", c)
        count += 1
        count += 1
        count += 1
        return None
    
    # 把n-1个盘子，从a塔借助于C塔，挪到B塔上
    hano(n-1, a, c, b)
 #   print(a, "-->", c)
    count += 1
    # 把n-1个盘子，从b塔，借助于a塔，挪到c塔上
    hano(n-1, b, a, c)
    
a = "A"
b = "B"
c = "C"

n = 50
startTime = time.time()
hano(n, a, b, c)
endTime = time.time()
print("count:{0}---time:{1}".format(count, (endTime - startTime)*1000))