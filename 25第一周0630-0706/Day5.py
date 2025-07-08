# 1.模块
# 含义：一个py文件就是一个模块，即导入一个模块本质上是执行一个文件
from Lib.importlib.resources import Package

# 1.1 分类

# 1.1.1内置模块
# 如:random time logging 直接导入使用
# 1.1.2 第三方模块
# 下载命令:cmd窗口输入 pip install 模块名
# 1.1.3自定义模块
# 即自己在项目中定义的模块
# 注意：命名要遵循标识符规定以及变量命名规范，且不要与内置模块冲突

# 1.2导入模块
# 1.2.1 方法一  import 模块名
# 语法:
# 导入模块
# import 模块名1
# import 模块名2
# 调用功能
# 模块名.功能名

# import pytest
# print(pytest.name)
# print(pytest.funa())

# 1.2.2 方法二  from...import....
# 语法
# 从模块中导入指定功能
# from 模块名 import 功能1,功能2...
# 调用功能
# 直接输入功能即可，不需要添加模块名
# from pytest import funa,name
# funa()
# print(name)
# funb()  #报错没有导入

# 1.2.3 方法三  from...import *
# 语法
# from 模块名 import * #导入模块的所有功能
# from pytest import *
# funa()
# print(name)
# funb()
#不建议过多使用*,重名函数同名函数会被覆盖

# 1.3 使用as 给模块取别名
# 模块名 as 别名
# 功能名 as 别名
# 导入多个功能使用,隔开

# 1.4 内置全局变量  __name__
# 语法
# if __name__ == '__main__':
# 作用
# 用来控制py文件在不同的应用场景执行不同的逻辑
# 1.4.1 __name__
# 1.文件在当前程序执行即自己执行自己: __name__ == __main__
# 2.文件被当作模块被其他文件导入: __name__ == 模块名

# import pytest
# print(pytest.name)



# 2.包
# 含义:项目结构中的文件夹/目录
# 与普通文件的区别,包含有__init__.py文件夹
# 作用:将有联系的模块放在同一个文件夹下，有效避免模块名称冲突，让结构清晰
# 新建包 : 右键项目名-> new -> Python Package

# import 导入包时，先执行__init__.py文件的代码(代码长度有上限，很小）
# 导包
# 方式一
# import pack_01

# 方式二
from pack_01 import register  #这是__init__.py文件，你别把我写胖了哦     这是register模块


# 2.1 __all__
# 本质是一个列表，列表里面的元素代表要导入的模块
# 作用：在__init__.py控制要引入的东西，减少代码
# from pack_01 import *
# register.reg()
# login.log()

# 2.2 包本质是一个模块，包可以包含包