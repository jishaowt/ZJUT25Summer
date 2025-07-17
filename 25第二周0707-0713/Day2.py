# 1.类与对象
# 1.1 类的三要素：1、类名 2、属性 3、方法
# 举例：
# 类名：人类
# 属性：肤色，身高，性别，年龄
# 方法：行走，思考，说话，学习

# 1.2 定义类
# 基本格式
# class 类名:
#     代码块

# class Washer:
#     height = 800
#     width = 600
# 查看属性 类名.属性名
# Washer.width = 1000
# print(Washer.width)

# 1.3 创建对象
# 对象名 = 类名()
# wa = Washer()
# print(wa)  #<__main__.Washer object at 0x0000028697B0D2B0>  对象在内存中的地址
#
# wa2 = Washer()
# print(wa2) #<__main__.Washer object at 0x0000021E03ED5090>  实例化多个对象

# 1.4 实例的方法和实例属性
# 1.4.1
# 实例方法：由对象调用，至少有一个self参数，执行实例方法的时候，自动将调用该方法的对象赋值给self

# class Washer():
#     width = 800
#     def wash(self):
#         print("我会洗衣服",self)
#         print("我会洗碗")
# # 实例化对象
# wa = Washer()
# print(wa)
# # 调用对象
# wa.wash()

# 1.4.2 实例属性
# 格式:self.属性名
# class Person:
#     name = 'jishao'
#     def introduce(self):
#         print('我是实例方法')
#         print(f'{Person.name}的年龄:{self.age}')
# pe = Person()
# pe.age = 20
# print(pe.age) #20 实例属性只能由实例访问,私有的,类属性是公共的
# pe.introduce()


# 2.构造函数  __init__()
# 作用：通常用来属性初始化或者赋值操作
# 注意：在类实例化对象的时候，会被自动调用

# class Person:
#     def __init__(self,name,age,gender,high):
#         print('这是__init__函数')
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.high = high
#     def play(self):
#         print('打LOL手游')
#     def introduc(self):
#         print(f'{self.name}的年龄是{self.age}，在打{self.play()}')
#
# pe = Person('wang',18,'male',175)
# pe.introduc()
# pe.play()
# pe2 = Person('jishao',11,'male',125)
# pe2.introduc()
# pe2.play()


# 3.析构函数 __del__()
# 删除对象的时候,解释器会默认调用__del__()方法

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('我是__init__函数')
#     def __del__(self):
#         print('我是__del__函数，被销毁了')
# p = Person('jishao', 22)
# # del p 语句执行的时候，内存会立即被回收，会调用对象本身的__del__()方法
# del p
# # 正常运行时，不会调用__del__(),对象执行结束之后，系统会自动调用__del__，主要表示语句块结束，回收内存

# ————————————————python基础学习完毕——————————————



# 人工智能基础    以下都在jupyter notebook 运行得出
# pip install matplotlib

# import matplotlib
# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# print(x,y)
#
# from matplotlib import pyplot as plt
# fig1 = plt.figure(figsize=(5,5))
# plt.plot(x,y)#直线图
# plt.show()   #显示

# from matplotlib import pyplot as plt
# fig1 = plt.figure(figsize=(5,5))
# plt.scatter(x,y)   #散点构图
# plt.title('y vs x')  #标题
# plt.show()

# numpy 的引入，数组的生产
# import numpy as np
# a = np.eye(5)  #5行5列 的单位矩阵E
# print(type(a))
# print(a)


# b = np.ones([5,5])   #5行5列 都是1的矩阵
# print(type(b))
# print(b)
# print(b.shape)

# c = a+b    #矩阵相加
# print(type(c))
# print(c.shape)
# print(c)











