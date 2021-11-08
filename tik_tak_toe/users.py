import random
from constants import USER_TEMPLATE, COMP_NAMES, SYMBOLS


def create_user(symbol):
    user = {}
    for itm in USER_TEMPLATE:
        user[itm[0]] = itm[1](symbol=symbol, user_type="USER")
    return user

def create_comp(mode, symbol):
     return {
         "name": random.choice(COMP_NAMES),
         "symbol": symbol,
         "steps": [],
         "all_steps": set(),
         "user_type": "COMP",
     }

MODES = {
    "COMP": {"creator": create_comp},
    "USER": {"creator": create_user},
}

def get_user(mode, symbol):
    return MODES[mode]["creator"](symbol=symbol)

def ask_mode():
    user_modes = {idx: itm for idx, itm in enumerate(MODES, 1)}
    modes_str = "\n".join(f"{key}: {value}" for key, value in user_modes.items())
    modes_string = f"Выберите номер режима игры\n{modes_str}"

    while True:
        try:
            mode_input = int(input(modes_string))
            return user_modes[mode_input]
        except ValueError:
            print("Недопустимый ввод!Вводите только число")
        except KeyError:
            print("Недопустимое значение!Повторите ввод")
        continue

def create_users(mode):
    users = []
    for symbol, mode in zip(SYMBOLS, ("USER", mode)):
        user = get_user(mode, symbol)
        users.append(user)
    return users
