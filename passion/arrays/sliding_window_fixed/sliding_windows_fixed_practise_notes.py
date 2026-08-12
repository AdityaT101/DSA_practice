from collections import defaultdict

# ==================== LeetCode 643 - Maximum Average Subarray I (EASY) ================
def findMaxAverage( arr, k):
   left = 0
   right = 0
   sum1 = 0
   max_sum = 0

   while( right < len(arr)):
       if right - left + 1 > k:
           max_sum = max(max_sum, sum1)
           sum1 -= arr[left]
           left += 1

       sum1 += arr[right]

       right += 1

   print(max_sum)


# ==================== Longest subarray sum ================


def MaxSubarraySum( arr, max_sum):
    left = 0
    right = 0
    sum = 0

    max_length_of_array = 0

    # Brute force -> but this goes in N^2 , hence we go for sliding window
    # for i in range( 0, len(arr)-1 ):
    #     for j in range( 0, len(arr) ):
    #         if sum( arr[i:j] ) <= max_sum and max_length_of_array[0] < len( arr[i:j]):
    #             max_length_of_array[0] = len( arr[i:j] )
    #             max_length_of_array[1] = i
    #             max_length_of_array[2] = j

    while( right < len(arr)) :
          sum += arr[right]

          while sum > max_sum :
              sum -= arr[left]
              left += 1

          if sum <= max_sum:
             max_length_of_array = max( max_length_of_array , right - left + 1 )

          right += 1

    print( max_length_of_array )



# ========== L3. Longest Substring Without Repeating Characters =========

def LongestSubarayWithoutRepeatingCharacters( str):
    left = 0
    right = 0
    hset = set()
    max_subarray_length = 0

    while( right < len(str)):
        while str[right] in hset:
           hset.remove( str[left])
           max_subarray_length -= 1
           left += 1

        hset.add( str[right])
        max_subarray_length += 1

        right += 1

    print( max_subarray_length)


# ========== Longest Substring with At Most K Distinct Characters =========

def LongestSubstringWith_K_DistinctCharacters( str, k):
    left = 0
    right = 0
    hmap = defaultdict(int)
    max_subarray_length = 0

    while ( right < len(str)):
        hmap[str[right]] += 1

        if len(hmap) > k:
            hmap[ str[left] ] -= 1
            if hmap[ str[left] ] == 0:
               del hmap[ str[left] ]
            left += 1

        max_subarray_length = max(right - left + 1, max_subarray_length)

        right += 1

    return max_subarray_length

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
    right = 0
    left = 0
    consecutive_count = 0
    max_consecutive_count = 0

    while right < len(arr):
        if arr[right] == 0:
             left = right + 1

        max_consecutive_count = max( max_consecutive_count, right - left + 1 )
        right+=1

    return max_consecutive_count


# ============================================================================
# PROBLEM 4B: LeetCode 487 - Max Consecutive Ones II and III
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


def findMaxConsecutiveOnes_II_and_III( arr , max_zeroes):
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

    count_of_zeroes  = 0
    max_return_value = 0

    while right < len(arr):
        if arr[right] == 0:
            count_of_zeroes  += 1

        # shrink the window from left based on a condition
        while( count_of_zeroes  > max_zeroes ):
            if arr[left] == 0:
               count_of_zeroes  -= 1
            left += 1

        max_return_value = max( max_return_value, right - left + 1)

        # expand the window from right generally
        right += 1

    return max_return_value

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
    hmap = defaultdict(int)
    max_length = 0

    while right < len(arr):
          hmap[ arr[right] ] += 1

          # shrink the left pointer based on the condition
          if len(hmap) > 2:
              hmap[arr[left]] -= 1
              if hmap[arr[left]] == 0:
                  del hmap[arr[left]]
              left += 1

          # find max variable length
          max_length = max( max_length, right + 1 - left)

          # expand the right pointer
          right += 1

    return max_length

# ============================================================================
# PROBLEM 5: LeetCode 76 - Minimum Window Substring
# ============================================================================

