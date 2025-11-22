"""
Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

def maxArea(height):
  
  """
  :type height: List[int]
  :rtype: int
  """
  
  # Initialize pointers at both ends of the array
  left = 0
  right = len(height) - 1
  max_water = 0
  
  while left < right:
      # The height of the container is limited by the shorter line
      current_height = min(height[left], height[right])
      current_width = right - left
      
      # Calculate area and update max_water if this is the new best
      current_area = current_height * current_width
      max_water = max(max_water, current_area)
      
      # CRITICAL STEP: Move the pointer of the shorter line inward.
      # We discard the shorter line because it limits the height.
      if height[left] < height[right]:
          left += 1
      else:
          right -= 1
          
  return max_water

height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height)) 