# -*- coding: cp1251 -*-
sentence = input("������ �������: ")
words = sentence.split()
shortest_word = min(words, key=len)
print(f"���������� �����: '{shortest_word}', ���� �������: {len(shortest_word)}")