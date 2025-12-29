"""
PREFIX SUM & RANGE QUERY PROBLEMS - COMPLETE SOLUTIONS
=======================================================

This file contains comprehensive solutions for prefix sum and range query problems,
organized from EASY → MEDIUM → HARD with detailed explanations and key insights.

Covers:
- PATTERN 3A: Basic Prefix Sum
- PATTERN 3B: Prefix Sum with Hash Map
- PATTERN 3C: 2D Prefix Sum

Each problem includes:
✓ Problem statement with examples
✓ Detailed key insights
✓ Step-by-step approach
✓ Optimized solution
✓ Time & space complexity
✓ Test cases with explanations
"""

# ============================================================================
# PATTERN TEMPLATE: PREFIX SUM
# ============================================================================

"""
UNIVERSAL PREFIX SUM TEMPLATE
==============================

Basic Concept:
--------------
prefix[i] = sum of elements from index 0 to i
range_sum(L, R) = prefix[R] - prefix[L-1]

Template Structure:
-------------------
def prefix_sum_template(arr):
    n = len(arr)
    prefix = [0] * (n + 1)  # Extra space for easier calculation
    
    # Build prefix sum array
    for i in range(n):
        prefix[i + 1] = prefix[i] + arr[i]
    
    # Query range sum [L, R]
    def range_sum(L, R):
        return prefix[R + 1] - prefix[L]
    
    return prefix, range_sum

Key Patterns:
-------------
1. Basic Prefix Sum: Build array, answer queries in O(1)
2. Prefix Sum + Hash Map: Track prefix sums to find subarrays with target sum
3. 2D Prefix Sum: Extend to matrices for rectangle sum queries
4. Running Sum: Maintain cumulative sum while iterating
5. Pivot Index: Find index where left_sum == right_sum
"""


# ============================================================================
# EASY PROBLEMS - FOUNDATIONAL CONCEPTS
# ============================================================================

print("=" * 70)
print("EASY PROBLEMS - MASTER THESE FIRST")
print("=" * 70)


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

def runningSum(nums):
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
    if not nums:
        return []
    
    # Build running sum in-place
    i = 1
    while i < len(nums):
        nums[i] += nums[i - 1]
        i += 1
    
    return nums


# Alternative: Using extra space
def runningSum_extra_space(nums):
    """
    Same logic but with extra space for clarity
    """
    if not nums:
        return []
    
    n = len(nums)
    result = [0] * n
    result[0] = nums[0]
    
    i = 1
    while i < n:
        result[i] = result[i - 1] + nums[i]
        i += 1
    
    return result


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

for nums in test_cases_1480:
    original = nums.copy()
    result = runningSum(nums.copy())
    print(f"Input: {original}")
    print(f"Output: {result}")
    print()


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

def pivotIndex(nums):
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
    if not nums:
        return -1
    
    # Calculate total sum
    total_sum = sum(nums)
    left_sum = 0
    
    # Check each index
    i = 0
    while i < len(nums):
        # At index i, check if left_sum == right_sum
        # right_sum = total_sum - left_sum - nums[i]
        # So we check: left_sum == total_sum - left_sum - nums[i]
        # Which simplifies to: 2 * left_sum + nums[i] == total_sum
        
        if 2 * left_sum + nums[i] == total_sum:
            return i
        
        left_sum += nums[i]
        i += 1
    
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

for nums, expected in test_cases_724:
    result = pivotIndex(nums)
    status = "✅" if result == expected else "❌"
    print(f"Input: {nums}")
    print(f"Expected: {expected}, Got: {result} {status}")
    print()


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
        """
        Build prefix sum array
        prefix[i] = sum of first i elements
        """
        n = len(nums)
        self.prefix = [0] * (n + 1)
        
        # Build prefix sum
        i = 0
        while i < n:
            self.prefix[i + 1] = self.prefix[i] + nums[i]
            i += 1
    
    def sumRange(self, left, right):
        """
        Return sum of elements from left to right inclusive
        Formula: prefix[right + 1] - prefix[left]
        """
        return self.prefix[right + 1] - self.prefix[left]


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

