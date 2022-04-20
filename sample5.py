f = open('Wed,20,Apr,2022,09,21,24.log', 'r')

log = []

for line in f:
    line = line.rstrip()
    l = line.split(",")
    print(l)
    log.append(l)

print(log)

f.close()