from sys import excepthook

try:
    num1 = int(input("Введите первое число:  "))
    num2 = int(input("Введите второе число:  "))
except ValueError:
    print("Вы ввели не число, введите число!")

message = '''
выберите операцию
+ : сложение        
- : вычитание 
* : умножение 
/ : деление
вы выбрали:
'''

operation = input(message)
if operation == '+':
    print('сложение')
    result = num1 + num2
elif operation == '-':
    print('вычитание')
    result = num1 - num2
elif operation == '*':
    print('умножение')
    result = num1 * num2
elif operation == '/':
    print('деление')
    try:
        result = num1 / num2
    except ZeroDivisionError:
        result = "Делить на 0 нельзя!"
else:
    result = "Неизвестная операция"
print("результат: ",result)