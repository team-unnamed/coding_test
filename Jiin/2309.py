import sys

dwarfs = [0 for _ in range(9)]

for i in range(9):
    dwarfs[i] = int(sys.stdin.readline().strip())

sum_height = sum(dwarfs)
faker1 = 9999
faker2 = 9999

for i in range(9):
    for j in range(i+1, 9):
         if sum_height - (dwarfs[i]+dwarfs[j]) == 100:
             faker1 = dwarfs[i]
             faker2 = dwarfs[j]
             break

dwarfs.remove(faker1)
dwarfs.remove(faker2)
dwarfs = sorted(dwarfs)

for dwarf in dwarfs:
    print(dwarf)
