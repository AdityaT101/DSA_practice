from collections import defaultdict

# ============================================================================
# PROBLEM 1: LeetCode 1480 - Running Sum of 1d Array (EASY)
# ============================================================================

"""
Problem:
--------
Given an array nums. We define a running sum of an array as
runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is [1, 1+2, 1+2+3, 1+2+3+4]

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6
"""


def runningSum(arr):
    """
    Approach: Build prefix sum array iteratively

    Key Insight:
    - This is the SIMPLEST form of prefix sum
    - Each element is the sum of all previous elements plus itself
    - We can build it in-place or use extra space
    - prefix[i] = prefix[i-1] + nums[i]
    - This is the foundation for all prefix sum problems
    - Time: O(n) - single pass through array
    - Space: O(1) if modifying in-place, O(n) for new array

    Pattern Recognition:
    - "running sum" → prefix sum
    - "cumulative" → prefix sum
    - Build result array where each element depends on previous sum

    Time: O(n)
    Space: O(1) if in-place, O(n) for new array
    """
    # result = [0] * len(arr)
    # result[0] = arr[0]
    #
    # i = 1
    # while i < len(arr):
    #     result[i] = arr[i] + result[i-1]
    #     i+=1
    #
    # return result


    temp = arr[0]

    i=1
    while( i < len(arr)):
        temp = temp + arr[i]
        arr[i] = temp
        i+=1

    return arr

# Test cases
print("\n" + "=" * 70)
print("Problem 1: LeetCode 1480 - Running Sum of 1d Array")
print("=" * 70)

test_cases_1480 = [
    [1, 2, 3, 4],
    [1, 1, 1, 1, 1],
    [3, 1, 2, 10, 1],
    [5],
    [-1, -2, -3]
]

# for nums in test_cases_1480:
#     original = nums.copy()
#     result = runningSum(nums.copy())
#     print(f"Input: {original}")
#     print(f"Output: {result}")
#     print()

# ============================================================================
# PROBLEM 2: LeetCode 724 - Find Pivot Index (EASY)
# ============================================================================

"""
Problem:
--------
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to 
the left of the index is equal to the sum of all the numbers strictly to 
the right of the index.

If the index is on the left edge, the left sum is 0. Similarly for right edge.

Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation: 
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation: No pivot index exists

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation: Left sum = 0, Right sum = 1 + (-1) = 0

Constraints:
- 1 <= nums.length <= 10^4
- -1000 <= nums[i] <= 1000
"""


def pivotIndex(arr):
    """
    Approach: Use total sum and running left sum

    Key Insight:
    - At pivot index i: left_sum == right_sum
    - We know: total_sum = left_sum + nums[i] + right_sum
    - If left_sum == right_sum, then: total_sum = 2 * left_sum + nums[i]
    - Rearranging: left_sum = (total_sum - nums[i]) / 2
    - Or simpler: left_sum == total_sum - left_sum - nums[i]
    - This means: 2 * left_sum + nums[i] == total_sum
    - We can check this condition while maintaining running left_sum
    - No need to build prefix array - just track running sum!

    Algorithm:
    1. Calculate total sum of array
    2. Iterate through array maintaining left_sum
    3. At each index, check if left_sum == total_sum - left_sum - nums[i]
    4. This is equivalent to: left_sum * 2 + nums[i] == total_sum
    5. Return first index where condition is true

    Pattern Recognition:
    - "sum to left" == "sum to right" → prefix sum concept
    - "pivot" or "equilibrium" → balance point using sums
    - Can solve without building full prefix array

    Time: O(n)
    Space: O(1)
    """
    i = 0
    left_sum = 0
    total_sum = sum(arr)

    while i < len(arr):
        if total_sum == 2*left_sum + arr[i]:
            return i

        left_sum += arr[i]

        i+=1

    return -1

# Test cases
print("\n" + "=" * 70)
print("Problem 2: LeetCode 724 - Find Pivot Index")
print("=" * 70)

test_cases_724 = [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0),
    ([1, -1, 0], 2),
    ([-1, -1, 0, 1, 1, 0], 5)
]

# for nums, expected in test_cases_724:
#     result = pivotIndex(nums)
#     status = "✅" if result == expected else "❌"
#     print(f"Input: {nums}")
#     print(f"Expected: {expected}, Got: {result} {status}")
#     print()



