import re

fname = input("Please enter the css file name: ")
ofile = open(fname)
c = 0
d = {}


def color_finder(line):
    global c
    global d
    x = re.findall('#[a-fA-F0-9]+', line)
    y = re.findall('#[a-fA-F0-9]+\s*{', line)
    for i in range(len(y)):
        if len(y[i]) < 7:
            y[i] = y[i][:4]
        else:
            y[i] = y[i][:7]
    for i in x:
        if len(i) == 4 or len(i) == 7:
            if i in y:
                continue
            else:
                d[i] = d.get(i, 0) + 1
                c += 1
                # print(i)
        else:
            continue


for line in ofile:
    color_finder(line)
# print(c)
sort_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
for i in sort_d:
    print(i[0], i[1])
