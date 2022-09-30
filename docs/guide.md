FastPro/
|-- scripts/
|   |— run.sh
|-- logs/
|   |-- 2022-3-10.log
|-- src/
|   |-- tests/
|   |   |-- __init__.py
|   |   |-- test_main.py|   |-- main.py
|   |-— config.py
|-- docs/
|   |-- data_api.md
|   |-- syscfg.yaml
|-- setup.py
|-- requirements.txt
|—- README.md
scripts: 也可以命名为bin，存放一些可执行文件，如脚本，我一般用来存放项目的启停管理脚本。

logs: 存放日志文件。

src: 存放python源码，入口文件最好命名为main.py。网上也有建议不要直接命名为src的，因为我是使用vscode作为编辑器，一些补全和高亮代码等插件在寻找路径的时候会默认将src添加到路径中，如果用其他名字的话需要修改配置。

src/tests：存放单元测试脚本。

docs: 存放文档和配置文件。

setup.py: 项目安装脚本。

requirements.txt: 项目依赖。

README.md: 项目说明文件。
一、在实际的工程项目中，Python由哪些文件模块组成呢？

首先，是顶层的包（类似文件夹）

其次，是各个模块（Python file）

然后，是类（class 定义类；面向对象【工程中必用，初学者可不用】）

最后，是变量和方法（函数）。其中，方法中也可以定义变量（方法中的变量）。



二、命名规范：

包：使用小写字母命名。多个单词之间用下划线分隔。

模块：使用小写字母命名。多个单词之间用下划线分隔。

类（驼峰命名法）：使用小写字母命名但是首字母大写。多个单词不需下划线，单词首字母大写。Python中一个模块可以包含多个类。私有类名称需要以下划线开头。e.g. HelloWorld 或 _HelloWorld

函数：使用小写字母命名。多个单词之间用下划线分隔。私有函数名称需要以下划线开头。

变量：使用小写字母命名。多个单词之间用下划线分隔。私有变量名称需要以下划线开头。

常量：使用大写字母命名。多个单词之间用下划线分隔。私有常量名称需要以下划线开头。



三、Python中的特殊模块_init_.py

1、 包含此模块的文件夹才能成为包。（需要确保包的命名符合规范，才能被导入）

2、 _init_.py当包被导入的时候会自动运行。



四、导包路径

分为绝对导入和相对导入

绝对导入（from只能从根目录导入）：

from my_first_package import *

from my_first_package import my_first_test

import my_first_package.my_first_test as p
p.func
相对导入（“.”代表当前目录，“..”代表上一层目录）：

from .my_second_package import my_second_test