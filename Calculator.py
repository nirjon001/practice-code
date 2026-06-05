def addition(a,b):
    result = a + b
    return result

def subtraction(a,b):
    result = a - b
    return result

def multiplication(a,b):
    result = a * b
    return result

def division(a,b):
    result = a / b
    return result


print("Enter 1st number:")
a = float(input().strip())

print("What do you want do ?\n"
      "1. Addition(+)\n"
      "2. Subtraction(-)\n"
      "3. Multiplication(X)\n"
      "4. Division(/)\n")


while True:
    choice = int(input().strip())
    if choice in [1, 2, 3, 4]:
        break
    print("Enter the number between 1-4")

print("Enter 2nd number:")
b = float(input().strip())

if choice == 1:
    result = addition(a, b)
    print(f"Addition: {result:.2f}")
elif choice == 2:
    result = subtraction(a, b)
    print(f"Subtraction: {result:.2f}")
elif choice == 3:
    result = multiplication(a, b)
    print(f"Multiplication: {result:.2f}")
elif choice == 4:
    result = division(a, b)
    print(f"Division: {result:.2f}")