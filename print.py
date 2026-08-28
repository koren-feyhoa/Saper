from random import choice

from Сапер import *



# test_matrix=[['0','0','*'],['0','*','*'],['*','0','0']]
# test_matri=count_num(test_matrix)
# show_matrix(test_matri)

test_matrix=[['0','0','*'],['0','0','*'],['*','0','0']]
test_matri=count_num(test_matrix)
search_null_points(test_matri,2,2)

# matrix=create_matrix(5,5)
# matrix=generate_numbers(matrix,chek_how_many_1(matrix,0.25))
# matrix=count_num(matrix)
# show_matrix(matrix)
choice=1
while choice!=0:
    print("Введите размер поля x'")
    x=int(input())
    print("Введите размер поля y'")
    y=int(input())
    matrix = create_matrix(x, y)
    matrix = generate_numbers(matrix, chek_how_many_1(matrix, 0.25))
    matrix = count_num(matrix)
    matrix_now=create_closed_matrix(x,y)
    show_part_matrix(matrix_now)
    print("Выберете ячейку")
    print("Введите координату x'")
    x = int(input())
    print("Введите координату y'")
    y = int(input())


