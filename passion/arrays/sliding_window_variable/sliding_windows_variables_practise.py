
# array traversals:-
#forward
# arr = [1, 2, 3, 4, 5]
#
# for a in arr:
#     print(a)
#
# for index in range(5):
#     print(index , arr[index])
#
# for index, value in enumerate(arr):
#     print(index , value)


# 2 pointer traversal
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# left, right = 0, len(arr) - 1

# while ( left <= right ):
#     print( arr[left] , arr[right])
#     left += 1
#     right -= 1

# slow fast traversal
# slow, fast = 0,0
#
# while fast < len(arr):
#     print( slow, fast)
#     slow += 1
#     fast += 2


# Sliding Window Traversal
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# window_length = 3
#
# left = 0
# right =  0

# fixed
# while( right <= len(arr)-1):
#     right = left + window_length
#     print( arr[left:right])
#     left+=1

# print( arr[3:])


#variable
def minSubArrayLen(arr, target):
    """
    Find the LENGTH of smallest subarray whose sum >= target.

    Example: arr = [2, 1, 5, 2, 3, 2], target = 7
    Answer: 2 (subarray [5, 2] has sum 7)

    Steps:
    1. Expand window by adding arr[right] to sum
    2. When sum >= target, try to shrink from left
    3. Track minimum length
    """

    left = 0
    right = 0
    min_length = float ('inf')
    sum = 0

    while right < len(arr):
        # Add the element to sum.
        sum = sum + arr[right]

        # whenever the target value has been reached, starting from the leftmost elements in the array
        # subtract from the sum variable.
        while sum >= target:
            # record the minimum length
            min_length = min(min_length, right+1 -left )

            sum = sum - arr[left]

            # move to the next element.
            left+=1

        # Increase the right variable.
        right += 1

    return 0 if min_length == float ('inf') else min_length



# Test cases
# print("=" * 70)
# print("Problem 1: LeetCode 209 - Minimum Size Subarray Sum")
# print("=" * 70)
# test_cases_209 = [
#     (7, [2,3,1,2,4,3]),
#     (4, [1,4,4]),
#     (11, [1,1,1,1,1,1,1,1]),
#     (15, [1,2,3,4,5])
# ]
#
# for target, nums in test_cases_209:
#     result = minSubArrayLen(nums, target)
#     print(f"Target: {target}, Nums: {nums}")
#     print(f"Result: {result}\n")



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
    Approach: Variable sliding window with set

    Key Insight:
    - Use set to track characters in current window
    - Expand window by adding right character
    - Contract window while duplicate exists
    - Track maximum length

    Time: O(n) - each character visited at most twice
    Space: O(min(n, m)) where m is charset size
    """

    left =0
    right=0
    hashmap= {}
    max_length = 0

    #traverse the entire word and keep on addign letters in the hashset
    while right < len(s):
        hashmap[s[right]] = hashmap.get(s[right],0) + 1

        # if the letter already exists in the hashmap, remove it,
        # then increment the left pointer
        # and also keep a track of max length
        while hashmap[s[right]] > 1:
            hashmap[s[left]] -= 1
            if hashmap[s[left]] == 0:
                del hashmap[s[left]]
            left += 1

        # Track maximum length
        max_length = max(max_length, right + 1 - left)

        right+=1

    return 0 if max_length == 0 else max_length


# Test cases
# print("=" * 70)
# print("Problem 2: LeetCode 3 - Longest Substring Without Repeating Characters")
# print("=" * 70)
# test_cases_3 = ["abcabcbb", "bbbbb", "pwwkew", "", "au", "dvdf"]
#
# for s in test_cases_3:
#     result1 = lengthOfLongestSubstring(s)
#     print(f"String: '{s}', {result1}")
#     print("=" * 70)



s = "abcabcbb"
dict = {}

# for index, value in enumerate(s):
#     print( index , value )
#
#     # if value not in dict:
#     #     dict[value] = []
#     # dict[value].append(index)
#
#     dict[value] = dict.get(value,0) + 1
#
#
# print(dict)

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


# def lengthOfLongestSubstringKDistinct(s, k):
#     """
#     Approach: Variable sliding window with hash map
#
#     Key Insight:
#     - Track character frequencies in window
#     - Expand window by adding right character
#     - Contract window while distinct chars > k
#     - Track maximum length
#
#     Time: O(n)
#     Space: O(k) - at most k+1 distinct characters in map
#     """
#     left = 0
#     right = 0
#     dict = {}
#     maximum_window_length = 0
#
#
#     while(right< len(s)):
#         # Track character frequencies in window
#         dict[s[right]] = dict.get(s[right],0) + 1
#
#         #  Contract window while distinct chars > k
#         while len(dict) > k:
#            # decrement/remove key/value pairs when len(dict) goes beyond k
#            if s[right] in dict:
#                dict[s[right]] -= 1
#                if dict[s[right]] == 0:
#                    del dict[s[right]]
#            left+=1
#
#         # Track maximum length
#         maximum_window_length = max(maximum_window_length , right+1 - left)
#
#         # Expand window by adding right character
#         right+=1
#
#     return(maximum_window_length)
#
# # Test cases
# print("=" * 70)
# print("Problem 3: LeetCode 340 - Longest Substring with At Most K Distinct")
# print("=" * 70)
# test_cases_340 = [
#     ("eceba", 2),
#     ("aa", 1),
#     ("abaccc", 2),
#     ("a", 1),
#     ("", 2)
# ]
#
# for s, k in test_cases_340:
#     result = lengthOfLongestSubstringKDistinct(s, k)
#     print(f"String: '{s}', k: {k}")
#     print(f"Result: {result}\n")

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


