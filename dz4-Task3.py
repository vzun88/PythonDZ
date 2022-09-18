# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

numbers=list(map(int,input('Введите числа через пробел -> ').split()))
numbersUnique = []
[numbersUnique.append(i) for i in numbers if i not in numbersUnique]
print(numbers)
print(f'Список из неповторяющихся элементов:\n{numbersUnique}')
