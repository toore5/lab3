# -*- coding: cp1251 -*-
sentence = input("Введіть речення: ")
words = sentence.split()
shortest_word = min(words, key=len)
print(f"Найкоротше слово: '{shortest_word}', його довжина: {len(shortest_word)}")