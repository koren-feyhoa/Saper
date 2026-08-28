import random

def generate_numbers(matrix:list[list[int]],count_1:int):
    x=len(matrix[0])
    y=len(matrix)
    for i in range(count_1):
        matrix[random.randint(0,y-1)][random.randint(0,x-1)]='*'
    return matrix


def create_matrix(x:int,y:int):
    matrix=[['0']*x for i in range(y)]
    return matrix

def count_num(matrix:list[list[int]]):
    x = len(matrix[0])
    y = len(matrix)
    for i in range(y):
        for j in range(x):
            if matrix[i][j]!='*':
                matrix[i][j]=str(chek_num(matrix,i,j))
    return matrix

def chek_is_bomb_or_not(matrix:list[list[int]],k:int,m:int):
    if matrix[k][m] == '*':
        return 1
    else:
        return 0

def chek_up_left(matrix:list[list[int]], i:int, j:int):
    count=0
    for k in range(i, i + 2):  # левый верхний угол
        for m in range(j, j + 2):
            count+=chek_is_bomb_or_not(matrix,k,m)
    return count

def check_up_right(matrix:list[list[int]],i:int,j:int):
    count=0
    for k in range(i, i + 2):
        for m in range(j - 1, j + 1):
            count+=chek_is_bomb_or_not(matrix,k,m)
    return count

def check_down_left(matrix:list[list[int]],i:int,j:int):
    count=0
    for k in range(i - 1, i + 1):
        for m in range(j, j + 2):
            count += chek_is_bomb_or_not(matrix, k, m)
    return count

def check_down_right(matrix:list[list[int]],i:int,j:int):
    count=0
    for k in range(i - 1, i + 1):
        for m in range(j - 1, j + 1):
            count += chek_is_bomb_or_not(matrix, k, m)
    return count

def chek_up(matrix:list[list[int]],i:int,j:int):
    count=0
    for k in range(i, i + 2):
        for m in range(j - 1, j + 2):
            count += chek_is_bomb_or_not(matrix, k, m)
    return count

def chek_down(matrix:list[list[int]],i:int,j:int):
    count=0
    for k in range(i - 1, i + 1):
        for m in range(j - 1, j + 2):
            count += chek_is_bomb_or_not(matrix, k, m)
    return count

def chek_left(matrix:list[list[int]],i:int,j:int):
    count=0
    for k in range(i - 1, i + 2):
        for m in range(j, j + 2):
            count += chek_is_bomb_or_not(matrix, k, m)
    return count
def chek_right(matrix:list[list[int]],i:int,j:int):
    count=0
    for k in range(i - 1, i + 2):
        for m in range(j - 1, j + 1):
            count += chek_is_bomb_or_not(matrix, k, m)
    return count

def chek_normal(matrix:list[list[int]],i:int,j:int):
    count=0
    for k in range(i - 1, i + 2):
        for m in range(j - 1, j + 2):
            count += chek_is_bomb_or_not(matrix, k, m)
    return count



def chek_num(matrix:list[list[int]],i:int,j:int):
    count=0
    if i==0 and j==0:
        count+=chek_up_left(matrix, i, j)
    elif i==0 and j==len(matrix[0])-1: #правый верхний угол
        count+=check_up_right(matrix,i,j)
    elif i==len(matrix)-1 and j==0:   #левый нижний угол
        count+=check_down_left(matrix,i,j)
    elif i==len(matrix)-1 and j==len(matrix[0])-1: #правый нижний угол
        count+=check_down_right(matrix,i,j)
    elif i==0:                                       #первая строка
        count+=chek_up(matrix,i,j)
    elif i==len(matrix)-1:                                       #последняя строка
        count+=chek_down(matrix,i,j)
    elif j==0:                                      #первый столбец
        count+=chek_left(matrix,i,j)
    elif j==len(matrix[0])-1:                     #последний столбец
        count+=chek_right(matrix,i,j)
    else:
        count+=chek_normal(matrix,i,j)
    return count






def chek_how_many_1(matrix:list[list[int]],viority:float):
    summ = 0
    for row in matrix:
        summ += len(row)
    how_many_1 = int(viority * summ)
    return how_many_1

def show_matrix(matrix:list[list[int]]):
    for row in matrix:
        print(row)

def create_closed_matrix(x:int,y:int):
    matrix = [['[]'] * x for i in range(y)]
    return matrix

## идем наверх. если наверху конец поля или цифра, то поворачиваем направо и идем до цифры или конца поля, потом от начальной точки идем налево
##
def search_null_points(matrix:list[list[int]],x:int,y:int):
    a=list()
    start_x=x
    start_y=y
    current_x=x
    current_y=y
    while y+1 < len(matrix[0]) and matrix[x][y+1]=='0':
        y += 1
        a.append([x,y])
    while y-1 >= 0 and matrix[x][y-1]=='0':
        y -= 1
        a.append([x,y])
    while x+1<len(matrix) and matrix[x+1][y]=='0':
        x+=1
        a.append([x,y])
    while x-1>=0 and matrix[x-1][y]=='0':
        x-=1
        a.append([x,y])

    return a

def show_part_matrix(matrix:list[list[int]],matrix_now:list[list[int]],x:int,y:int):
    if matrix[x][y] in ('1','2','3','4','5','6','7','8'):
        matrix_now[x][y]=matrix[x][y]
        return matrix_now
    if matrix[x][y]=='*':
        show_game_over()
        return matrix
    if matrix[x][y]=='0':
        return 0
    # for i in range(len(matrix)):
    #     for j in range(len(matrix[0])):
    #
    #         matrix[i][j]='[]'
    # show_matrix(matrix)

def show_game_over():
    print("Вы взорвали бомбу. Игра закончилась")



test_matrix=[['0','0','0','0','0','0','0'],
             ['0','0','0','0','0','0','0'],
             ['*','0','0','0','0','0','0']
             ]
test_matri=count_num(test_matrix)
result=search_null_points(test_matri,2,2)
print(result)

print("пролдж")