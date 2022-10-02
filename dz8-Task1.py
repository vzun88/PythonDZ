# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

point=[3,5,2,3,2]

def pointMin(lis):
    maximus = max(lis)
    minimus= min(lis)
    lisPoint=list(map((lambda x: minimus if x==maximus else x), lis))
    print(' '.join(map(str,lisPoint)))

pointMin(point)
