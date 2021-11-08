def get_board(size):
    return [[0 for _ in range(size)] for _ in range(size)]

def board_match(board):
    def chek_line(line):
        line_set = set(line)
        if 0 not in line_set and len(line_set) == 1:
            raise ValueError("CHECK_LINE")
        return False

    board_len = len(board)
    diagonal = map(lambda idx:board[idx][idx], range(0, board_len))
    diagonal_invert = map(lambda idx:board[idx][board_len - idx - 1], range(board_len -1, -1, -1))
    try:
        _ = any(map(chek_line, (diagonal, diagonal_invert)))
        for row, column in zip(board, zip(*board)):
            _ = any(map(chek_line, (row, column)))
    except ValueError as exc:
        if 'CHECK_LINE' in exc.args:
            return True
        else:
            raise exc
    return False

def print_board(board):
    first_row = f'__{"|".join(map(str, range(len(board))))}_'
    str_rows = "\n".join(map(lambda itm:f"{itm[0]}_{'|'.join(map(str, itm[1]))}_", enumerate(board)))
    print(f"{first_row}\n{str_rows}\n{'#'*len(first_row)}")