# ============================================================================
# PROBLEM 3: LeetCode 303 - Range Sum Query - Immutable (EASY)
# ============================================================================

"""
Problem:
--------
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right 
inclusive where left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums 
  between indices left and right inclusive.

Example 1:
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output:
[null, 1, -1, -3]

Explanation:
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

Constraints:
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls will be made to sumRange
"""


class NumArray:
    """
    Approach: Build prefix sum array during initialization

    Key Insight:
    - This is the CLASSIC prefix sum problem
    - Multiple queries → precompute prefix sums
    - Without prefix sum: Each query takes O(n) → Total O(q * n)
    - With prefix sum: Build once O(n), each query O(1) → Total O(n + q)
    - The key formula: sum[L, R] = prefix[R+1] - prefix[L]
    - We use prefix[i] = sum of first i elements (0-indexed)
    - Extra element prefix[0] = 0 makes calculation cleaner
    - This avoids edge case handling for L = 0

    Why prefix[R+1] - prefix[L]?
    - prefix[R+1] = sum[0...R]
    - prefix[L] = sum[0...L-1]
    - Difference = sum[L...R] ✅

    Example:
    nums = [1, 2, 3, 4, 5]
    prefix = [0, 1, 3, 6, 10, 15]

    Query sum[1, 3] (elements 2, 3, 4):
    prefix[4] - prefix[1] = 10 - 1 = 9 ✅

    Pattern Recognition:
    - "multiple queries" + "range sum" → prefix sum
    - "immutable" → precompute once
    - Trade space for time: O(n) space for O(1) queries

    Time: O(n) for init, O(1) for sumRange
    Space: O(n)
    """

    def __init__(self, nums):
        self.prefix = [ 0 ] * (len(nums)+1)
        i=0
        while i < len(nums):
            self.prefix[i+1] = self.prefix[i] + nums[i]
            i+=1


    def sumRange(self, left, right):
        return self.prefix[ right + 1 ] - self.prefix[ left ] # *** v v imp*.


# Test cases
print("\n" + "=" * 70)
print("Problem 3: LeetCode 303 - Range Sum Query - Immutable")
print("=" * 70)

nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)

queries = [
    (0, 2, 1),
    (2, 5, -1),
    (0, 5, -3),
    (1, 3, -2),
    (0, 0, -2)
]

print(f"Array: {nums}")
print(f"Prefix: {numArray.prefix}")
print()

# for left, right, expected in queries:
#     result = numArray.sumRange(left, right)
#     status = "✅" if result == expected else "❌"
#     print(f"sumRange({left}, {right}) = {result} (expected: {expected}) {status}")



# ==================== GfG - Max Sum Subarray of Size K (related: LeetCode 643 - Maximum Average Subarray I) ================
# NOTE: This returns the max SUM of a size-k window. For LC 643 (max average), divide the result by k.
def findMaxSubarray( arr, k):
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




class Solution:
    def findMaxAverage(self, arr, k: int) -> float:
        left = 0
        right = 0
        intermittent_sum = 0
        max_sum = float('-inf')

        while (right < len(arr)):
            if (right + 1 - left) > k:
                max_sum = max(max_sum, intermittent_sum)
                intermittent_sum -= arr[left]
                left += 1

            intermittent_sum += arr[right]

            right += 1

        if max_sum == float('-inf'):
            return intermittent_sum / k
        else:
            return max_sum / k




# ==================== GfG - Longest Subarray with Sum <= K (no direct LeetCode equivalent) ================
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

          max_length_of_array = max( max_length_of_array , right - left + 1 )

          right += 1

    print( max_length_of_array )

arr = [ 1, 12, -5, -6, 50, 3, 10, -20, 31]
# arr = [1, 1, 1]
max_sum = 20
MaxSubarraySum( arr, max_sum)

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
    (7, [2, 3, 1, 2, 4, 3]),
    (4, [1, 4, 4]),
    (11, [1, 1, 1, 1, 1, 1, 1, 1]),
    (15, [1, 2, 3, 4, 5])
]

for target, nums in test_cases_209:
    result = minSubArrayLen(target, nums)
    print(f"Target: {target}, Nums: {nums}")
    print(f"Result: {result}\n")

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



# ========== LeetCode 3 - Longest Substring Without Repeating Characters ==========

