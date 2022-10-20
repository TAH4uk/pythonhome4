# Задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def dividers(n):
   i = 2
   devider = []
   while i * i <= n:
       while n % i == 0:
           devider.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       devider.append(n)
   return devider

N = int(input("Введите число N: "))
div = dividers(N)

print(f"Простые множители числа {N} = {div}")