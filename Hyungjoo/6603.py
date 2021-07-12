from itertools import combinations

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    num_count, num_list = nums[0], nums[1:]

    for case in combinations(num_list, 6):
        print(*case)

    print()
