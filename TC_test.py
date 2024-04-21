import math
from TrigCalculator import calculate_sin_taylor, calculate_cos_taylor, calculate_tan_taylor, calculate_cot_taylor


# 该函数用作对四种三角函数计算函数的功能进行测试，由 王财成同学 进行设计和验证
# 函数名：test_trig_calculator，  调用来自TrigCalculator.py 的三角函数计算函数
# calculate_sin_taylor, calculate_cos_taylor, calculate_tan_taylor, calculate_cot_taylor
def test_trig_calculator():
    # 测试正弦函数
    print("下面开始正弦函数测试：")
    print("--------------------------------------------------------")
    test_cases = [0, 30, 45, 60, 90, 180, 270, 360]
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
    test_cases = [0, 30, 45, 60, 90, 180, 270, 360]
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

    # 测试反正弦函数
    print("下面开始反正弦函数测试：")
    print("--------------------------------------------------------")
    test_cases = [-1,-0.75,-0.5, 0, 0.5,0.75, 1]
    terms = 10
    for value in test_cases:
        calculator_result = calculate_asin_taylor(value, terms)
        math_result = math.degrees(math.asin(value))
        print(f"Value: {value}")
        print(f"Calculator Result (Asin): {calculator_result}")
        print(f"Math Result (Asin): {math_result}")
        print(f"Error (Asin): {abs(calculator_result - math_result)}")
        print("")
    print("--------------------------------------------------------")

    # 测试反正切函数
    print("下面开始反正切函数测试：")
    print("-------------------------------------------------------")
    test_cases = [-1, -0.5, 0, 0.5, 1]
    terms = 10
    for value in test_cases:
        calculator_result = calculate_atan_taylor(value, terms)
        math_result = math.degrees(math.atan(value))
        print(f"Value: {value}")
        print(f"Calculator Result (Atan): {calculator_result}")
        print(f"Math Result (Atan): {math_result}")
        print(f"Error (Atan): {abs(calculator_result - math_result)}")
        print("")
    print("--------------------------------------------------------")

    return 0



# 执行测试
test_trig_calculator()
