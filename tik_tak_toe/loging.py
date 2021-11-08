import datetime
from constants import FILE_HANDLERS, INIT_ROW_TEMPLATE

def write_data_to_file(handler:str, message:str, mode = "a"):
    file = open(FILE_HANDLERS[handler], mode, encoding="UTF-8")
    try:
        file.write(message)
    except IOError:
        print("Ошибка записи файла")
    finally:
        file.close()

def init_line_to_dict(line, delimiter = "___"):
    result = {}
    line_data = line[:-1].split(delimiter)
    for key, data in zip(INIT_ROW_TEMPLATE, line_data):
        result[key] = INIT_ROW_TEMPLATE[key](data)
    return result

def get_last_row(handler):
    try:
        file = open(FILE_HANDLERS[handler], "r", encoding="UTF-8")
    except FileNotFoundError:
        return None
    try:
        line = None
        for line in file:
            pass
        else:
            return line
    except IndexError:
        return None
    finally:
        file.close()

def get_game_num():
    inc = 1
    try:
        file = open(FILE_HANDLERS["GAME_NUM"], "r", encoding="UTF-8")
    except FileNotFoundError:
        write_data_to_file("GAME_NUM", str(inc), "w")
        return inc
    try:
        data = file.read()
        if not data:
            return inc
        inc = int(data) + 1
        return inc
    except IOError:
        print("Ошибка чтения значения")
    finally:
        file.close()
        write_data_to_file("GAME_NUM", str(inc), "w")

def write_init(init_data):
    names = ",".join(itm["name"] for itm in init_data["users"])
    init_string = f"{init_data['game_num']}; Режим игры:{init_data['mode']}; Игроки:{names}; Время игры:{datetime.datetime.now().isoformat()}\n"
    write_data_to_file("INIT_GAME", init_string)

def write_step(user, step, step_number, game_num):
    step_string = "/".join(map(str, step))
    log_string = f"{game_num}; Игрок:{user['name']}; Шаг:{step_string}; {step_number}\n"
    write_data_to_file("GAME_STEP", log_string)


def write_end_game(winner, step_num):
    if winner:
        result_str = f"На {step_num} ходу победил {winner['name']}\n"
    else:
        result_str = f"На {step_num} ходу ничья\n"
    write_data_to_file("GAME_END", result_str)





