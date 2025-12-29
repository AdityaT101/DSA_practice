"""
Final Dynamic Programming Problems
==================================
This file contains additional high-frequency dynamic programming problems
commonly asked in FAANG and top tech company interviews that weren't included
in the previous files.

Each problem includes:
1. Problem statement and examples
2. Key insights for solving
3. Pattern template/approach
4. Solution with detailed explanations
5. Time and space complexity
6. Test cases with expected outputs

These problems complete the comprehensive DP problem collection.
"""

# ============================================================================
# MEDIUM PROBLEMS
# ============================================================================


# ============================================================================
# PROBLEM 1: LeetCode 213 - House Robber II (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are a professional robber planning to rob houses along a street. Each house has a certain amount 
of money stashed. All houses at this place are arranged in a circle. That means the first house is 
the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it 
will automatically contact the police if two adjacent houses were broken into on the same night.

Given an array nums representing the amount of money of each house, return the maximum amount of 
money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000
"""

def rob(nums):
    """
    Approach: Dynamic Programming with Case Analysis
    
    Key Insight:
    - This is an extension of the House Robber problem, but with houses arranged in a circle
    - The circular arrangement means we can't rob both the first and last houses
    - We can break the problem into two cases:
      1. Rob houses 0 to n-2 (exclude last house)
      2. Rob houses 1 to n-1 (exclude first house)
    - Apply the original House Robber DP solution to each case
    - Take the maximum of the two results
    
    DP State:
    - dp[i] = maximum amount that can be robbed up to house i
    
    DP Recurrence:
    - dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    Pattern Recognition:
    - Case analysis (breaking circular problem into linear problems)
    - Reusing simpler DP solutions
    - Non-adjacent item selection
    
    Time: O(n) - two passes through the array
    Space: O(1) - using only a few variables
    """
    def rob_simple(arr):
        """Helper function to solve the original House Robber problem"""
        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]
        
        # Track maximum money up to two houses back and one house back
        prev2 = arr[0]
        prev1 = max(arr[0], arr[1])
        
        for i in range(2, len(arr)):
            # Current maximum is either rob current + prev2, or skip current (prev1)
            current = max(arr[i] + prev2, prev1)
            prev2, prev1 = prev1, current
        
        return prev1
    
    n = len(nums)
    
    # Handle edge cases
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    
    # Case 1: Rob houses 0 to n-2 (exclude last house)
    # Case 2: Rob houses 1 to n-1 (exclude first house)
    return max(rob_simple(nums[:-1]), rob_simple(nums[1:]))


# Test cases
print("\n" + "=" * 70)
print("Problem 1: LeetCode 213 - House Robber II")
print("=" * 70)

test_cases_213 = [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),
    ([200, 3, 140, 20, 10], 340)
]

for nums, expected in test_cases_213:
    result = rob(nums)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 2: LeetCode 494 - Target Sum (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer 
in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build 
the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:
Input: nums = [1], target = 1
Output: 1

Constraints:
- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000
"""

def findTargetSumWays(nums, target):
    """
    Approach: Dynamic Programming (Subset Sum Variation)
    
    Key Insight:
    - This problem can be transformed into a subset sum problem:
      * Let P be the positive subset and N be the negative subset
      * sum(P) - sum(N) = target
      * sum(P) + sum(N) = sum(nums)
      * 2 * sum(P) = target + sum(nums)
      * sum(P) = (target + sum(nums)) / 2
    - So we need to find the number of ways to choose a subset that sums to (target + sum(nums)) / 2
    
    DP State:
    - dp[i][j] = number of ways to get sum j using first i elements
    - Optimized 1D: dp[j] = number of ways to get sum j
    
    DP Recurrence:
    - dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
    - Optimized 1D: dp[j] = dp[j] + dp[j-num]
    
    Pattern Recognition:
    - Subset sum counting variation
    - State transformation to simplify problem
    - Bottom-up DP
    
    Time: O(n * sum) where sum is the transformed target
    Space: O(sum) for the optimized solution
    """
    total = sum(nums)
    
    # Handle edge cases
    if abs(target) > total or (target + total) % 2 != 0:
        return 0
    
    # The target sum for the subset problem
    subset_sum = (target + total) // 2
    
    # Optimized 1D DP
    dp = [0] * (subset_sum + 1)
    dp[0] = 1  # Base case: there's 1 way to get sum 0 (take no elements)
    
    for num in nums:
        for j in range(subset_sum, num - 1, -1):
            dp[j] += dp[j - num]
    
    return dp[subset_sum]


