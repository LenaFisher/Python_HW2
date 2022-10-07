# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# from string import digits

digit = float(input("введите вещественное число: "))
result = 0
if(digit < 1):
    digit = digit * 100
while digit > 0:
    temp = digit % 10
    digit = digit // 10
    result = result + temp
print(int(result))

