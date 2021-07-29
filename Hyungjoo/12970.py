n, k = map(int, input().split())

is_possible = False
for a_num in range(1, n):
    if a_num * (n - a_num) >= k:
        is_possible = True
        b_nums = n - a_num

        left = k
        counts = []
        for b_num in range(n - a_num, 0, -1):
            counts.append(left // b_num)
            left %= b_num

        answer = ""
        for a_count in reversed(counts):
            answer = "A" * a_count + "B" + answer
        answer += "A" * (a_num - sum(counts))

        is_possible = True
        print(answer)
        break

if not is_possible:
    print(-1)
