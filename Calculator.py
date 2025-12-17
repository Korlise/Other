while True:
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        op = input("Операция (+, -, *, /): ")
        
        if op == '+': result = a + b
        elif op == '-': result = a - b
        elif op == '*': result = a * b
        elif op == '/': result = a / b if b != 0 else "Ошибка: деление на 0"
        else: result = "Неизвестная операция"
        
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: введите числа!")