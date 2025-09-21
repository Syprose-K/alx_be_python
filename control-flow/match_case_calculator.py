#match_case_calculator.py
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = int(num1 + num2)
        print("The result is: " + str(result))
    case "-":
        result = int(num1 - num2)
        print("The result is: " + str(result))
    case "*":
        result = int(num1 * num2)
        print("The result is: " + str(result))
    case "/":
        if num2 != 0:
            result = int(num1 / num2)
            print("The result is: " + str(result))
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please choose one of +, -, *, /.")
