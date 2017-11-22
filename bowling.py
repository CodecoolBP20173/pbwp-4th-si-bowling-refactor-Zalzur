def score(game):
    '''Transforms a given string to score, according to the scoring of bowling.
        "X" indicates strike, "/" indicates spare, "-" indicates miss.
        Example: "1/35XXX458/X3/XX6" = 189 points
        Returns: The score of the string (int)'''
    result = 0
    frame = 1
    in_first_half_of_frame = True
    for i in range(len(game)):
        # Adds the value of the character to result:
        if game[i] == '/':
            last_frame_half = get_value(game[i-1])
            result += 10 - last_frame_half
        else:
            result += get_value(game[i])
        # If it's a strike or a spare adds the bonus points to result:
        if frame < 10 and get_value(game[i]) == 10:
            result = handle_bonus_points(game, i, result)
        # Keeps track of the rounds (frame):
        frame, in_first_half_of_frame = frame_counter(frame, in_first_half_of_frame, game[i])
    return result


def frame_counter(frame, in_first_half_of_frame, char):
    '''Trace which frame we are in and which half of it.
        Returns: -The number of the frame we are in (int).
                 -True, if we are in the first half. False, if the second half (Boolean).'''
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
    '''Handles the bonus points:
        -"/" (spare): 10 + the score of the next round.
        -"X" (strike): 10 + the score of the next 2 rounds
        Returns: The result with the bonus points added to it. (int)'''
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
    '''Gives back the value of the given character (this given character must be a string).
        "X" and "/" worth 10 points.
        "-" worths 0 point.
        The numbers worth equal as themselves.
        Returns: The value of the given character (int)'''
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
