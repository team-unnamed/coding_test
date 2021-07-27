s = input()
t = input()

cur = t
while True:
    if cur[-1] == "A":
        cur = cur[:-1]
    elif cur[-1] == "B":
        cur = "".join(list(reversed(cur[:-1])))

    if len(cur) == len(s):
        break

if cur == s:
    print(1)
else:
    print(0)
