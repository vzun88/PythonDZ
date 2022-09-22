# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Создаём файл и записываем в него текст
def r(fl):
    with open(fl,'a') as db:
        db.writelines(input('Введите что нибудь ->'))

# Открывает и считывает файл
def readBase(file):
    with open(file, 'r', encoding='utf-8') as db:
        db=db.read()
    return db
# Метод принимает имя файла для записи ахива и сам архив
def writReadArhive(file,listBase):
    with open(file, 'w+', encoding='utf-8') as data:
        data.writelines(''.join(map(str, listBase)))
        data.seek(0)
        return data.read()

# Метод сжатия файла. Принимает файл с исхоным текстом и файл для храниения архива
def zipArhive(file='base.txt',fileArhive='baseArhive.txt'):
    count1=0
    count2=0
    zip=[]
    with open(file, 'r', encoding='utf-8') as db:
        db=db.read()
    for i in range(1,len(db)+1):
        if db[-i]!=db[-i-1]:
            if count2:
                zip.insert(0,count2)
                count2=0
                continue
            zip.insert(0,db[-i])
            count1+=1
            if i == len(db)-1:
                zip.insert(0,-count1)
                break
        else:
            if db[-i]==db[-i-1]:
                if count1:
                    zip.insert(0,-(count1))
                    count1=0
                if not count2: 
                    zip.insert(0,db[-i])
                    count2+=1
                if count2: count2+=1
                if i == len(db)-1:
                    zip.insert(0,count2)
                    zip=''.join(map(str, zip))
                    break
    return writReadArhive(fileArhive, zip)

# Вывоим на экран % сжатия. Если <0 то эффект от сжатия отрицательный
def effekt (readBase, arhive):
    compression=len(readBase)/len(arhive)
    print(f'Эфaективность сжатия -> {compression}')


# Сборка
fName='base.txt'
r(fName):
rbd=readBase(fName)
arh=zipArhive(fName)
print(rbd)
print(arh)

effekt(rbd,arh)
