"""
Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
"""


def nextPermutation(nums):

    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    n = len(nums)
    
    # Edge case: arrays with 0 or 1 element have no next permutation
    if n <= 1:
        return
    
    # =====================================================================
    # STEP 1: Find the pivot
    # =====================================================================
    # Traverse from right to left to find the first element that breaks
    # the descending order (i.e., nums[i] < nums[i + 1])
    # This element needs to be replaced with a slightly larger element
    # to get the next permutation
    i = n - 2  # Start from second-to-last element
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # If i == -1, the entire array is in descending order (largest permutation)
    # We just need to reverse to get the smallest permutation
    
    if i >= 0:
        # =================================================================
        # STEP 2: Find the successor (smallest element greater than pivot)
        # =================================================================
        # Traverse from right to find the first element greater than nums[i]
        # Since the right portion is in descending order, the first element
        # we find that is greater than nums[i] is the smallest such element
        j = n - 1
        while j > i and nums[j] <= nums[i]:
            j -= 1
        
        # =================================================================
        # STEP 3: Swap pivot with successor
        # =================================================================
        # After this swap, nums[i] is replaced with the next larger value
        # The portion after i is still in descending order
        nums[i], nums[j] = nums[j], nums[i]
    
    # =====================================================================
    # STEP 4: Reverse the suffix
    # =====================================================================
    # The elements after index i are in descending order
    # Reverse them to get the smallest possible arrangement (ascending order)
    # This gives us the lexicographically smallest suffix
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# Example usage and test cases
# Test case 1: Normal case
test1 = [1, 2, 3]
nextPermutation(test1)
print(f"[1,2,3] -> {test1}")  # Expected: [1, 3, 2]

# Test case 2: Descending order (wrap around)
test2 = [3, 2, 1]
nextPermutation(test2)
print(f"[3,2,1] -> {test2}")  # Expected: [1, 2, 3]

# Test case 3: With duplicates
test3 = [1, 1, 5]
nextPermutation(test3)
print(f"[1,1,5] -> {test3}")  # Expected: [1, 5, 1]

# Test case 4: Larger example
test4 = [1, 5, 8, 4, 7, 6, 5, 3, 1]
nextPermutation(test4)
print(f"[1,5,8,4,7,6,5,3,1] -> {test4}")  # Expected: [1, 5, 8, 5, 1, 3, 4, 6, 7]