class NegativeNumberException(Exception):
    pass


def input_number():
    """User input number"""
    number = int(input("Enter a number: "))
    try:
        if number < 0:
            raise NegativeNumberException
        return number
    except NegativeNumberException:
        return "NegativeNumberException, number must not be negative"


if __name__ == "__main__":
    print(input_number())