def LongestSubarayWithoutRepeatingCharacters( str):
    left = 0
    right = 0
    hset = set()
    max_subarray_length = 0

    while( right < len(str)):
        while str[right] in hset:
           hset.remove( str[left])
           left += 1

        hset.add( str[right])
        max_subarray_length = max(max_subarray_length, right + 1 - left)

        right += 1

    print( max_subarray_length)


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
    [4, 2, 4, 5, 6],
    [5, 2, 1, 2, 5, 2, 1, 2, 5],
    [1, 2, 3, 4, 5],
    [1, 1, 1, 1]
]

for nums in test_cases_1695:
    result = maximumUniqueSubarray(nums)
    print(f"Nums: {nums}")
    print(f"Result: {result}\n")



# ========== LeetCode 340 - Longest Substring with At Most K Distinct Characters ==========

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
# PROBLEM 4B: LeetCode 487 - Max Consecutive Ones II  /  LeetCode 1004 - Max Consecutive Ones III
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
# leetcode 424. Longest Repeating Character Replacement
# ============================================================================

from collections import defaultdict
def characterReplacement(arr: str, k: int):
    left = 0
    right = 0
    hmap = defaultdict(int)
    max_length = 0
    max_freq = 0

    while (right < len(arr)):

        hmap[arr[right]] += 1

        # go through all the hmap.values() and find max
        max_freq = max( max_freq, max(list(hmap.values())))

        while((right+1 - left) - max_freq > k):
            hmap[arr[left]] -= 1
            left += 1

        max_length = max(max_length, right + 1 - left)

        right += 1

    return max_length


print("=" * 70)
print("Problem: LeetCode 424 - Longest Repeating Character Replacement")
print("=" * 70)
test_cases_424 = [
    ("AABABBA", 1, 4),
    ("ABAB", 2, 4),
    ("AAABBCCD", 2, 5),
    ("AAAA", 2, 4),
    ("AAAAABABBA", 1, 7),
    ("ABCDE", 1, 2),
    ("AAAB", 0, 3),
    ("A", 0, 1),
]

for s, k, expected in test_cases_424:
    result = characterReplacement(s, k)
    status = "✅" if result == expected else "❌"
    print(f"Input: s='{s}', k={k}")
    print(f"Expected: {expected}, Got: {result} {status}")
    print()

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


def minWindow( str, t):
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
    if not str or not t:
        return ""

    left = 0
    right = 0
    source_hmap = {}

    target_hmap = {}
    for element in t:
        target_hmap[element] = target_hmap.get(element, 0) + 1

    min_left = left
    min_right = right

    matching_count = 0
    min_length = float('inf')


    while( right < len(str)):
        if str[right] in target_hmap:
            # go on dding the elements into source_hmap
            source_hmap[ str[right]] +=  1

            # in event of counts of elements becoming same between source and target, increment matching_count
            if source_hmap[ str[right]] == target_hmap[ str[right]]:
                matching_count += 1

        while matching_count == len(target_hmap):
            # record min_length
            # Update result
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_left = left
                min_right = right

            if str[left] in source_hmap:
                source_hmap[ str[left]] -= 1

                if source_hmap[ str[left]] < target_hmap[ str[left]]:
                    matching_count -= 1
            left += 1

        right += 1

    return "" if min_length == float('inf') else str[ min_left : min_right+1]


# ============================================================================
# PROBLEM: LeetCode 443 - String Compression
# ============================================================================

"""
Problem:
--------
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters:
- If the group's length is 1, append the character to s.
- Otherwise, append the character followed by the group's length.

The compressed string should be stored in the input character array chars.
Return the new length of the array.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: chars becomes ["a","2","b","2","c","3"]

Example 2:
Input: chars = ["a"]
Output: 1
Explanation: chars stays ["a"]

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: chars becomes ["a","b","1","2"]

Constraints:
- 1 <= chars.length <= 2000
- chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol
"""


def compress(arr):
    """
    Approach: Two pointers (read/write pattern)

    Key Insight:
    - Use 'right' pointer to read and count consecutive characters
    - Use 'left' pointer to write the compressed result
    - For each group: write the char, then write count digits if count > 1
    - This is an in-place compression, so we overwrite the original array
    - The key is: read groups with right, write compressed with left

    Time: O(n)
    Space: O(1)
    """

    left = 0  # write pointer
    right = 0  # read pointer
    n = len(arr)

    while right < n:
        char = arr[right]
        count = 0

        # Count consecutive characters (expand read pointer)
        while right < n and arr[right] == char:
            right += 1
            count += 1

        # Write the character
        arr[left] = char
        left += 1

        # Write the count if > 1 (e.g., 12 becomes '1', '2')
        if count > 1:
            for digit in str(count):
                arr[left] = digit
                left += 1

    return left


