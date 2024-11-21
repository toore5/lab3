# -*- coding: cp1251 -*-
n = int(input("Введіть чотиризначне число n: "))
while n > 9999 or n < 1000:
    n = int(input("Число повинно бути чотиризначним. Введіть інше число: "))
max_digit = max(str(n))
print("Найбільша цифра в числі:", max_digit)