# """
# Problem:
# --------
# Given two strings s and t, return the minimum window substring of s such
# that every character in t (including duplicates) is included in the window.
# If no such substring exists, return "".
#
# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: "BANC" is the minimum window containing A, B, C
#
# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
#
# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
#
# Constraints:
# - 1 <= s.length, t.length <= 10^5
# - s and t consist of uppercase and lowercase English letters
# """
#
# def covers(source, target):
#     return all(source.get(ch, 0) >= cnt for ch, cnt in target.items())
#
#
# def minWindow( str, t):
#     """
#     Approach: Variable sliding window with two hash maps
#
#     Key Insight:
#     - Track required character counts from t
#     - Track current window character counts
#     - Expand window until all characters satisfied
#     - Contract window while maintaining validity
#     - Track minimum window
#
#     Time: O(|s| + |t|)
#     Space: O(|s| + |t|)
#     """
#     if not str or not t:
#         return ""
#
#     left = 0
#     right = 0
#     source_hmap = {}
#
#     target_hmap = {}
#     for element in t:
#         target_hmap[element] = target_hmap.get(element, 0) + 1
#
#     min_left = left
#     min_right = right
#
#     matching_count = 0
#     min_length = float('inf')
#
#
#     while( right < len(str)):
#         if str[right] in target_hmap:
#             # go on dding the elements into source_hmap
#             source_hmap[ str[right]] +=  1
#
#             # in event of counts of elements becoming same between source and target, increment matching_count
#             if source_hmap[ str[right]] == target_hmap[ str[right]]:
#                 matching_count += 1
#
#         while matching_count == len(target_hmap):
#             # record min_length
#             # Update result
#             if right - left + 1 < min_length:
#                 min_length = right - left + 1
#                 min_left = left
#                 min_right = right
#
#             if str[left] in source_hmap:
#                 source_hmap[ str[left]] -= 1
#
#                 if source_hmap[ str[left]] < target_hmap[ str[left]]:
#                     matching_count -= 1
#             left += 1
#
#         right += 1
#
#     return "" if min_length == float('inf') else str[ min_left : min_right+1]




def NiceSubarray( arr , k ):
    left = 0
    right = 0
    count = 0
    final_count = 0

    while( right < len(arr)):
        if arr[right] % 2 == 1:
            count += 1

        while count > k:
            if arr[left] % 2 == 1:
                count -= 1
            left += 1

        while count == k:
            final_count += 1

            if arr[left] % 2 == 0:
                left += 1

        right += 1

    return final_count


def BinarySubarraySum( arr, goal):
    left = 0
    right = 0
    sum = 0
    final_count = 0

    while ( right < len(arr)):
        sum += arr[right]

        while sum > goal:
            sum -= arr[left]
            left += 1
            if sum == goal:
                final_count += 1

        if sum == goal:
          final_count += 1

        right += 1

    return final_count


# ============================================================================

