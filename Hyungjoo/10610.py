n = input()

if "0" in n:
    for i in range(len(n)):
        if n[i] == "0":
            candidate = n[:i] + n[i + 1:] + "0"
            if int(candidate) % 30 == 0:
                print("".join(sorted(candidate, reverse=True)))
            else:
                print(-1)
            break
    else:
        print(-1)
else:
    print(-1)
