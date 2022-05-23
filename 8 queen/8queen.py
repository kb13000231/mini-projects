import time

start_time = time.time()


def queen(pos, occupied, solutions, possible):
    possibility = list(possible - set(occupied) - {pos-1, pos+1})
    remain = list(possible-set(occupied))
    if len(possibility) == 1 and len(remain) == 1:
        occupied.append(possibility[0])
        l1 = []
        l2 = []
        for i in range(len(occupied)):
            if i + occupied[i] not in l1:
                l1.append(i+occupied[i])
            if i+7-occupied[i] not in l2:
                l2.append(i+7-occupied[i])
        if len(l1) == 8 and len(l2) == 8:
            if occupied not in solutions:
                solutions.append(occupied)
        return None

    for i in possibility:
        temp = list(occupied)
        occupied.append(i)
        queen(i, occupied, solutions, possible)
        occupied = temp
    return None


solutions = []
possible = {0, 1, 2, 3, 4, 5, 6, 7}
for i in range(8):
    occupied = [i]
    queen(i, occupied, solutions, possible)
print(time.time() - start_time, "seconds")
