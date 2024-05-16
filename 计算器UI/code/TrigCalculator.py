#import tkinter as tk
#from tkinter import messagebox
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

def calculate_sin():
    try:
        angle = float(angle_entry.get())   
        terms = int(terms_entry.get())  
        result = calculate_sin_taylor(angle, terms) 
        result_label.config(text=f"sin({angle}) = {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for angle and terms.")

def calculate_cos():
    try:
        angle = float(angle_entry.get())  
        terms = int(terms_entry.get())  
        result = calculate_cos_taylor(angle, terms)  
        result_label.config(text=f"cos({angle}) = {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for angle and terms.")

def calculate_asin_taylor(x, terms):
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

def calculate_asin():
    try:
        angle = float(angle_entry.get())
        terms = int(terms_entry.get())
        result = calculate_asin_taylor(angle, terms)
        result_label.config(text=f"asin({angle}) = {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for angle and terms.")

def calculate_atan():
    try:
        angle = float(angle_entry.get())
        terms = int(terms_entry.get())
        result = calculate_atan_taylor(angle, terms)
        result_label.config(text=f"atan({angle}) = {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for angle and terms.")

 
# 创建主窗口
# window = tk.Tk()
# window.title("三角函数计算器")

# 角度输入
# angle_label = tk.Label(window, text="角度：")
# angle_label.grid(row=0, column=0, padx=10, pady=10)
# angle_entry = tk.Entry(window)
# angle_entry.grid(row=0, column=1, padx=10, pady=10)

# 项数输入
# terms_label = tk.Label(window, text="项数：")
# terms_label.grid(row=1, column=0, padx=10, pady=10)
# terms_entry = tk.Entry(window)
# terms_entry.grid(row=1, column=1, padx=10, pady=10)

# 计算按钮
# sin_button = tk.Button(window, text="sin", command=calculate_sin)
# sin_button.grid(row=2, column=0, padx=10, pady=10)
# cos_button = tk.Button(window, text="cos", command=calculate_cos)
# cos_button.grid(row=2, column=1, padx=10, pady=10)
# asin_button = tk.Button(window, text="asin", command=calculate_asin)
# asin_button.grid(row=2, column=2, padx=10, pady=10)
# atan_button = tk.Button(window, text="atan", command=calculate_atan)
# atan_button.grid(row=2, column=3, padx=10, pady=10)

# 结果显示
# result_label = tk.Label(window, text="")
# result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# 运行主循环
# window.mainloop()
