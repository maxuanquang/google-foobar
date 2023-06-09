def find_lcm(a, b):
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



import pdb
pdb.set_trace()