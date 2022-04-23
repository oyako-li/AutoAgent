f = open('Fri,22,Apr,2022,08,04,05.log', 'r')

log = []

for line in f:
    line = line.rstrip()
    l = line.split(",")
    print(l)
    log.append(l)

f.close()