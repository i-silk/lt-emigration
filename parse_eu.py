f = open('/Users/ingasilk/Downloads/eu_pop_2018.txt')
o = open('/Users/ingasilk/Downloads/eu_pop_2018.csv', 'w')

for line in f:
    sp = line.split()
    country = '"' + ' '.join(sp[:-4]) + '"'
    joined = ','.join([country] + sp[-4:])
    o.write(joined + '\n')

o.close()
f.close()
