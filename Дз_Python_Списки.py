# Модуль 4. Строки. Списки. Часть 2
# Задание 1
print("Задание 1 ")
example_user = input("Введите пример: ")
if "+" in example_user:
    example = example_user.split("+")
    num1 = int(example[0])
    num2 = int(example[1])
    result = num1 + num2
elif "-" in example_user:
    example = example_user.split("-")
    num1 = int(example[0])
    num2 = int(example[1])
    result = num1 - num2
elif "/" in example_user:
    example = example_user.split("/")
    num1 = int(example[0])
    num2 = int(example[1])
    result = num1 / num2
elif "*" in example_user:
    example = example_user.split("*")
    num1 = int(example[0])
    num2 = int(example[1])
    result = num1 * num2
print(f"Результат: {result}")

# Задание 2
import random
num_elements = random.randint(5, 20) # Случайное количество элементов для списка
list1 = [random.randint(-100, 100) for i in range(num_elements)]
minimum = min(list1)
maximum = max(list1)
negative = 0
positive = 0
zero = 0
for i in list1:
    if i < 0:
        negative += 1
    elif i >= 0:
        positive += 1
    elif i == 0:
        zero += 1
print(f"Максимальное число: {maximum}")
print(f"Минимальное число: {minimum}")
print(f"Количество отрицательных чисел: {negative}")
print(f"Количество положительных чисел: {positive}")
print(f"Количество нулей: {zero}")