for left, right, expected in queries:
    result = numArray.sumRange(left, right)
    status = "✅" if result == expected else "❌"
    print(f"sumRange({left}, {right}) = {result} (expected: {expected}) {status}")


# ============================================================================
# MEDIUM PROBLEMS - CORE INTERVIEW QUESTIONS
# ============================================================================

print("\n\n" + "=" * 70)
print("MEDIUM PROBLEMS - FAANG FAVORITES")
print("=" * 70)


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
    if not nums:
        return 0
    
    # Hash map: {prefix_sum: frequency}
    prefix_map = {0: 1}  # Empty subarray has sum 0
    current_sum = 0
    count = 0
    
    i = 0
    while i < len(nums):
        # Update running sum
        current_sum += nums[i]
        
        # Check if (current_sum - k) exists
        # If yes, we found subarray(s) with sum = k
        if current_sum - k in prefix_map:
            count += prefix_map[current_sum - k]
        
        # Add current sum to map
        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1
        
        i += 1
    
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

for nums, k, expected in test_cases_560:
    result = subarraySum(nums, k)
    status = "✅" if result == expected else "❌"
    print(f"Input: nums={nums}, k={k}")
    print(f"Expected: {expected}, Got: {result} {status}")
    print()


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

def subarraysDivByK(nums, k):
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
    if not nums:
        return 0
    
    # Hash map: {remainder: frequency}
    remainder_map = {0: 1}  # Sum 0 is divisible by any k
    current_sum = 0
    count = 0
    
    i = 0
    while i < len(nums):
        # Update running sum
        current_sum += nums[i]
        
        # Calculate remainder (Python handles negative correctly)
        remainder = current_sum % k
        
        # If this remainder exists, we found subarray(s) divisible by k
        if remainder in remainder_map:
            count += remainder_map[remainder]
        
        # Add remainder to map
        remainder_map[remainder] = remainder_map.get(remainder, 0) + 1
        
        i += 1
    
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

for nums, k, expected in test_cases_974:
    result = subarraysDivByK(nums, k)
    status = "✅" if result == expected else "❌"
    print(f"Input: nums={nums}, k={k}")
    print(f"Expected: {expected}, Got: {result} {status}")
    print()


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

def findMaxLength(nums):
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
    if not nums:
        return 0
    
    # Hash map: {prefix_sum: first_index}
    sum_map = {0: -1}  # Sum 0 at index -1
    current_sum = 0
    max_length = 0
    
    i = 0
    while i < len(nums):
        # Transform: 0 → -1, 1 → 1
        current_sum += 1 if nums[i] == 1 else -1
        
        # If we've seen this sum before, calculate length
        if current_sum in sum_map:
            length = i - sum_map[current_sum]
            max_length = max(max_length, length)
        else:
            # Store first occurrence
            sum_map[current_sum] = i
        
        i += 1
    
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

for nums, expected in test_cases_525:
    result = findMaxLength(nums)
    status = "✅" if result == expected else "❌"
    print(f"Input: {nums}")
    print(f"Expected: {expected}, Got: {result} {status}")
    print()


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
    if not nums or len(nums) < 2:
        return False
    
    # Hash map: {remainder: first_index}
    remainder_map = {0: -1}  # Sum 0 at index -1
    current_sum = 0
    
    i = 0
    while i < len(nums):
        # Update running sum
        current_sum += nums[i]
        
        # Calculate remainder
        remainder = current_sum % k
        
        # Check if remainder exists and length >= 2
        if remainder in remainder_map:
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            # Store first occurrence
            remainder_map[remainder] = i
        
        i += 1
    
    return False


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

# ============================================================================
# PROBLEM 9: LeetCode 1124 - Longest Well-Performing Interval (MEDIUM/HARD)
# ============================================================================

"""
Problem:
--------
We are given hours, a list of the number of hours worked per day for a 
given employee.

A day is considered to be a tiring day if and only if the number of hours 
worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of 
tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

Example 1:
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6] (3 tiring days > 0 non-tiring)

Example 2:
Input: hours = [6,6,6]
Output: 0

Constraints:
- 1 <= hours.length <= 10^4
- 0 <= hours[i] <= 16
"""