# Alternative: Using sliding window approach
def findMaxConsecutiveOnes_SlidingWindow(arr):
    """
    Sliding window approach (k=0 flips allowed)
    """

    left = 0
    right = 0
    max_length = 0

    while right < len(arr):
        if arr[right] == 1:
            max_length = max(max_length,right+1-left)
        else:
            left = right+1

        right+=1

    return 0 if max_length == 0 else max_length

# Test cases
print("=" * 70)
print("Problem 4A: LeetCode 485 - Max Consecutive Ones I")
print("=" * 70)
test_cases_485 = [
    [1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [1]
]

# for nums in test_cases_485:
#     result = findMaxConsecutiveOnes_SlidingWindow(nums)
#     print(f"Nums: {nums}")
#     print(f"Result: {result}\n")


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


def findMaxConsecutiveOnes_II(arr):
    """
    Approach: Variable sliding window with k=1

    Key Insight:
    - Find longest subarray with at most 1 zero
    - Track count of zeros in current window
    - Expand window by adding right element
    - Contract window while zeros > 1

    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = 0
    count_of_zeros = 0
    k = 1 # can flip atmost one 0 at a time.
    max_length = 0

    while right < len(arr):
        if arr[right] == 0:
            count_of_zeros += 1

        while count_of_zeros > k :
            if arr[left] == 0:
                count_of_zeros -= 1
            left += 1

        max_length = max(max_length , right+1 - left)

        right+=1

    return 0 if max_length == 0 else max_length


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
    [1,1,0,0,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1]
]

# for nums in test_cases_487:
#     result = findMaxConsecutiveOnes_II(nums)
#     print(f"Nums: {nums}")
#     print(f"Result: {result}\n")

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
    - Find longest subarray with at most k zeros
    - Track count of zeros in current window
    - Expand window by adding right element
    - Contract window while zeros > k

    Time: O(n)
    Space: O(1)
    """



# Test cases
print("=" * 70)
print("Problem 4C: LeetCode 1004 - Max Consecutive Ones III")
print("=" * 70)
test_cases_1004 = [
    ([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2),
    ([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3),
    ([1, 1, 1, 1], 0),
    ([0, 0, 0, 0], 2)
]
#
# for nums, k in test_cases_1004:
#     result = longestOnes(nums, k)
#     print(f"Nums: {nums}, k: {k}")
#     print(f"Result: {result}\n")


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


def minWindow(arr, t):
    """
    Approach: Variable sliding window with two hash maps

    Key Insight:
    - Track required character counts from t
    - Track current window character counts
    - Expand window until all characters satisfied
    - Contract window while maintaining validity
    - Track minimum window

    Time: O(|s| + |t|)
    Space: O(|s| + |t|)
    """
    if not arr or not t:
        return ""
    
    left = 0
    right = 0
    source_hmap = {}

    target_hmap = {}
    for element in t:
        target_hmap[element] = target_hmap.get(element,0)+1

    min_left = left
    min_right = right

    matching_count = 0
    min_length = float('inf')

    while right < len(arr):

        if arr[right] in target_hmap:
            # go on dding the elements into source_hmap
            source_hmap[arr[right]] = source_hmap.get(arr[right],0) + 1

            # in event of counts of elements becoming same between source and target, increment matching_count
            if source_hmap[arr[right]] == target_hmap[arr[right]]:
                matching_count +=1

        while matching_count == len(target_hmap):
            #record min_length
            # Update result
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
                min_right = right

            if arr[left] in source_hmap:
                source_hmap[arr[left]] -= 1

                if  source_hmap[arr[left]]  < target_hmap[arr[left]]:
                    matching_count -= 1
            left += 1

        right+=1


    return "" if min_length == float('inf') else s[min_left:min_right + 1]




#test_cases
print("=" * 70)
print("Problem 5: LeetCode 76 - Minimum Window Substring")
print("=" * 70)
test_cases_76 = [
    ("ADOBBBECODEBANC", "ABC"),
    ("a", "a"),
    ("a", "aa"),
    ("ab", "b"),
    ("abc", "cba")
]

# for s, t in test_cases_76:
#     result = minWindow(s, t)
#     print(f"s: '{s}', t: '{t}'")
#     print(f"Result: '{result}'\n")

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


def totalFruit(arr):
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
    right = 0
    hmap = {}
    max_length = 0


    while right < len(arr):
        hmap[arr[right]] = hmap.get(arr[right],0) + 1


        while len(hmap) > 2:

            hmap[arr[left]] -= 1

            if hmap[arr[left]] ==0 :
                del hmap[arr[left]]

            left += 1

        max_length = max(max_length, right + 1 - left)

        right += 1

    return 0 if max_length == 0 else max_length


# Test cases
print("=" * 70)
print("Problem 7: LeetCode 904 - Fruit Into Baskets")
print("=" * 70)
test_cases_904 = [
    [1, 2, 1],
    [0, 1, 2, 2],
    [1, 2, 3, 2, 2],
    [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
]

# for fruits in test_cases_904:
#     result = totalFruit(fruits)
#     print(f"Fruits: {fruits}")
#     print(f"Result: {result}\n")

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


def maximumUniqueSubarray(arr):
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
    right = 0
    max_sum = 0
    intermediate_sum = 0
    hset = set()

    while right < len(arr):
        # when we encountere a duplicate value, remove the element from hset
        # and contract from the left end.
        while arr[right] in hset:
            hset.remove(arr[left])
            intermediate_sum -= arr[left]
            left+=1

        # 1. keep on adding unique elements into hashset and to sum as well.
        # i.e keep on expanding the window in the right
        hset.add(arr[right])
        intermediate_sum += arr[right]

        # keep on finding the max_sum iteratively.
        max_sum = max(max_sum, intermediate_sum)

        right += 1

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


def longestSubarray(arr):
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
    right = 0
    count_of_zeros = 0
    max_length = 0

    while right < len(arr):

        if arr[right] == 0:
            count_of_zeros += 1

        while count_of_zeros > 1:
            if arr[left] == 0:
                count_of_zeros -= 1

            left += 1
        max_length = max(max_length, right - left)


        right += 1


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
