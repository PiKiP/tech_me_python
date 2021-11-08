import sys
from users import MODES


HELP = ["help", "h"]

TERMINAL_INPUT = {
    "mode": '',
    "names": [],
}

def help():
    print("""Для выбор режима, необходимо вводить:
           -для игры с компьютером python main.py COMP
           -для игры с другим игроком python main.py USER
Далее вводите ваше имя.
Если произошел неверный ввод, игра предложит вам
выбрать номера режима игры.
Чтобы снова вернуться к подсказке, можно ввести 'help' или 'h'
""")
    sys.exit(0)

def terminal():
    try:
        argv_mode = sys.argv[1]
        if argv_mode.upper() in MODES:
            TERMINAL_INPUT["mode"] = argv_mode
        elif argv_mode in HELP:
            help()
    except IndexError:
        pass

    if not TERMINAL_INPUT["mode"]:
        return None

    try:
        TERMINAL_INPUT["names"] = sys.argv[2:]
    except IndexError:
        pass