def longestWPI(hours):
    """
    Approach: Prefix Sum + Hash Map with Transformation

    Key Insight:
    - Similar to "Contiguous Array" problem
    - Transform: hours > 8 → +1, hours <= 8 → -1
    - Problem becomes: find longest subarray with sum > 0
    - Use prefix sum: if prefix[j] > prefix[i], then sum[i+1...j] > 0
    - But we want sum > 0, not sum = 0, so approach is different
    - Hash map stores: {prefix_sum: first_index}
    - For each position with sum > 0, length = current_index + 1
    - For each position with sum <= 0, look for (sum - 1) in map
    - Why sum - 1? Because if prefix[i] = sum - 1, then sum[i+1...j] = 1 > 0

    Algorithm:
    1. Transform hours: >8 → +1, <=8 → -1
    2. Use hash map to store {prefix_sum: first_index}
    3. For each position:
       - If sum > 0, entire subarray from start is valid
       - If sum <= 0, look for (sum - 1) in map
       - Store first occurrence of each sum
    4. Track maximum length

    Example Walkthrough:
    hours = [9,9,6,0,6,6,9]
    Transform: [1,1,-1,-1,-1,-1,1]

    i=0, val=1:
      sum=1 > 0, max_len = 1
      map = {1:0}

    i=1, val=1:
      sum=2 > 0, max_len = 2
      map = {1:0, 2:1}

    i=2, val=-1:
      sum=1 > 0, max_len = 3
      map = {1:0, 2:1}

    i=3, val=-1:
      sum=0 <= 0, look for (0-1=-1) in map? No
      map = {1:0, 2:1, 0:3}

    i=4, val=-1:
      sum=-1 <= 0, look for (-1-1=-2) in map? No
      map = {1:0, 2:1, 0:3, -1:4}

    i=5, val=-1:
      sum=-2 <= 0, look for (-2-1=-3) in map? No
      map = {1:0, 2:1, 0:3, -1:4, -2:5}

    i=6, val=1:
      sum=-1 <= 0, look for (-1-1=-2) in map? Yes at index 5!
      len = 6-5 = 1, max_len = 3

    Result: 3

    Why Look for (sum - 1)?
    - We want subarray with sum > 0
    - If prefix[j] - prefix[i] > 0, then prefix[j] > prefix[i]
    - Smallest positive difference is 1
    - So we look for prefix[i] = prefix[j] - 1

    Pattern Recognition:
    - "more X than Y" → transform to sum > 0
    - "longest interval" + "sum > 0" → prefix sum + hash map
    - Similar to "Contiguous Array" but with inequality

    Time: O(n)
    Space: O(n)
    """
    if not hours:
        return 0

    # Hash map: {prefix_sum: first_index}
    sum_map = {}
    current_sum = 0
    max_length = 0

    i = 0
    while i < len(hours):
        # Transform: >8 → +1, <=8 → -1
        current_sum += 1 if hours[i] > 8 else -1

        # If sum > 0, entire subarray from start is valid
        if current_sum > 0:
            max_length = i + 1
        else:
            # Look for (sum - 1) to get subarray with sum > 0
            if current_sum - 1 in sum_map:
                length = i - sum_map[current_sum - 1]
                max_length = max(max_length, length)

            # Store first occurrence
            if current_sum not in sum_map:
                sum_map[current_sum] = i

        i += 1

    return max_length


# Test cases
print("\n" + "=" * 70)
print("Problem 9: LeetCode 1124 - Longest Well-Performing Interval")
print("=" * 70)

test_cases_1124 = [
    ([9, 9, 6, 0, 6, 6, 9], 3),
    ([6, 6, 6], 0),
    ([9, 9, 9], 3),
    ([6, 9, 9], 3),
    ([9, 6, 9, 6, 9], 5)
]

for hours, expected in test_cases_1124:
    result = longestWPI(hours)
    status = "✅" if result == expected else "❌"
    print(f"Input: {hours}")
    print(f"Expected: {expected}, Got: {result} {status}")
    print()


# ============================================================================
# MATRIX PROBLEMS
# ============================================================================

# ============================================================================
# PROBLEM 8: LeetCode 304 - Range Sum Query 2D - Immutable (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined 
by its upper left corner (row1, col1) and lower right corner (row2, col2).

