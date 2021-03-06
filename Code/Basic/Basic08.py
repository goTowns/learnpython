'''
功能：九九乘法表
重点：循环结构的嵌套
作者：薛景
最后修改于：2019/05/27
'''

for i in range(1,10):
    for j in range(1,10):
        print("%d*%d=%2d" % (i, j, i*j), end=" ")
        # 格式符“%2d”表示该整数占2个字符宽度
        # print函数的参数end=" "表示以空格作为输出的结束标记，取代原来的默认的换行
    print()     # 此处的print语句表示打印一个换行

'''
简单的解释一下：因为内层循环9次，外层循环也是9次，所以内层中的print，一共执行了81次
而程序中的第二个print语句，因为只被外层循环包括，未包括在内层存循环中，所以只执行了9次

思考题：我国古代数学家张丘建在《算经》一书中提出的数学问题：公鸡一只值五钱，母鸡一只值
三钱，小鸡三只值一钱。百钱买百鸡，问公鸡、母鸡、小鸡各几何？
'''