def score(game):
    result = 0
    frame = 1
    in_first_half_of_frame = True
    for i in range(len(game)):
        if game[i] == '/':
            last_frame_half = get_value(game[i-1])
            result += 10 - last_frame_half
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            result = handle_bonus_points(game, i, result)
        frame, in_first_half_of_frame = frame_counter(frame, in_first_half_of_frame, game[i])
    return result


def frame_counter(frame, in_first_half_of_frame, char):
    if not in_first_half_of_frame:
        frame += 1
    if in_first_half_of_frame is True:
        in_first_half_of_frame = False
    else:
        in_first_half_of_frame = True
    if char == 'X' or char == 'x':
        in_first_half_of_frame = True
        frame += 1
    return frame, in_first_half_of_frame


def handle_bonus_points(game, i, result):
    if game[i] == '/':
        result += get_value(game[i+1])
    elif game[i] == 'X' or game[i] == 'x':
        result += get_value(game[i+1])
        if game[i+2] == '/':
            result += 10 - get_value(game[i+1])
        else:
            result += get_value(game[i+2])
    return result


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