Implement the NumMatrix class:
- NumMatrix(int[][] matrix) Initializes the object with the integer matrix.
- int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of 
  the elements of matrix inside the rectangle.

Example:
Input:
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2],
   [5, 6, 3, 2, 1],
   [1, 2, 0, 1, 5],
   [4, 1, 0, 1, 7],
   [1, 0, 3, 0, 5]]], 
 [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output:
[null, 8, 11, 12]

Explanation:
NumMatrix numMatrix = new NumMatrix(matrix);
numMatrix.sumRegion(2, 1, 4, 3); // return 8
numMatrix.sumRegion(1, 1, 2, 2); // return 11
numMatrix.sumRegion(1, 2, 2, 4); // return 12

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- -10^4 <= matrix[i][j] <= 10^4
- 0 <= row1 <= row2 < m
- 0 <= col1 <= col2 < n
- At most 10^4 calls will be made to sumRegion
"""

class NumMatrix:
    """
    Approach: 2D Prefix Sum
    
    Key Insight:
    - Extension of 1D prefix sum to 2D
    - prefix[i][j] = sum of all elements in rectangle from (0,0) to (i-1,j-1)
    - Use inclusion-exclusion principle to calculate rectangle sum
    - Formula for sum of rectangle (r1,c1) to (r2,c2):
      sum = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
    
    Visual Explanation:
    To get sum of rectangle (r1,c1) to (r2,c2):
    
    +-------+-------+
    |   A   |   B   |  ← prefix[r1][c2+1]
    +-------+-------+
    |   C   | TARGET|  ← prefix[r2+1][c2+1]
    +-------+-------+
            ↑
    prefix[r2+1][c1]
    
    TARGET = prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]
    
    Why add prefix[r1][c1]?
    - We subtracted it twice (once in each subtraction)
    - So we need to add it back once
    
    Building 2D Prefix Sum:
    prefix[i][j] = matrix[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    Visual:
    +-------+-------+
    | P[i-1]| P[i-1]|
    | [j-1] | [j]   |
    +-------+-------+
    | P[i]  | P[i]  |
    | [j-1] | [j]   | ← We're calculating this
    +-------+-------+
    
    Pattern Recognition:
    - "2D matrix" + "multiple range queries" → 2D prefix sum
    - "rectangle sum" → inclusion-exclusion principle
    - Trade space O(m*n) for time O(1) per query
    
    Time: O(m*n) for init, O(1) for sumRegion
    Space: O(m*n)
    """
    
    def __init__(self, matrix):
        """
        Build 2D prefix sum array
        prefix[i][j] = sum of rectangle from (0,0) to (i-1,j-1)
        """
        if not matrix or not matrix[0]:
            self.prefix = [[]]
            return
        
        m, n = len(matrix), len(matrix[0])
        # Extra row and column for easier calculation
        self.prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build 2D prefix sum
        i = 1
        while i <= m:
            j = 1
            while j <= n:
                self.prefix[i][j] = (
                    matrix[i-1][j-1] +
                    self.prefix[i-1][j] +
                    self.prefix[i][j-1] -
                    self.prefix[i-1][j-1]
                )
                j += 1
            i += 1
    
    def sumRegion(self, row1, col1, row2, col2):
        """
        Return sum of rectangle from (row1,col1) to (row2,col2)
        Using inclusion-exclusion principle
        """
        return (
            self.prefix[row2+1][col2+1] -
            self.prefix[row1][col2+1] -
            self.prefix[row2+1][col1] +
            self.prefix[row1][col1]
        )


# Test cases
print("\n" + "=" * 70)
print("Problem 8: LeetCode 304 - Range Sum Query 2D - Immutable")
print("=" * 70)

matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

numMatrix = NumMatrix(matrix)

queries = [
    (2, 1, 4, 3, 8),
    (1, 1, 2, 2, 11),
    (1, 2, 2, 4, 12),
    (0, 0, 4, 4, 58)
]

print("Matrix:")
for row in matrix:
    print(row)
print()

for row1, col1, row2, col2, expected in queries:
    result = numMatrix.sumRegion(row1, col1, row2, col2)
    status = "✅" if result == expected else "❌"
    print(f"sumRegion({row1}, {col1}, {row2}, {col2}) = {result} (expected: {expected}) {status}")



# ============================================================================
# HARD PROBLEMS - ADVANCED TECHNIQUES
# ============================================================================

print("\n\n" + "=" * 70)
print("HARD PROBLEMS - MASTER LEVEL")
print("=" * 70)




# ============================================================================
# PROBLEM 10: LeetCode 1314 - Matrix Block Sum (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a m x n matrix mat and an integer k, return a matrix answer where 
each answer[i][j] is the sum of all elements mat[r][c] for:
- i - k <= r <= i + k
- j - k <= c <= j + k
- (r, c) is a valid position in the matrix

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]

Constraints:
- m == mat.length
- n == mat[i].length
- 1 <= m, n, k <= 100
- 1 <= mat[i][j] <= 100
"""

def matrixBlockSum(mat, k):
    """
    Approach: 2D Prefix Sum with Boundary Handling
    
    Key Insight:
    - For each cell (i,j), we need sum of rectangle:
      - Top-left: (max(0, i-k), max(0, j-k))
      - Bottom-right: (min(m-1, i+k), min(n-1, j+k))
    - Use 2D prefix sum to calculate rectangle sum in O(1)
    - Build prefix sum array first, then calculate each answer cell
    - Handle boundaries carefully (don't go out of matrix bounds)
    
    Algorithm:
    1. Build 2D prefix sum array (same as Problem 8)
    2. For each cell (i,j) in result:
       - Calculate boundaries: r1, c1, r2, c2
       - Use prefix sum to get rectangle sum
    3. Return result matrix
    
    Boundary Calculation:
    - r1 = max(0, i - k)
    - c1 = max(0, j - k)
    - r2 = min(m - 1, i + k)
    - c2 = min(n - 1, j + k)
    
    Pattern Recognition:
    - "sum of neighbors" + "k-distance" → 2D prefix sum
    - "for each cell" + "rectangle sum" → precompute prefix sum
    - Similar to range query but with dynamic ranges
    
    Time: O(m*n) for building prefix + O(m*n) for calculating answer = O(m*n)
    Space: O(m*n) for prefix array
    """
    if not mat or not mat[0]:
        return []
    
    m, n = len(mat), len(mat[0])
    
    # Build 2D prefix sum
    prefix = [[0] * (n + 1) for _ in range(m + 1)]
    
    i = 1
    while i <= m:
        j = 1
        while j <= n:
            prefix[i][j] = (
                mat[i-1][j-1] +
                prefix[i-1][j] +
                prefix[i][j-1] -
                prefix[i-1][j-1]
            )
            j += 1
        i += 1
    
    # Calculate answer for each cell
    answer = [[0] * n for _ in range(m)]
    
    i = 0
    while i < m:
        j = 0
        while j < n:
            # Calculate boundaries
            r1 = max(0, i - k)
            c1 = max(0, j - k)
            r2 = min(m - 1, i + k)
            c2 = min(n - 1, j + k)
            
            # Calculate rectangle sum using prefix
            answer[i][j] = (
                prefix[r2+1][c2+1] -
                prefix[r1][c2+1] -
                prefix[r2+1][c1] +
                prefix[r1][c1]
            )
            
            j += 1
        i += 1
    
    return answer


# Test cases
print("\n" + "=" * 70)
print("Problem 10: LeetCode 1314 - Matrix Block Sum")
print("=" * 70)

test_cases_1314 = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [[12, 21, 16], [27, 45, 33], [24, 39, 28]]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, [[45, 45, 45], [45, 45, 45], [45, 45, 45]])
]

