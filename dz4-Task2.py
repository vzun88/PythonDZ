# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# Заполняем список простыми множителями числа
def numberList(n,listX):
    for i in range(2,n+1):
        if i==n: 
            listX.append(i)
            break
        if not n%i: 
            listX.append(i) 
            numberList(n//i,listX) 
            break

# Выводим список множителей
def printList(n):
    listNatur=[]
    numberList(n,listNatur)
    print(f'Состав простых множителей числа : \n{listNatur}')


numNatur=int(input('Введите натуральное число -> '))

printList(numNatur)
