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


def calculate_sin():
    angle = float(angle_entry.get())
    terms = int(terms_entry.get())
    result = calculate_sin_taylor(angle, terms)
    result_label.config(text=f"sin({angle}) = {result}")


def calculate_cos():
    angle = float(angle_entry.get())
    terms = int(terms_entry.get())
    result = calculate_cos_taylor(angle, terms)
    result_label.config(text=f"cos({angle}) = {result}")


def calculate_asin_taylor(x, terms):
    """使用泰勒级数展开计算反正弦函数， 由彭万同学进行编写"""
    asinx = x
    numerator = x
    denominator = 1
    sign = 1
    # Loop to calculate arcsine using Taylor series
    for n in range(1, terms):
        numerator *= (x * x)
        denominator = (2 * n) * (2 * n + 1)
        sign *= -1
        asinx += (sign * numerator) / denominator
    return math.degrees(asinx)  # Convert the result to degrees



def calculate_atan_taylor(x, terms):
    """使用泰勒级数展开计算反正切函数， 由彭万同学进行编写"""
    atanx = x
    # Loop to calculate arctangent using Taylor series
    for n in range(1, terms):
        atanx += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return math.degrees(atanx)  # Convert the result to degrees


def calculate_asin():
    """执行反正弦函数计算， 由彭万同学进行编写"""
    return 0


def calculate_atan():
    """执行反正切函数计算， 由彭万同学进行编写"""
    return 0


"""三角函数计算窗口， 由王禹轩同学进行编写"""
# 创建主窗口
window = tk.Tk()
window.title("三角函数计算器")

# 角度输入
angle_label = tk.Label(window, text="角度：")
angle_label.grid(row=0, column=0, padx=10, pady=10)
angle_entry = tk.Entry(window)
angle_entry.grid(row=0, column=1, padx=10, pady=10)

# 项数输入
terms_label = tk.Label(window, text="项数：")
terms_label.grid(row=1, column=0, padx=10, pady=10)
terms_entry = tk.Entry(window)
terms_entry.grid(row=1, column=1, padx=10, pady=10)

# 计算按钮
sin_button = tk.Button(window, text="sin", command=calculate_sin)
sin_button.grid(row=2, column=0, padx=10, pady=10)
cos_button = tk.Button(window, text="cos", command=calculate_cos)
cos_button.grid(row=2, column=1, padx=10, pady=10)
asin_button = tk.Button(window, text="asin", command=calculate_asin)
asin_button.grid(row=2, column=2, padx=10, pady=10)
atan_button = tk.Button(window, text="atan", command=calculate_atan)
atan_button.grid(row=2, column=3, padx=10, pady=10)

# 结果显示
result_label = tk.Label(window, text="")
result_label.grid(row=3, column=0, columnspan=4, padx=10, pady=10)

# 运行主循环
window.mainloop()
