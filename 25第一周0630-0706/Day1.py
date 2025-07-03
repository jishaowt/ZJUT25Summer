# 1 常见bug：1输入错误  2缩进错误 3语法错误 4命名错误

# 2 断点调试
# print(123)
# print(123)
# print(123)
# print(123)
# print(123)
# debug中代码蓝色为要运行的代表
# Show Exception point 显示执行断点
# Step Into 下一步
# Run to Cursor 跳到下一个断点的位置

# 3 注释
"""
我是多行注释
"""
from os import remove

'''
我是多行注释
而 ctrl+/ 是单行注释 增加或减少
'''

# 4 快捷键:ctrl+D 是复制到下一行 ctrl+f 是查找

# 5 输出函数print()
# print("哈哈哈""嘻嘻嘻""嘿嘿嘿")
# # 英文逗号
# print("哈哈哈","嘻嘻嘻","嘿嘿嘿")
# # sep用法 默认为空
# print("哈哈哈","嘻嘻嘻","嘿嘿嘿",sep='|')
# # end用法 默认是\n
# print("hello",end=" ")
# print("world")
# print("hello world")

# 6 变量 作用:用于保存数据  格式: 变量名 = 值    可重复赋值、其他类型
# num1 = 1  # 1、在内存中创建一个1的数据 2、创建一个变量num1，把1这个数据保存到变量num1中
# num2 = 10
# total = num1+num2
# print(total)

# 7 标识符  规定:字母、数字、_ 组成 数字不能开头  不能是关键字  严格区分大小写

# 8 命名规范  1、见名知义 username 2 下划线分隔法 user_name 3 驼峰法 UserName

# 9 数值类型  检查数据类型方法 type()  1、整型:int 2、浮点型:float 3、布尔型:bool (True  False) 4、复数型:complex( z= a + bj,j是固定的)

# 10 字符串 用单引号或双引号
# name = jishao #报错
# name = "jishao"
# print(type(name))

# 11 格式化输出
# 占位符  %  %s字符串  %d整型  %4d 设置数字位数，不足前面补空白,超出原样输出  %f 默认保留后6位小数
# name = "jishao"
# age = 6
# weight = 120
# print("name是:%s,age是:%d,weight是:%06d"%(name,age,weight))
# print("name是:%s,age是:%d,weight是:%02d"%(name,age,weight))
##%%  使用
# print("I am %%jishao%%" %())
## f格式化
# name = "jishao"
# age = 6
# print(f"name是:{name},age是:{age}")

# 12 运算符  + - * /  除的商是浮点型  //取整除,忽略小数,拿整数部分   %取余   **取幂

# 13 输入函数 input()  为字符串类型
# name = input("请输入姓名:")
# print(name)
# name1 = input("请输入姓名one:")
# name2 = input("请输入姓名two:")
# name3 = name1+name2
# print(name3)

# 14 转义字符 \t制表符 \n换行符 \r回车 \\反斜杠符合  r原生字符串，不转义
# print("321\t654")
# print("321\r654")
# print("321\\456")
# print(r"321\r654")

# 15 if判断  注意缩进  else: 不添加条件
# age = 17
# if age<18:
#     print('禁止未成年人进入')
#
# score = eval(input("请输入成绩:"))
# if score == 100:
#     print("你真帮！")
# elif score < 100 and score > 60:
#     print("不错！")
# else:
#     print("加油，继续努力！")
#
# temp = 36.5
# ticket = False
# if ticket == True:
#     print('可以进站了哈哈哈',end=',')
#     if temp >= 36.5 and temp <= 37.3:
#         print('体温正常，可以回家了')
#     elif temp >= 40:
#         print('体温异常，需要隔离')
# else:
#     print('没票先购票')

# 16 while循环
# i = 0
# sum = 0
# while i<=100:  #成立则循环，不成立则退出
#     sum += i
#     i += 1
# print(sum)
#九九乘法表
# i = 1
# j = 1
# while i <= 9:
#     while j <= 9:
#         print(f"{i}*{j}={i*j}",end="\t")
#         j = j + 1
#     print("\n")
#     j = i + 1
#     i = i + 1

# 17 for循环
# str= "hello world"
# for i in str:
#     print(i)
##range()使用方法
# for i in range(1,9,2):
#     print(i)
#
# s = 0
# for i in range(1,101):
#     s = s + i
# print(s)

# 18 break 与 continue 的差异