for mat, k, expected in test_cases_1314:
    result = matrixBlockSum(mat, k)
    status = "✅" if result == expected else "❌"
    print(f"Input: mat={mat}, k={k}")
    print(f"Expected: {expected}")
    print(f"Got: {result} {status}")
    print()


# ============================================================================
# SUMMARY & KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 70)
print("SUMMARY: PREFIX SUM & RANGE QUERY PATTERNS")
print("=" * 70)

print("""
KEY PATTERNS:
=============

1. BASIC PREFIX SUM (Problems 1-3)
   - Build prefix array: prefix[i] = sum of first i elements
   - Range query: sum[L,R] = prefix[R+1] - prefix[L]
   - Use case: Multiple range queries on immutable array
   - Time: O(n) build, O(1) query
   - Space: O(n)

2. PREFIX SUM + HASH MAP (Problems 4-7)
   - Track prefix sums in hash map
   - Find subarrays with target sum/property
   - Key formula: prefix[j] - prefix[i] = k → prefix[i] = prefix[j] - k
   - Use case: Count/find subarrays with specific sum
   - Time: O(n)
   - Space: O(n)

3. MODULO WITH PREFIX SUM (Problems 5, 7)
   - Use remainders instead of actual sums
   - Find subarrays divisible by k
   - Key: Same remainder → difference divisible by k
   - Use case: Divisibility problems
   - Time: O(n)
   - Space: O(k)

4. TRANSFORMATION TRICK (Problems 6, 9)
   - Transform problem to "find subarray with sum = 0" or "sum > 0"
   - Example: Equal 0s and 1s → treat 0 as -1, find sum = 0
   - Example: More X than Y → treat X as +1, Y as -1, find sum > 0
   - Use case: Balance/comparison problems
   - Time: O(n)
   - Space: O(n)

5. 2D PREFIX SUM (Problems 8, 10)
   - Extend to matrices for rectangle queries
   - Build: prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1]
   - Query: Use inclusion-exclusion principle
   - Use case: Matrix range queries
   - Time: O(m*n) build, O(1) query
   - Space: O(m*n)

PROBLEM IDENTIFICATION:
=======================
- "range sum" + "multiple queries" → Basic prefix sum
- "subarray sum equals k" → Prefix sum + hash map
- "divisible by k" → Prefix sum + hash map with modulo
- "equal number of X and Y" → Transform to sum = 0
- "more X than Y" → Transform to sum > 0
- "matrix" + "rectangle sum" → 2D prefix sum
- "at least length k" → Track indices in hash map

COMMON MISTAKES TO AVOID:
=========================
1. Forgetting to initialize hash map with {0: -1} or {0: 1}
2. Not handling negative numbers correctly
3. Off-by-one errors in prefix array indexing
4. Forgetting length constraint (e.g., length >= 2)
5. Not storing first occurrence for longest subarray problems
6. Incorrect 2D prefix sum formula (inclusion-exclusion)
7. Not handling matrix boundaries correctly

INTERVIEW TIPS:
===============
1. Always ask: "Can array have negative numbers?" (affects approach)
2. Clarify: "Do we need to return indices or just count?"
3. Consider: "Is array mutable or immutable?" (affects preprocessing)
4. Think: "Can I transform the problem?" (0→-1, >8→+1, etc.)
5. Remember: Hash map stores FIRST occurrence for longest subarray
6. Remember: Hash map stores FREQUENCY for counting subarrays
7. For 2D problems, draw the rectangle and inclusion-exclusion diagram

COMPLEXITY PATTERNS:
====================
- Basic prefix sum: O(n) time, O(n) space
- Prefix sum + hash map: O(n) time, O(n) space
- Prefix sum + modulo: O(n) time, O(k) space
- 2D prefix sum: O(m*n) time, O(m*n) space

MUST-KNOW PROBLEMS FOR FAANG:
==============================
⭐⭐⭐ LeetCode 560: Subarray Sum Equals K (Most Important!)
⭐⭐⭐ LeetCode 525: Contiguous Array (Clever transformation)
⭐⭐ LeetCode 974: Subarray Sums Divisible by K
⭐⭐ LeetCode 523: Continuous Subarray Sum
⭐⭐ LeetCode 304: Range Sum Query 2D

PRACTICE PROGRESSION:
=====================
Week 1: Problems 1-3 (Basic prefix sum)
Week 2: Problems 4-5 (Prefix sum + hash map)
Week 3: Problems 6-7 (Transformation + modulo)
Week 4: Problems 8-10 (2D prefix sum + advanced)

All solutions use optimal time and space complexity!
Master these patterns and you'll ace prefix sum problems in interviews! 🚀
""")

print("=" * 70)
print("END OF PREFIX SUM & RANGE QUERY SOLUTIONS")
print("=" * 70)
