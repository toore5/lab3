# -*- coding: cp1251 -*-
n = int(input("������ ������������ ����� n: "))
while n > 9999 or n < 1000:
    n = int(input("����� ������� ���� �������������. ������ ���� �����: "))
max_digit = max(str(n))
print("�������� ����� � ����:", max_digit)