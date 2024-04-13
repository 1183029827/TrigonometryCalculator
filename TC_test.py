import math
from TrigCalculator import calculate_sin_taylor, calculate_cos_taylor, calculate_tan_taylor, calculate_cot_taylor


# 该函数用作对四种三角函数计算函数的功能进行测试，由 王财成同学 进行设计和验证
# 函数名：test_trig_calculator，  调用来自TrigCalculator.py 的三角函数计算函数
# calculate_sin_taylor, calculate_cos_taylor, calculate_tan_taylor, calculate_cot_taylor
def test_trig_calculator():
   # 测试正弦函数
    print("下面开始正弦函数测试：")
    print("--------------------------------------------------------")
    test_cases = [0, 30, 40, 45, 60, 90, 180,270,360]
    terms = 10
    for angle in test_cases:
        calculator_result = calculate_sin_taylor(angle, terms)
        math_result = math.sin(math.radians(angle))
        print(f"Angle: {angle}°")
        print(f"Calculator Result (Sin): {calculator_result}")
        print(f"Math Result (Sin): {math_result}")
        print(f"Error (Sin): {abs(calculator_result - math_result)}")
        print("")
    print("--------------------------------------------------------")

    # 测试余弦函数
    print("下面开始余弦函数测试：")
    print("--------------------------------------------------------")
    test_cases = [0, 30, 40, 45, 60, 90, 180,270,360]
    terms = 10
    for angle in test_cases:
        calculator_result = calculate_cos_taylor(angle, terms)
        math_result = math.cos(math.radians(angle))
        print(f"Angle: {angle}°")
        print(f"Calculator Result (Cos): {calculator_result}")
        print(f"Math Result (Cos): {math_result}")
        print(f"Error (Cos): {abs(calculator_result - math_result)}")
        print("")
    print("--------------------------------------------------------")

    # 测试正切函数
    print("下面开始正切函数测试：")
    print("--------------------------------------------------------")
  
    test_cases = [0, 30, 45, 60]
    terms = 10
    for angle in test_cases:
        if angle in [90, 270]:
            calculator_result = float('inf')  # 角度为90度或270度时，正切函数的结果为无穷大
            math_result = float('inf')
        else:
            calculator_result = calculate_tan_taylor(angle, terms)
            math_result = math.tan(math.radians(angle))
        print(f"Angle: {angle}°")
        print(f"Calculator Result (Tan): {calculator_result}")
        print(f"Math Result (Tan): {math_result}")
        print(f"Error (Tan): {abs(calculator_result - math_result)}")
        print("")
    print("--------------------------------------------------------")

    # 测试余切函数
    print("下面开始余切函数测试：")
    print("--------------------------------------------------------")
    for angle in test_cases:
        if angle in [0, 180, 360]:
            calculator_result = float('inf')  # 角度为0度、180度或360度时，余切函数的结果为无穷大
            math_result = float('inf')
        else:
            calculator_result = calculate_cot_taylor(angle, terms)
            math_result = 1 / math.tan(math.radians(angle))
     
        print(f"Angle: {angle}°")
        print(f"Calculator Result (Cot): {calculator_result}")
        print(f"Math Result (Cot): {math_result}")
        print(f"Error (Cot): {abs(calculator_result - math_result)}")
        print("")
    print("--------------------------------------------------------")

    return 0



# 执行测试
test_trig_calculator()
