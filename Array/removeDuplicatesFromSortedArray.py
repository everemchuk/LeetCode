"""
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.
Consider the number of unique elements in nums to be k.
After removing duplicates, return the number of unique elements k.
"""

def removeDuplicates(nums):
  
  """
  :type nums: List[int]
  :rtype: int
  """

  # Edge case: If the array is empty, there are 0 unique elements
  if not nums:
      return 0
  
  # Initialize the insert pointer 'k'.
  # We start at 1 because the first element (index 0) is always unique 
  # and doesn't need to move.
  k = 1
  start = 1 
  
  # Loop through the array starting from the second element (index 1)
  # 'i' acts as our scanner pointer.
  for i in range(start, len(nums)):
      
      # Check if the current element is different from the previous one.
      # Since the array is sorted, this indicates a new unique value.
      if nums[i] != nums[i - 1]:
          
          # If unique, place it at the current insert position 'k'
          nums[k] = nums[i]
          
          # Move the insert position forward to be ready for the next unique number
          k += 1
  
  # Return 'k', which represents the count of unique elements.
  # It also serves as the index where the non-unique (junk) data starts.
  return k

nums = [0,0,1,1,1,2,2,3,3,4]

print(removeDuplicates(nums))