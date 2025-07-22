import pyfiglet
import ascii_magic

ascii_banner = pyfiglet.figlet_format("CALCULATOR")
print(ascii_banner)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Operator dictionary
operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

should_accumulate = True
num1 = float(input("What's your 1st Number: "))

while should_accumulate:
    # Show available operators
    for symbol in operator:
        print(symbol)

    # Get operator and second number
    operator_symbol = input("Pick Operator: ")
    num2 = float(input("What's your 2nd Number: "))

    # Perform operation
    calculation_function = operator[operator_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operator_symbol} {num2} = {answer}")

    # Ask user to continue or not
    choice = input(f"Type 'Y' to continue calculation with {answer}, or 'N' to exit: ").lower()
    if choice == "y":
        num1 = answer
    else:
        should_accumulate = False
