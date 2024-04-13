import tkinter as tk
import math


def calculate_factorial(n):
        """计算阶乘"""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)




def calculate_sin_taylor(x, terms):
      """使用泰勒级数展开计算正弦函数"""
    x = math.radians(x)  # 将角度转换为弧度
    sinx = 0
    for n in range(terms):
        numerator = (-1) ** n
        denominator = calculate_factorial(2 * n + 1)
        sinx += (numerator * x ** (2 * n + 1)) / denominator
    return sinx
  


def calculate_cos_taylor(x, terms):
        """使用泰勒级数展开计算余弦函数"""
    x = math.radians(x)  # 将角度转换为弧度
    cosx = 0
    for n in range(terms):
        numerator = (-1) ** n
        denominator = calculate_factorial(2 * n)
        cosx += (numerator * x ** (2 * n)) / denominator
    return cosx


def calculate_arcsin_taylor(x, terms):
    """使用泰勒级数展开计算反正弦函数"""
    arcsinx = 0
    for n in range(terms):
        coefficient = ((-1) ** n) * factorial(2 * n) // ((4 ** n) * (factorial(n) ** 2) * (2 * n + 1))
        term = coefficient * (x ** (2 * n + 1))
        arcsinx += term
    return arcsinx


def calculate_arctan_taylor(x, terms):
    """使用泰勒级数展开计算反正切函数"""
    arctanx = 0
    for n in range(terms):
        coefficient = (-1) ** n / (2 * n + 1)
        term = coefficient * (x ** (2 * n + 1))
        arctanx += term
    return arctanx


def calculate_tan_taylor(x, terms):
    """使用泰勒级数展开计算正切函数， 由彭万同学进行编写"""
    return 0


def calculate_cot_taylor(x, terms):
    """使用泰勒级数展开计算余切函数， 由彭万同学进行编写"""
    return 0


def calculate_tan():
    """执行正切函数计算， 由彭万同学进行编写"""
    return 0


def calculate_cot():
    """执行余切函数计算， 由彭万同学进行编写"""
    return 0


"""三角函数计算窗口， 由王禹轩同学进行编写"""
