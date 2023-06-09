import math
import operator as op
from functools import reduce


def solution(width, height, states):
    col_permutations = gen_permutations(width)
    row_permutations = gen_permutations(height)

    total = 0
    for cp in col_permutations:
        curr_sum = 0
        for rp in row_permutations:
            num_fixed_matrices = count_fixed_matrices(rp, cp, states)
            curr_sum += num_fixed_matrices
        total += curr_sum

    G = math.factorial(width) * math.factorial(height)
    result = total // G
    return str(result)


class Permutation:
    def __init__(self, fixed, cycles, count):
        self.fixed = fixed
        self.cycles = cycles
        self.count = count


def gen_permutations(n):
    result = []
    for fixed in range(n - 1):
        cycles_list = numbers_sum_to_n(n - fixed)
        for cycles in cycles_list:
            p = make_permutation(n, fixed, cycles)
            result.append(p)

    result.append(Permutation(n, [], 1))  # identity permutation
    return result


def make_permutation(n, fixed, cycles):
    count = ncr(n, fixed)

    remains = n - fixed
    repeated_len, previous_len = 1, 0

    for length in cycles:
        selections = ncr(remains, length)
        remains = remains - length
        disjoint_cycles = math.factorial(length - 1)
        count = count * selections * disjoint_cycles

        if previous_len == length:
            repeated_len += 1
        else:
            count = count // math.factorial(repeated_len)
            repeated_len = 1
            previous_len = length

    count = count // math.factorial(repeated_len)
    return Permutation(fixed, cycles, count)


def count_fixed_matrices(rp, cp, s):
    # Number of configurations of free matrices
    fixed = s ** (rp.fixed * cp.fixed)

    # Number of configurations of matrices that have just one axis permuted
    m = s ** (cp.fixed * len(rp.cycles))
    fixed *= m

    m = s ** (rp.fixed * len(cp.cycles))
    fixed *= m

    # Number of configurations of matrices that have 2 axises permuted
    t = 0
    for lr in rp.cycles:
        for lc in cp.cycles:
            v = lr * lc // lcm(lr, lc)
            t += v
    m = s ** t
    fixed *= m

    # Multiply with number of duplicate cycles
    fixed *= rp.count
    fixed *= cp.count

    return fixed


def numbers_sum_to_n(n):
    res = []
    recursive_numbers_sum_to_n([], n, res)
    return res


def recursive_numbers_sum_to_n(path, left, res):
    if left < 0:
        return
    if left == 0:
        res.append(list(path))
    start = 2 if len(path) == 0 else path[-1]
    for num in range(start, left + 1):
        recursive_numbers_sum_to_n(path + [num], left - num, res)


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom


def lcm(a, b):
    # Find the maximum of the two numbers
    max_num = max(a, b)

    # Start with the larger number and increment by the maximum
    lcm = max_num

    while True:
        # Check if both numbers are divisible by lcm
        if lcm % a == 0 and lcm % b == 0:
            return lcm

        # Increment lcm by the maximum number
        lcm += max_num


if __name__ == "__main__":
    inputs = [
        (1, 1, 1),
        (1, 1, 2),
        (1, 1, 3),
        (1, 1, 4),
        (2, 1, 1),
        (2, 1, 2),
        (2, 1, 3),
        (2, 2, 1),
        (2, 2, 2),
        (2, 2, 3),
        (2, 2, 4),
        (3, 2, 2),
        (3, 2, 3),
        (3, 2, 4),
        (3, 3, 2),
        (3, 3, 5),
        (3, 3, 10),
        (8, 3, 4),
        (2, 9, 7),
        (5, 5, 5),
        (12, 12, 20),
    ]

    answers = [
        "1",
        "2",
        "3",
        "4",
        "1",
        "3",
        "6",
        "1",
        "7",
        "27",
        "76",
        "13",
        "92",
        "430",
        "36",
        "57675",
        "27969700",
        "1774852035",
        "4498416692",
        "20834113243925",
        "97195340925396730736950973830781340249131679073592360856141700148734207997877978005419735822878768821088343977969209139721682171487959967012286474628978470487193051591840"
    ]

    correct = 0
    for input, answer in zip(inputs, answers):
        output = solution(*input)
        print("input :", input)
        print("output:", output)
        print("answer:", answer)
        print("----------------------")
        if output == answer:
            correct += 1
    print(f"Congratulations! You scored {correct} out of {len(answers)}.")

    # import pdb
    # pdb.set_trace()
