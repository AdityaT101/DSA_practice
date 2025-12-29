"""
SLIDING WINDOW - VARIABLE WINDOW SIZE
======================================
Complete solutions for all LeetCode problems under Pattern 2B

Pattern Template:
-----------------
left = 0
window_state = initialize()

for right in range(len(array)):
    # Expand window
    add element at right to window_state
    
    # Contract window while condition violated
    while window is invalid:
        remove element at left from window_state
        left += 1
    
    # Update result with current valid window
    update_result(right - left + 1)

Time Complexity: O(n) - each element visited at most twice
Space Complexity: O(k) - for tracking window contents
"""

# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 1: LeetCode 209 - Minimum Size Subarray Sum
# ============================================================================

"""
Problem:
--------
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is >= target.
If no such subarray exists, return 0.

Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: [4,3] has minimal length with sum >= 7

Example 2:
Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:
Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

Constraints:
- 1 <= target <= 10^9
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
"""

def minSubArrayLen(target, nums):
    """
    Approach: Variable sliding window
    
    Key Insight:
    - We want to find the SMALLEST subarray whose sum is >= target
    - Start with an empty window and keep expanding it to the right
    - As soon as the window sum becomes >= target, we have a valid window
    - Now try to SHRINK the window from the left to make it even smaller
    - Keep shrinking while the sum is still >= target (window is still valid)
    - Record the smallest valid window length we find during this process
    - The key is: expand to find valid windows, contract to minimize them
    
    Time: O(n) - each element visited at most twice
    Space: O(1)
    """
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(nums)):
        # Expand window: add right element
        current_sum += nums[right]
        
        # Contract window: while condition is met, try to shrink
        while current_sum >= target:
            # Update result before shrinking
            min_length = min(min_length, right - left + 1)
            
            # Shrink from left
            current_sum -= nums[left]
            left += 1
    
    # Return 0 if no valid subarray found
    return min_length if min_length != float('inf') else 0


# Test cases
print("=" * 70)
print("Problem 1: LeetCode 209 - Minimum Size Subarray Sum")
print("=" * 70)
test_cases_209 = [
    (7, [2,3,1,2,4,3]),
    (4, [1,4,4]),
    (11, [1,1,1,1,1,1,1,1]),
    (15, [1,2,3,4,5])
]

for target, nums in test_cases_209:
    result = minSubArrayLen(target, nums)
    print(f"Target: {target}, Nums: {nums}")
    print(f"Result: {result}\n")


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 2: LeetCode 3 - Longest Substring Without Repeating Characters
# ============================================================================

"""
Problem:
--------
Given a string s, find the length of the longest substring without 
repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: "b" is the longest substring

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: "wke" is the longest substring

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces
"""

def lengthOfLongestSubstring(s):
    """
    Approach: Variable sliding window with hash set
    
    Key Insight:
    - We want to find the LONGEST substring with NO repeating characters
    - Use a set to remember which characters are currently in our window
    - Keep expanding the window to the right by adding new characters
    - If we encounter a character that's already in the window (duplicate!),
      we need to shrink the window from the left until the duplicate is removed
    - Once the duplicate is gone, the window is valid again
    - Track the maximum valid window length we see throughout this process
    - The key is: expand to grow the window, contract when duplicates appear
    
    Time: O(n) - each character visited at most twice
    Space: O(min(n, m)) where m is charset size
    """
    left = 0
    char_set = set()
    max_length = 0
    
    for right in range(len(s)):
        # Contract window: remove duplicates from left
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Expand window: add right character
        char_set.add(s[right])
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Alternative solution using hash map (tracks last seen index)
def lengthOfLongestSubstring_v2(s):
    """
    Optimized approach using hash map to store last seen index.
    Can skip directly to position after duplicate.
    
    Time: O(n)
    Space: O(min(n, m))
    """
    char_index = {}  # char -> last seen index
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character seen and is in current window
        if s[right] in char_index and char_index[s[right]] >= left:
            # Move left to position after last occurrence
            left = char_index[s[right]] + 1
        
        # Update last seen index
        char_index[s[right]] = right
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
print("=" * 70)
print("Problem 2: LeetCode 3 - Longest Substring Without Repeating Characters")
print("=" * 70)
test_cases_3 = ["abcabcbb", "bbbbb", "pwwkew", "", "au", "dvdf"]

for s in test_cases_3:
    result1 = lengthOfLongestSubstring(s)
    result2 = lengthOfLongestSubstring_v2(s)
    print(f"String: '{s}'")
    print(f"Result (v1): {result1}, Result (v2): {result2}\n")


# ============================================================================
# PROBLEM 3: LeetCode 340 - Longest Substring with At Most K Distinct Characters
# ============================================================================

"""
Problem:
--------
Given a string s and an integer k, return the length of the longest 
substring of s that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: "ece" has 2 distinct characters

Example 2:
Input: s = "aa", k = 1
Output: 2

Constraints:
- 1 <= s.length <= 5 * 10^4
- 0 <= k <= 50
"""

