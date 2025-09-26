def perform_operation(num1: float, num2: float, operation: str)-> float:
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    else:
        if num2 == 0:
            return "Cannot divide by zero."
        else:
            return num1 / num2