# Test cases
print("=" * 70)
print("Problem: LeetCode 443 - String Compression")
print("=" * 70)
test_cases_443 = [
    ["a", "a", "b", "b", "c", "c", "c"],
    ["a"],
    ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"],
    ["a", "a", "a", "b", "b", "a", "a"]
]

# for chars in test_cases_443:
#     original = chars.copy()
#     result = compress(chars)
#     print(f"Input: {original}")
#     print(f"Output length: {result}, Compressed: {chars[:result]}\n")


# ============================================================================
# Group Anagrans
# ============================================================================


from collections import defaultdict

def groupAnagrams(arr):
    hmap = defaultdict(list)

    for word in arr:
        key = ''.join( sorted(word))
        print(key)
        hmap[key].append(word)

    return list(hmap.values())

arr = ["eat","tea","tan","ate","nat","bat"]

print( groupAnagrams(arr) )




# ============================================================================# ============================================================================# ============================================================================
# ============================================================================# ============================================================================# ============================================================================


# ============================================================================
# PROBLEM 4: LeetCode 560 - Subarray Sum Equals K (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an array of integers nums and an integer k, return the total number 
of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Explanation: Subarrays [1,1] at indices (0,1) and (1,2)

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2
Explanation: Subarrays [1,2] and [3]

Example 3:
Input: nums = [1,-1,0], k = 0
Output: 3
Explanation: Subarrays [1,-1], [0], and [1,-1,0]

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""


def subarraySum(arr, k):
    """
    Approach: Prefix Sum + Hash Map

    Key Insight:
    - This is THE MOST IMPORTANT prefix sum + hash map problem
    - Brute force: Check all subarrays O(n²) or O(n³)
    - Key observation: If prefix_sum[j] - prefix_sum[i] = k
      Then subarray from i+1 to j has sum = k
    - Rearranging: prefix_sum[i] = prefix_sum[j] - k
    - So for each position j, check if (current_sum - k) exists in hash map
    - Hash map stores: {prefix_sum: count of times we've seen this sum}
    - Why count? Because multiple positions can have same prefix sum
    - Each occurrence represents a different subarray ending at current position

    Algorithm:
    1. Use hash map to store {prefix_sum: frequency}
    2. Initialize with {0: 1} (empty subarray has sum 0)
    3. For each element, update running sum
    4. Check if (current_sum - k) exists in map
    5. If yes, add its frequency to result (all those positions form valid subarrays)
    6. Add current_sum to map

    Example Walkthrough:
    nums = [1, 2, 3], k = 3

    i=0, num=1:
      sum=1, check (1-3=-2) in map? No
      map = {0:1, 1:1}, count=0

    i=1, num=2:
      sum=3, check (3-3=0) in map? Yes! count += map[0] = 1
      map = {0:1, 1:1, 3:1}, count=1

    i=2, num=3:
      sum=6, check (6-3=3) in map? Yes! count += map[3] = 1
      map = {0:1, 1:1, 3:1, 6:1}, count=2

    Result: 2 subarrays → [1,2] and [3]

    Why This Works:
    - At each position, we're asking: "How many previous positions have
      prefix_sum = current_sum - k?"
    - Each such position forms a subarray with sum = k ending at current position
    - By storing frequencies, we count all possible subarrays

    Pattern Recognition:
    - "count subarrays" + "sum equals k" → prefix sum + hash map
    - "contiguous" → prefix sum
    - "can have negative numbers" → can't use sliding window, must use hash map

    Time: O(n)
    Space: O(n) for hash map
    """

    i = 0
    hmap = {}
    hmap[0] = 1
    prefix_sum = 0
    count = 0

    while( i < len(arr)):
        # iterate through each element and form a prefix_sum array
        prefix_sum += arr[i]

        if prefix_sum-k in hmap:
            count += hmap[ prefix_sum-k ]

        hmap[prefix_sum] = hmap.get(prefix_sum, 0) + 1

        i+=1



    print(arr)
    print( prefix_sum )
    print(hmap)
    return count


