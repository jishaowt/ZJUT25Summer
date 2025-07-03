# 1、类型转换
# 1.1 int()
# a = 1.2
# print(type(a))
# b = int(a)
# print(b,type(b))

# str->int
# print(int("1.2")) #报错
# print(int("-10")) #如果字符串里面有除数字和正负号(得数字前)以外的字符，就会报错， .也会
# print(int('10-')) #报错

# age = int(input('输入你的年龄:'))
# print(type(age))
#
# if age >= 18:
#     print('成年人')
# else:
#     print('未成年')


# 1.2 float()
# print(float(input('输入一个数：')))
# 字符串转换与int相同


# 1.3 str() 任何类型都可以转化为字符串
# n = 100
# print(type(n))
# n2 = str(n)
# print(type(n2))
# st = str(-1.8000)  #会去除尾部为0的数
# print((st))

# li = [1,2,3,4,5]
# print(type(li))
# st = str(li)
# print(st)
# print(type(st))

# 1.4 eval()   #用来执行一个字符串表达式，返回一个表达式的值  即去引号
# print(10+10)
# print('10+10')
# print('10'+'10')
# print(eval('10'+'10'))  #1010
# print(eval('10+10'))   #20

# str -> list
# str = "[[1,2],[3,4],[5,6]]"
# print(str,type(str))  #[[1,2],[3,4],[5,6]] <class 'str'>
# list = eval(str)
# print(list,type(list))  #[[1, 2], [3, 4], [5, 6]] <class 'list'>

# str-> dict  与 str -> list 相同

# eval() 强大但不够安全，可以被任意篡改


# 1.5 list()
# 可转化的类型有：str、tuple、dict、set
# print(list("asdfgg"))  #['a', 's', 'd', 'f', 'g', 'g']
# print(list(123456))  #报错



# 2.深浅拷贝
#2.1赋值
# li = [1,2,3,4,5,6,7,8,9]
# li2 = li
# print("li:",li)
# print("li2:",li2)
# li.append(10)
# print("li:",li)
# print("li2:",li2)
# 赋值:等于一个共享资源,一个值的改变会完全被另一个值共享


# 2.2钱拷贝
# 会创建新的对象,拷贝第一层的数据,嵌套层会指向原来的内存地址
# import copy  #引入copy
# li = [1,2,3,4,[5,6,7]]
# li2 = copy.copy(li)
# print(li)
# print(li2)
# 查看内存地址 id()
# print(id(li))  #内存地址不同
# print(id(li2))
# li.append(8)
# print(li)
# print(li2)
# print(li[3])  #4  外层的内存地址不同，但是内层的内存地址相同
# print(li2[3]) #4
# 优点; 效率高,占用空间少,数据半共享


# 2.3 深拷贝 数据完全不共享
# import  copy
# li = [1,2,3]
# li2 = copy.deepcopy(li)
# print(li)
# print(li2)
# li.append(10)
# li2.append(8)
# print(li)
# print(li2)
# print(id(li))
# print(id(li2))
# print(id(li[3])) #拷贝前的地址相同，修改后不同
# print(id(li2[3]))
# 深浅拷贝只针对可变对象，不可变对象没有拷贝说法。



# 3.可变类型
# 常见的可变类型: list、dict、set
# li = [1,2,3]
# print(id(li))
# li.append(4)
# print(id(li))



# 4.不可变对象  数值型、字符串、元组
# 变量对应的值不能被修改,如果修改就会生成一个新的值从而分配新的内存空间
# n = 10
# print('原地址:',n,id(n)) #原地址: 10 140717736543432
# n = 15
# print('新地址:',n,id(n)) #新地址: 15 140717736543592

# str = '112'
# print(id(str))  #2090161836592
# str = '1223'
# print(id(str))  #2090162402432

# tua = (1,2,3)
# print(id(tua)) #1414207423168
# tua = (13,33)
# print(id(tua)) #1414167018944



# 5.函数
# 含义:将对立的代码块组织成一个整体，使其具有特殊功能的代码集，在需要的时候能被调用

# 5.1定义函数
# def 函数名():
#     函数体

# 5.2 调用函数
# 函数名()

# def login():
#     print("登录成功")
#     print("_______")
# 调用前，要保证函数已经定义
# login()



# 6.返回值 return
# 函数执行结束后,最后給调用者一个结果

# def buy():
#     return "芒果",20 #('芒果', 20),遇到return就结束了，下面代码不执行,多个返回值时以元组形式返回
# print(buy())

# 1、没有return 返回None
# 2、一个return，就把值返回给调用者
# 3、多个返回值，以元组形式给调用者

# return 与 print区别
# 1、return表示函数结束,print会一直执行
# 2、return是返回结果,print是打印结果



# 7.参数
# 7.1形参与实参
# 定义格式:
# def 函数名(形参a,形成b):   #形参，定义函数时的变量
#     函数体
# 函数名(实参1,实参2)  #调用函数是，小括号里面的具体值

# def add(a,b):
#     return a+b
# print(add(2,3))

# 7.2函数参数
# 1、必备参数(位置参数)
# 含义:传递与定义的参数个数与顺序一致

# 2、可设置默认值,按顺序来

# 3、可变参数
# 格式:def func(*args)  #以元组形式接受
# def func(*args):
#     print(args)
#     print(type(args))
# func('海绵宝宝','派大星','章鱼哥')  #('海绵宝宝', '派大星', '章鱼哥')  <class 'tuple'>

# 4、关键字参数
# 格式:def func(**kwargs)  #以字典形式接受
# def fund(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
# fund(a=1, b=2, c=3)  #采用键等于值的形式  {'a': 1, 'b': 2, 'c': 3}  <class 'dict'>
# 作用:扩展函数的功能




# 8.函数嵌套
# 8.1嵌套调用
# 含义:在一个函数里面调用另一个函数
# def study():
#     print("studing",end=' ')
# def course():
#     study()
#     print("Python基础语法")
# course()  #studing Python基础语法

# 8.2嵌套定义
# 含义:在一个函数中定义另外一个函数
# def study():
#     print("studing",end=' ')
#     def func():
#         print("Python基础语法")
#     func()  #不要在内层函数调用外层函数
# study()  #studing Python基础语法
