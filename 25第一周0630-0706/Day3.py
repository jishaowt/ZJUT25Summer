# 1.作用域
# 含义:指的是变量生效范围,分两种,局部变量和全局变量
# 1.1 全局变量
# 函数外部定义的变量，在整个文件都是有效的
# a = 100
# def test1():
#     print("这是test1中a的值:",a)
# def test2():
#     a = 120
#     print("这是test2中a的值:",a)
# print('调用前a的值:',a)   #调用前a的值: 100
# test1()    #这是test1中a的值: 100
# test2() #这是test2中a的值: 120
# print('调用后a的值:',a) #调用后a的值: 100

# 1.2局部变量
# 含义:函数内部定义的变量，从定义位置开始到函数结束位置有效
# def func():
#     num = 100
#     print("num:",num)
# func()
# print("num:",num)  #报错

# def funa():
#     num = 100
#     print("funa中的num:",num)
# funa()
#
# def funb():
#     num = 120
#     print("funb中的num:",num)
# funb()

# 1.3 global
# 将变量声明为全局变量
# 语法格式:global 变量名
# a = 100
# def test1():
#     print("这是test1中a的值:",a)
# def test2():
#     global a
#     a = 120
#     print("这是test2中a的值:",a)
# print('调用前a的值:',a) #调用前a的值: 100
# test2()   #这是test2中a的值: 120
# test1()   #这是test1中a的值: 120
# print('调用后a的值:',a)  #调用后a的值: 120

# def study():
#     global name,age
#     name = "python基础"
#     age = 18
#     print(f'{age}岁我们在学习:',name)
# study()  #18岁我们在学习: python基础
# print(name,age)  #python基础 18
# def work():
#     print(name)
# work()  #python基础

# global 关键字可以对全局变量进行修改，也可以在局部作用域声明一个全局变量


# 1.4 nonlocal
# 用来声明外层的局部变量,只能在嵌套函数中使用,在外部函数先进行声明,内部函数进行nonlocal声明
# a = 10
# def outer():
#     a = 5
#     def inner():
#         nonlocal a
#         a = 20
#         def inner2():
#             a = 30
#             print("inner2()中函数a的值:",a)
#         inner2()
#         print("inner()中函数a的值:", a)
#     inner()
#     print("outer()中函数a的值:",a)
# outer()  #inner2()中函数a的值: 30  inner()中函数a的值: 20  outer()中函数a的值: 20

# a = 10
# def outer():
#     a = 5
#     def inner():
#         # nonlocal a
#         a = 20
#         def inner2():
#             nonlocal a
#             a = 30
#             print("inner2()中函数a的值:",a)
#         inner2()
#         print("inner()中函数a的值:", a)
#     inner()
#     print("outer()中函数a的值:",a)
# outer()  #inner2()中函数a的值: 30  inner()中函数a的值: 30  outer()中函数a的值: 5



# 2.匿名函数
# 2.1 基本语法
# 函数名 = lambda 形参 : 返回值(表达式)
# 调用: 结果 = 函数名(实参)

# 普通函数
# def add(a,b):
#     return a+b
# print(add(1,2))

# 匿名函数
# add = lambda x, y: x + y  #x,y为匿名函数的形参，x+y是返回值的表达式 lambda不需要写return
# print(add(1, 2))

# 2.2 lambda参数形式
# 函数名 = lambda 形参 : 返回值(表达式)
# 无参数时
# func = lambda :'芒果一个'
# print(func())  #芒果一个
# 一个参数
# funb = lambda name:name
# print(funb('jishao'))  #jishao
# 两个参数时
# fund = lambda name,age=16:(name,age)
# print(fund("wang"))  #('wang', 16)
# print(fund("jishao",20)) #('jishao', 20)
# 默认参数必须写在非默认参数后面

# 关键字参数
# fund = lambda **kwargs:kwargs
# print(fund(a=1, b=2))  #{'a': 1, 'b': 2}

# 2.3 lambda 结合if判断
# a = 5
# b = 10
# print('a 比 b 大') if a > b else print('a 比 b 小')

# compa = lambda a, b: 'a 比 b 大' if a > b else 'a 比 b 小'
# print(compa(1, 2))

# lambda 特点:只能实现简单的逻辑,如果逻辑复杂就不建议使用lambda



# 3、内置函数
# 查看所有的内置函数
# import builtins
# print(dir(builtins))
# 大写字母开头一般为内置常量名,小写字母开头一般为内置函数名

# print(min(-8,5,key=abs))  #先求绝对值再比较

# zip() 将可迭代对象作为参数，将对象中对应的元素打包成一个个元组
# li = [1,2,3,4]
# li2 = ["a","b"]
# # for i in zip(li,li2):
# #     print(i)
# #     print(type(i))
# print(list(zip(li,li2)))

# map()  对每一个可迭代对象进行映射，分别去执行
# map(func,iter1):   func --自己定义的函数  iter1 要放进去的可迭代对象
# 简单来说就是对象的每一个元素都去执行这个函数
# li = [1,2,3]
# # def func1(x):
# #     return x*5
# func1 = lambda x: x*5
# mp = map(func1, li)  #函数名不需要小括号
# print(mp)  #<map object at 0x0000023DBBEE14B0>
# # for x in mp:
# #     print(x)
# print(list(mp))

# reduce()  ; 先把对象中的两个元素取出，计算出一个值然后保存着，接下来把这个计算值跟第三个元素进行计算
# from functools import reduce  #导包
# # 格式：
# print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))

# reduce(function,sequence)

# li2 = [1,2,3,4]
# def add(x,y):  #两个参数
#     return x+2*y   #19
# res = reduce(add, li2)
# print(res)


# 4、拆包
# 含义：对于函数有多个返回值，去掉元组，列表，或者字典 直接取里面的数据的过程
# tua = (1,2,3,4)
# print(tua)
# print(tua[0])

# 方法一
# tua = (1,2,3,4)
# a,b,c,d = tua
# print(a,b,c,d)

# tua = (1,2,3,4)
# a,b = tua  #报错 要求元组内的个数与接受的变量个数相同
# print(a,b)
# 一般在获取元组值的时候使用

# 方法二
# tua = (1,2,3,4)
# a,*b = tua
# print(a,b)  #1 [2, 3, 4]
# c,*d = b
# print(*d)  #3 4   套娃一样的  单独取，剩下的交给*
# 一般在函数调用时使用
# def func1(a,b,*args):
#     print(a,b)  #1 2
#     print(args,type(args))  #(3, 4) <class 'tuple'>
# func1(1,2,3,4)