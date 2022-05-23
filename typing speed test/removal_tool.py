ofile = open('fq.txt', 'r')
ofile2 = open('quotes.txt', 'w')
for line in ofile.readlines():
    line.strip()
    line = line.split(';')
    line = line[1] if len(line) > 1 else line[0]
    if len(line) < 80:
        ofile2.write(line)
    else:
        continue
