#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/30 03:29
# @Author  : toby
# @File    : 2.文档字符串.py
# @Software: PyCharm
# @Desc:
# print(dict.update.__doc__)  # 查看字典update函数的文档


# 单行文档字符串写法
def one_line_docstrings():
    """这是单行文档字符的写法主要用于无输入输出函数或方法描述"""
    pass


# 比较全的文档字符串写法
def full_docstrings(param: str) -> str:
    """函数名称 函数作用描述和解析
    这边可以添加一些更加详细的描述

    Note: 使用注意写这边

    Args:
        param: 这边对参数进行描述比如类型，作用
        ...

    Return:
        返回值类型和作用描述

    Raise:
        错误类型: 出现错误的原因
    """
    pass


print(full_docstrings.__doc__)
