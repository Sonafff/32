a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
operation = input("Enter the operation (+, -, *, /, %, **, //): ")

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    result = a / b
elif operation == '%':
    result = a % b
elif operation == '**':
    result = a ** b
elif operation == '//':
    result = a // b
else:
    print("Invalid operation entered!")
    exit()

print(f'Result of {a} {operation} {b} = {result}')

if operation == '+':
    result = result + c
elif operation == '-':
    result = result - c
elif operation == '*':
    result = result * c
elif operation == '/':
    result = result / c
elif operation == '%':
    result = result % c
elif operation == '**':
    result = result ** c
elif operation == '//':
    result = result // c

print(f'Result of {a} {operation} {b} {operation} {c} = {result}')
