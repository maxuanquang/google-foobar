import math

class Solution:
    def primes_set(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primes_set(n // i).union(set([i]))
        return set([n])

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int, help="Input number")
    args = parser.parse_args()

    solution = Solution()
    primes = solution.primes_set(args.num)
    print(f"Primes set of {args.num} is {primes}")

