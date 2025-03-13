#simple program to prompt user for 2 numbers and a mathematical sign to calculate the result
name = str(input("Enter your name: "))
print("Hello", name)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# prompt user for mathematical sign
sign = input("Enter a mathematical sign (+, -, *, /): ")

# perform the calculation based on the sign entered
if sign == "+":
    print(num1, "+", num2, "=", num1 + num2)
    result = num1 + num2
    print(f"{name}, the result is {result}")
elif sign == "-":
    print(num1, "-", num2, "=", num1 - num2)
    result = num1 - num2
    print(f"{name}, the result is {result}")
    # add code to handle division by zero
elif sign == "*":
    print(num1, "*", num2, "=", num1 * num2)
    result = num1 * num2
    print(f"{name}, the result is {result}")
    # add code to handle multiplication by zero
elif sign == "/":
    if num2 == 0:
        print("Cannot divide by zero")
        exit()