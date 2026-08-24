# Scientific Calculator
import math

result = None

def add(a, b):  # Addition
    return a + b

def subtract(a, b):  # Subtraction
    return a - b

def multiply(a, b):  # Multiplication
    return a * b

def divide(a, b):  # Division
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def get_number(prompt):
    value = input(prompt).strip().lower()
    if value == "pi":
        return math.pi
    elif value == "e":
        return math.e
    else:
        return float(value)

while True:
    result = None

    print("\nWelcome to the Calculator!")
    print("Choose an operation:\n")

    left = [
        "1. Addition (+)",
        "2. Subtraction (-)",
        "3. Multiplication (*)",
        "4. Division (/)",
        "5. Factorial (!)",
        "6. Exponents (a^b)",
        "7. Squares (a^2)",
        "8. Cubes (a^3)",
        "9. Square root (√)"
    ]

    right = [
        "10. Trigonometry [sin(x), cos(x), tan(x)]",
        "11. Inverse Trigonometry [asin(x), acos(x), atan(x)]",
        "12. Common Logarithms (log base 10)",
        "13. Natural Logarithms (log base e)",
        "14. Absolute value (|a|)"
    ]

    for i in range(len(left)):
        if i < len(right):
            print(f"{left[i]:<40}{right[i]}")
        else:
            print(left[i])

    print("\n#----Additional Constants----#")
    print("1. Pi (π)")
    print("2. Euler's number (e)")

    choice = input("\nEnter the number of your choice (1-14): ")

    # ---------- TWO NUMBER OPERATIONS ----------
    if choice in ["1", "2", "3", "4", "6"]:
        num1 = get_number("Enter the first number (or type pi or e): ")
        num2 = get_number("Enter the second number (or type pi or e): ")

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "6":
            result = num1 ** num2

    # ---------- ONE NUMBER OPERATIONS ----------
    elif choice in ["5", "7", "8", "9", "10", "11", "14"]:
        num1 = float(input("Enter a number: "))

        if choice == "5":
            n = int(num1)
            if n < 0:
                result = "Error: Factorials are not defined for negative numbers"
            else:
                result = math.factorial(n)

        elif choice == "7":
            result = num1 ** 2

        elif choice == "8":
            result = num1 ** 3

        elif choice == "9":
            if num1 < 0:
                result = "Error: You can't square root negative numbers"
            else:
                result = math.sqrt(num1)

        elif choice == "10":
            angle = float(input("Enter an angle in degrees: "))
            radians = math.radians(angle)

            result = (
                "sin(" + str(angle) + ") = " + str(math.sin(radians)) + "\n" +
                "cos(" + str(angle) + ") = " + str(math.cos(radians)) + "\n" +
                "tan(" + str(angle) + ") = " + str(math.tan(radians))
            )

        elif choice == "11":
            value = float(input("Enter a value between -1 and 1 for asin/acos, or any real number for atan: "))

            results = ""

            if -1 <= value <= 1:
                results += "arcsin(" + str(value) + ") = " + str(math.degrees(math.asin(value))) + " degrees\n"
                results += "arccos(" + str(value) + ") = " + str(math.degrees(math.acos(value))) + " degrees\n"
            else:
                results += "arcsin/arccos undefined for this input\n"

            results += "arctan(" + str(value) + ") = " + str(math.degrees(math.atan(value))) + " degrees"
            result = results

        elif choice == "14":
            result = abs(num1)

    elif choice == "12":
        num1 = get_number("Enter a number (or type pi or e): ")
        if num1 <= 0:
            result = "Error: log undefined for zero or negative numbers"
        else:
            result = math.log10(num1)

    elif choice == "13":
        num1 = get_number("Enter a number (or type pi or e): ")
        if num1 <= 0:
            result = "Error: Natural Logarithms undefined for zero or negative numbers"
        else:
            result = math.log(num1)

    else:
        result = "Invalid choice!"

    if result is not None:
        print("\nResult:", result)
    else:
        print("\nError: No result found")

    again = input("\nDo another calculation? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye!")
        break




