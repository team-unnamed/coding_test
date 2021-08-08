n = int(input())

# count how many numbers there are
num_counts = {}
for num in map(int, input().split()):
    if num not in num_counts:
        num_counts[num] = 0
    num_counts[num] += 1

input()
print(*list(map(lambda x: num_counts[int(x)] if int(x) in num_counts else 0, input().split())))
