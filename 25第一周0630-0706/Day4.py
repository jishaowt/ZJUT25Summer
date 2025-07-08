# 1、异常
# 含义：程序执行过程中出现的非正常的流程现象
from inspect import Traceback

# 1.1 常见种类
# NameError:使用一个还未被赋值的变量
# SystemError:代码不符合python语法规定
# IndexError:下标/索引超出范围
# ZeroDivisionError:除数为0
# KeyError:字典不存在这个键
# IOError:输入/输出操作失败
# AttributeError:对象没有这个属性
# ValueError:传入的值错误
# TypeError:类型错误，传入类型不匹配
# ImportError:无法引入模块或包，基本上是路径问题
# IndentationError:缩进错误，代码没有正确对齐

# 1.2异常处理
# 方法一: 根据控制台的错误提示找到错误点并分析改正
# print(abc)
# Traceback:异常的追踪信息，可以追溯到程序的异常的具体位置
# XXXError:异常类型，后面会包含异常具体信息

# 方式二:对异常进行捕获处理

# 异常处理(捕获异常)
# 语法格式一:
# try:
#     不能确定是否能够执行正常执行的代码  一般只放一行代码
# except:
#     如果检测到异常，就执行这个位置的代码
#     可以声明了指定异常类型(元组形式编写),错误不是指定类型则会报错
#     Exception是万能异常，捕获任意异常类型

# try:
#     print(abc)
# except:
#     print("上面代码有错误哦！")

# try:
#     print(abc)
# except Exception as e:
#     # as e 相当于把异常信息保存到变量e中
#     print("上面代码有错误哦！")
#     print(e)   #name 'abc' is not defined


# 语法格式二:
# try:
#     可能引起异常的代码
# except:
#     出现异常现象的处理代码
# else:
#     没有捕获异常执行的代码

# try:
#     print('aa')
# except Exception as e:
#     print(e)
#     print('error')
# else:
#     print('else:no error')

# st = [1,2,3,4,5]
# try:
#     print(st[4])
# except Exception as e:
#     print(e)
#     print('error')
# else:
#     print('没有超出下标范围')


# 语法格式三:
# try:
#     可能引起异常的代码
# except:
#     出现异常现象的处理代码
# else:
#     没有捕获异常，则执行的代码
# finally:
#     try代码结束后运行的代码，不管异常是否存在，都会执行

# st = [1,2,3,4,5]
# try:
#     print(st[4])
# except Exception as e:
#     print(e)
#     print('error')
# else:
#     print('没有超出下标范围')
# finally:
#     print('真开心,美好的一天，没什么东西能打扰我的输出')


# 抛出异常  raise
# 步骤
# 1、创建一个Exception('xxx')对象,xxx是异常提示信息
# 2、raise抛出这个对象(异常对象)

# raise Exception("异常抛出")

# def func1():
#     raise Exception("异常抛出")
#     print('nb')  #执行了raise语法，后面不会执行
# func1()

# 需求:用户输入密码,判断密码长度是否符合规范,不符合抛出异常
# def login():
#     pwd = input('请输入密码')
#     if len(pwd) == 6:
#         print('密码长度正确')
#         return '登录成功'
#     else:
#         raise Exception('密码长度不符合')
# try:
#     print(login())
# except Exception as e:
#     print(e)

# 捕获异常是为了检测到异常时，程序能进行执行，程序不会终止