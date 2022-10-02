# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода). Через рекурсию необходимо делать
# Input: 2 -> 3 4
# Output: 4 3

# Считаем (по пробелам) количество введённых чисел
def f(strN,a=0,count=0):
    if strN.find(' ',a,len(strN))!=-1:
        a=strN.find(' ',a,len(strN))
        return f(strN,a+1,count+1)
    else:
        return count+1

# Возвращаем числа в обратном порядке через рекурсию
def fReverse(strN,x=-1):
    if x==-len(strN)-1:
        return
    else:
        print(strN[x],end='')
        return fReverse(strN,x-1)

# Проверка на соответствие количества введенных чисел числу n (через рекурсию)
def valid(num):
    strN=input(f'Введите числа в количестве {num} через 1 пробел -> ')
    k=f(strN)
    if k==num: return strN
    else:
        return valid(num)

# Сборка
n=int(input('Введите количество элементов в последовательности -> '))

strNum=valid(n)
fReverse(strNum)
