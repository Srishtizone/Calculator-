num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
 
if op == "+":
    print("Answer =", num1 + num2)
elif op == "-":
    print("Answer =", num1 - num2)
elif op == "*":
    print("Answer =", num1 * num2)
elif op == "/":
    print("Answer =", num1 / num2)
else:
    print("Wrong operator!")
