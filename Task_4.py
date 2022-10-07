# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. 


from random import randint
pos_1 = int(input("введите позицию 1: "))-1
pos_2 = int(input("введите позицию 2: "))-1
arr = []
n=int(input("Введите число: "))
for i in range(n):
    arr.append(randint(-n,n))
print(arr)
print(arr[pos_1]*arr[pos_2])