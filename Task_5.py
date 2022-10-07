# Реализуйте алгоритм перемешивания списка. Без функции shuffle из модуля random.

from random import randint

arr = []
n=int(input("Введите длину массива: "))
for i in range(n):
    arr.append(i)
print(arr)

for i in range(n):
    index=randint(0,n-1)
    temp=arr[index]
    arr[index]=arr[i]
    arr[i]=temp
print(arr)