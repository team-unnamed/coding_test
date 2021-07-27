n = input()

candidate = "".join(sorted(n, reverse=True))

if candidate[-1] == "0":
    if int(candidate[:-1]) % 3 == 0:
        print(candidate)
    else:
        print(-1)
else:
    print(-1)
