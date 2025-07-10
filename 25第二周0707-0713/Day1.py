# 1.递归函数
# 含义：一个函数内部不调用其他函数，而是调用他自己本身的话，这个函数就是递归函数
# 条件
# 1、必须要有一个明确的结束条件 --递归出口
# 2、相邻两次重复之间有紧密的联系
# 3、每次更进一步的递归，问题规模相比上次递归都要有所减少

# 实现1-100相加
# def add():
#     s = 0
#     for i in range(101):
#         s += i
#     print(s)
# add()

# 递归函数
# def add2(n):
#     if n == 0:
#         return 0
#     return n + add2(n-1)
# print(add2(100))

# 斐波那契数列
# 1,1,2,3,5,8
# def func1(n):
#     if n <= 1:
#         return n
#     return func1(n-2)+func1(n-1)
# print(func1(6))

# 优点：
# 简洁，逻辑清晰，解题更加明了
# 缺点：
# 占用内存空间大



# 2.闭包
# 2.1条件
# 1、函数嵌套(函数里面再定义函数)
# 2、内层函数使用外层函数的局部变量
# 3、外层函数的返回值是内层函数的函数名

# def outer():
#     n = 10
#     def inner():
#         print(n)
#     return inner   #返回inner 而不是inner()是因为inner函数有参数时，写法不规范
# print(outer())  #返回的是内层函数的内存地址

# 2.2调用写法
# 第一种调用写法
# outer()()
# 第二种调用写法
# ot = outer()  #调用外函数  <function outer.<locals>.inner at 0x000001D3EFF50FE0>
# ot()           #调用内函数  10


# def outer(m):  #外函数，m是形参，也是外函数的局部变量
#     n = 10
#     def inner():  #内函数
#         print('计算结果是:',m+n)
#     return inner  #返回inner 而不是inner()是因为inner函数有参数时，写法不规范
# ot = outer(20)  # 调用函数，返回的是内层函数的内存地址
# ot()  #调用内函数

# 函数引用
# def funa():
#     print(123)
# print(funa) #函数名里面保存了函数所在的位置的引用

# id(): 判断两个变量是否是同一个值的引用
# a = 1  #a是变量名，存的是1这个数值所在的地址，就是a存了对数值1的引用
# print(a)
# print(id(a))

# a = 2  #值发生了变化，内存地址也会变化
# print(id(a)) #140717651018696
# print(id(2)) #140717651018696

# def test1():
#     print('111')
# test1()
# print(test1)  #内存地址
# te = test1
# te()       #通过函数引用调用函数

# 2.3 每次开启内涵数都在使用同一份闭包变量
# def outer(m):
#     print('这是outer()函数中的值：',m)
#     def inner(n):
#         print('这是inner()函数中的值：',n)
#         return  m+n # 在inner函数中 返回m+n
#     return inner
# ot = outer(10)  #调用外函数，给outer()传值
# # 第一次调用内函数，给inner()函数传值
# print(ot(20))  #调用内函数，给inner()传值   10+20
# # 第二次调用内函数
# print(ot(50)) # 10+50

# 总结: 使用闭包的过程中，一旦外函数被调用一次，返回了内函数的引用，虽然每次调用函数，会开启一个函数
#      但是闭包变量实际上只有一份，每次开启内涵数都在使用同一份闭包变量



# 3.装饰器
# def test(fn):   #fn是普通形参
#     print('登入')
#     print('注册')
#     fn()
# def test2():
#     print('打印')
# test(test2)
# 以上修改核心代码与增加调用都不合适

# 装饰器含义:本质就是一个闭包函数，它的好处就是在不修改原有代码的基础上，增加额外功能
# 条件：
#         1、不修改原程序或函数的代码
#         2、不改变函数或程序的调用方法

# 3.1 标准版的装饰器
# 被装饰的原函数：
# def send1():
#     print("护送高考试卷到浙江省")
#
# # 写一个闭包函数作为装饰器来增加对原函数
# def outer1(fn):
#     def inner1():
#         print("护送高考试卷到江苏省")
#         fn()  #被装饰的函数  send1()
#         print("护送高考试卷到上海市")
#     return inner1
#
# ot = outer1(send1)
# ot()

# 装饰器的原理就是将原有的函数重新定义为以原函数为参数的闭包


# 3.2 语法糖
# 格式 ；@装饰器名称
# def outer1(fn):
#     def inner1():
#         print('111')
#         fn()
#         print('333')
#     return inner1
#
# @outer1      #这个就是语法糖  给函数的帽子
# def send():
#     print('222')
# send()

# 3.3被装饰的函数有参数
# def outer(fn):
#     def inner(name):
#         fn(name)
#         print(f'{name}在当监考老师，可是又出门打游戏去了')
#         print('他很开心开心')
#     return inner
# @outer
# def func1(name):
#     print('这是被装饰的函数，徐浩然')
# func1('jishao')

# 3.4被装饰的函数有多个参数
# def func(*args,**kwargs):
#     print(args)
#     print(kwargs)
# # func(name= 'jishao')
#
# def outer(fn):
#     def inner(*args,**kwargs):
#         fn(*args,**kwargs)
#         # print(f'{args}{kwargs}了，在当监考老师，可是又出门打游戏去了')
#         # print('他很开心开心')
#     return inner
# ot = outer(func)
# ot('susu','nanana',name = 'jishao',age= 18)


# 3.5 多个装饰器
# 第一个装饰器
# def deco1(fn):
#     def inner():
#         return '哈哈哈'+fn()+"优秀"
#     return inner
# # 第二个装饰器
# def deco2(fn):
#     def inner():
#         return "优秀,"+fn()+'基础很好'
#     return inner
# # 被装饰的函数一
# @deco1
# @deco2  #先离函数近的语法糖先执行，外层再执行
# def test():
#     return '晚上学python'
# print(test())

# ————————————————python基础学习完毕——————————————




















