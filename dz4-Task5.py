# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import re
import string
mnogochlen1=[]
mnogochlen2=[]
x='x'
y='y'
minus='-'
plus='+'

def f(lis,mnogochlen):
    odnochlen=()
    Flag=True

    for i in range(len(lis)):
        if Flag==True:
            if ((lis[i] == x) or (lis[i] == y)):
                # Выесняем есть ли цифры перед знаками
                if i==0: 
                    odnochlen+=(1,)
                else:
                    st=(''.join(lis[0:i]))
                    odnochlen+=(st,)

                # Выесняем количество неизвестных (1 или 2)
                if (i+1)<len(lis) and ((lis[i+1] == x) or (lis[i+1] == y)):
                    st=(''.join(lis[i:i+2]))
                    odnochlen+=(st,)
                    Flag=False
                    if i+2==len(lis): 
                        odnochlen+=(0,)
                else:
                    odnochlen+=(lis[i],)
                    if i+1==len(lis):
                        odnochlen+=(0,)
        # Выесняем есть ли степень
        if lis[i-1] == '^':
            odnochlen+=(lis[i],)

        # Проверка на простое число без неизвестных
        if x not in lis and y not in lis:
            odnochlen+=(0,lis)

    # Добавляем полученные кортежи одночленов в список многочлена
    mnogochlen.append(odnochlen)
    del odnochlen
    return mnogochlen

# Записываем многочлены в файл и сразу считываем их
def fileData(name):
    data=open(name,'w+')
    data.write(input('введите формулу многочлена (например 2x^2+xy+5) ->'))
    data.seek(0)
    form=data.read()
    data.close()
    return form

# Раскладываем извлечённый из файла многочлен на одночлены
def fMnogochlen(nameFile, mnogochlen):
    formul = re.split('[+-/*=]', fileData(nameFile))
    for i in range(len(formul)):
        f(formul[i],mnogochlen)

fMnogochlen('file1.txt',mnogochlen1)
fMnogochlen('file2.txt',mnogochlen2)

# Находим сумму чисел без неизвестных (x и y)
def sum(mnogochlen):
    count=0
    for i in range(len(mnogochlen)):
        if mnogochlen[i][0]==0:
            count+=int(mnogochlen[i][1])
    return count

sums=sum(mnogochlen1)+sum(mnogochlen2)






print(mnogochlen1)
print(mnogochlen2)
