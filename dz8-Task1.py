# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

point=[3,5,2,3,1]

def pointMin(list):
    for i in range(len(list)):
        if list[i]>3: list[i]=1
    s=' '.join(str(i) for i in list)
    print(s)

pointMin(point)
