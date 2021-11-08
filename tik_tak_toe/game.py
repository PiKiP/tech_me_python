from itertools import cycle
from board import get_board, board_match, print_board
from loging import write_init, get_game_num, write_step, write_end_game
from steps import user_step
from users import ask_mode, create_users
from terminal import terminal, TERMINAL_INPUT

def game_init():
    print("Добро пожаловать в игру Крестики Нолики")
    terminal()
    mode = TERMINAL_INPUT["mode"]
    if not mode:
        mode = ask_mode()
    game_num = get_game_num()
    init_data = {
        "users": create_users(mode),
        "board": get_board(3),
        "mode": mode,
        "game_num": game_num
    }
    write_init(init_data)
    return init_data

def game_cycle(users, board, mode, game_num):
    winner = None
    step_num = None
    steps = set()
    for step_num, user in enumerate(cycle(users), 1):
        user["all_steps"] = steps
        print(f"Ход игрока: {user['name']}")
        print_board(board)
        step = user_step(user, board)
        user["steps"].append(step)
        steps.add(step)
        write_step(user, step, step_num, game_num)
        if board_match(board):
            winner = user
            break
        if step_num > 8:
            break
    return step_num, winner


def game_end(step_num, winner):
    result_str = f'победил игрок {winner["name"]}' if winner else 'Ничья'
    result_print = f"На {step_num} ходу {result_str}"
    write_end_game(winner, step_num)
    print(result_print)
    vars = ("Y", "N")
    while True:
        user_input = input(f"Начать новую игру?{'/'.join(vars)}").upper()
        if user_input in vars:
            return user_input == vars[0]
        print("Неверный ввод! Повторите")

