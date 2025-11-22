"""
Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
"""

def longestCommonPrefix(strs):
    
    """
    :type strs: List[str]
    :rtype: str
    """
    
    # Safety Check: If the list is empty [], return empty string ""
    if not strs:
        return ""
        
    # Initialization: Assume the first string is the prefix
    prefix = strs[0]
    
    # Loop through the list, starting from the SECOND string (index 1)
    # We start at 1 because we don't need to compare the first string to itself.
    for s in strs[1:]:
        
        # The 'While' Loop: 
        # As long as the current string 's' does NOT start with our 'prefix'...
        while not s.startswith(prefix):
            
            # Shorten the prefix
            # prefix[:-1] means "take the string from start up to the last char"
            # Effectively, this deletes the last character.
            prefix = prefix[:-1]
            
            # Emergency Exit
            # If we shortened the prefix so much it became empty, 
            # it means there is no common prefix at all.
            if not prefix:
                return ""
    
    # Return whatever is left of the prefix
    return prefix

test_list = ["flower", "flow", "flight"]

print(longestCommonPrefix(test_list))  # Output: "fl"