# Test cases
print("\n" + "=" * 70)
print("Problem 2: LeetCode 494 - Target Sum")
print("=" * 70)

test_cases_494 = [
    ([1, 1, 1, 1, 1], 3, 5),
    ([1], 1, 1),
    ([1, 2, 1], 0, 2),
    ([0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 256)
]

for nums, target, expected in test_cases_494:
    result = findTargetSumWays(nums, target)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums}, target={target} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 3: LeetCode 64 - Minimum Path Sum (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
- m == grid.length
- n == grid[i].length
- 1 <= m, n <= 200
- 0 <= grid[i][j] <= 100
"""

def minPathSum(grid):
    """
    Approach: Dynamic Programming (2D Grid)
    
    Key Insight:
    - At each cell, the minimum path sum is the cell's value plus the minimum of:
      1. The minimum path sum to the cell above
      2. The minimum path sum to the cell on the left
    - We can use DP to build up the solution from the top-left to bottom-right
    - This is a classic grid traversal minimization problem
    
    DP State:
    - dp[i][j] = minimum path sum to reach cell (i, j)
    
    DP Recurrence:
    - dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    - Handle edge cases for first row and column
    
    Pattern Recognition:
    - Grid traversal with constraints
    - Minimization problem
    - Bottom-up DP with base cases
    
    Time: O(m * n) where m, n are the grid dimensions
    Space: O(m * n) for the DP table (can be optimized to O(n) with 1D array)
    """
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    # Initialize DP table with grid values
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = grid[0][0]
    
    # Fill first row
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    # Fill first column
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    # Fill rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    
    return dp[m-1][n-1]


# Space-optimized solution
def minPathSum_optimized(grid):
    """
    Space-optimized solution using 1D array
    
    Time: O(m * n)
    Space: O(n) - only need to store one row
    """
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    dp = [float('inf')] * n
    dp[0] = 0
    
    for i in range(m):
        dp[0] = dp[0] + grid[i][0]
        
        for j in range(1, n):
            dp[j] = grid[i][j] + min(dp[j-1], dp[j])
    
    return dp[n-1]


# Test cases
print("\n" + "=" * 70)
print("Problem 3: LeetCode 64 - Minimum Path Sum")
print("=" * 70)

test_cases_64 = [
    ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
    ([[1, 2, 3], [4, 5, 6]], 12),
    ([[1, 2], [1, 1]], 3),
    ([[1]], 1)
]

for grid, expected in test_cases_64:
    result = minPathSum(grid)
    status = "✅" if result == expected else "❌"
    print(f"grid=[...] → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 4: LeetCode 338 - Counting Bits (EASY) ⭐⭐
# ============================================================================

"""
Problem:
--------
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
- 0 <= n <= 10^5
"""

def countBits(n):
    """
    Approach: Dynamic Programming with Bit Manipulation
    
    Key Insight:
    - The number of 1's in the binary representation of a number follows a pattern
    - For number i, the count of 1's is related to previous numbers
    - i & (i - 1) removes the rightmost 1 bit in i
    - So, the count of 1's in i = 1 + count of 1's in (i & (i - 1))
    - Alternatively, we can use the pattern where count(i) = count(i >> 1) + (i & 1)
    
    DP State:
    - dp[i] = number of 1's in the binary representation of i
    
    DP Recurrence:
    - dp[i] = dp[i & (i - 1)] + 1
    - Alternative: dp[i] = dp[i >> 1] + (i & 1)
    
    Pattern Recognition:
    - Bit manipulation with DP
    - Finding patterns in binary representation
    - Leveraging bitwise operations
    
    Time: O(n) - one pass through numbers 0 to n
    Space: O(n) - for the result array
    """
    # Initialize array with 0 for all indices
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Use bit manipulation: count of 1's in i = count in (i & (i-1)) + 1
        dp[i] = dp[i & (i - 1)] + 1
    
    return dp


# Alternative solution using right shift pattern
def countBits_alternative(n):
    """
    Alternative approach using right shift pattern
    
    Time: O(n)
    Space: O(n)
    """
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Right shift drops the rightmost bit
        # Add 1 if the rightmost bit was 1
        dp[i] = dp[i >> 1] + (i & 1)
    
    return dp


# Test cases
print("\n" + "=" * 70)
print("Problem 4: LeetCode 338 - Counting Bits")
print("=" * 70)

test_cases_338 = [
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 1, 2]),
    (10, [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2])
]

for n, expected in test_cases_338:
    result = countBits(n)
    status = "✅" if result == expected else "❌"
    print(f"n={n} → {result} (expected: {expected}) {status}")


# ============================================================================
# HARD PROBLEMS
# ============================================================================


# ============================================================================
# PROBLEM 5: LeetCode 354 - Russian Doll Envelopes (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and 
height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater 
than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Constraints:
- 1 <= envelopes.length <= 10^5
- envelopes[i].length == 2
- 1 <= wi, hi <= 10^5
"""

def maxEnvelopes(envelopes):
    """
    Approach: Sorting + Longest Increasing Subsequence
    
    Key Insight:
    - Sort the envelopes by width in ascending order
    - For envelopes with the same width, sort by height in descending order
    - This ensures we can only choose one envelope of a given width
    - Then find the longest increasing subsequence based on height
    - This 2D problem is transformed into a 1D LIS problem
    
    DP State:
    - dp[i] = length of longest increasing subsequence ending at envelope i
    
    Pattern Recognition:
    - 2D extension of LIS
    - Sorting to simplify problem
    - Clever transformation from 2D to 1D
    - Binary search optimization
    
    Time: O(n log n) for sorting and binary search
    Space: O(n) for the dp array
    """
    if not envelopes:
        return 0
    
    # Sort by width ascending, then by height descending
    # This ensures we can't have two envelopes with same width in the LIS
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    # Extract heights to form the LIS problem
    heights = [env[1] for env in envelopes]
    
    # Find LIS with patience sort (binary search optimization)
    lis = []
    
    for height in heights:
        # Find the position to insert height in lis
        left, right = 0, len(lis)
        
        while left < right:
            mid = (left + right) // 2
            if lis[mid] < height:
                left = mid + 1
            else:
                right = mid
        
        # If height is larger than all elements in lis, append it
        if left == len(lis):
            lis.append(height)
        else:
            # Otherwise, replace the first element that is >= height
            lis[left] = height
    
    return len(lis)


# Test cases
print("\n" + "=" * 70)
print("Problem 5: LeetCode 354 - Russian Doll Envelopes")
print("=" * 70)

test_cases_354 = [
    ([[5, 4], [6, 4], [6, 7], [2, 3]], 3),
    ([[1, 1], [1, 1], [1, 1]], 1),
    ([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]], 4),
    ([[30, 50], [12, 2], [3, 4], [12, 15]], 3)
]

