def solution(xs):
    '''This functions output maximum product of a non-empty subset of input list xs

    Parameters
    ----------
    xs: list
        A non-empty list include of integers
    '''
    # Your code here
    min_so_far, max_so_far = xs[0], xs[0]
    for num in xs[1:]:
        prod_1, prod_2 = min_so_far * num, max_so_far * num
        min_product = min([num, prod_1, prod_2])
        max_product = max([num, prod_1, prod_2])
        # Update min_so_far and max_so_far
        min_so_far = min(min_so_far, min_product)
        max_so_far = max(max_so_far, max_product)
    return str(max_so_far)

if __name__ == '__main__':
    input = [-1000]
    output = solution(input)
    print(output)