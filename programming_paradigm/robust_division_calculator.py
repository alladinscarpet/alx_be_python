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
        # convert both values to floats as sys.arg reads strings
        numerator = float(numerator)
        denominator = float(denominator)

        # manually raise zero division error
        if denominator == 0:
            raise ZeroDivisionError

        result = numerator / denominator
        return f"The result of the division is: {result}"

    # handles error instead of letting program crash.
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    # handless inappropriate values passed to a function
    except ValueError :
        return f"Invalid input type: please enter numeric values only."


