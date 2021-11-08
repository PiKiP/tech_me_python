import random


def get_step():
    while True:
        result = []
        input_step = input("Введите координаты хода через пробел\n")
        steps = input_step.split(" ")
        try:
            if len(steps) != 2:
                raise ValueError
            for itm in steps:
                result.append(int(itm))
        except ValueError:
            print("Ошибка ввода! Повторите")
            continue
        return tuple(result)

def chek_step(board, step: tuple):
    try:
        cell = board[step[0]][step[1]]
        if not cell:
            return True
    except IndexError:
        print("Неверные координаты")
    return False

def user_step(user:dict, board):
    if user["user_type"] == "COMP":
        step = auto_step(user, board)
        if chek_step(board, step):
            board[step[0]][step[1]] = user["symbol"]
            return step
    while True:
        step = get_step()
        if chek_step(board, step):
            board[step[0]][step[1]] = user["symbol"]
            return step
        else:
            print("Ячейка не существует или уже занята")
            continue


def auto_step(user, board):
    board_size = len(board)
    all_steps_vars = set((i, j) for i in range(board_size) for j in range(board_size))
    return random.choice(tuple(all_steps_vars.difference(user["all_steps"])))