# 19 字符串
#Unicode 都是2个字符 转化快，占用空间大   utf-8：不定长编码，精确对应，慢，空间少
# str = 'hello'
# print(type(str))
# str1 = str.encode() #编码
# print("编码后的str:",str1)
# print(type(str1)) #bytes，以字节为单位进行处理
# str2 = str1.decode() #解码
# print("解码后的str1:",str2)
# print(type(str2))
#
#常见操作
# +字符串拼接  *字符串重复输出str*2
# str[i]输出字符串第i-1个成员，可负。可切片   in/not in判断成员是否在 返回bool型
# st = "asdfghjkl"
# print(st[-1::-1]) #lkjhgfdsa
# print(st[-1::])  #l
# print(st[-1:-5:-1])#lkjh
# 查找
# print(st.find("a"))  #返回下标
# print(st.find("w",0,9)) #找不到返回-1
# print(st.index("w")) #返回下标，找不到报错
# count 匹配字符个数，没有返回0
# upper() and lower()  isupper() and islower() 判断对象为整体
# startwith()判断子字符串是否在 开头，返回bool型
# endtwith()判断子字符串是否在  结尾，返回bool型
# 修改
# replace(旧,新,次数)
# split() 指定分隔符来切字符串,默认多次
# st = "hello,python"
# print(st.split(","))  #['hello', 'python']
# print(st.split("o"))  #['hell', ',pyth', 'n']
# print(st.split("a"))  #['hello,python']
# print(st.split("o",1))  #['hell', ',python']
# capitalize():第一个大写，其它小写
# str= "aaAAA"
# print(str.capitalize()) #Aaaaa

# 20 列表
# 列表名 = [元素1,元素2,...]  与字符串一样是可迭代对象，可for循环取值
# 添加
# li = ["one","two","three"]
# li.append("four")  #只能尾部增加,元素始终是一个一个增加
# li.append(["five","six"])
# li.extend(["five","six"]) #尾部批量增加元素
# li.insert(1,"seven")  #必须指定位置
# print(li)
# li.sort()
# print(li)
# li.insert("seven")  #报错
# 修改
# 直接通过下标修改
# 查找
# in / not in
# 删除
# del li[2]  下标
# pop 默认删除最后一个，超出报错，下标
# remove 根据元素值来删除，不存在报错，值
# 排序
# sort and  reverse:列表倒序，不看值
#
# 列表推到式
# [表达式 for 变量 in 列表]
# li = [1,2,3,4,5]
# [print(i*5) for i in li]
# [表达式 for 变量 in 列表 if 条件]
# [print(i*5) for i in li if i%2==1]
# 列表嵌套 看成多维的 li[][]

# 21 元组 tuple  只能查，不能增删改
# 元组名 = (元素1,) #只有一个末尾必须加,
# count(),index(),len()
# 应用场景: 1、函数的返回值和参数 2、格式化输出后面的()本质就是一个元组 3、数据不可以被修改，保护数据安全

# 22 字典
# 字典格式: 字典名 = {建1:值1,建2:值2,...}
# 键名具有唯一性,键与值成对出现
# dic = {'name':'wang','name2':'jishao'}
# print(type(dic))
# print(dic)
# 常见操作 增删改查
# 查找  变量名[键名]  |  变量名.get(键名)
# dic = {'name':'wang','name2':'jishao'}
# print(dic['name'])  #wang
# print(dic['age'])   #键名不存在则报错
# print(dic.get('name3'))  #None
# print(dic.get('name3','不存在'))  #不存在
# print(dic.get('name2'))  #jishao
# len(dic)
# 添加元素  变量名[键名] = 数据  ,不存在则新增
# dic["age"] = 18
# print(dic)
# 修改元素   通过key找到则可修改
# dic["name"] = "tao"
# print(dic)
# 删除元素   del删除指定元素   |   clear清空整个字典  | pop
# dic = {'name':'wang','name2':'jishao'}
# del dic
# print(dic) #删除了整个字典，报错
# dic = {'name':'wang','name2':'jishao'}
# del dic['age'] #没有指定键名，报错
# dic = {'name': 'wang', 'name2': 'jishao'}
# dic.clear()
# print(dic)  #保留字典，情况字典所有东西
# dic = {'name': 'wang', 'name2': 'jishao'}
# dic.pop("age") #键不存在就会报错
# dic.popitem()  #默认删除最后一个键值对
# print(dic)
# keys():返回字典使用键名
# dic = {'name': 'wang', 'name2': 'jishao'}
# print(dic.keys())  #dict_keys(['name', 'name2'])
# for i in dic:  #for 只取键名
#     print(i)
# values():返回字典使用值
# dic = {'name': 'wang', 'name2': 'jishao'}
# print(dic.values())  #dict_values(['wang', 'jishao'])
# for i in dic.values():  #for 只取值
#     print(i)
# items() 返回字典所有的键值对
# dic = {'name': 'wang', 'name2': 'jishao'}
# print(dic.items())  #dict_items([('name', 'wang'), ('name2', 'jishao')])
# for i in dic.items():  #for ('name', 'wang')  ('name2', 'jishao')
#     print(i)
# 应用场景 ：描述一个事物对于的属性

# 23 集合  具有无序性
# 集合名 = {元素1,元素2,}
# s1 = {}  #空字典
# s1 = set()  #空集合
# 无序性
# s1 = {'a', 'b', 'c'}
# print(s1)  #运行结果不同  数字运行结果一样
# print(hash("a")) #hash表中位置发生改变
# print(hash(1))  #int,hash表中位置不变
# 无序性：不能修改集合中的值
# 唯一性:自动去重
# add() update() remove() pop() discard()

# 24 交集&和并集|  集合的唯一性


