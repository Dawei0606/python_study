#! /usr/bin/python
# -*- coding:utf-8 -*-

import re  # 引用正则模块

def tidy(result):  # 建一个函数，用于整理算式中重复的加减号
    if '+-' in result:
        result = result.replace("+-", '-')
    if "--" in result:
        result = result.replace('--', '+')
    return result

def jiajian_jisuan(result):  # 计算加减法
    result = re.findall('\-?\d+\.?\d*', result)
    count = 0
    for i in result:
        count += float(i)
    count = str(count)
    return count

def chengchu_jisuan(result):  # 计算最小的括号里的表达式的乘除法
    if '*' in result:
        result = result.split('*')
        result = str(float(result[0]) * float(result[1]))
    elif '/' in result:
        result = result.split('/')
        result = str(float(result[0]) / float(result[1]))
    return result

def xiaokuohao_jisuan(formula):  # 计算最里层带括号的表达式
    res = formula.strip('()')  # 去除小括号 -40/5-8+9
    while True:
        new_result = re.search('\d+\.?\d*[*/]-?\d\.?\d*', res)  # 优先提取出乘除法来计算
        if new_result:
            condition_res = new_result.group()
            result = chengchu_jisuan(condition_res)   # 乘除法计算的结果
            res = res.replace(condition_res, result)  # 把结果替换回原来的表达式
            res = tidy(res)   # 整理计算之后的表达式
        else:
            ret = jiajian_jisuan(res)
            return ret
def condition_str(s):
    s = s.replace(' ', '')  # 拿到字符串首先去除字符串中的空格
    while True:
        result = re.search('\([^()]+\)', s)  # 用re 找到最里层的括号的表达式
        if result:  # 把最里层括号表达式计算出来
            res = result.group()   # 把找到的对象用.group方法转换成字符串
            ret = xiaokuohao_jisuan(res)
            s = s.replace(res, ret)
            s = tidy(s)
        else:
            result = xiaokuohao_jisuan(s)
            return result

s = '111 - 3 * (8/2-(6+3)+3-2*(9+11))'
print(condition_str(s))
