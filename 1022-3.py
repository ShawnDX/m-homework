#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
# FileName :   1022-3.py
# Date     :   2020/10/22 22:11:05
# Author   :   Xu Du
# Version  :   1.0
# E-mail   :   duxu.cup@outlook.com
# Desc     :   None
"""

# here put the import lib

# 这种方法在数很大的时候依然可以保持较小的内存占用，具体原因你可以思考
def even_sum(m):
    fi_f = 1
    fi_r = 1
    sum = 0
    
    # 定义循环，只要fibo数列的值不大于m，就继续循环
    while fi_r <= m:
        
        # 如果为偶数，则求和 
        if fi_r % 2 == 0:
            sum +=fi_r

        # 同时生成下一个斐波那契数列的值
        temp = fi_f
        fi_f = fi_r
        fi_r = fi_f + temp

    return sum

print(even_sum(4000000))