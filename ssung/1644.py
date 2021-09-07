"""

1. 에라토스테네스의 체를 이용하여 N이하의 소수를 모두 구하여 prime_list에 작은 수부터 담는다.
2. 투포인터를 이용해 구간 합이 N보다 작으면 오른쪽 포인터가 가리키는 수를 더한 뒤 오른쪽 포인터를 한 칸 옮긴다.
2-1. 오른쪽 포인터가 범위를 벗어나면 함수를 종료
3. 구간 합이 N보다 크거나 같으면 왼쪽 포인터가 가리키는 수를 더한 뒤 왼쪽 포인터를 오른쪽으로 한 칸 옮긴다.
4. 구간 합이 N이 되면 경우의 수 +1
5. 왼쪽 포인터가 오른쪽 포인터보다 더 오른쪽에 있으면 함수를 종료

"""
import sys

input = sys.stdin.readline

N = int(input())
isPrime = [True for _ in range(N + 1)]


def Eratos(n):
    for i in range(2, n + 1):
        if isPrime[i]:
            for j in range(i + i, n + 1, i):
                isPrime[j] = False


Eratos(N)
prime_list = [i for i in range(2, N + 1) if isPrime[i]]  # 소수를 차례대로 list에 담는다.

answer = 0
left = right = part_sum = 0
while left <= right:
    if part_sum < N:  # N보다 작으면 오른쪽 포인터에 있는 수를 더한다. (범위를 벗어난 경우 종료)
        if right == len(prime_list):
            break
        part_sum += prime_list[right]
        right += 1

    else:  # N보다 크거나 같으면 왼쪽 포인터에 있는 수를 더한다.
        part_sum -= prime_list[left]
        left += 1

    if part_sum == N:  # N과 같으면 경우의수 +1
        answer += 1

print(answer)
