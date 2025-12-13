"""
Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
"""

def removeElement(nums, val):
  
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    
    # Initialize 'k', which acts as our "Writer" pointer.
    # It keeps track of the position where the NEXT valid number should be placed.
    # It also serves as the counter for how many valid elements we have found.
    k = 0
    
    # Start a loop 'i' that acts as our "Reader" pointer.
    # It scans through every single element in the array from start to finish.
    for i in range(len(nums)):
        
        # Check the current number the Reader 'i' is looking at.
        # If nums[i] is NOT the value we want to remove, it means we want to keep it.
        if nums[i] != val:
            
            # Copy the valid number from position 'i' to position 'k'.
            # Note: If i and k are the same (at the start), this just overwrites
            # the number with itself, which is harmless.
            nums[k] = nums[i]
            
            # Move the Writer 'k' forward one slot.
            # This prepares 'k' to receive the next valid number we find.
            k += 1
        
        # If nums[i] WAS equal to 'val', we do nothing in this iteration.
        # The loop simply continues to the next 'i'.
        # Because we didn't increment 'k', that position stays waiting 
        # for a valid number to overwrite the unwanted 'val'
    # After the loop finishes, 'k' holds the count of valid elements.
    # The first 'k' elements of the array are now the correct numbers.
    return k

nums = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))