def safe_divide(numerator, denominator):
    try:
        # Try to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Try to perform the division
        result = num / denom
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
