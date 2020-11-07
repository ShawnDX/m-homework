#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
# FileName :   1022-2.py
# Date     :   2020/10/22 21:56:03
# Author   :   Xu Du
# Version  :   1.0
# E-mail   :   duxu.cup@outlook.com
# Desc     :   None
"""

# here put the import lib

# 这种方法在数很大的时候很占用内存，具体原因你可以思考
def even_sum(m):
    fi=[1, 1]
    i = 0
    sum = 0

    # 定义循环，只要fibo数列的值不大于m，就继续循环
    while fi[i] <= m:
        
        # 如果为偶数，则求和 
        if fi[i] % 2 == 0:
            sum +=fi[i]
        
        # 往后移动一位
        i += 1

        # 同时生成下一个斐波那契数列的值
        fi.append(fi[i] + fi[i -1])
    return sum

print(even_sum(4000000))