class Solution:  
    def find_factors(self, num):
        factors = []
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                factors.append(i)
                if i != num // i:
                    factors.append(num // i)
        return factors

  
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--num", type=int, help="Input number")
    args = parser.parse_args()

    solution = Solution()
    factors = solution.find_factors(num=args.num)
    print(f"Factors of {args.num} is {factors}")

