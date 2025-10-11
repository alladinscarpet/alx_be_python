"""
In this script, define a class Calculator
that includes both a class method and a static method to perform calculations.
This task aims to illustrate when and how to use
@classmethod and @staticmethod decorators,
highlighting their differences and practical applications.
"""

class Calculator:
    calculation_type = "Arithmetic Operations"  # Class specific

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b