def solution(nums):
    # Your code here
    from collections import defaultdict
    memo = defaultdict(int)
    def backtrack(idx, path_length):
        if (idx, path_length) in memo:
            return memo[(idx, path_length)]
        if path_length == 3:
            memo[(idx, path_length)] = 1
            return memo[(idx, path_length)]
        res = 0
        for nxt_idx in range(idx + 1, len(nums)):
            if nums[nxt_idx] % nums[idx] == 0:
                res += backtrack(nxt_idx, path_length + 1)
        memo[(idx, path_length)] = res
        return memo[(idx, path_length)]

    res = 0
    for i in range(len(nums)):
        res += backtrack(i, 1)
    return res


if __name__ == '__main__':
    # input = [1, 1, 1]
    input = [1, 2, 3, 4, 5, 6]
    # input = [3, 6]
    output = solution(input)
    print(output)
    