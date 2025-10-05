"""
Implement a division calculator that robustly
handles errors like division by zero
and non-numeric inputs using command line arguments.
Create two Python scripts: robust_division_calculator.py,
which contains the division logic including error handling,
and main.py, which interfaces with the user through the command line.
"""


def safe_divide(numerator, denominator):
    try:
        # Convert both values to floats as sys.arg reads strings
        numerator = float(numerator)
        denominator = float(denominator)

        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        result = numerator / denominator
        return result

    except ZeroDivisionError:
        return "Cannot divide by zero."
    except ValueError :
        return f"Invalid input type: please enter numeric values only."


