import openpyxl as op


def conv(fname):
    a = fname.split('.')
    ofname = a[0] + '.csv'
    xlsobj = op.load_workbook(fname)
    sheet = xlsobj.active
    data = sheet.rows
    ofile = open(ofname, 'w+')
    for row in data:
        dlist = list(row)
        for i in range(len(dlist)):
            if i == len(dlist) - 1:
                ofile.write(str(dlist[i].value))
            else:
                ofile.write(str(dlist[i].value) + ',')
        ofile.write('\n')
    return ofname


a = open(conv(input("First file in comparison: ")), 'r')
b = open(conv(input("Second file in comparison: ")), 'r')

c = a.readlines()
d = b.readlines()
g = len(c[0].split(','))

for i in range(max(len(c), len(d))):
    try:
        if i > len(c) - 1:
            raise ValueError
        else:
            c[i] = c[i].replace('\n', '')
            d[i] = d[i].replace('\n', '')
            e = c[i].split(',')
            f = d[i].split(',')
            if i == 0:
                print('line number', ','.join(e), ','.join(f))
            elif len(e) != len(f):
                print(i+1, ','.join(e), ','.join(f))
            else:
                for j in range(len(e)):
                    if e[j] != f[j]:
                        print(i+1, ','.join(e), ','.join(f))
                    else:
                        continue
                continue
    except ValueError:
        d[i] = d[i].replace('\n', '')
        elist = [str(0)]*g
        wxyz = ','.join(elist)
        print(i+1, wxyz.replace('0', ' '), d[i], g)
