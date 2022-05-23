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
            if i+n-1-occupied[i] not in l2:
                l2.append(i+n-1-occupied[i])
        if len(l1) == n and len(l2) == n:
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
n = int(input("To find the number of solutions possible for the n-queen problem please enter your n: "))
if n == 1:
    print([['Q']])
else:
    possible = set([i for i in range(n)])

    for i in range(n):
        occupied = [i]
        queen(i, occupied, solutions, possible)

    ans = []
    for solution in solutions:
        lst = []
        for pos in solution:
            astr = '.'*pos + 'Q' + '.'*(n-pos-1)
            lst.append(astr)
        ans.append(lst)

    print(ans)
