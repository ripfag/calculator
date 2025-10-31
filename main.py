message = '''
выберите операцию
+ : сложение        
- : вычитание 
* : умножение 
/ : деление
вы выбрали:
'''

try:
    num1 = int(input("Введите первое число:  "))
    num2 = int(input("Введите второе число:  "))
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
        result = num1 / num2

except ValueError:
    result = "Вы ввели не число, введите число!"

except NameError:
    result = "Вы ввели не число, введите число!!"

except ZeroDivisionError:
    result = "Делить на 0 нельзя!"

else:
    result = "Неизвестная операция"
print("результат: ", result)