if __name__ == "__main__":

    print("=" * 70)
    print("Problem: LeetCode 1248 - Count Number of Nice Subarrays")
    print("=" * 70)
    test_cases_binary = [
        ([1, 0, 1, 0, 1], 2, 4),
        ([0, 0, 0, 0, 0], 0, 15),
        ([1, 0, 1, 0, 1], 0, 2),
        ([0, 1, 1, 1, 1], 3, 3),
        ([1, 1, 1, 1, 1], 5, 1),
        ([0, 1, 0], 1, 4),
    ]

    for arr, goal, expected in test_cases_binary:
        result = BinarySubarraySum(arr, goal)
        status = "✅" if result == expected else "❌"
        print(f"Input: arr={arr}, goal={goal}")
        print(f"Expected: {expected}, Got: {result} {status}")
        print()

    # ============================================================================

    # print("=" * 70)
    # print("Problem: LeetCode 1248 - Count Number of Nice Subarrays")
    # print("=" * 70)
    # test_cases_nice = [
    #     # ([1, 1, 1, 2, 1, 1], 3),
    #     # ([2, 4, 6], 1),
    #     ([ 2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2),
    #     # ([1, 1, 1, 1, 1], 1),
    #     # ([1, 2, 3, 4, 5], 2),
    # ]
    #
    # for arr, k in test_cases_nice:
    #     print(f"arr: {arr}, k: {k}")
    #     print("Result: ", end="")
    #     print(NiceSubarray(arr, k))


    # ============================================================================
    # print("=" * 70)
    # print("Problem 5: LeetCode 76 - Minimum Window Substring")
    # print("=" * 70)
    # test_cases_76 = [
    #     ("ADOBBBECODEBANC", "ABC"),
    #     ("a", "a"),
    #     ("a", "aa"),
    #     ("ab", "b"),
    #     ("abc", "cba")
    # ]
    #
    # for s, t in test_cases_76:
    #     result = minWindow(s, t)
    #     print(f"s: '{s}', t: '{t}'")
    #     print(f"Result: '{result}'\n")

    # ============================================================================
    # print("=" * 70)
    # print("Problem 7: LeetCode 904 - Fruit Into Baskets")
    # print("=" * 70)
    # test_cases_904 = [
    #     [1, 2, 1],
    #     [0, 1, 2, 2],
    #     [1, 2, 3, 2, 2],
    #     [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    # ]
    #
    # for fruits in test_cases_904:
    #     result = totalFruit(fruits)
    #     print(f"Fruits: {fruits}")
    #     print(f"Result: {result}\n")

    # ============================================================================
    # print("=" * 70)
    # print("Problem 4B: LeetCode 487 - Max Consecutive Ones II")
    # print("=" * 70)
    # test_cases_487 = [
    #     [ 1, 0, 1, 1, 0, 1, 1, 1, 1, 1 ,0 ],
    #     [1, 0, 1, 1, 0, 1],
    #     [1, 1, 1, 1],
    #     [0, 0, 0, 0],
    #     [0, 1, 1, 0, 1],
    #     [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
    # ]
    #
    # for nums in test_cases_487:
    #     result = findMaxConsecutiveOnes_II_and_III(nums, 1)
    #     print(f"Nums: {nums}")
    #     print(f"Result: {result}\n")

    # ============================================================================
    # print("=" * 70)
    # print("Problem 4A: LeetCode 485 - Max Consecutive Ones I")
    # print("=" * 70)
    # test_cases_485 = [
    #     [1, 1, 0, 1, 1, 1],
    #     [1, 0, 1, 1, 0, 1],
    #     [1, 1, 1, 1],
    #     [0, 0, 0, 0],
    #     [1]
    # ]
    #
    # for nums in test_cases_485:
    #     result = findMaxConsecutiveOnes_SlidingWindow(nums)
    #     print(f"Nums: {nums}")
    #     print(f"Result: {result}\n")

    #==================== LongestSubstringWith_K_DistinctCharacters ================
    # print("=" * 70)
    # print("Problem 3: LeetCode 340 - Longest Substring with At Most K Distinct")
    # print("=" * 70)
    # test_cases_340 = [
    #     ("eceba", 2),
    #     ("aa", 1),
    #     ("abaccc", 2),
    #     ("a", 1),
    #     ("aabc", 2),
    #     ("cdbdzabnmhbcd", 3)
    # ]
    #
    # for s, k in test_cases_340:
    #     result = LongestSubstringWith_K_DistinctCharacters( s, k)
    #     print(f"String: '{s}', k: {k}")
    #     print(f"Result: {result}\n")

    # ==================== L3. Longest Substring Without Repeating Characters =======
    # str = "cdbzarbcd"
    # LongestSubarayWithoutRepeatingCharacters(str)

    # ==================== Longest subarray sum ================

    # arr = [ 1, 12, -5, -6, 50, 3, 10, -20, 31]
    # # arr = [1, 1, 1]
    # max_sum = 20
    # MaxSubarraySum( arr, max_sum)

    # ==================== LeetCode 643 - Maximum Average Subarray I (EASY) ================
    # arr = [ 1, 12, -5, -6, 50, 3, 10, -20, 31 ]
    # k = 3
    # findMaxAverage(arr, k)


