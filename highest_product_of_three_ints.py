def highest_product_of_three_ints(nums):
    """
    >>> highest_product_of_three_ints([5, 6, 3, 9, 7, 2])
    378
    >>> highest_product_of_three_ints([-5, -6, -3, 9, 7, 2])
    270
    """
    highest = None
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            for k, num3 in enumerate(nums):
                if i != j and j != k and i != k:
                    highest = max(highest, (num1 * num2 * num3))
    return highest 


def highest_product_of_three_ints_optimized(nums):
    """
    >>> highest_product_of_three_ints_optimized([5, 6, 3, 9, 7, 2])
    378
    >>> highest_product_of_three_ints_optimized([-5, -6, -3, 9, 7, 2])
    270
    """
    highest = max(nums[0], nums[1])
    lowest = min(nums[0], nums[1])
    highest_product_of_three = nums[0] * nums[1] * nums[2]
    highest_product_of_two = nums[0] * nums[1]
    lowest_product_of_two = nums[0] * nums[1]
    for i in range(2, len(nums)):
        highest_product_of_three = max(highest_product_of_three,
                                        (nums[i] * highest_product_of_two),
                                        (nums[i] * lowest_product_of_two))
        highest_product_of_two = max(highest_product_of_two, 
                                        (nums[i] * highest), 
                                        (nums[i] * lowest))
        lowest_product_of_two = min(lowest_product_of_two, 
                                        (nums[i] * highest), 
                                        (nums[i] * lowest))
        highest = max(highest, nums[i])
        lowest = min(lowest, nums[i])


        
    return highest_product_of_three

def highest_product_of_k_ints(nums, k):
    """
    >>> highest_product_of_k_ints([5, 6, 3, 9, 7, 2], 2)
    63
    >>> highest_product_of_k_ints([5, 6, 3, 9, 7, 2], 3)
    378
    >>> highest_product_of_k_ints([5, 6, 3, 9, 7, 2], 4)
    1890
    >>> highest_product_of_k_ints([5, 6, 3, 9, 7, 2], 5)
    5670
    >>> highest_product_of_k_ints([-5, -6, -3, 9, 7, 2], 4)
    1890
    >>> highest_product_of_k_ints([-5, -6, -3, 9, 7, 2], 3)
    270
    """
    if len(nums) < k:
        return "Not enough numbers in list with given k."

    highest_products = [nums[0]] * k
    lowest_products = [nums[0]] * k
    for i in range(1, k):
        highest_products[i] = max(highest_products[i-1] * nums[i]
        lowest_products[i] = lowest_products[i-1] * nums[i]
        highest_products[0] = max(highest_products[0], nums[i])
        lowest_products[0] = min(lowest_products[0], nums[i])
    print highest_products
    print lowest_products

if __name__ == '__main__':
    import doctest
    doctest.testmod()