# Test cases
print("\n" + "=" * 70)
print("Problem 4: LeetCode 560 - Subarray Sum Equals K (MEDIUM)")
print("=" * 70)

test_cases_560 = [
    ([1, 1, 1], 2, 2),
    ([1, 2, 3], 3, 2),
    ([1, -1, 0], 0, 3),
    ([1], 1, 1),
    ([1, 2, 1, 2, 1], 3, 4),
    ([-1, -1, 1], 0, 1),
    ([1, 2, 3, 4, 5], 9, 2)
]
#
# for nums, k, expected in test_cases_560:
#     result = subarraySum(nums, k)
#     status = "✅" if result == expected else "❌"
#     print(f"Input: nums={nums}, k={k}")
#     print(f"Expected: {expected}, Got: {result} {status}")
#     print()

# ============================================================================
# PROBLEM 5: LeetCode 974 - Subarray Sums Divisible by K (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given an integer array nums and an integer k, return the number of 
non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: Subarrays with sum divisible by 5:
[4,5,0,-2,-3,1], [5], [5,0], [5,0,-2,-3], [0], [0,-2,-3], [-2,-3]

Example 2:
Input: nums = [5], k = 9
Output: 0

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- 2 <= k <= 10^4
"""


def subarraysDivByK(arr, k):
    """
    Approach: Prefix Sum + Hash Map with Modulo

    Key Insight:
    - Similar to "Subarray Sum Equals K" but with divisibility
    - Key observation: If (prefix[j] - prefix[i]) % k == 0
      Then subarray from i+1 to j has sum divisible by k
    - This means: prefix[j] % k == prefix[i] % k
    - So we track remainders (modulo values) instead of actual sums
    - If two positions have same remainder, their difference is divisible by k
    - Hash map stores: {remainder: count of positions with this remainder}

    Important Modulo Property:
    - In Python, -1 % 5 = 4 (always positive)
    - In some languages, -1 % 5 = -1 (can be negative)
    - To handle negative remainders: remainder = (sum % k + k) % k
    - Or in Python, just use sum % k (already handles negatives correctly)

    Algorithm:
    1. Use hash map to store {remainder: frequency}
    2. Initialize with {0: 1} (sum 0 is divisible by any k)
    3. For each element, update running sum
    4. Calculate remainder = sum % k
    5. If remainder exists in map, add its count to result
    6. Add remainder to map

    Example Walkthrough:
    nums = [4,5,0,-2,-3,1], k = 5

    i=0, num=4:
      sum=4, remainder=4%5=4
      map = {0:1, 4:1}, count=0

    i=1, num=5:
      sum=9, remainder=9%5=4
      remainder 4 exists! count += map[4] = 1
      map = {0:1, 4:2}, count=1

    i=2, num=0:
      sum=9, remainder=9%5=4
      remainder 4 exists! count += map[4] = 2
      map = {0:1, 4:3}, count=3

    ... and so on

    Why This Works:
    - If prefix[j] % k == prefix[i] % k
    - Then (prefix[j] - prefix[i]) % k == 0
    - This means sum[i+1...j] is divisible by k
    - By counting frequencies, we count all such pairs

    Pattern Recognition:
    - "divisible by k" → use modulo operation
    - "count subarrays" + "divisibility" → prefix sum + hash map with remainders
    - Similar to "Subarray Sum Equals K" but with modulo

    Time: O(n)
    Space: O(k) - at most k different remainders
    """

    i=0
    hmap = {}
    hmap[0] = 1
    count = 0
    prefix_sum = [0] * (len(arr)+1)

    while( i<len(arr) ):
        # form the prefix sum array
        prefix_sum[i+1] = prefix_sum[i] + arr[i]

        if prefix_sum[i+1]%k in hmap:
            count += hmap[ prefix_sum[i+1]%k ]

        hmap[ prefix_sum[i+1]%k ] = hmap.get( prefix_sum[i+1]%k, 0 ) + 1

        i+=1

    return count

# Test cases
print("\n" + "=" * 70)
print("Problem 5: LeetCode 974 - Subarray Sums Divisible by K")
print("=" * 70)

test_cases_974 = [
    ([4, 5, 0, -2, -3, 1], 5, 7),
    ([5], 9, 0),
    ([2, -2, 2, -4], 6, 2),
    ([-1, 2, 9], 2, 2)
]

# for nums, k, expected in test_cases_974:
#     result = subarraysDivByK(nums, k)
#     status = "✅" if result == expected else "❌"
#     print(f"Input: nums={nums}, k={k}")
#     print(f"Expected: {expected}, Got: {result} {status}")
#     print()

# ============================================================================
# PROBLEM 6: LeetCode 525 - Contiguous Array (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given a binary array nums, return the maximum length of a contiguous 
subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0,1] has equal number of 0s and 1s

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0,1] or [1,0] are the longest subarrays

Example 3:
Input: nums = [0,0,1,0,0,0,1,1]
Output: 6
Explanation: [0,1,0,0,0,1,1] has 3 zeros and 3 ones (but not longest)
             [0,0,1,0,0,0,1,1] starting at index 0 has 4 zeros and 4 ones (length 8)
             Wait, let me recalculate: [1,0,0,0,1,1] at indices 2-7 has equal 0s and 1s

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
"""


