def get_products_of_all_ints_except_at_index(nums):
    """
    Given a list of numbers, return a list of products of the rest of the
    numbers other than the number at that index (without using division).
    >>> get_products_of_all_ints_except_at_index([1, 7, 3, 4])
    [84, 12, 28, 21]
    """

    results = []
    for i in range(len(nums)):
        current_product = 1
        for j, num2 in enumerate(nums): 
            if i != j:
                current_product = current_product * num2
        results.append(current_product)
    return results

def get_products_of_all_ints_except_at_index_optimized(nums):
    """
    Given a list of numbers, return a list of products of the rest of the
    numbers other than the number at that index (without using division).
    >>> get_products_of_all_ints_except_at_index_optimized([1, 7, 3, 4])
    [84, 12, 28, 21]
    """

    results = []
    product_before_index = 1
    for i, num in enumerate(nums):
        product_after_index = 1
        for j, num2 in enumerate(nums):
            if j > i:
                product_after_index *= num2
        results.append(product_after_index * product_before_index)
        product_before_index = product_before_index * num
    return results

def get_products_of_all_ints_except_at_index_optimized2(nums):
    """
    Given a list of numbers, return a list of products of the rest of the
    numbers other than the number at that index (without using division).
    >>> get_products_of_all_ints_except_at_index_optimized2([1, 7, 3, 4])
    [84, 12, 28, 21]
    >>> get_products_of_all_ints_except_at_index_optimized2([1, 7, 0, 4])
    [0, 0, 28, 0]
    >>> get_products_of_all_ints_except_at_index_optimized2([5, 7])
    [7, 5]
    >>> get_products_of_all_ints_except_at_index_optimized2([3])
    [1]
    """

    results = [None] * len(nums)
    current_product = 1
    for i in xrange(len(nums)):
        results[i] = current_product
        current_product *= nums[i]
    current_product2 = 1
    j = len(nums) - 1
    while j >= 0:
        results[j] *= current_product2
        current_product2 *= nums[j]
        j -= 1
    return results



if __name__ == '__main__':
    import doctest
    doctest.testmod()