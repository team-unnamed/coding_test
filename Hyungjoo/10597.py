def get_size(seq: str) -> int:
    seq_size = len(seq)
    for i in range(1, 51):
        seq_size -= len(str(i))
        if seq_size == 0:
            return i


def search(seq: str, is_used: dict, ans: list):
    if not seq:
        print(" ".join(ans))
        return True
    else:
        global n
        success = False

        # one digit number case
        target_num = seq[:1]
        if target_num in is_used and not is_used[target_num]:
            is_used[target_num] = True
            success = search(seq[1:], is_used, ans + [target_num])
            is_used[target_num] = False

        # two digit number case
        if len(seq) >= 2 and not success:
            target_num = seq[:2]
            if target_num in is_used and not is_used[target_num]:
                is_used[target_num] = True
                success = search(seq[2:], is_used, ans + [target_num])
                is_used[target_num] = False

        if success:
            return True

        return False


kriii = input()
n = get_size(kriii)
is_used = {str(i + 1): False for i in range(n)}

search(kriii, is_used, [])