def findMaxLength(arr):
    """
    Approach: Prefix Sum + Hash Map with Clever Transformation

    Key Insight:
    - This is a BRILLIANT application of prefix sum concept
    - Key trick: Treat 0 as -1, then problem becomes "find longest subarray with sum = 0"
    - Why? If we have equal 0s and 1s, then sum of (1s and -1s) = 0
    - Example: [0,1,0,1] → [-1,1,-1,1] → sum = 0 ✅
    - Now use prefix sum: if prefix[j] == prefix[i], then sum[i+1...j] = 0
    - Hash map stores: {prefix_sum: first_index where we saw this sum}
    - We want LONGEST subarray, so store FIRST occurrence of each sum
    - Length = current_index - first_occurrence_index

    Algorithm:
    1. Use hash map to store {prefix_sum: first_index}
    2. Initialize with {0: -1} (sum 0 at index -1 for subarrays starting at 0)
    3. For each element:
       - Add 1 if element is 1, add -1 if element is 0
       - If current_sum exists in map, calculate length
       - If current_sum doesn't exist, add it to map
    4. Track maximum length

    Example Walkthrough:
    nums = [0, 1, 0, 1]
    Transform: [-1, 1, -1, 1]

    i=0, num=-1:
      sum=-1, not in map
      map = {0:-1, -1:0}, max_len=0

    i=1, num=1:
      sum=0, exists at index -1! len = 1-(-1) = 2
      map = {0:-1, -1:0}, max_len=2

    i=2, num=-1:
      sum=-1, exists at index 0! len = 2-0 = 2
      map = {0:-1, -1:0}, max_len=2

    i=3, num=1:
      sum=0, exists at index -1! len = 3-(-1) = 4
      map = {0:-1, -1:0}, max_len=4

    Result: 4 (entire array has equal 0s and 1s)

    Why Store First Occurrence?
    - We want LONGEST subarray
    - If we see same sum again, the gap from first occurrence is longer
    - Example: sum=5 at index 2, sum=5 at index 10
      → Subarray [3...10] has sum 0, length = 8

    Pattern Recognition:
    - "equal number of X and Y" → transform to "sum = 0"
    - "longest subarray" + "sum = 0" → prefix sum + hash map
    - Store first occurrence for maximum length

    Time: O(n)
    Space: O(n)
    """

    i=0
    hmap = {}
    hmap[0] = -1
    running_sum = 0
    max_length = 0

    while( i < len(arr) ):
        running_sum += -1 if arr[i] == 0 else 1

        if running_sum in hmap:
            max_length = max( max_length , i - hmap[running_sum] )
        else:
            hmap[running_sum] =  i

        i+=1

    return max_length

# Test cases
print("\n" + "=" * 70)
print("Problem 6: LeetCode 525 - Contiguous Array (MEDIUM)")
print("=" * 70)

test_cases_525 = [
    ([0, 1], 2),
    ([0, 1, 0], 2),
    ([0, 0, 1, 0, 0, 0, 1, 1], 6),
    ([0, 1, 1, 0, 1, 1, 1, 0], 4),
    ([0, 0, 0, 1, 1, 1], 6)
]

# for nums, expected in test_cases_525:
#     result = findMaxLength(nums)
#     status = "✅" if result == expected else "❌"
#     print(f"Input: {nums}")
#     print(f"Expected: {expected}, Got: {result} {status}")
#     print()


# ============================================================================
# PROBLEM 7: LeetCode 523 - Continuous Subarray Sum (MEDIUM)
# ============================================================================


