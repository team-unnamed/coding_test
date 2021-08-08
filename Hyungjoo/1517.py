n = int(input())
nums = list(map(int, input().split()))
ans = 0


# use merge sorting. using bubble sorting excceed time limit.
def merge_sort(nums):
    global ans

    if len(nums) == 1:
        return nums
    else:
        nums_len = len(nums)
        sorted_left = merge_sort(nums[:nums_len // 2])
        sorted_right = merge_sort(nums[nums_len // 2:])

        left_len = len(sorted_left)
        right_len = len(sorted_right)

        sorted_nums = []
        left_i, right_i = 0, 0
        while left_i < left_len and right_i < right_len:
            if sorted_left[left_i] <= sorted_right[right_i]:
                sorted_nums.append(sorted_left[left_i])
                left_i += 1
            elif sorted_left[left_i] > sorted_right[right_i]:
                sorted_nums.append(sorted_right[right_i])
                right_i += 1
                # count up when the number of right array is appended on new array.
                ans += left_len - left_i

        if left_i == left_len:
            sorted_nums.extend(sorted_right[right_i:])
        else:
            sorted_nums.extend(sorted_left[left_i:])

        return sorted_nums


sorted_nums = merge_sort(nums)
print(ans)
