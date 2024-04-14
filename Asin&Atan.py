def calculate_asin():
    angle = float(angle_entry.get())  # Get the angle from the entry widget and convert it to a float
    terms = int(terms_entry.get())    # Get the number of terms from the entry widget and convert it to an integer
    result = calculate_asin_taylor(angle, terms)  # Calculate arcsine using Taylor series
    result_label.config(text=f"asin({angle}) = {result}")  # Update the result label with the calculated arcsine


def calculate_atan():
    angle = float(angle_entry.get())  # Get the angle from the entry widget and convert it to a float
    terms = int(terms_entry.get())    # Get the number of terms from the entry widget and convert it to an integer
    result = calculate_atan_taylor(angle, terms)  # Calculate arctangent using Taylor series
    result_label.config(text=f"atan({angle}) = {result}")  # Update the result label with the calculated arctangent


#Calculate the factorial
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)  # Recursive function to calculate factorial


#Arcsine functions are calculated using Taylor series expansions
def calculate_asin_taylor(x, terms):
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


#Arctangent functions are computed using Taylor series expansions
def calculate_atan_taylor(x, terms):
    atanx = x
    
    # Loop to calculate arctangent using Taylor series
    for n in range(1, terms):
        atanx += ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
    return math.degrees(atanx)  # Convert the result to degrees