"""
Problem:
--------
Given an integer array nums and an integer k, return true if nums has a 
good subarray or false otherwise.

A good subarray is a subarray where:
- its length is at least two, and
- the sum of the elements of the subarray is a multiple of k.

Example 1:
Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2,4] is a continuous subarray of size 2 whose sum is 6

Example 2:
Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23,2,6,4,7] is a continuous subarray whose sum is 42 = 7 * 6

Example 3:
Input: nums = [23,2,6,4,7], k = 13
Output: false

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= sum(nums[i]) <= 2^31 - 1
- 1 <= k <= 2^31 - 1
"""


def checkSubarraySum(nums, k):
    """
    Approach: Prefix Sum + Hash Map with Modulo (Track Indices)

    Key Insight:
    - Similar to "Subarray Sums Divisible by K" but need length >= 2
    - If (prefix[j] - prefix[i]) % k == 0, then sum[i+1...j] is divisible by k
    - This means: prefix[j] % k == prefix[i] % k
    - Hash map stores: {remainder: first_index where we saw this remainder}
    - Important: We need j - i >= 2 (subarray length >= 2)
    - So check if current_index - stored_index >= 2

    Edge Cases:
    - k = 0: Not possible per constraints (k >= 1)
    - nums[i] = 0: Handle with modulo
    - Multiple zeros: [0,0] with any k should return True

    Algorithm:
    1. Use hash map to store {remainder: first_index}
    2. Initialize with {0: -1} (for subarrays starting at index 0)
    3. For each element:
       - Update running sum
       - Calculate remainder = sum % k
       - If remainder exists and (current_index - stored_index >= 2), return True
       - If remainder doesn't exist, store it
    4. Return False if no valid subarray found

    Example Walkthrough:
    nums = [23,2,4,6,7], k = 6

    i=0, num=23:
      sum=23, remainder=23%6=5
      map = {0:-1, 5:0}

    i=1, num=2:
      sum=25, remainder=25%6=1
      map = {0:-1, 5:0, 1:1}

    i=2, num=4:
      sum=29, remainder=29%6=5
      remainder 5 exists at index 0! length = 2-0 = 2 >= 2 ✅
      Return True

    Why Store First Occurrence?
    - We want to find ANY valid subarray (length >= 2)
    - First occurrence gives us the longest possible subarray
    - But we only need to check if length >= 2

    Pattern Recognition:
    - "sum divisible by k" + "length >= 2" → prefix sum + hash map with index tracking
    - "at least" constraint → check distance between indices
    - Similar to other modulo problems but with length constraint

    Time: O(n)
    Space: O(min(n, k)) - at most k different remainders
    """

# Test cases
print("\n" + "=" * 70)
print("Problem 7: LeetCode 523 - Continuous Subarray Sum")
print("=" * 70)

test_cases_523 = [
    ([23, 2, 4, 6, 7], 6, True),
    ([23, 2, 6, 4, 7], 6, True),
    ([23, 2, 6, 4, 7], 13, False),
    ([5, 0, 0, 0], 3, True),
    ([0, 0], 1, True),
    ([1, 0], 2, False)
]

for nums, k, expected in test_cases_523:
    result = checkSubarraySum(nums, k)
    status = "✅" if result == expected else "❌"
    print(f"Input: nums={nums}, k={k}")
    print(f"Expected: {expected}, Got: {result} {status}")
    print()




# ==================== LeetCode 1248 - Count Number of Nice Subarrays ================
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


# ==================== LeetCode 930 - Binary Subarrays With Sum ================
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
    # print("Problem: LeetCode 930 - Binary Subarrays With Sum")
    # print("=" * 70)
    # test_cases_binary = [
    #     ([1, 0, 1, 0, 1], 2, 4),
    #     ([0, 0, 0, 0, 0], 0, 15),
    #     ([1, 0, 1, 0, 1], 0, 2),
    #     ([0, 1, 1, 1, 1], 3, 3),
    #     ([1, 1, 1, 1, 1], 5, 1),
    #     ([0, 1, 0], 1, 4),
    # ]
    #
    # for arr, goal, expected in test_cases_binary:
    #     result = BinarySubarraySum(arr, goal)
    #     status = "✅" if result == expected else "❌"
    #     print(f"Input: arr={arr}, goal={goal}")
    #     print(f"Expected: {expected}, Got: {result} {status}")
    #     print()

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


