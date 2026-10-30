# 1 Program to find the largest among 3 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third  number: "))

print(max(num1, num2, num3))


# 2. Simple calculator

num1 = float(input("Enter the first number: "))
operator = input("Enter an Operator(+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    if num2 != 0 :
        print("result:", num1 / num2)
    else:
         print("error")

else:
    print("Invalid operator!")






