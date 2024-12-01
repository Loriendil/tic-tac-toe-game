import random

def count_nulls(scroll):
    """Count all zeros in a given N x N matrix and return their positions."""
    # Дана матрица N x N.
    # Посчитать все нули.
    # Возвратить кортеж с парами чисел, строка и столбец, в которых находятся нули матрицы.
    result = []
    for row in range(len(scroll)):
        for col in range(len(scroll[row])):
            if scroll[row][col] == 0:
                result.append((row, col))
    return result

def get_matrix_element(matrix, element, element_num):
    """Return specific elements from the matrix based on the type and index. element is a row, column or diagonal,
    element_num is the ordinal number of the matrix part"""
    result = []

    # I make sure that element_num belongs to the acceptable range.
    if element_num < 0 or element_num > len(matrix):
        print('Error: element_num is out of range. Function get_matrix_element()')
        return result

    match element:
        case 1:  # Column
            result = [row[element_num - 1] for row in matrix]
        case 2:  # Row
            result = matrix[element_num - 1]
        case 3:  # Main diagonal
            result = [matrix[i][i] for i in range(len(matrix))]
        case 4:  # Minor diagonal
            result = [matrix[i][len(matrix) - 1 - i] for i in range(len(matrix))]
        case _:  # Not a correct option. We need an error handler in general... in theory...
            print('Error: Invalid element type. Function get_matrix_element()')
    return result

def check_victory(matrix, e_type, e_num):
    """Check if there is a winner in the game based on the specified element."""
    result = get_matrix_element(matrix, e_type, e_num)
    total = sum(result)
    # If function get_matrix_element() returns 3 or -3, then whole matrix element (row, column, etc.) contains
    # all non-zero number.
    if total == 3:
        return 1 # winner is X-player
    elif total == -3:
        return -1 # winner is O-player

    elif all(cell != 0 for row in matrix for cell in row):
        return 2
    return 0

def create_board(board_size = 3):
    # создаём игровое поле N на N
    board = []
    # заполняем поле нулями, которые будут означать, что поле пустое.
    for i_tem in range(board_size):
        board_row = list()
        for j_tem in range(board_size):
            board_row.append(0)
        board.append(board_row)
    return board

def player_choose_place(board_size):
    """Prompt the player to choose a position on the board."""
    while True:
        print(
            f'Введите номер столбца, а затем номер строки начиная с 1 до {board_size} через запятую.[введите целое натуральное число]')
        coordinates_string = input()
        separator = ','
        if separator in coordinates_string:
            coord_list = coordinates_string.split(separator)
            if coord_list[0].isnumeric() and coord_list[1].isnumeric():
                if (int(coord_list[0]) != 0) and (int(coord_list[1]) != 0):
                    return int(coord_list[0]) - 1, int(coord_list[1]) - 1
                else:
                    continue
            else:
                continue
        else:
            continue

def is_cell_empty(coord, board):
    """Check if the specified cell is empty; if not, prompt for a new position."""
    while True:
        if board[coord[0]][coord[1]] != 0:
            coord = player_choose_place(len(board))
            continue
        else:
            return True

def taking_turns_mech(current_player, player_id, board):
    """Manage the turn-taking mechanism for players and the computer."""
    board_size = len(board)
    if current_player > 0:
        if player_id > 0:
            print('X-Player acts!')
        else:
            print('X-PC acts!')
    else:
        if current_player < 0:
            if player_id < 0:
                print('O-Player acts!')
            else:
                print('O-PC acts!')

    print('Here is battlefield:')
    print(board)
    if current_player > 0:
        if player_id > 0:
            print('X-Player looks on board for his turn!')
            player_x_input = player_choose_place(board_size)
            if is_cell_empty(player_x_input, board):   # из-за того, что правильный ввод не передаётся
                board[player_x_input[0]][player_x_input[1]] = 1 # ошибочные координаты не заменяются
            else:                                               # на правильные
            # А зачем нам вся история с проверками, если мы можем проверять вхождение ввода, в
            # массив свободных ячеек, как при работе НПС? Меньше разнородных проверок - лучше!
                print('Error! Cell for X-Player is not empty! Choose another!')
            print('X-Player places at that cell X')
        else:
            print('X-PC looks on board for his turn!')
            board_map = count_nulls(board)
            if len(board_map) > 0:
                index = random.randrange(start=0, stop=len(board_map))
                pc_x_input = board_map.pop(index)
                board[pc_x_input[0]][pc_x_input[1]] = 1
            else:
                print("Error! There is no place for X-PC to place it's piece!")
            print('X-PC places at that cell X')

    else:
        if current_player < 0:
            if player_id < 0:
                print('O-Player looks on board for his turn!')
                player_o_input = player_choose_place(board_size)
                if is_cell_empty(player_o_input, board):
                    board[player_o_input[0]][player_o_input[1]] = -1
                else:
                    print('Error! Cell for O-Player is not empty! Choose another!')
                print('O-Player places at that cell O')
            else:
                print('O-PC takes his turn!')
                board_map = count_nulls(board)
                if len(board_map) > 0:
                    index = random.randrange(start=0, stop=len(board_map))
                    pc_o_input = board_map.pop(index)
                    board[pc_o_input[0]][pc_o_input[1]] = -1
                else:
                    print("Error! There is no place for O-PC to place it's piece!")
                print('O-PC places at that cell o')