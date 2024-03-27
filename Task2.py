def additional(num1, num2):
    """Adds two numbers"""
    return num1 + num2


def subtract(num1, num2):
    """Subtracts two numbers"""
    return num1 - num2


def multiply(num1, num2):
    """Multiplies two numbers"""
    return num1 * num2


def divide(num1, num2):
    """Divides two numbers"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Division by zero error"


def power(num1, num2):
    """Powers two numbers"""
    try:
        return num1 ** num2
    except ZeroDivisionError:
        return "You can't raise zero to a negative power"


def menu():
    """Menu options"""
    while True:
        try:
            number1 = int(input("Enter first number: "))
            number2 = int(input("Enter second number: "))
        except ValueError:
            print("Input must be an integer")
            break

        print("1. additional\n2. subtraction\n3. multiplication\n4. division\n5. power\n6. exit")
        choice = input("Select the operation: ").strip()

        match choice:
            case "1":
                print(additional(number1, number2))
            case "2":
                print(subtract(number1, number2))
            case "3":
                print(multiply(number1, number2))
            case "4":
                print(divide(number1, number2))
            case "5":
                print(power(number1, number2))
            case "6":
                break
            case _:
                print("Incorrect input, please try again!")


if __name__ == '__main__':
    menu()
