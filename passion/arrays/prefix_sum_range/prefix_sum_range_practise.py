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









