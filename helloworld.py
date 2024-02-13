# Filename: factorial_calculator.py

def calculate_factorial(n):
    """Calculate the factorial of a given number."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage:
if __name__ == "__main__":
    number = int(input("Enter a number to calculate its factorial: "))
    result = calculate_factorial(number)
    print(f"The factorial of {number} is: {result}")
