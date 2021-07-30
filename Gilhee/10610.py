numbers = list(input())
numbers.sort(reverse=True)

sum = 0
for i in numbers:
    sum += int(i)
if sum % 3 != 0 or "0" not in numbers:
    print(-1)
else:
    print(''.join(numbers))