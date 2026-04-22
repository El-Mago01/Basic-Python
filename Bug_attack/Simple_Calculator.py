def simple_calculator(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        #print(operation, num2, num1)
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero!")
            return
    else:
        print("Invalid operation!")
        return

    print(f"Result: {result}")


simple_calculator(15, 3, '/') # should be 5.0