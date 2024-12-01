import random
import utility_funcs as uf

#  1 - Х-player
# -1 - O-player
#  2 - player controlled by human
# -2 - player, controlled by PC

def play(player_id):
    while True:
        if player_id > 0:
            print('You have chosen to challenge a friend!')
        if player_id < 0:
            print('You have chosen to challenge the computer!')

        board_size = input('What size of playing field do you want? [enter a natural number]')
        if board_size.strip().isdigit() and int(board_size) > 0:
            board_size = int(board_size)
            break

    board = uf.create_board(board_size)
    first_turn = random.choice([-1, 1])
    player = first_turn

    victory = False
    while not victory:
        # Зачем нужен условный переход, если мы можем принудительно присвоением менять сторону
        # и передавать противоположный player_id гарантировано противоположный.
        uf.taking_turns_mech(player, player_id, board)
        player = -player

        for elem in range(0, len(board)):
            for e_type in range(1, 4):
                victory_id = uf.check_victory(board, e_type, elem)
                if victory_id == 1:
                    print('Winner is X-Player!')
                    victory = True
                    break

                elif victory_id == -1:
                    print('Winner is O-Player!')
                    victory = True
                    break

                elif victory_id == 2:
                    print('A draw has been recorded in the game of Tic-Tac-Toe!')
                    victory = True
                    break
            if victory:
                break