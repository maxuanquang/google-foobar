def solution(l):
    '''
    This function input a list numbers
    Output the max number can be formed by numbers in input, and output must be divisible by 3
    '''
    # Your code here
    nums = sorted(l)
    total_sum = sum(nums)
    def check_divisible(path, n, curr_nums):
        '''This function removes each element in l, from small number to big number
        Then check if the remain numbers can form a number that is divisible by 3

        Paremeters
        ----------
        i : int
            Current index in nums
        path: list
            Current numbers in nums to be removed
        n: int
            Total numbers to remove
        '''
        if len(path) == n:
            if (total_sum - sum(path)) % 3 != 0:
                return 0
            new_nums = sorted(nums, reverse=True)
            for num in path:
                new_nums.remove(num)
            return int(''.join([str(num) for num in new_nums]))
        
        for idx in range(len(curr_nums)):
            num = check_divisible(path + [curr_nums[idx]], n, curr_nums[idx+1:])
            if num: 
                return num
        return 0
            
    for n in range(len(nums)):
        num = check_divisible([], n, nums)
        if num: return num
    return 0


if __name__ == '__main__':
    input = [3, 1, 4, 1, 5, 9]
    input = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    output = solution(input)
    print(output)