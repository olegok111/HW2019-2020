#coding: utf-8
FILE = 'rw_1.txt'
FEM_MATCH = ('ШНА', 'ЧНА', 'ВНА')
MAL_MATCH = ('ВИЧ', 'ЬИЧ', 'ШИЧ')
fln = dict()
mln = dict()
with open(FILE, 'r', encoding='utf8') as infile:
    datatable = infile.readlines()
    r = 0
    for line in datatable[1:]:
        line = line.replace('(', '').replace(')', '')
        line = line.upper()
        if 'УТЕРЯНА' in line or 'ЗАБЛОКИРОВАНА' in line or 'NULL' in line or '.' in line or ',' in line or 'VIP' in line:
            continue
        r += 1
        line_data = line.split()
        try:
            if line_data[1][-1] == 'А':
                try:
                    fln[line_data[1]] += 1
                except:
                    fln[line_data[1]] = 1
            else:
                try:
                    mln[line_data[1]] += 1
                except:
                    mln[line_data[1]] = 1
        except:
            pass
        #print(line_data)
m_list = list((i, mln[i]) for i in mln.keys())
f_list = list((i, fln[i]) for i in fln.keys())
m_list.sort(key=lambda x:x[1], reverse=True)
f_list.sort(key=lambda x:x[1], reverse=True)
print(mln)
print('МУЖ')
for i in range(10):
    print(m_list[i][0], m_list[i][1])
    if i == len(m_list) - 1:
        break
print('ЖЕН')
for i in range(10):
    print(f_list[i][0], f_list[i][1])
    if i == len(f_list) - 1:
        break
