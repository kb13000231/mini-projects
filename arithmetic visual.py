def arithmetic_arranger(problems, res=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'
    fline = []
    oper = []
    sline = []
    rline = []
    leng = []
    for i in problems:
        a = i.split()
        if a[0].isdigit() is False or a[2].isdigit() is False:
            return 'Error: Numbers must only contain digits.'
        if len(a[0]) > 4 or len(a[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        fline.append(a[0])
        oper.append(a[1])
        sline.append(a[2])
        leng.append(max(len(a[0]), len(a[2])))
        if a[1] == '+':
            r = int(a[0]) + int(a[2])
            rline.append(str(r))
        elif a[1] == '-':
            r = int(a[0]) - int(a[2])
            rline.append(str(r))
        else:
            return 'Error: Operator must be '+' or '-'.'
    for i in range(len(fline)):
        fline[i] = fline[i].rjust(leng[i]+2, ' ')
        sline[i] = oper[i] + sline[i].rjust(leng[i]+1, ' ')
        rline[i] = rline[i].rjust(leng[i]+2, ' ')

    first = '    '.join(fline)
    second = '    '.join(sline)
    dline = '    '.join(['-'*(i+2) for i in leng])
    resul = '    '.join(rline)
    final = '\n'.join([first, second, dline, resul]) if res is True else '\n'.join([first, second, dline])
    return final


ls = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print_res = input("Do you want to print the result!(Y/N)")
print_res = True if print_res.upper() == 'Y' else False
print(arithmetic_arranger(ls, print_res))
