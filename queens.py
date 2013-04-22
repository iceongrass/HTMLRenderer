def conflict(state, nextX):
    nextY = len(state)
    for i in range (nextY):
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False

def queen(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                if not conflict(state,pos):
                    for result in queen(num, state+(pos,)):
                        yield (pos,)+result
            
