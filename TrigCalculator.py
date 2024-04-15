import tkinter as tk
import math


def calculate_factorial(n):
    """计算阶乘"""
    if n == 0:  # 如果 n 为 0，阶乘为 1
        return 1
    else:  # 否则，递归计算 n 的阶乘
        return n * calculate_factorial(n - 1)




def calculate_sin_taylor(x, terms):
    """使用泰勒级数展开计算正弦函数"""
    x = math.radians(x)  # 将角度转换为弧度
    sinx = 0
    for n in range(terms):
        numerator = (-1) ** n  # 计算每项的分子
        denominator = calculate_factorial(2 * n + 1)  # 计算每项的分母
        sinx += (numerator * x ** (2 * n + 1)) / denominator  # 计算并累加每一项
    return sinx
  


def calculate_cos_taylor(x, terms):
    """使用泰勒级数展开计算余弦函数"""
    x = math.radians(x)  # 将角度转换为弧度
    cosx = 0
    for n in range(terms):
        numerator = (-1) ** n  # 计算每项的分子
        denominator = calculate_factorial(2 * n)  # 计算每项的分母
        cosx += (numerator * x ** (2 * n)) / denominator  # 计算并累加每一项
    return cosx


def def calculate_asin_taylor(x, terms):  
        """使用泰勒级数展开计算反正弦函数"""    
        asinx = x    
        numerator = x    
        denominator = 1    
        sign = 1    
for n in range(1, terms):       
        numerator *= (x * x)       
        denominator = (2 * n) * (2 * n + 1)       
        sign *= -1       
        asinx += (sign * numerator) / denominator 
 return math.degrees(asinx)

def calculate_atan_taylor(x, terms):    
"""使用泰勒级数展开计算反正切函数"""   
        atanx = x   
for n in range(1, terms):     
        atanx += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)   
return math.degrees(atanx)


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
