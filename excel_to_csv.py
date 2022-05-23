import openpyxl as op


def conv(fname):
    a = fname.split('.')
    ofname = a[0] + '.csv'
    xlsobj = op.load_workbook(fname)
    sheet = xlsobj.active
    data = sheet.rows
    ofile = open(ofname, 'w+')
    for row in data:
        ls = list(row)
        for i in range(len(ls)):
            if i == len(ls) - 1:
                ofile.write(str(ls[i].value))
            else:
                ofile.write(str(ls[i].value) + ',')
        ofile.write('\n')
    return ofname

# Test
# ifname = input('Please input the file name to convert: ')
# a = conv(ifname)
# print(a)
