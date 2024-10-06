game_size=int(input("What Size Game GoPy?"))
def dynamic_matrix(width):
    row = 1
    matrix = ""
    for i in range(width * width):
        if i == width * row - 1:
            matrix = matrix + str(i) + "\n"
            row += 1
        else:
            matrix = matrix + str(i) + "\t"
    return matrix

matrix = dynamic_matrix(game_size)
print(matrix)
matrix_list=matrix.replace("\n","\t").rstrip("\t").split("\t")

def row_checking(matrix_list,who):  #the "who" parameter takes "X" or "O" , it makes function more usable
    for i in range(game_size):
        if matrix_list[ i * game_size: (i + 1) * game_size].count(who) == game_size:
            return "Winner: {}".format(who)

def column_checking(matrix_list,who):
     for i in range(game_size):
         column = []
         for j in range(game_size):
             column.append(matrix_list[i+j*game_size])
         if column.count(who)==game_size:
             return "Winner: {}".format(who)


def diagonal_check_l_to_r(matrix_list,who):
    diagonal=[]
    for i in range(game_size):
        diagonal.append(matrix_list[i+i*game_size])
    if diagonal.count(who)==game_size:
        return "Winner: {}".format(who)

def diagonal_check_r_to_l(matrix_list,who):
    diagonal=[]
    for i in range(1,game_size+1):
        diagonal.append(matrix_list[i*(game_size-1)])
    if diagonal.count(who)==game_size:
        return "Winner: {}".format(who)

allowed_characters=tuple(range(game_size*game_size)) # contains the matrix numbers that user gave the size

while True:
    player_1=int(input("Player 1 turn--> ")) #takes a number that user want to replace it with "X"
    if player_1 not in allowed_characters:
        print("please enter a valid number")



    matrix = matrix.replace(str(player_1),"X",1)  # change only first occurence of the number player_1
    matrix_list = matrix.replace("\n", "\t").rstrip("\t").split("\t")
    print(matrix)
    if bool(row_checking(matrix_list,"X")):  # checks if the function gives none or an output
        print(row_checking(matrix_list,"X"))
        break
    if bool(column_checking(matrix_list,"X")):
        print(column_checking(matrix_list, "X"))
        break
    if bool(diagonal_check_r_to_l(matrix_list,"X")):
        print(diagonal_check_r_to_l(matrix_list, "X"))
        break
    if bool(diagonal_check_l_to_r(matrix_list,"X")):
        print(diagonal_check_l_to_r(matrix_list, "X"))
        break

    player_2 = int(input("Player 2 turn--> "))   #takes a number that user want to replace it with "O"
    if player_2 not in allowed_characters:
        print("Please enter a valid number")
    matrix = matrix.replace(str(player_2),"O",1)
    matrix_list = matrix.replace("\n", "\t").rstrip("\t").split("\t") # makes matrix a list contains only numbers to make changes easier
    print(matrix)
    if bool(row_checking(matrix_list,"O")):
        print(row_checking(matrix_list, "O"))
        break
    if bool(column_checking(matrix_list,"O")):
        print(column_checking(matrix_list, "O"))
        break
    if bool(diagonal_check_r_to_l(matrix_list,"O")):
        print(diagonal_check_r_to_l(matrix_list, "O"))
        break
    if bool(diagonal_check_l_to_r(matrix_list,"O")):
        print(diagonal_check_l_to_r(matrix_list,"O"))
        break







