# 1 Сделать таблицу сложения и таблицу возведения в степень


def print_operation_table(operation, num_rows=9, num_columns=9):
    #Вывод первой строки от 1 до num_columns
    print(*(i for i in range(1,num_columns+1)), sep='\t')

    for j in range(2,num_rows+1):
        for k in range(1,num_columns+1):
            if k!=1:
                calculon=operation(j,k)
                print(calculon,end= '\t')
            else: print(j,end= '\t')
        print()

print_operation_table(lambda x, y: x+y)
