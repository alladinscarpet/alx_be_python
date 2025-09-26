'''
Create a Python script named temp_conversion_tool.py.
This script will define functions to convert temperatures
between Celsius and Fahrenheit, demonstrating the use of 
global variables to store conversion factors that are accessible within functions.
'''

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


temp = int(input("Enter the temperature to convert: "))
degree = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if degree == 'c':
    print(f"{temp}°C is {convert_to_fahrenheit(temp)}°F")
elif degree == 'f':
    print(f"{temp}°F is {convert_to_celsius(temp)}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")