def lengthOfLongestSubstringKDistinct(s, k):
    """
    Approach: Variable sliding window with hash map
    
    Key Insight:
    - We want the LONGEST substring that has AT MOST k different characters
    - Use a hashmap to count how many times each character appears in the window
    - Keep expanding the window to the right, adding new characters
    - The number of keys in the hashmap tells us how many distinct characters we have
    - If distinct characters exceed k, the window becomes invalid
    - Shrink the window from the left until we have exactly k distinct characters again
    - When removing a character completely (count becomes 0), delete it from hashmap
    - Track the maximum valid window length throughout this process
    - The key is: expand freely, contract when we have too many distinct characters
    
    Time: O(n)
    Space: O(k) - at most k+1 distinct characters in map
    """
    if k == 0:
        return 0
    
    left = 0
    char_count = {}
    max_length = 0
    
    for right in range(len(s)):
        # Expand window: add right character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Contract window: while too many distinct characters
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
print("=" * 70)
print("Problem 3: LeetCode 340 - Longest Substring with At Most K Distinct")
print("=" * 70)
test_cases_340 = [
    ("eceba", 2),
    ("aa", 1),
    ("abaccc", 2),
    ("a", 1),
    ("", 2)
]

for s, k in test_cases_340:
    result = lengthOfLongestSubstringKDistinct(s, k)
    print(f"String: '{s}', k: {k}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 4A: LeetCode 485 - Max Consecutive Ones I
# ============================================================================

"""
Problem:
--------
Given a binary array nums, return the maximum number of consecutive 1's 
in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
"""

def findMaxConsecutiveOnes(nums):
    """
    Approach: Simple iteration (or sliding window with k=0)
    
    Key Insight:
    - We want to find the LONGEST sequence of consecutive 1's (no flips allowed)
    - Simple approach: keep a running count of consecutive 1's
    - Every time we see a 1, increment the count
    - Every time we see a 0, reset the count back to 0 (sequence broken)
    - Track the maximum count we've seen throughout the entire array
    - Alternative view: this is a sliding window with k=0 (zero flips allowed)
    - The key is: count while you see 1's, reset when you hit a 0
    
    Time: O(n)
    Space: O(1)
    """
    max_count = 0
    current_count = 0
    
    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    
    return max_count


# Alternative: Using sliding window approach
def findMaxConsecutiveOnes_SlidingWindow(nums):
    """
    Sliding window approach (k=0 flips allowed)
    """
    left = 0
    zero_count = 0
    max_length = 0
    k = 0  # No flips allowed
    
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
print("=" * 70)
print("Problem 4A: LeetCode 485 - Max Consecutive Ones I")
print("=" * 70)
test_cases_485 = [
    [1,1,0,1,1,1],
    [1,0,1,1,0,1],
    [1,1,1,1],
    [0,0,0,0],
    [1]
]

for nums in test_cases_485:
    result = findMaxConsecutiveOnes(nums)
    print(f"Nums: {nums}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 4B: LeetCode 487 - Max Consecutive Ones II
# ============================================================================

"""
Problem:
--------
Given a binary array nums, return the maximum number of consecutive 1's 
in the array if you can flip at most one 0.

Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the maximum number of consecutive 1s.
After flipping, the maximum number of consecutive 1s is 4.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation: Flip either the first or second zero to get 4 consecutive 1s.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1

Follow-up: What if the input numbers come in one by one as an infinite stream?
"""

def findMaxConsecutiveOnes_II(nums):
    """
    Approach: Variable sliding window with k=1
    
    Key Insight:
    - We can flip AT MOST 1 zero to become a 1, so we're looking for the
      LONGEST subarray that contains at most 1 zero (we'll flip that zero)
    - Keep track of how many zeros are currently in our window
    - Keep expanding the window to the right, adding elements
    - If we encounter a zero, increment our zero count
    - If zero count exceeds 1 (we have more than 1 zero), the window is invalid
    - Shrink the window from the left until we have at most 1 zero again
    - Track the maximum valid window length (this is our answer)
    - The key is: we can tolerate 1 zero, but if we get a 2nd zero, we must shrink
    
    Time: O(n)
    Space: O(1)
    """
    left = 0
    zero_count = 0
    max_length = 0
    k = 1  # Can flip at most 1 zero
    
    for right in range(len(nums)):
        # Expand window: add right element
        if nums[right] == 0:
            zero_count += 1
        
        # Contract window: while too many zeros
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Alternative: Track last zero position (for follow-up)
def findMaxConsecutiveOnes_II_Stream(nums):
    """
    Optimized for streaming: Track position of last zero
    
    This approach works well for infinite streams because
    we only need to track one previous zero position.
    """
    max_length = 0
    left = 0
    last_zero_index = -1
    
    for right in range(len(nums)):
        if nums[right] == 0:
            # Move left to position after the last zero
            left = last_zero_index + 1
            last_zero_index = right
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
print("=" * 70)
print("Problem 4B: LeetCode 487 - Max Consecutive Ones II")
print("=" * 70)
test_cases_487 = [
    [1,0,1,1,0],
    [1,0,1,1,0,1],
    [1,1,1,1],
    [0,0,0,0],
    [0,1,1,0,1],
    [1,1,0,0,1,1,1]
]

for nums in test_cases_487:
    result = findMaxConsecutiveOnes_II(nums)
    print(f"Nums: {nums}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 4C: LeetCode 1004 - Max Consecutive Ones III
# ============================================================================

"""
Problem:
--------
Given a binary array nums and an integer k, return the maximum number of 
consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: Flip the two 0's at indices 4 and 10

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: Flip 0's at indices 4, 5, and 9

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
- 0 <= k <= nums.length
"""

def longestOnes(nums, k):
    """
    Approach: Variable sliding window
    
    Key Insight:
    - We can flip AT MOST k zeros to become 1's, so we're looking for the
      LONGEST subarray that contains at most k zeros (we'll flip all those zeros)
    - This is a generalization of the previous problem (k=1 becomes k=any number)
    - Keep track of how many zeros are currently in our window
    - Keep expanding the window to the right, adding elements
    - If we encounter a zero, increment our zero count
    - If zero count exceeds k (we have more than k zeros), the window is invalid
    - Shrink the window from the left until we have at most k zeros again
    - Track the maximum valid window length (this is our answer)
    - The key is: we can tolerate k zeros, but if we get the (k+1)th zero, we must shrink
    
    Time: O(n)
    Space: O(1)
    """
    left = 0
    zero_count = 0
    max_length = 0
    
    for right in range(len(nums)):
        # Expand window: add right element
        if nums[right] == 0:
            zero_count += 1
        
        # Contract window: while too many zeros
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
print("=" * 70)
print("Problem 4C: LeetCode 1004 - Max Consecutive Ones III")
print("=" * 70)
test_cases_1004 = [
    ([1,1,1,0,0,0,1,1,1,1,0], 2),
    ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3),
    ([1,1,1,1], 0),
    ([0,0,0,0], 2)
]

for nums, k in test_cases_1004:
    result = longestOnes(nums, k)
    print(f"Nums: {nums}, k: {k}")
    print(f"Result: {result}\n")


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 5: LeetCode 76 - Minimum Window Substring
# ============================================================================

"""
Problem:
--------
Given two strings s and t, return the minimum window substring of s such 
that every character in t (including duplicates) is included in the window.
If no such substring exists, return "".

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: "BANC" is the minimum window containing A, B, C

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""

Constraints:
- 1 <= s.length, t.length <= 10^5
- s and t consist of uppercase and lowercase English letters
"""

def minWindow(s, t):
    """
    Approach: Variable sliding window with two hash maps
    
    Key Insight:
    - We want the SMALLEST substring in s that contains ALL characters from t
    - Use two hashmaps: one for what we NEED (from t), one for what we HAVE (current window)
    - Use a counter to track how many unique characters have been satisfied
    - Keep expanding the window to the right, adding characters
    - When a character's count in window matches its required count, increment satisfied counter
    - Once all characters are satisfied (formed == required), we have a valid window
    - Now try to SHRINK from the left to make the window smaller while keeping it valid
    - Record the smallest valid window we find
    - When shrinking causes a character to drop below its requirement, stop shrinking
    - The key is: expand until valid, then shrink to minimize, repeat
    
    Time: O(|s| + |t|)
    Space: O(|s| + |t|)
    """
    if not s or not t:
        return ""
    
    # Count characters needed from t
    target_count = {}
    for char in t:
        target_count[char] = target_count.get(char, 0) + 1
    
    required = len(target_count)  # Number of unique chars in t
    formed = 0  # Number of unique chars in window with desired frequency
    
    # Window character counts
    window_count = {}
    
    # Result: (window_length, left, right)
    result = float('inf'), 0, 0
    
    left = 0
    
    for right in range(len(s)):
        # Expand window: add character from right
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if frequency of current char matches desired count
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1
        
        # Contract window: while all characters are satisfied
        while formed == required and left <= right:
            # Update result if current window is smaller
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            # Remove character from left
            char = s[left]
            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed -= 1
            
            left += 1
    
    # Return empty string if no valid window found
    return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]


# Test cases
print("=" * 70)
print("Problem 5: LeetCode 76 - Minimum Window Substring")
print("=" * 70)
test_cases_76 = [
    ("ADOBECODEBANC", "ABC"),
    ("a", "a"),
    ("a", "aa"),
    ("ab", "b"),
    ("abc", "cba")
]

for s, t in test_cases_76:
    result = minWindow(s, t)
    print(f"s: '{s}', t: '{t}'")
    print(f"Result: '{result}'\n")


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 6: LeetCode 424 - Longest Repeating Character Replacement
# ============================================================================

"""
Problem:
--------
You are given a string s and an integer k. You can choose any character 
of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter 
you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with 'B's or vice versa

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace one 'A' in the middle with 'B', "AABBBBA"

Constraints:
- 1 <= s.length <= 10^5
- s consists of only uppercase English letters
- 0 <= k <= s.length
"""

def characterReplacement(s, k):
    """
    Approach: Variable sliding window with frequency map
    
    Key Insight:
    - We want the LONGEST substring where we can make all characters the same by replacing at most k characters
    - Key formula: window_length - max_frequency = number of replacements needed
    - If (window_length - max_frequency) <= k, the window is valid (we have enough replacements)
    - Example: window "AABBA" has length 5, max_frequency is 3 (three A's)
      So we need 5 - 3 = 2 replacements to make all A's. If k >= 2, it's valid!
    - Track character frequencies in the current window using a hashmap
    - Track the maximum frequency of any single character in the window
    - Keep expanding the window to the right
    - If replacements needed exceeds k, shrink from the left
    - The key is: maximize the dominant character's count, replace the rest
    
    Time: O(n)
    Space: O(26) = O(1) for uppercase letters
    """
    left = 0
    char_count = {}
    max_frequency = 0
    max_length = 0
    
    for right in range(len(s)):
        # Expand window: add right character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Update max frequency in current window
        max_frequency = max(max_frequency, char_count[s[right]])
        
        # Contract window: if replacements needed > k
        # window_length - max_frequency = replacements needed
        while (right - left + 1) - max_frequency > k:
            char_count[s[left]] -= 1
            left += 1
            # Note: We don't need to update max_frequency when shrinking
            # because we only care about finding a larger window
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
print("=" * 70)
print("Problem 6: LeetCode 424 - Longest Repeating Character Replacement")
print("=" * 70)
test_cases_424 = [
    ("ABAB", 2),
    ("AABABBA", 1),
    ("AAAA", 0),
    ("ABBB", 2),
    ("ABCDE", 1)
]

for s, k in test_cases_424:
    result = characterReplacement(s, k)
    print(f"s: '{s}', k: {k}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 7: LeetCode 904 - Fruit Into Baskets
# ============================================================================

"""
Problem:
--------
You are visiting a farm that has a single row of fruit trees. The trees 
are represented by an integer array fruits where fruits[i] is the type 
of fruit the ith tree produces.

You want to collect as much fruit as possible. However, you only have 
two baskets, and each basket can only hold a single type of fruit.

Starting from any tree, you must pick exactly one fruit from every tree 
(including the start tree) while moving to the right. The picked fruits 
must fit in one of your baskets.

Return the maximum number of fruits you can pick.

Example 1:
Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees

Example 2:
Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2]

Example 3:
Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2]

Constraints:
- 1 <= fruits.length <= 10^5
- 0 <= fruits[i] < fruits.length
"""

def totalFruit(fruits):
    """
    Approach: Variable sliding window (same as longest substring with at most 2 distinct)
    
    Key Insight:
    - This problem is actually "find the LONGEST subarray with at most 2 distinct elements"
    - You have 2 baskets, so you can only collect 2 different types of fruits
    - We want to maximize the number of fruits collected (longest subarray)
    - Use a hashmap to track how many of each fruit type is in the current window
    - Keep expanding the window to the right, adding fruits
    - If we encounter a 3rd distinct fruit type, the window becomes invalid
    - Shrink the window from the left until we're back to 2 distinct fruit types
    - Track the maximum window length (maximum fruits collected)
    - The key is: you can have at most 2 types, so shrink when you get a 3rd type
    
    Time: O(n)
    Space: O(1) - at most 3 fruit types in map
    """
    left = 0
    fruit_count = {}
    max_fruits = 0
    
    for right in range(len(fruits)):
        # Expand window: add right fruit
        fruit_count[fruits[right]] = fruit_count.get(fruits[right], 0) + 1
        
        # Contract window: while more than 2 distinct fruits
        while len(fruit_count) > 2:
            fruit_count[fruits[left]] -= 1
            if fruit_count[fruits[left]] == 0:
                del fruit_count[fruits[left]]
            left += 1
        
        # Update result
        max_fruits = max(max_fruits, right - left + 1)
    
    return max_fruits


# Test cases
print("=" * 70)
print("Problem 7: LeetCode 904 - Fruit Into Baskets")
print("=" * 70)
test_cases_904 = [
    [1,2,1],
    [0,1,2,2],
    [1,2,3,2,2],
    [3,3,3,1,2,1,1,2,3,3,4]
]

for fruits in test_cases_904:
    result = totalFruit(fruits)
    print(f"Fruits: {fruits}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 8: LeetCode 1658 - Minimum Operations to Reduce X to Zero
# ============================================================================

"""
Problem:
--------
You are given an integer array nums and an integer x. In one operation, 
you can either remove the leftmost or the rightmost element from the 
array nums and subtract its value from x.

Return the minimum number of operations to reduce x to exactly 0 if it 
is possible, otherwise, return -1.

Example 1:
Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: Remove last two elements [2,3]

Example 2:
Input: nums = [5,6,7,8,9], x = 4
Output: -1

Example 3:
Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
Explanation: Remove [3,2] from left and [1,1,3] from right

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= x <= 10^9
"""

def minOperations(nums, x):
    """
    Approach: Variable sliding window (reverse thinking)
    
    Key Insight:
    - This is a REVERSE THINKING problem - don't think about what to remove!
    - If we remove elements from edges that sum to x, the middle elements sum to (total - x)
    - So instead: find the LONGEST subarray in the middle that sums to (total - x)
    - The longer the middle subarray, the fewer elements we remove from edges
    - Example: nums = [1,1,4,2,3], x = 5, total = 11
      We want middle to sum to 11-5=6. Longest is [1,4] or [4,2] (length 2)
      So we remove 5-2=3 elements from edges
    - Use sliding window to find the longest subarray with sum = (total - x)
    - Answer = array_length - longest_middle_subarray_length
    - The key is: maximize what you KEEP in the middle, minimize what you REMOVE from edges
    
    Time: O(n)
    Space: O(1)
    """
    target = sum(nums) - x
    
    # Edge case: need to remove all elements
    if target == 0:
        return len(nums)
    
    # Edge case: impossible
    if target < 0:
        return -1
    
    left = 0
    current_sum = 0
    max_length = -1
    
    for right in range(len(nums)):
        # Expand window: add right element
        current_sum += nums[right]
        
        # Contract window: while sum > target
        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1
        
        # Update result if sum equals target
        if current_sum == target:
            max_length = max(max_length, right - left + 1)
    
    # If no valid subarray found, return -1
    return -1 if max_length == -1 else len(nums) - max_length


# Test cases
print("=" * 70)
print("Problem 8: LeetCode 1658 - Minimum Operations to Reduce X to Zero")
print("=" * 70)
test_cases_1658 = [
    ([1,1,4,2,3], 5),
    ([5,6,7,8,9], 4),
    ([3,2,20,1,1,3], 10),
    ([1,1], 3),
    ([8,1,1,1,1], 5)
]

for nums, x in test_cases_1658:
    result = minOperations(nums, x)
    print(f"Nums: {nums}, x: {x}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 9: LeetCode 1695 - Maximum Erasure Value
# ============================================================================

"""
Problem:
--------
You are given an array of positive integers nums and want to erase a 
subarray containing unique elements. The score you get by erasing the 
subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

Example 1:
Input: nums = [4,2,4,5,6]
Output: 17
Explanation: [2,4,5,6] has sum 17

Example 2:
Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: [5,2,1] or [1,2,5] has sum 8

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
"""

def maximumUniqueSubarray(nums):
    """
    Approach: Variable sliding window with hash set
    
    Key Insight:
    - We want the subarray with UNIQUE elements that has the MAXIMUM sum
    - This is similar to "longest substring without repeating characters" but we track sum instead of length
    - Use a set to remember which numbers are currently in our window
    - Keep expanding the window to the right, adding elements and their values to the sum
    - If we encounter a duplicate (number already in the set), the window becomes invalid
    - Shrink the window from the left until the duplicate is removed
    - Keep track of the current window sum and update the maximum sum seen
    - The key is: expand to grow the sum, contract when duplicates appear
    
    Time: O(n)
    Space: O(n)
    """
    left = 0
    num_set = set()
    current_sum = 0
    max_sum = 0
    
    for right in range(len(nums)):
        # Contract window: remove duplicates from left
        while nums[right] in num_set:
            num_set.remove(nums[left])
            current_sum -= nums[left]
            left += 1
        
        # Expand window: add right element
        num_set.add(nums[right])
        current_sum += nums[right]
        
        # Update result
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Test cases
print("=" * 70)
print("Problem 9: LeetCode 1695 - Maximum Erasure Value")
print("=" * 70)
test_cases_1695 = [
    [4,2,4,5,6],
    [5,2,1,2,5,2,1,2,5],
    [1,2,3,4,5],
    [1,1,1,1]
]

for nums in test_cases_1695:
    result = maximumUniqueSubarray(nums)
    print(f"Nums: {nums}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 10: LeetCode 1493 - Longest Subarray of 1's After Deleting One Element
# ============================================================================

"""
Problem:
--------
Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's 
in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: Delete 0, get [1,1,1]

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: Delete 0 at index 4, get [0,1,1,1,1,1,0,1]

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: Must delete one element

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
"""

def longestSubarray(nums):
    """
    Approach: Variable sliding window
    
    Key Insight:
    - We MUST delete exactly one element from the array (this is required!)
    - After deletion, we want the longest possible subarray of 1's
    - Strategy: find the longest subarray with at most 1 zero (we'll delete that zero)
    - This is similar to "Max Consecutive Ones II" but with a twist
    - The twist: we MUST delete one element, so answer = window_length - 1
    - If the array is all 1's (no zeros), we still must delete one 1
    - If we have a zero in the window, we delete it; if no zero, we delete a 1
    - Use sliding window to find longest subarray with at most 1 zero
    - The key is: tolerate at most 1 zero, then subtract 1 for the required deletion
    
    Time: O(n)
    Space: O(1)
    """
    left = 0
    zero_count = 0
    max_length = 0
    
    for right in range(len(nums)):
        # Expand window: add right element
        if nums[right] == 0:
            zero_count += 1
        
        # Contract window: while more than 1 zero
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        
        # Update result (subtract 1 because we must delete one element)
        max_length = max(max_length, right - left)
    
    return max_length


# Test cases
print("=" * 70)
print("Problem 10: LeetCode 1493 - Longest Subarray After Deleting One Element")
print("=" * 70)
test_cases_1493 = [
    [1,1,0,1],
    [0,1,1,1,0,1,1,0,1],
    [1,1,1],
    [0,0,0],
    [1,0,1,1,0,1]
]

for nums in test_cases_1493:
    result = longestSubarray(nums)
    print(f"Nums: {nums}")
    print(f"Result: {result}\n")

# *** please discard the problme no for below problem.it been imported from 'string_manipulation_pattern_match'
# ============================================================================
# PROBLEM 12: LeetCode 395 - Longest Substring with At Least K Repeating (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a string s and an integer k, return the length of the longest substring 
of s such that the frequency of each character in this substring is greater 
than or equal to k.

Example 1:
Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:
Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:
- 1 <= s.length <= 10^4
- s consists of only lowercase English letters
- 1 <= k <= 10^5
"""


def longestSubstring(arr, k):
    """
    Approach: Divide and Conquer

    Key Insight:
    - If a character appears less than k times in entire string, it can't be in valid substring
    - Use such characters as split points
    - Recursively check each split segment
    - Base case: if all characters appear >= k times, return length

    Why Divide and Conquer?
    - Sliding window doesn't work well here (hard to maintain constraint)
    - Characters with freq < k act as "invalid" separators
    - Split string by invalid characters
    - Recursively find longest in each segment

    Algorithm:
    1. Count frequency of all characters
    2. If all chars have freq >= k, return len(s)
    3. Find first character with freq < k
    4. Split string by this character
    5. Recursively check each segment
    6. Return maximum length found

    Alternative:
    - Sliding window with 26 iterations (one for each unique char count)
    - For each target unique count, find longest substring

    Pattern Recognition:
    - "at least k repeating" → frequency checking
    - "longest substring" → divide and conquer or sliding window
    - Characters with low freq split the string

    Time: O(n) average, O(n²) worst case
    Space: O(n) for recursion stack
    """
    if len(arr) < k:
        return 0

    hmap = {}
    i = 0
    left = 0
    right = 0
    max_length = 0

    while (i < len(arr)):
        hmap[arr[i]] = hmap.get(arr[i], 0) + 1
        i += 1

    while (right < len(arr)):
        if hmap[arr[right]] >= k:
            max_length = max(max_length, right + 1 - left)
        elif hmap[arr[right]] < k:
            left = right + 1

        right += 1

    return max_length


# Test cases
print("\n" + "=" * 70)
print("Problem 11: LeetCode 395 - Longest Substring At Least K Repeating")
print("=" * 70)

test_cases_395 = [
    ("aaabb", 3, 3),
    ("ababbc", 2, 5),
    ("a", 1, 1),
    ("aaabbb", 3, 6)
]

for s, k, expected in test_cases_395:
    result = longestSubstring(s, k)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', k={k} → {result} (expected: {expected}) {status}")


# ============================================================================
# SUMMARY & PATTERN RECOGNITION
# ============================================================================

"""
VARIABLE WINDOW SIZE - PATTERN RECOGNITION:
===========================================

When to Use Variable Window:
----------------------------
✓ "Longest/shortest subarray/substring with condition"
✓ "At most K" or "At least K" constraints
✓ "Minimum/maximum length"
✓ Need to find optimal window size

Key Characteristics:
-------------------
1. Window size changes dynamically
2. Two pointers: left and right
3. Right always moves forward
4. Left moves when condition violated
5. Each element visited at most twice → O(n)

Template Structure:
------------------
left = 0
state = initialize()

for right in range(n):
    # 1. Expand: add right element to window
    update_state(right)
    
    # 2. Contract: shrink while invalid
    while window_invalid(state):
        remove_left_element()
        left += 1
    
    # 3. Update: record result
    update_result(right - left + 1)

Common Variations:
-----------------
1. Track with Set: Unique elements (LC 3, 1695)
2. Track with Map: Frequencies/counts (LC 76, 340, 424)
3. Track with Counter: Specific element count (LC 1004, 1493)
4. Reverse Thinking: Find complement (LC 1658)

Problem Categories:
------------------
1. Unique Elements: LC 3, 1695
2. K Distinct: LC 340, 904
3. K Replacements: LC 1004, 424, 1493
4. Contains All: LC 76
5. Sum-based: LC 209, 1658

Time Complexity: O(n) for all
Space Complexity: O(1) to O(k) depending on tracking needs

NOTE: Fixed Window Size Problems
---------------------------------
The following problems use FIXED window size and have been moved to:
'sliding_window_fixed_solutions.py'

- LC 438: Find All Anagrams in a String
- LC 567: Permutation in String  
- LC 30:  Substring with Concatenation of All Words

These use a different template (fixed size) rather than variable expansion/contraction.
"""

# HIGHEST FREQUENCY (Must Know for Interviews) - FAANG HARD PROBLEMS
# ============================================================================
# PROBLEM 11: LeetCode 992 - Subarrays with K Different Integers
# ============================================================================

"""
Problem:
--------
Given an integer array nums and an integer k, return the number of good 
subarrays of nums.

A good array is an array where the number of different integers in that 
array is exactly k.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays with exactly 2 distinct integers:
[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: [1,2,1,3], [2,1,3], [1,3,4]

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i], k <= nums.length
"""

def subarraysWithKDistinct(nums, k):
    """
    Approach: Sliding window with mathematical transformation
    
    Key Insight:
    - "Exactly K distinct" is HARD to track directly with sliding window
    - But "At Most K distinct" is EASY (we already know this pattern!)
    - Mathematical trick: Exactly K = (At Most K) - (At Most K-1)
    - Example: nums = [1,2,1,2,3], k = 2
      - At Most 2: [1], [1,2], [2], [1], [1,2], [2], [2,3], [1,2,1], [2,1], [1,2,1,2], [2,1,2], [1,2,1,2,3] = many
      - At Most 1: [1], [2], [1], [2], [3] = 5
      - Exactly 2 = At Most 2 - At Most 1
    - Create a helper function for "at most K distinct"
    - The key is: transform "exactly K" into difference of two "at most K" problems
    
    Time: O(n)
    Space: O(k)
    """
    
    def atMostK(k):
        """Helper: Count subarrays with at most K distinct integers"""
        if k == 0:
            return 0
        
        left = 0
        count_map = {}
        result = 0
        
        for right in range(len(nums)):
            # Expand window: add right element
            count_map[nums[right]] = count_map.get(nums[right], 0) + 1
            
            # Contract window: while more than k distinct
            while len(count_map) > k:
                count_map[nums[left]] -= 1
                if count_map[nums[left]] == 0:
                    del count_map[nums[left]]
                left += 1
            
            # All subarrays ending at right with at most k distinct
            # are valid: [left, right], [left+1, right], ..., [right, right]
            result += right - left + 1
        
        return result
    
    # Exactly K = At Most K - At Most (K-1)
    return atMostK(k) - atMostK(k - 1)


# Test cases
print("=" * 70)
print("Problem 11: LeetCode 992 - Subarrays with K Different Integers (HARD)")
print("=" * 70)
test_cases_992 = [
    ([1, 2, 1, 2, 3], 2),
    ([1, 2, 1, 3, 4], 3),
    ([1, 2], 1),
    ([1, 1, 1, 1], 1)
]

for nums, k in test_cases_992:
    result = subarraysWithKDistinct(nums, k)
    print(f"nums: {nums}, k: {k}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 12: LeetCode 159 - Longest Substring with At Most 2 Distinct Characters
# ============================================================================

"""
Problem:
--------
Given a string s, return the length of the longest substring that 
contains at most two distinct characters.

Example 1:
Input: s = "eceba"
Output: 3
Explanation: "ece" has 2 distinct characters

Example 2:
Input: s = "ccaabbb"
Output: 5
Explanation: "aabbb" has 2 distinct characters

Constraints:
- 1 <= s.length <= 10^5
- s consists of English letters
"""

def lengthOfLongestSubstringTwoDistinct(s):
    """
    Approach: Variable sliding window with hash map
    
    Key Insight:
    - We want the LONGEST substring with AT MOST 2 distinct characters
    - This is exactly the same as "Fruit Into Baskets" (LC 904)!
    - Use a hashmap to count character frequencies in the current window
    - Keep expanding the window to the right, adding characters
    - If we encounter a 3rd distinct character, the window becomes invalid
    - Shrink the window from the left until we have at most 2 distinct characters
    - Track the maximum valid window length
    - The key is: you can have at most 2 types, shrink when you get a 3rd
    
    Time: O(n)
    Space: O(1) - at most 3 characters in map
    """
    left = 0
    char_count = {}
    max_length = 0
    
    for right in range(len(s)):
        # Expand window: add right character
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Contract window: while more than 2 distinct characters
        while len(char_count) > 2:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
print("=" * 70)
print("Problem 12: LeetCode 159 - Longest Substring with At Most 2 Distinct")
print("=" * 70)
test_cases_159 = [
    "eceba",
    "ccaabbb",
    "a",
    "aa",
    "abcabcabc"
]

for s in test_cases_159:
    result = lengthOfLongestSubstringTwoDistinct(s)
    print(f"s: '{s}'")
    print(f"Result: {result}\n")


print("=" * 70)
print("VARIABLE WINDOW SIZE PATTERN - COMPLETE!")
print("=" * 70)
print("\n🎯 FAANG-READY VARIABLE SLIDING WINDOW COLLECTION (12 Problems)")
print("\nProblems Covered:")
print("1.  LC 209  - Minimum Size Subarray Sum ⭐⭐⭐⭐")
print("2.  LC 3    - Longest Substring Without Repeating Characters ⭐⭐⭐⭐⭐")
print("3.  LC 340  - Longest Substring with At Most K Distinct Characters ⭐⭐")
print("4A. LC 485  - Max Consecutive Ones I ⭐⭐ (NOT true sliding window)")
print("4B. LC 487  - Max Consecutive Ones II ⭐⭐")
print("4C. LC 1004 - Max Consecutive Ones III ⭐⭐⭐")
print("5.  LC 76   - Minimum Window Substring (HARD) ⭐⭐⭐⭐⭐")
print("6.  LC 424  - Longest Repeating Character Replacement ⭐⭐⭐⭐")
print("7.  LC 904  - Fruit Into Baskets ⭐⭐⭐")
print("8.  LC 1658 - Minimum Operations to Reduce X to Zero ⭐⭐⭐")
print("9.  LC 1695 - Maximum Erasure Value ⭐⭐")
print("10. LC 1493 - Longest Subarray After Deleting One Element ⭐⭐")
print("11. LC 992  - Subarrays with K Different Integers (HARD) ⭐⭐⭐⭐")
print("12. LC 159  - Longest Substring with At Most 2 Distinct ⭐⭐⭐")
print("\n⭐ = Frequency Rating (More stars = Asked more often)")
print("\n📁 FIXED WINDOW PROBLEMS (moved to 'sliding_window_fixed_solutions.py'):")
print("   - LC 438: Find All Anagrams in a String ⭐⭐⭐⭐⭐")
print("   - LC 567: Permutation in String ⭐⭐⭐⭐")
print("   - LC 30:  Substring with Concatenation of All Words (HARD) ⭐⭐⭐⭐")
print("\n🔥 TOP 5 MUST-KNOW FOR FAANG (Variable Window):")
print("   LC 3, LC 76, LC 424, LC 992, LC 209")
print("\nAll solutions use O(n) time complexity!")
print("\n📚 Problem Series:")
print("\nMax Consecutive Ones (4A, 4B, 4C):")
print("  - LC 485:  k=0 flips allowed (simple counter, NOT sliding window)")
print("  - LC 487:  k=1 flip allowed (true sliding window)")
print("  - LC 1004: k=any flips allowed (generalized)")
print("\n'Exactly K' Transformation (11):")
print("  - LC 992: Exactly K = At Most K - At Most (K-1)")
print("  - This technique applies to many 'exactly K' problems!")
print("\n" + "=" * 70)

# ============================================================================
# SUMMARY & PATTERN RECOGNITION
# ============================================================================

"""
VARIABLE WINDOW SIZE - PATTERN RECOGNITION:
===========================================

When to Use Variable Window:
----------------------------
✓ "Longest/shortest subarray/substring with condition"
✓ "At most K" or "At least K" constraints
✓ "Minimum/maximum length"
✓ Need to find optimal window size

Key Characteristics:
-------------------
1. Window size changes dynamically
2. Two pointers: left and right
3. Right always moves forward
4. Left moves when condition violated
5. Each element visited at most twice → O(n)

Template Structure:
------------------
left = 0
state = initialize()

for right in range(n):
    # 1. Expand: add right element to window
    update_state(right)
    
    # 2. Contract: shrink while invalid
    while window_invalid(state):
        remove_left_element()
        left += 1
    
    # 3. Update: record result
    update_result(right - left + 1)

Common Variations:
-----------------
1. Track with Set: Unique elements (LC 3, 1695)
2. Track with Map: Frequencies/counts (LC 76, 340, 424)
3. Track with Counter: Specific element count (LC 1004, 1493)
4. Reverse Thinking: Find complement (LC 1658)
5. Mathematical Transformation: Exactly K = At Most K - At Most (K-1) (LC 992)

Problem Categories:
------------------
1. Unique Elements: LC 3, 1695
2. K Distinct: LC 340, 904, 159
3. K Replacements: LC 1004, 424, 1493
4. Contains All: LC 76
5. Sum-based: LC 209, 1658
6. Exactly K: LC 992

Time Complexity: O(n) for all
Space Complexity: O(1) to O(k) depending on tracking needs

NOTE: Fixed Window Size Problems
---------------------------------
The following problems use FIXED window size and have been moved to:
'sliding_window_fixed_solutions.py'

- LC 438: Find All Anagrams in a String
- LC 567: Permutation in String  
- LC 30:  Substring with Concatenation of All Words

These use a different template (fixed size) rather than variable expansion/contraction.
"""
