#  Проверить все ли объекты имеют одинаковое значение некоторой характеристики. Написать функцию same_by(chara,objects):

values=[]
values1=[0,2,3,4,6]

characteristic=(lambda x: x%2)

# Функция проверки на одинаковые возвращаемые характеристики объектов
def same_by(chara,objects):
    if not objects: print(True)
    else:
        for i in range(len(objects)):
            if chara(objects[0])!=chara(objects[i]): 
                print(False)
                break
            if i==len(objects)-1:
                print(True)

same_by(characteristic,values)