for envelopes, expected in test_cases_354:
    result = maxEnvelopes(envelopes)
    status = "✅" if result == expected else "❌"
    print(f"envelopes={envelopes} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 6: LeetCode 174 - Dungeon Game (HARD) ⭐⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. 
The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned 
in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health 
point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health 
upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that 
increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the 
bottom-right room where the princess is imprisoned.

Example 1:
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: 
RIGHT-> RIGHT -> DOWN -> DOWN.

Example 2:
Input: dungeon = [[0]]
Output: 1

Constraints:
- m == dungeon.length
- n == dungeon[i].length
- 1 <= m, n <= 200
- -1000 <= dungeon[i][j] <= 1000
"""

def calculateMinimumHP(dungeon):
    """
    Approach: Dynamic Programming (Bottom-Up, Right-to-Left)
    
    Key Insight:
    - Unlike typical grid problems, work backwards from bottom-right to top-left
    - Define dp[i][j] as minimum health needed at position (i,j) to reach princess
    - At each cell, take the minimum health needed from right or down cells,
      then subtract the value of the current cell
    - Ensure health never falls below 1
    
    DP State:
    - dp[i][j] = minimum health needed at position (i,j)
    
    DP Recurrence:
    - dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
    
    Pattern Recognition:
    - Reverse grid DP (bottom-up, right-to-left)
    - Min-max optimization
    - Health preservation constraint
    - Working backwards from goal
    
    Time: O(m * n) where m, n are dimensions of dungeon
    Space: O(m * n) for the DP table (can be optimized to O(n))
    """
    if not dungeon or not dungeon[0]:
        return 0
    
    m, n = len(dungeon), len(dungeon[0])
    
    # Initialize DP table with large values
    dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
    
    # Base case: need 1 health to be at princess cell (after accounting for cell value)
    dp[m][n-1] = dp[m-1][n] = 1
    
    # Fill the DP table from bottom-right to top-left
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # Minimum health needed from the next rooms
            min_health_needed = min(dp[i+1][j], dp[i][j+1])
            
            # Health needed at current cell
            dp[i][j] = max(1, min_health_needed - dungeon[i][j])
    
    return dp[0][0]


# Space-optimized solution
def calculateMinimumHP_optimized(dungeon):
    """
    Space-optimized solution using 1D array
    
    Time: O(m * n)
    Space: O(n)
    """
    if not dungeon or not dungeon[0]:
        return 0
    
    m, n = len(dungeon), len(dungeon[0])
    dp = [float('inf')] * (n + 1)
    dp[n-1] = 1
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # Minimum health needed from the next rooms
            min_health_needed = min(dp[j], dp[j+1])
            
            # Health needed at current cell
            dp[j] = max(1, min_health_needed - dungeon[i][j])
    
    return dp[0]


# Test cases
print("\n" + "=" * 70)
print("Problem 6: LeetCode 174 - Dungeon Game")
print("=" * 70)

test_cases_174 = [
    ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
    ([[0]], 1),
    ([[-3, 5]], 4),
    ([[1, -4, 5, -99], [2, -2, -2, -1]], 3)
]

for dungeon, expected in test_cases_174:
    result = calculateMinimumHP(dungeon)
    status = "✅" if result == expected else "❌"
    print(f"dungeon={dungeon} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 7: LeetCode 583 - Delete Operation for Two Strings (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English letters.
"""

def minDistance(word1, word2):
    """
    Approach: Dynamic Programming (Longest Common Subsequence)
    
    Key Insight:
    - The problem reduces to finding the longest common subsequence (LCS)
    - After finding the LCS, the minimum deletions needed is:
      (length of word1 - LCS) + (length of word2 - LCS)
    - This counts characters in each string that aren't part of the LCS
    
    DP State:
    - dp[i][j] = length of LCS between word1[0...i-1] and word2[0...j-1]
    
    DP Recurrence:
    - If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    Pattern Recognition:
    - LCS application
    - String transformation
    - Converting one problem to another
    - Deletion minimization
    
    Time: O(m * n) where m, n are lengths of word1 and word2
    Space: O(m * n) for the DP table (can be optimized to O(min(m, n)))
    """
    m, n = len(word1), len(word2)
    
    # Initialize DP table for LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Calculate minimum deletions
    lcs_length = dp[m][n]
    min_deletions = (m - lcs_length) + (n - lcs_length)
    
    return min_deletions


# Test cases
print("\n" + "=" * 70)
print("Problem 7: LeetCode 583 - Delete Operation for Two Strings")
print("=" * 70)

test_cases_583 = [
    ("sea", "eat", 2),
    ("leetcode", "etco", 4),
    ("abc", "def", 6),
    ("intention", "execution", 8)
]

for word1, word2, expected in test_cases_583:
    result = minDistance(word1, word2)
    status = "✅" if result == expected else "❌"
    print(f"word1='{word1}', word2='{word2}' → {result} (expected: {expected}) {status}")


# ============================================================================
# CONCLUSION AND FINAL SUMMARY
# ============================================================================

"""
Complete Dynamic Programming Pattern Collection:

This collection of problems covers all major DP patterns and techniques that appear
in technical interviews at top tech companies:

1. Linear DP:
   - Basic: Climbing Stairs, House Robber, Min Cost Climbing Stairs
   - Advanced: House Robber II (circular), Decode Ways

2. Grid/Matrix DP:
   - Path Problems: Unique Paths, Minimum Path Sum
   - Area Problems: Maximal Rectangle, Maximal Square
   - Complex Constraints: Dungeon Game

3. String Processing DP:
   - Substring/Subsequence: Longest Palindromic Substring/Subsequence, LCS
   - String Matching: Interleaving String, Edit Distance, Regular Expression Matching
   - Transformation: Delete Operation for Two Strings

4. Optimization Problems:
   - Knapsack Variations: Partition Equal Subset Sum, Target Sum
   - Interval Problems: Burst Balloons, Maximum Profit in Job Scheduling

5. State Machine DP:
   - Stock Trading: Best Time to Buy and Sell Stock with Cooldown/Transactions
   - Multiple States: Longest Valid Parentheses

6. Counting Problems:
   - Combinatorial: Distinct Subsequences, Palindromic Substrings
   - Bit Manipulation: Counting Bits

7. Advanced Techniques:
   - 2D Extension of 1D Problems: Russian Doll Envelopes (2D LIS)
   - Binary Search Optimization: Longest Increasing Subsequence
   - Case Analysis: House Robber II, Best Time to Buy and Sell Stock III/IV

Mastering these problems and patterns will prepare you for virtually any dynamic 
programming challenge in technical interviews.
"""
