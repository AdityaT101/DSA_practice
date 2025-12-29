"""
Dynamic Programming Problem Solutions

This file contains solutions to common dynamic programming problems,
organized by difficulty level (Easy, Medium, Hard).
Each problem includes:
- Problem statement
- Key insights for understanding the dynamic programming approach
- Pattern template
- Time and space complexity analysis
- Detailed solution with comments
- Test cases

Problems are carefully selected to cover:
1. Classic DP problems
2. FAANG interview questions
3. High-frequency interview questions
4. Various DP patterns (e.g., sequences, grids, optimization)
"""

# ============================================================================
# EASY PROBLEMS - FUNDAMENTALS OF DP
# ============================================================================


# ============================================================================
# CORE DP PATTERNS
# ============================================================================

# 1. Bottom-up iterative (tabulation)
def dp_bottom_up_template(problem_input):
    # 1. Define the state (what each cell in the DP table means)
    # 2. Initialize the base cases
    dp = [0] * n
    dp[0] = base_case
    
    # 3. State transitions (fill the table)
    for i in range(1, n):
        dp[i] = some_function(dp[i-1], ...)
    
    # 4. Return the final state
    return dp[n-1]

# 2. Top-down recursive with memoization
def dp_top_down_template(problem_input):
    # Memoization cache
    memo = {}
    
    def dp(state):
        # 1. Base cases
        if state in base_cases:
            return base_case_value
            
        # 2. Check if already calculated
        if state in memo:
            return memo[state]
            
        # 3. Calculate result using subproblems
        result = some_function(dp(smaller_state), ...)
            
        # 4. Store in memo and return
        memo[state] = result
        return result
        
    return dp(initial_state)


# ============================================================================
# PROBLEM 1: LeetCode 70 - Climbing Stairs (EASY)
# ============================================================================

"""
Problem:
--------
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
- 1 <= n <= 45
"""

def climbStairs(n):
    """
    Approach: 1D Dynamic Programming (Bottom-Up)
    
    Key Insight:
    - This is a classic Fibonacci sequence problem in disguise
    - For any stair i, we can reach it by:
      1. Taking a single step from stair (i-1)
      2. Taking a double step from stair (i-2)
    - Thus, number of ways to reach stair i = ways to reach (i-1) + ways to reach (i-2)
    - Base cases: 1 way to reach step 1, 2 ways to reach step 2
    - Drawing the decision tree shows overlapping subproblems
    
    DP State:
    - dp[i] = number of distinct ways to reach step i
    
    DP Recurrence:
    - dp[i] = dp[i-1] + dp[i-2]
    
    Pattern Template:
    1. Define what each state in our DP array represents
    2. Identify the base cases
    3. Write the recurrence relation to transition between states
    4. Determine the order to fill the DP array
    5. Return the final answer
    
    Time: O(n) - we calculate each step once
    Space: O(n) - for the DP array (can be optimized to O(1))
    """
    # Handle base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Initialize DP array
    dp = [0] * (n + 1)
    dp[1] = 1  # One way to reach step 1
    dp[2] = 2  # Two ways to reach step 2
    
    # Fill DP array using recurrence relation
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


# Optimized solution with constant space
def climbStairs_optimized(n):
    """
    Space-optimized version using just two variables
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Initialize the first two values
    a, b = 1, 2
    
    # Calculate the next values
    for i in range(3, n + 1):
        a, b = b, a + b
    
    return b


# Test cases
print("\n" + "=" * 70)
print("Problem 1: LeetCode 70 - Climbing Stairs")
print("=" * 70)

test_cases_70 = [
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8)
]

for n, expected in test_cases_70:
    result = climbStairs(n)
    status = "✅" if result == expected else "❌"
    print(f"n={n} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 2: LeetCode 198 - House Robber (EASY/MEDIUM)
# ============================================================================

"""
Problem:
--------
You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security systems connected 
and it will automatically contact the police if two adjacent houses were broken 
into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400
"""

def rob(nums):
    """
    Approach: 1D Dynamic Programming
    
    Key Insight:
    - At each house, we have two options:
      1. Rob this house + maximum money from houses up to i-2
      2. Skip this house + maximum money from houses up to i-1
    - Take the maximum of these two options
    - The decision at each step affects future decisions (optimal substructure)
    - The same subproblems are evaluated multiple times (overlapping subproblems)
    
    DP State:
    - dp[i] = maximum amount that can be robbed up to house i
    
    DP Recurrence:
    - dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
    Pattern Recognition:
    - Non-adjacent item selection problem
    - Need to keep track of "include current" vs "exclude current"
    - Decision at each step depends on previous decisions
    
    Time: O(n) - we process each house once
    Space: O(n) - for the DP array (can be optimized to O(1))
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, n):
        # Either rob current house + money from i-2, or skip current house
        dp[i] = max(nums[i] + dp[i-2], dp[i-1])
    
    return dp[n-1]


# Optimized solution with constant space
def rob_optimized(nums):
    """
    Space-optimized version using just two variables
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Track maximum money up to two houses back and one house back
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        # Current maximum is either rob current + prev2, or skip current (prev1)
        current = max(nums[i] + prev2, prev1)
        prev2, prev1 = prev1, current
    
    return prev1


# Test cases
print("\n" + "=" * 70)
print("Problem 2: LeetCode 198 - House Robber")
print("=" * 70)

test_cases_198 = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([2, 1, 1, 2], 4)
]

for nums, expected in test_cases_198:
    result = rob(nums)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 3: LeetCode 746 - Min Cost Climbing Stairs (EASY)
# ============================================================================

"""
Problem:
--------
You are given an integer array cost where cost[i] is the cost of ith step on a 
staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:
- 2 <= cost.length <= 1000
- 0 <= cost[i] <= 999
"""

def minCostClimbingStairs(cost):
    """
    Approach: 1D Dynamic Programming
    
    Key Insight:
    - At each step i, we can arrive either from step i-1 or step i-2
    - We want the minimum cost path to reach each step
    - After paying the cost at a step, we can take 1 or 2 steps forward
    - We need to reach the "top" which is the position after the last element
    
    DP State:
    - dp[i] = minimum cost to reach step i
    
    DP Recurrence:
    - dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    Pattern Recognition:
    - Path optimization problem (find min/max path)
    - Decision depends on previous steps
    - Need to track minimum cumulative cost
    
    Time: O(n) - we process each step once
    Space: O(n) - for the DP array (can be optimized to O(1))
    """
    n = len(cost)
    
    # Initialize DP array
    dp = [0] * n
    dp[0] = cost[0]
    dp[1] = cost[1]
    
    # Fill DP array
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    
    # Return minimum of last two steps (can reach top from either)
    return min(dp[n-1], dp[n-2])


# Optimized solution with constant space
def minCostClimbingStairs_optimized(cost):
    """
    Space-optimized version using just two variables
    """
    n = len(cost)
    prev1 = cost[1]
    prev2 = cost[0]
    
    for i in range(2, n):
        current = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, current
    
    return min(prev1, prev2)


# Test cases
print("\n" + "=" * 70)
print("Problem 3: LeetCode 746 - Min Cost Climbing Stairs")
print("=" * 70)

test_cases_746 = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)
]

for cost, expected in test_cases_746:
    result = minCostClimbingStairs(cost)
    status = "✅" if result == expected else "❌"
    print(f"cost={cost} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 4: LeetCode 303 - Range Sum Query - Immutable (EASY)
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

Example:
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
- At most 10^4 calls will be made to sumRange.
"""

class NumArray:
    """
    Approach: Prefix Sum (DP)
    
    Key Insight:
    - Precompute cumulative sums to efficiently answer range queries
    - The sum of range [i, j] can be calculated as prefix_sum[j+1] - prefix_sum[i]
    - We add 1 to the indices in the prefix sum array to simplify boundary cases
    - This is a simple but powerful application of dynamic programming
    
    DP State:
    - prefix_sum[i] = sum of all elements from nums[0] to nums[i-1]
    
    DP Recurrence:
    - prefix_sum[i+1] = prefix_sum[i] + nums[i]
    
    Pattern Recognition:
    - Range query optimization
    - Precomputation to make repeated queries efficient
    - Trading construction time for query time
    
    Time: 
    - Constructor: O(n) - building the prefix sum array
    - sumRange: O(1) - constant time lookup
    Space: O(n) - for the prefix sum array
    """
    def __init__(self, nums):
        n = len(nums)
        self.prefix_sum = [0] * (n + 1)
        
        # Build prefix sum array
        for i in range(n):
            self.prefix_sum[i + 1] = self.prefix_sum[i] + nums[i]
    
    def sumRange(self, left, right):
        # Return sum of range using prefix sums
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# Test cases
print("\n" + "=" * 70)
print("Problem 4: LeetCode 303 - Range Sum Query - Immutable")
print("=" * 70)

nums = [-2, 0, 3, -5, 2, -1]
num_array = NumArray(nums)

test_cases_303 = [
    (0, 2, 1),
    (2, 5, -1),
    (0, 5, -3)
]

for left, right, expected in test_cases_303:
    result = num_array.sumRange(left, right)
    status = "✅" if result == expected else "❌"
    print(f"sumRange({left}, {right}) → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 5: LeetCode 53 - Maximum Subarray (EASY)
# ============================================================================

"""
Problem:
--------
Given an integer array nums, find the contiguous subarray (containing at least 
one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

def maxSubArray(nums):
    """
    Approach: Dynamic Programming (Kadane's Algorithm)
    
    Key Insight:
    - At each position, we have two choices:
      1. Start a new subarray from the current element
      2. Extend the previous subarray by including the current element
    - Choose whichever gives a larger sum
    - Keep track of the maximum sum seen so far
    - This is Kadane's algorithm, a classic DP approach
    
    DP State:
    - dp[i] = maximum sum of subarray ending at index i
    
    DP Recurrence:
    - dp[i] = max(nums[i], dp[i-1] + nums[i])
    
    Pattern Recognition:
    - Contiguous subsequence optimization
    - Local vs. global optimal values
    - Reset when cumulative sum becomes negative
    
    Time: O(n) - single pass through the array
    Space: O(1) - constant extra space (with optimization)
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = dp[0]
    
    for i in range(1, n):
        # Either start new subarray from current element or extend previous
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        max_sum = max(max_sum, dp[i])
    
    return max_sum


# Optimized solution with constant space
def maxSubArray_optimized(nums):
    """
    Space-optimized version of Kadane's Algorithm
    """
    if not nums:
        return 0
    
    current_sum = max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Either start new subarray or extend previous
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Test cases
print("\n" + "=" * 70)
print("Problem 5: LeetCode 53 - Maximum Subarray")
print("=" * 70)

test_cases_53 = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    ([-1], -1)
]

for nums, expected in test_cases_53:
    result = maxSubArray(nums)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums} → {result} (expected: {expected}) {status}")


# ============================================================================
# MEDIUM PROBLEMS - INTERMEDIATE DP CONCEPTS
# ============================================================================


# ============================================================================
# PROBLEM 6: LeetCode 5 - Longest Palindromic Substring (MEDIUM) 
# ============================================================================

"""
Problem:
--------
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab" or "aba" (both are valid)
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
- 1 <= s.length <= 1000
- s consists of only digits and English letters
"""

def longestPalindrome(s):
    """
    Approach: Dynamic Programming (2D)
    
    Key Insight:
    - A palindrome reads the same forward and backward
    - If a substring is a palindrome, removing its first and last character also gives a palindrome
    - Use this insight to build larger palindromes from smaller ones
    - Define dp[i][j] = whether substring s[i...j] is a palindrome
    - Base cases: single characters are palindromes; two adjacent same characters are palindromes
    - For longer substrings, check if first and last chars match + inner substring is palindrome
    
    DP State:
    - dp[i][j] = True if substring s[i...j] is a palindrome, False otherwise
    
    DP Recurrence:
    - dp[i][j] = True if s[i] == s[j] AND (j - i <= 2 OR dp[i+1][j-1])
    - Explanation: substring is palindrome if first & last chars match AND
      inner substring is palindrome (or has length <= 1)
    
    Pattern Recognition:
    - String processing with subproblems
    - State depends on smaller substrings
    - Bottom-up filling of DP table diagonally
    - Track best solution while filling table
    
    Time: O(n²) - need to check all possible substrings
    Space: O(n²) - for the 2D DP table
    """
    if not s:
        return ""
    
    n = len(s)
    # Initialize DP table
    dp = [[False for _ in range(n)] for _ in range(n)]
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Track longest palindrome
    start = 0
    max_length = 1
    
    # Check for 2-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for longer palindromes
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1  # ending index
            
            # Check if current substring is palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                
                # Update longest palindrome if needed
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]


# Alternate solution: Expand around center (more efficient)
def longestPalindrome_optimized(s):
    """
    Approach: Expand Around Center
    
    Rather than using DP, we can expand around each potential center.
    There are 2n-1 centers: each character and each space between characters.
    
    Time: O(n²) but with much lower constant factor than DP approach
    Space: O(1) - constant space
    """
    if not s:
        return ""
    
    def expand_around_center(left, right):
        """Expand outward from center while maintaining palindrome property."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length of palindrome
    
    start, max_length = 0, 0
    
    for i in range(len(s)):
        # Expand around i as center (odd length palindromes)
        len1 = expand_around_center(i, i)
        # Expand around i and i+1 as center (even length palindromes)
        len2 = expand_around_center(i, i + 1)
        
        # Update longest palindrome
        length = max(len1, len2)
        if length > max_length:
            max_length = length
            # Calculate start index
            start = i - (length - 1) // 2
    
    return s[start:start + max_length]


# Test cases
print("\n" + "=" * 70)
print("Problem 6: LeetCode 5 - Longest Palindromic Substring")
print("=" * 70)

test_cases_5 = [
    ("babad", ["bab", "aba"]),
    ("cbbd", ["bb"]),
    ("a", ["a"]),
    ("ac", ["a", "c"]),
    ("racecar", ["racecar"])
]

for s, expected_options in test_cases_5:
    result = longestPalindrome(s)
    status = "✅" if result in expected_options else "❌"
    print(f"s='{s}' → '{result}' (expected one of: {expected_options}) {status}")


# ============================================================================
# PROBLEM 7: LeetCode 322 - Coin Change (MEDIUM) 
# ============================================================================

"""
Problem:
--------
You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that 
amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
- 1 <= coins.length <= 12
- 1 <= coins[i] <= 2^31 - 1
- 0 <= amount <= 10^4
"""

def coinChange(coins, amount):
    """
    Approach: Bottom-Up Dynamic Programming
    
    Key Insight:
    - For each amount from 0 to target amount, calculate minimum coins needed
    - For amount i, try each coin and see if it can give a better solution
    - If we can make amount (i - coin) with k coins, then we can make amount i with k+1 coins
    - Take minimum across all valid coins
    - This is a classic minimization problem with optimal substructure
    
    DP State:
    - dp[i] = minimum number of coins needed to make amount i
    
    DP Recurrence:
    - dp[i] = 1 + min(dp[i-coin] for coin in coins if i-coin >= 0)
    
    Pattern Recognition:
    - Minimum coins to reach target (optimization problem)
    - Building up solution from smaller denominations
    - Handling unreachable amounts (set to infinity)
    - "Making change" pattern common in DP problems
    
    Time: O(amount * n) where n is the number of coin denominations
    Space: O(amount) for the DP array
    """
    # Initialize DP array with "infinity" values
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # Calculate minimum coins for each amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:  # Can use this coin
                dp[i] = min(dp[i], 1 + dp[i - coin])
    
    # Check if amount can be made
    return dp[amount] if dp[amount] != float('inf') else -1


# Test cases
print("\n" + "=" * 70)
print("Problem 7: LeetCode 322 - Coin Change")
print("=" * 70)

test_cases_322 = [
    ([1, 2, 5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1, 3, 4, 5], 7, 2),
    ([2, 5, 10, 1], 27, 4)
]

for coins, amount, expected in test_cases_322:
    result = coinChange(coins, amount)
    status = "✅" if result == expected else "❌"
    print(f"coins={coins}, amount={amount} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 8: LeetCode 300 - Longest Increasing Subsequence (MEDIUM) 
# ============================================================================

"""
Problem:
--------
Given an integer array nums, return the length of the longest strictly 
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some 
or no elements without changing the order of the remaining elements.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:
- 1 <= nums.length <= 2500
- -10^4 <= nums[i] <= 10^4
"""

def lengthOfLIS(nums):
    """
    Approach: Dynamic Programming
    
    Key Insight:
    - For each element, determine the longest increasing subsequence ending at that element
    - Check all previous elements to see if the current element can extend any previous subsequence
    - LIS ending at position i = 1 + max(LIS ending at position j) for all j < i where nums[j] < nums[i]
    - Track the global maximum LIS length
    
    DP State:
    - dp[i] = length of longest increasing subsequence ending at position i
    
    DP Recurrence:
    - dp[i] = 1 + max(dp[j]) for all j < i where nums[j] < nums[i]
    - if no such j exists, dp[i] = 1 (single element subsequence)
    
    Pattern Recognition:
    - Subsequence problems often use this pattern
    - Optimal substructure: optimal solution includes optimal solutions to subproblems
    - Need to compare current element with all previous elements
    - Common optimization: binary search (patience sort) for O(n log n)
    
    Time: O(n²) - for each position, check all previous positions
    Space: O(n) - for the DP array
    """
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n  # Initialize: min LIS length is 1 (element itself)
    
    # Calculate LIS for each position
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # Return maximum value in dp array
    return max(dp)


# Optimized solution using binary search - O(n log n)
def lengthOfLIS_optimized(nums):
    """
    Approach: Patience Sort / Binary Search
    
    This approach maintains a list of smallest ending numbers for subsequences of each length.
    Binary search is used to find the right position for each element.
    
    Time: O(n log n) - significant improvement for large inputs
    Space: O(n) - for the tails array
    """
    if not nums:
        return 0
    
    # tails[i] = smallest value that ends an increasing subsequence of length i+1
    tails = []
    
    for num in nums:
        # Binary search to find the position to insert num
        left, right = 0, len(tails)
        
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If we're at the end, append to extend the LIS
        if left == len(tails):
            tails.append(num)
        else:
            # Otherwise, replace the value at the found position
            tails[left] = num
    
    return len(tails)


# Test cases
print("\n" + "=" * 70)
print("Problem 8: LeetCode 300 - Longest Increasing Subsequence")
print("=" * 70)

test_cases_300 = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
    ([4, 10, 4, 3, 8, 9], 3)
]

for nums, expected in test_cases_300:
    result = lengthOfLIS(nums)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 9: LeetCode 62 - Unique Paths (MEDIUM) 
# ============================================================================

"""
Problem:
--------
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot 
is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Right -> Down
3. Down -> Down -> Right

Constraints:
- 1 <= m, n <= 100
- The answer will be less than or equal to 2 * 10^9
"""

def uniquePaths(m, n):
    """
    Approach: 2D Dynamic Programming
    
    Key Insight:
    - For each cell, the number of ways to reach it is the sum of:
      1. Number of ways to reach the cell above it
      2. Number of ways to reach the cell to its left
    - This is because the robot can only move down or right
    - Grid boundaries have only one way to reach them (straight line)
    - This forms a 2D DP table where each cell depends on cells above and to the left
    
    DP State:
    - dp[i][j] = number of unique paths to reach cell (i, j)
    
    DP Recurrence:
    - dp[i][j] = dp[i-1][j] + dp[i][j-1]
    - Base cases: dp[0][j] = dp[i][0] = 1 (only one way to reach any cell in first row/column)
    
    Pattern Recognition:
    - Grid traversal problem with 2D DP
    - Path counting with restricted movements
    - Combinatorial problem in disguise (combination formula: (m+n-2)!/(m-1)!/(n-1)!)
    - Building solutions from smaller subproblems
    
    Time: O(m * n) - need to fill the entire DP table
    Space: O(m * n) - for the 2D DP table (can be optimized to O(min(m, n)))
    """
    # Initialize DP table with 1s (base cases)
    dp = [[1 for _ in range(n)] for _ in range(m)]
    
    # Fill DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]


# Space-optimized solution
def uniquePaths_optimized(m, n):
    """
    Space-optimized solution using 1D array
    
    Since each cell only depends on the cell above and to the left,
    we can use a 1D array and update it in-place.
    
    Time: O(m * n)
    Space: O(n) - only need to store one row
    """
    dp = [1] * n  # Initialize with 1s (base cases for first row)
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j-1]  # Current cell = cell above (dp[j]) + cell to left (dp[j-1])
    
    return dp[n-1]


# Mathematical solution (combination formula)
def uniquePaths_math(m, n):
    """
    Mathematical solution using combinations
    
    The problem is equivalent to finding how many ways to arrange (m-1) down moves
    and (n-1) right moves, which is C(m+n-2, m-1) or C(m+n-2, n-1).
    
    Time: O(min(m, n))
    Space: O(1)
    """
    from math import factorial
    
    return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))


# Test cases
print("\n" + "=" * 70)
print("Problem 9: LeetCode 62 - Unique Paths")
print("=" * 70)

test_cases_62 = [
    (3, 7, 28),
    (3, 2, 3),
    (7, 3, 28),
    (1, 1, 1),
    (10, 10, 48620)
]

for m, n, expected in test_cases_62:
    result = uniquePaths(m, n)
    status = "✅" if result == expected else "❌"
    print(f"m={m}, n={n} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 10: LeetCode 139 - Word Break (MEDIUM) 
# ============================================================================

"""
Problem:
--------
Given a string s and a dictionary of strings wordDict, return true if s can be 
segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
- 1 <= s.length <= 300
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 20
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.
"""

def wordBreak(s, wordDict):
    """
    Approach: Dynamic Programming
    
    Key Insight:
    - For each position i, check if the string up to i can be segmented
    - If we can segment up to position j, and s[j:i] is a word in wordDict,
      then we can segment up to position i
    - This builds a solution incrementally from smaller subproblems
    - Use DP to avoid redundant work (checking the same substring multiple times)
    
    DP State:
    - dp[i] = True if string s[0...i-1] can be segmented, False otherwise
    
    DP Recurrence:
    - dp[i] = True if there exists j < i such that dp[j] = True AND s[j...i-1] is in wordDict
    
    Pattern Recognition:
    - String segmentation problem
    - Check all possible break points
    - Build solution incrementally
    - Use word lookup for efficiency
    
    Time: O(n²) - where n is the length of string s
    Space: O(n) - for the DP array
    """
    n = len(s)
    # Convert wordDict to set for O(1) lookup
    word_set = set(wordDict)
    
    # Initialize DP array
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can always be segmented
    
    # Fill DP array
    for i in range(1, n + 1):
        for j in range(i):
            # Check if string up to j can be segmented and if s[j:i] is in wordDict
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[n]


# Test cases
print("\n" + "=" * 70)
print("Problem 10: LeetCode 139 - Word Break")
print("=" * 70)

test_cases_139 = [
    ("leetcode", ["leet", "code"], True),
    ("applepenapple", ["apple", "pen"], True),
    ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
    ("aaaaaaa", ["aaaa", "aaa"], True),
    ("goalspecial", ["go", "goal", "special"], True)
]

for s, wordDict, expected in test_cases_139:
    result = wordBreak(s, wordDict)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', wordDict={wordDict} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 11: LeetCode 121 - Best Time to Buy and Sell Stock (EASY) ⭐⭐
# ============================================================================

"""
Problem:
--------
You are given an array of prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

def maxProfit(prices):
    """
    Approach: One Pass with Minimum Tracking
    
    Key Insight:
    - Track the minimum price seen so far
    - For each price, calculate potential profit if selling at current price
    - Update maximum profit if the current potential profit is greater
    
    DP State:
    - While not explicitly DP, we track:
    - min_price: minimum price seen so far
    - max_profit: maximum profit possible
    
    Pattern Recognition:
    - Local & global optimal values
    - Greedy with minimum tracking
    
    Time: O(n) where n is the length of prices
    Space: O(1) constant space
    """
    if not prices:
        return 0
    
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # If we find a new minimum price, update it
        if price < min_price:
            min_price = price
        # Calculate potential profit if selling at current price
        # Update max_profit if current profit is better
        else:
            current_profit = price - min_price
            max_profit = max(max_profit, current_profit)
    
    return max_profit


# Test cases
print("\n" + "=" * 70)
print("Problem 11: LeetCode 121 - Best Time to Buy and Sell Stock")
print("=" * 70)

test_cases_121 = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2], 1),
    ([3, 2, 6, 5, 0, 3], 4)
]

for prices, expected in test_cases_121:
    result = maxProfit(prices)
    status = "✅" if result == expected else "❌"
    print(f"prices={prices} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 12: LeetCode 122 - Best Time to Buy and Sell Stock II (EASY) ⭐⭐
# ============================================================================

"""
Problem:
--------
You are given an array of prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one 
share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No transaction is done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4
"""

def maxProfit2(prices):
    """
    Approach: Greedy with Peak Valley or Profit Accumulation
    
    Key Insight:
    - We can perform multiple transactions
    - We should buy at every "valley" and sell at every "peak"
    - Simply accumulating all positive price differences gives the same result
    
    DP State:
    - While this can be framed as DP, a greedy approach is cleaner
    - Accumulate profit whenever current price > previous price
    
    Pattern Recognition:
    - Greedy algorithm (local optimization leads to global optimization)
    - Peak-valley analysis
    
    Time: O(n) where n is the length of prices
    Space: O(1) constant space
    """
    if not prices:
        return 0
    
    max_profit = 0
    
    for i in range(1, len(prices)):
        # If current price is higher than previous, take the profit
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    
    return max_profit


# Alternative approach using state machine
def maxProfit2_dp(prices):
    """
    Approach: State Machine DP
    
    DP States:
    - held: maximum profit if we end the day with stock
    - not_held: maximum profit if we end the day without stock
    
    Time: O(n)
    Space: O(1)
    """
    if not prices:
        return 0
    
    # Initial states
    not_held = 0  # Maximum profit when not holding a stock
    held = -prices[0]  # Maximum profit when holding a stock (starting with buying first day)
    
    for i in range(1, len(prices)):
        # If we don't have stock, either keep it that way or sell what we bought yesterday
        prev_not_held = not_held
        not_held = max(not_held, held + prices[i])
        
        # If we have stock, either keep it or buy new stock
        held = max(held, prev_not_held - prices[i])
    
    # Final answer must be the state where we don't hold any stock
    return not_held


# Test cases
print("\n" + "=" * 70)
print("Problem 12: LeetCode 122 - Best Time to Buy and Sell Stock II")
print("=" * 70)

test_cases_122 = [
    ([7, 1, 5, 3, 6, 4], 7),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
    ([3, 2, 6, 5, 0, 3], 7)
]

for prices, expected in test_cases_122:
    result = maxProfit2(prices)
    status = "✅" if result == expected else "❌"
    print(f"prices={prices} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 13: LeetCode 279 - Perfect Squares (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the 
product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 
and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9

Constraints:
- 1 <= n <= 10^4
"""

def numSquares(n):
    """
    Approach: Dynamic Programming (Bottom-Up)
    
    Key Insight:
    - For each number i from 1 to n, calculate the minimum number of perfect squares needed
    - For each i, try all possible perfect squares j*j ≤ i, and take the minimum
    
    DP State:
    - dp[i] = minimum number of perfect squares that sum to i
    
    DP Recurrence:
    - dp[i] = min(dp[i], dp[i - j*j] + 1) for all j where j*j ≤ i
    
    Pattern Recognition:
    - Coin change variation
    - Mathematical DP
    - Optimization problem
    
    Time: O(n * sqrt(n)) - iterate through n and for each consider sqrt(n) perfect squares
    Space: O(n) for the DP array
    """
    # Initialize dp array with maximum value (n+1 is sufficient as upper bound)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: 0 can be represented with 0 perfect squares
    
    for i in range(1, n + 1):
        # Try all possible perfect squares less than or equal to i
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    
    return dp[n]


# Alternative using BFS (often faster in practice)
from collections import deque

def numSquares_bfs(n):
    """
    Approach: Breadth-First Search
    
    Key Insight:
    - Treat this as a shortest path problem in a graph
    - Each node is a number, and edges connect nodes that differ by a perfect square
    - BFS guarantees the shortest path (minimum number of perfect squares)
    
    Time: O(n * sqrt(n))
    Space: O(n)
    """
    # Edge case
    if n <= 0:
        return 0
    
    # Generate all perfect squares ≤ n
    perfect_squares = []
    i = 1
    while i * i <= n:
        perfect_squares.append(i * i)
        i += 1
    
    # BFS
    queue = deque([n])
    level = 0
    visited = set([n])
    
    while queue:
        level += 1
        size = len(queue)
        
        for _ in range(size):
            curr = queue.popleft()
            
            for square in perfect_squares:
                remainder = curr - square
                
                if remainder == 0:  # Found solution
                    return level
                
                if remainder > 0 and remainder not in visited:
                    visited.add(remainder)
                    queue.append(remainder)
                
                if remainder < 0:  # No need to check larger squares
                    break
    
    return -1  # Should never reach here given the constraints


# Test cases
print("\n" + "=" * 70)
print("Problem 13: LeetCode 279 - Perfect Squares")
print("=" * 70)

test_cases_279 = [
    (12, 3),
    (13, 2),
    (1, 1),
    (43, 3),
    (18, 2)
]

for n, expected in test_cases_279:
    result = numSquares(n)
    status = "✅" if result == expected else "❌"
    print(f"n={n} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 14: LeetCode 368 - Largest Divisible Subset (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given a set of distinct positive integers nums, return the largest subset answer such that 
every pair (answer[i], answer[j]) of elements in this subset satisfies:
- answer[i] % answer[j] == 0, or
- answer[j] % answer[i] == 0

If there are multiple solutions, return any of them.

Example 1:
Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.

Example 2:
Input: nums = [1,2,4,8]
Output: [1,2,4,8]

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 2 * 10^9
- All the integers in nums are unique.
"""

def largestDivisibleSubset(nums):
    """
    Approach: Dynamic Programming with Path Reconstruction
    
    Key Insight:
    - Sort the array to simplify divisibility check
    - For each number, find the longest valid subset ending with numbers smaller than it
    - Track both the length and the previous index for path reconstruction
    
    DP State:
    - dp[i] = size of largest divisible subset ending with nums[i]
    - prev[i] = index of previous element in the subset
    
    DP Recurrence:
    - dp[i] = max(dp[j] + 1) for all j < i where nums[i] % nums[j] == 0
    
    Pattern Recognition:
    - Extended LIS (Longest Increasing Subsequence)
    - Path reconstruction in DP
    - Mathematical relationship between elements
    
    Time: O(n²) where n is the length of nums
    Space: O(n) for the dp and prev arrays
    """
    if not nums:
        return []
    
    # Sort the array to simplify divisibility checks
    nums.sort()
    n = len(nums)
    
    # Initialize DP arrays
    dp = [1] * n  # dp[i] = size of largest divisible subset ending with nums[i]
    prev = [-1] * n  # prev[i] = index of previous element in the subset
    
    # Find the maximum subset size and the index where it ends
    max_size = 1
    max_index = 0
    
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:  # nums[i] is divisible by nums[j]
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
        
        if dp[i] > max_size:
            max_size = dp[i]
            max_index = i
    
    # Reconstruct the result subset
    result = []
    while max_index != -1:
        result.append(nums[max_index])
        max_index = prev[max_index]
    
    # Reverse to get the subset in ascending order
    return result[::-1]


# Test cases
print("\n" + "=" * 70)
print("Problem 14: LeetCode 368 - Largest Divisible Subset")
print("=" * 70)

test_cases_368 = [
    ([1, 2, 3], [1, 2]),
    ([1, 2, 4, 8], [1, 2, 4, 8]),
    ([4, 8, 10, 240], [4, 8, 240]),
    ([5], [5])
]

for nums, expected in test_cases_368:
    result = largestDivisibleSubset(nums)
    # Check if result is a valid divisible subset with expected size
    valid = True
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if result[j] % result[i] != 0:
                valid = False
                break
    status = "✅" if valid and len(result) == len(expected) else "❌"
    print(f"nums={nums} → {result} (expected length: {expected}) {status}")


# ============================================================================
# PROBLEM 15: LeetCode 377 - Combination Sum IV (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an array of distinct integers nums and a target integer target, return the number of possible
combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation: The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0

Constraints:
- 1 <= nums.length <= 200
- 1 <= nums[i] <= 1000
- All the elements of nums are unique.
- 1 <= target <= 1000
"""

def combinationSum4(nums, target):
    """
    Approach: Dynamic Programming (Bottom-Up)
    
    Key Insight:
    - Count combinations to build each value from 0 to target
    - For each intermediate target value, try to use each number from nums
    - Order matters in this problem (unlike traditional combination problems)
    
    DP State:
    - dp[i] = number of ways to form sum i using numbers from nums
    
    DP Recurrence:
    - dp[i] += dp[i - num] for each num in nums if i >= num
    
    Pattern Recognition:
    - Permutation variant of coin change problem
    - Bottom-up DP building towards target
    - Counting problem with order mattering
    
    Time: O(target * n) where n is the length of nums
    Space: O(target) for the DP array
    """
    # Initialize dp array
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: one way to make sum 0 (take no elements)
    
    # Build up the dp array
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    
    return dp[target]


# Alternative top-down approach with memoization
def combinationSum4_topdown(nums, target):
    """
    Approach: Dynamic Programming (Top-Down with Memoization)
    
    Time: O(target * n)
    Space: O(target)
    """
    memo = {0: 1}  # Base case: one way to make sum 0
    
    def helper(remaining):
        if remaining in memo:
            return memo[remaining]
        
        count = 0
        for num in nums:
            if remaining >= num:
                count += helper(remaining - num)
                
        memo[remaining] = count
        return count
    
    return helper(target)


# Test cases
print("\n" + "=" * 70)
print("Problem 15: LeetCode 377 - Combination Sum IV")
print("=" * 70)

test_cases_377 = [
    ([1, 2, 3], 4, 7),
    ([9], 3, 0),
    ([1, 2, 3], 32, 181997601),
    ([2, 1, 3], 35, 1132436852),
    ([4, 2, 1], 32, 39882198)
]

for nums, target, expected in test_cases_377:
    result = combinationSum4(nums, target)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums}, target={target} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 16: LeetCode 120 - Triangle (MEDIUM) ⭐⭐
# ============================================================================

"""
Problem:
--------
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on
index i on the current row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i - 1].length + 1
- -10^4 <= triangle[i][j] <= 10^4
"""

def minimumTotal(triangle):
    """
    Approach: Dynamic Programming (Bottom-Up)
    
    Key Insight:
    - Start from the bottom row and work your way up
    - For each position, choose the minimum of the two possible paths below it
    
    DP State:
    - dp[i][j] = minimum path sum starting from position (i,j) to bottom
    
    DP Recurrence:
    - dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])
    
    Pattern Recognition:
    - Bottom-up DP
    - Path minimization
    - Working backwards from the goal
    
    Time: O(n²) where n is the number of rows in the triangle
    Space: O(n²) for the full triangle (can be optimized to O(n))
    """
    # Make a copy of the triangle to use as our DP table
    dp = [row[:] for row in triangle]
    
    # Start from the second to last row and work up
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # For each position, choose minimum of two paths below
            dp[i][j] += min(dp[i + 1][j], dp[i + 1][j + 1])
    
    # The top element now has the minimum path sum
    return dp[0][0]


# Space-optimized solution
def minimumTotal_optimized(triangle):
    """
    Space-optimized solution using a single row
    
    Time: O(n²)
    Space: O(n)
    """
    # Start with the bottom row
    dp = triangle[-1][:]
    
    # Work our way up
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # Update dp in-place
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
    
    return dp[0]


# Test cases
print("\n" + "=" * 70)
print("Problem 16: LeetCode 120 - Triangle")
print("=" * 70)

test_cases_120 = [
    ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
    ([[-10]], -10),
    ([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]], 14),
    ([[1], [-2, -5], [3, 6, 9], [-1, 2, 4, -3]], -1)
]

for triangle, expected in test_cases_120:
    result = minimumTotal(triangle)
    status = "✅" if result == expected else "❌"
    print(f"triangle=[...] → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 17: LeetCode 413 - Arithmetic Slices (MEDIUM) ⭐⭐
# ============================================================================

"""
Problem:
--------
An integer array is called arithmetic if it consists of at least three elements and if the 
difference between any two consecutive elements is the same.

For example:
- "abc" is a predecessor of "abac" because we can insert "a" between "b" and "c".
- "cba" is not a predecessor of "bcad" because we cannot insert one character to make "cba" equal to "bcad".

A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is 
a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k = 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Example 1:
Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chains is ["a","ba","bda","bdca"].

Example 2:
Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5
Explanation: All the words can be put in a word chain ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

Example 3:
Input: words = ["abcd","dbqca"]
Output: 1
Explanation: The trivial word chain ["abcd"] is one of the longest word chains.
["dbqca"] is another longest word chain.

Constraints:
- 1 <= words.length <= 1000
- 1 <= words[i].length <= 16
- words[i] only consists of lowercase English letters.
"""

def longestStrChain(words):
    """
    Approach: Dynamic Programming with Hash Map
    
    Key Insight:
    - Sort words by length to process from shorter to longer
    - For each word, try removing one character at a time
    - If the resulting word exists, current word can extend its chain
    
    DP State:
    - dp[word] = length of longest chain ending with word
    
    DP Recurrence:
    - dp[word] = max(dp[word], dp[predecessor] + 1) for all valid predecessors
    
    Pattern Recognition:
    - Hash map based DP
    - Word transformation
    - Longest path in an implicit graph
    - Similar to LIS (Longest Increasing Subsequence) pattern
    
    Time: O(N * L²) where N is number of words, L is max word length
    Space: O(N) for the DP dictionary
    """
    # Sort words by length (ascending)
    words.sort(key=len)
    
    # Initialize dp dictionary
    dp = {}  # word -> length of longest chain ending with this word
    
    # Initialize result
    max_chain = 1
    
    for word in words:
        # Each word by itself forms a chain of length 1
        dp[word] = 1
        
        # Try removing one character at a time
        for i in range(len(word)):
            # Remove the i-th character
            predecessor = word[:i] + word[i+1:]
            
            # If the predecessor exists, update the chain length
            if predecessor in dp:
                dp[word] = max(dp[word], dp[predecessor] + 1)
        
        # Update the global maximum
        max_chain = max(max_chain, dp[word])
    
    return max_chain


# Test cases
print("\n" + "=" * 70)
print("Problem 19: LeetCode 1048 - Longest String Chain")
print("=" * 70)

test_cases_1048 = [
    (["a", "b", "ba", "bca", "bda", "bdca"], 4),
    (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
    (["abcd", "dbqca"], 1),
    (["a", "ab", "ac", "bd", "abc", "abd", "abdd"], 4)
]

for words, expected in test_cases_1048:
    result = longestStrChain(words)
    # Check if result is a valid chain with expected length
    valid = True
    for i in range(len(result)):
        for j in range(i+1, len(result)):
            if len(result[j]) != len(result[i]) + 1:
                valid = False
                break
    status = "✅" if valid and len(result) == expected else "❌"
    print(f"words={words} → {result} (expected length: {expected}) {status}")


# ============================================================================
# PROBLEM 20: LeetCode 1049 - Last Stone Weight II (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose any two stones and smash them together. 
Suppose the stones have weights x and y with x <= y. The result of this smash is:
- If x == y, both stones are destroyed.
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Example 1:
Input: stones = [2,7,4,1,8,1]
Output: 1
Explanation: We can combine 2 and 4 to get 2, so the array converts to [2,7,1,8,1] then,
we can combine 7 and 8 to get 1, so the array converts to [2,1,1,1] then,
we can combine 2 and 1 to get 1, so the array converts to [1,1,1] then,
we can combine 1 and 1 to get 0, so the array converts to [1], which is the final result.

Example 2:
Input: stones = [31,26,33,21,40]
Output: 5

Constraints:
- 1 <= stones.length <= 30
- 1 <= stones[i] <= 100
"""

def lastStoneWeightII(stones):
    """
    Approach: Dynamic Programming (Subset Sum Variation)
    
    Key Insight:
    - The problem can be transformed into a subset sum problem
    - We want to partition stones into two groups to minimize their difference
    - This is equivalent to finding a subset with sum closest to half of the total sum
    
    DP State:
    - dp[i] = whether a sum i can be formed with some combination of stones
    
    DP Recurrence:
    - dp[j] = dp[j] OR dp[j-stones[i]] for each stone i
    
    Pattern Recognition:
    - Subset sum / 0-1 Knapsack variation
    - State transformation to simplify problem
    - Minimizing difference between two groups
    
    Time: O(n * sum) where n is number of stones and sum is total weight
    Space: O(sum) for the DP array
    """
    total_sum = sum(stones)
    target = total_sum // 2  # Try to find a subset sum closest to half
    
    # Initialize DP array
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: we can always form sum 0 by taking no stones
    
    # Fill the DP array
    for stone in stones:
        # We need to iterate in reverse to avoid using the same stone multiple times
        for j in range(target, stone - 1, -1):
            dp[j] = dp[j] or dp[j - stone]
    
    # Find the largest sum <= target that can be formed
    for j in range(target, -1, -1):
        if dp[j]:
            # One subset has sum j, the other has sum (total_sum - j)
            # The difference is the final stone weight
            return total_sum - 2 * j
    
    # Should never reach here given the constraints
    return 0


# ============================================================================
# PROBLEM 21: LeetCode 887 - Super Egg Drop (HARD) ⭐⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.

You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor 
higher than f will break, and any egg dropped at or below floor f will not break.

Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). 
If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it.

Return the minimum number of moves that you need to determine with certainty what the value of f is.

Example 1:
Input: k = 1, n = 2
Output: 2
Explanation: 
Drop the egg from floor 1. If it breaks, f = 0. Otherwise, drop the egg from floor 2. If it breaks, f = 1. Otherwise, f = 2.

Example 2:
Input: k = 2, n = 6
Output: 3

Example 3:
Input: k = 3, n = 14
Output: 4

Constraints:
- 1 <= k <= 100
- 1 <= n <= 10^4
"""

def superEggDrop(k, n):
    """
    Approach: Dynamic Programming with Binary Search Optimization
    
    Key Insight:
    - If we drop an egg from floor x:
      1. If it breaks, we need to check floors 1 to x-1 with k-1 eggs
      2. If it doesn't break, we need to check floors x+1 to n with k eggs
    - The optimal strategy minimizes the worst-case number of moves
    - Use binary search to find the optimal floor to drop from
    
    DP State:
    - dp[i][j] = minimum moves needed with i eggs and j floors
    
    DP Recurrence:
    - dp[i][j] = 1 + min(max(dp[i-1][x-1], dp[i][j-x])) for all x from 1 to j
    
    Pattern Recognition:
    - Decision optimization
    - Binary search application in DP
    - Minimax algorithm
    
    Time: O(k * n * log n) with binary search optimization
    Space: O(k * n) for the DP table
    """
    # Initialize DP table
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    # Base cases:
    # With 1 egg, we need j moves for j floors (linear check)
    for j in range(1, n + 1):
        dp[1][j] = j
    
    # With 0 floors, we need 0 moves
    # With 1 floor, we need 1 move
    for i in range(1, k + 1):
        dp[i][0] = 0
        dp[i][1] = 1
    
    # Fill the DP table
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            # Binary search to find the optimal floor x to drop from
            left, right = 1, j
            while left <= right:
                mid = (left + right) // 2
                broken = dp[i-1][mid-1]  # egg breaks at mid
                not_broken = dp[i][j-mid]  # egg doesn't break at mid
                
                if broken >= not_broken:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # The optimal floor to drop from is 'left-1'
            # (the largest floor where broken <= not_broken)
            x = left - 1
            dp[i][j] = 1 + max(dp[i-1][x-1], dp[i][j-x])
    
    return dp[k][n]


# Alternative approach with mathematical insight (much faster)
def superEggDrop_optimized(k, n):
    """
    Approach: DP with state redefinition
    
    Key Insight:
    - Instead of dp[k][n] representing the minimum moves for k eggs and n floors,
      we define dp[k][m] = maximum floors that can be checked with k eggs and m moves
    - We find the smallest m such that dp[k][m] >= n
    
    Time: O(k * log n)
    Space: O(k)
    """
    # dp[i][j] = maximum number of floors that can be checked with i eggs and j moves
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    moves = 0
    while dp[k][moves] < n:
        moves += 1
        for i in range(1, k + 1):
            # With i eggs and moves moves, we can check:
            # 1 + dp[i-1][moves-1] (if egg breaks) + dp[i][moves-1] (if egg doesn't break) floors
            dp[i][moves] = dp[i-1][moves-1] + dp[i][moves-1] + 1
    
    return moves


# Test cases
print("\n" + "=" * 70)
print("Problem 21: LeetCode 887 - Super Egg Drop")
print("=" * 70)

test_cases_887 = [
    (1, 2, 2),
    (2, 6, 3),
    (3, 14, 4),
    (2, 10, 4),
    (4, 200, 8)
]

for k, n, expected in test_cases_887:
    # Using optimized version due to faster runtime
    result = superEggDrop_optimized(k, n)
    status = "✅" if result == expected else "❌"
    print(f"k={k}, n={n} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 22: LeetCode 1359 - Count All Valid Pickup and Delivery Options (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Example 2:
Input: n = 2
Output: 6
Explanation: All possible orders:
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Example 3:
Input: n = 3
Output: 90

Constraints:
- 1 <= n <= 500
"""

def countOrders(n):
    """
    Approach: Dynamic Programming with Combinatorial Math
    
    Key Insight:
    - For n=1, there's only one valid sequence: (P1, D1)
    - For n=2, we need to insert P2 and D2 into the sequence (P1, D1)
    - When adding the nth pair, we have 2n-1 positions for P(n) and 2n positions for D(n)
    - But D(n) must come after P(n), so for each position of P(n), we have (2n - position of P(n)) choices for D(n)
    - The total number of ways to insert the nth pair is the sum of (2n - i) for i from 0 to 2n-1, which is n(2n+1)
    
    DP State:
    - dp[i] = number of valid sequences for i orders
    
    DP Recurrence:
    - dp[i] = dp[i-1] * i * (2*i - 1)
    
    Pattern Recognition:
    - Combinatorial DP
    - Recursive counting
    - Constrained permutation
    
    Time: O(n) for n iterations
    Space: O(1) for the optimized version (just track the current count)
    """
    MOD = 10**9 + 7
    
    if n == 1:
        return 1
    
    # Start with 1 valid sequence for n=1
    count = 1
    
    # For each additional order
    for i in range(2, n + 1):
        # Calculate ways to insert the i-th pair:
        # For each position of P(i), count valid positions for D(i)
        # This equals i * (2i - 1)
        count = (count * i * (2 * i - 1)) % MOD
    
    return count


# Alternative mathematical solution
def countOrders_math(n):
    """
    Pure mathematical solution using the formula:
    - result = (2n)! / (2^n)
    
    Time: O(n)
    Space: O(1)
    """
    MOD = 10**9 + 7
    
    # Calculate (2n)! / 2^n
    result = 1
    for i in range(1, n + 1):
        # Multiply by (2i-1) for the pickup positions
        result = (result * (2 * i - 1)) % MOD
        # Multiply by i for the delivery positions
        result = (result * i) % MOD
    
    return result


# Test cases
print("\n" + "=" * 70)
print("Problem 22: LeetCode 1359 - Count All Valid Pickup and Delivery Options")
print("=" * 70)

test_cases_1359 = [
    (1, 1),
    (2, 6),
    (3, 90),
    (4, 2520),
    (5, 113400)
]

for n, expected in test_cases_1359:
    result = countOrders(n)
    status = "✅" if result == expected else "❌"
    print(f"n={n} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 23: LeetCode 403 - Frog Jump (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
A frog is crossing a river. The river is divided into some number of units, and at each unit, 
there may or may not be a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog
can cross the river by landing on the last stone. Initially, the frog is on the first stone 
and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. 
The frog can only jump in the forward direction.

Example 1:
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone,
then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.

Example 2:
Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.

Constraints:
- 2 <= stones.length <= 2000
- 0 <= stones[i] <= 2^31 - 1
- stones[0] == 0
- stones is sorted in a strictly increasing order.
"""

def canCross(stones):
    """
    Approach: Dynamic Programming with Memoization
    
    Key Insight:
    - For each stone, track all possible jump sizes that can reach it
    - Use recursion with memoization to explore all possible paths
    - The position and the previous jump size together form our state
    
    DP State:
    - dp[i][k] = whether the frog can reach the last stone starting from position i with previous jump k
    
    Pattern Recognition:
    - State-dependent transitions
    - Recursive DP with memoization
    - Decision tree pruning
    
    Time: O(n²) where n is the number of stones
    Space: O(n²) for the memoization cache
    """
    # Convert stones to a set for O(1) lookup
    stone_positions = set(stones)
    
    # Create a memoization cache
    memo = {}
    
    def can_reach_end(position, jump):
        # Base case: reached the last stone
        if position == stones[-1]:
            return True
        
        # Check memoization cache
        if (position, jump) in memo:
            return memo[(position, jump)]
        
        # Try all possible next jumps: k-1, k, k+1
        result = False
        for next_jump in [jump - 1, jump, jump + 1]:
            # Skip invalid jumps
            if next_jump <= 0:
                continue
                
            next_position = position + next_jump
            
            # Check if the next position has a stone
            if next_position in stone_positions:
                result = result or can_reach_end(next_position, next_jump)
                
                # Early termination if a valid path is found
                if result:
                    break
        
        # Cache the result
        memo[(position, jump)] = result
        return result
    
    # Start from the first stone with initial jump of 0 (next jump will be 1)
    return can_reach_end(0, 0)


# Alternative iterative approach using DP with sets
def canCross_iterative(stones):
    """
    Approach: Dynamic Programming with Sets
    
    Key Insight:
    - For each stone, maintain a set of possible jump sizes that can reach it
    - Iterate through all stones and build up these sets
    
    Time: O(n²) where n is the number of stones
    Space: O(n²) for the jump sets
    """
    n = len(stones)
    
    # Edge case: always need first jump to be 1
    if stones[1] != 1:
        return False
    
    # Initialize a dictionary to store possible jumps for each stone
    # dp[stone_position] = set of possible jumps that can reach this stone
    dp = {stone: set() for stone in stones}
    dp[0].add(0)  # Starting position with 0 jump
    dp[1].add(1)  # First stone can be reached with jump of 1
    
    for i in range(1, n):
        if not dp[stones[i]]:  # If no ways to reach this stone, skip
            continue
            
        for k in dp[stones[i]]:  # For each possible jump that reaches this stone
            # Try k-1, k, k+1 for the next jump
            for next_jump in [k - 1, k, k + 1]:
                if next_jump <= 0:
                    continue
                    
                next_position = stones[i] + next_jump
                
                if next_position in dp:  # If there's a stone at next_position
                    dp[next_position].add(next_jump)
    
    # Check if the last stone has any possible jumps (meaning it can be reached)
    return len(dp[stones[-1]]) > 0


# Test cases
print("\n" + "=" * 70)
print("Problem 23: LeetCode 403 - Frog Jump")
print("=" * 70)

test_cases_403 = [
    ([0, 1, 3, 5, 6, 8, 12, 17], True),
    ([0, 1, 2, 3, 4, 8, 9, 11], False),
    ([0, 1], True),
    ([0, 2], False),
    ([0, 1, 3, 6, 10, 15, 21, 28], True)
]

for stones, expected in test_cases_403:
    # Using the iterative version for more efficient execution
    result = canCross_iterative(stones)
    status = "✅" if result == expected else "❌"
    print(f"stones={stones} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 24: LeetCode 983 - Minimum Cost For Tickets (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You have planned some train traveling one year in advance. The days of the year in which
you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:
- A 1-day pass is sold for costs[0] dollars.
- A 7-day pass is sold for costs[1] dollars.
- A 30-day pass is sold for costs[2] dollars.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is <= shelfWidth,
then build another level of the shelf of the bookcase so that the total height of the bookcase has increased 
by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given 
sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, 
the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Example 1:
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes:
We buy a 1-day pass for day 1, which costs 2.
We buy a 7-day pass for days 4, 5, 6, 7, 8, which costs 7.
We buy a 1-day pass for day 20, which costs 2.
In total, you spent $11 and covered all the days of your travel.

Example 2:
Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes:
We buy a 30-day pass for days 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31, which costs 15.
We buy a 1-day pass for day 31, which costs 2.
In total, you spent $17 and covered all the days of your travel.

Constraints:
- 1 <= days.length <= 365
- 1 <= days[i] <= 365
- days is in strictly increasing order.
- costs.length == 3
- 1 <= costs[i] <= 1000
"""

def mincostTickets(days, costs):
    """
    Approach: Dynamic Programming (Bottom-Up)
    
    Key Insight:
    - For each day in our travel plan, we have 3 options:
      1. Buy a 1-day pass for today
      2. Buy a 7-day pass (covering today + next 6 days)
      3. Buy a 30-day pass (covering today + next 29 days)
    - We choose the option that minimizes cost
    
    DP State:
    - dp[i] = minimum cost to cover days[0...i]
    
    DP Recurrence:
    - dp[i] = min(
        costs[0] + dp[last day not covered by 1-day pass],
        costs[1] + dp[last day not covered by 7-day pass],
        costs[2] + dp[last day not covered by 30-day pass]
      )
    
    Pattern Recognition:
    - Interval-based DP
    - Calendar optimization
    - Multiple ways to cover each element
    
    Time: O(n) where n is the number of travel days
    Space: O(n) for the DP array
    """
    # Create a set of travel days for quick lookup
    travel_days = set(days)
    
    # Last travel day
    last_day = days[-1]
    
    # Initialize DP array
    dp = [0] * (last_day + 1)
    
    # Fill the DP array
    for i in range(1, last_day + 1):
        # If not a travel day, cost is the same as previous day
        if i not in travel_days:
            dp[i] = dp[i - 1]
        else:
            # Consider buying a 1-day pass
            one_day = dp[i - 1] + costs[0]
            
            # Consider buying a 7-day pass
            seven_day = dp[max(0, i - 7)] + costs[1]
            
            # Consider buying a 30-day pass
            thirty_day = dp[max(0, i - 30)] + costs[2]
            
            # Choose the minimum cost option
            dp[i] = min(one_day, seven_day, thirty_day)
    
    return dp[last_day]


# Alternative approach using recursion with memoization
def mincostTickets_memo(days, costs):
    """
    Approach: Dynamic Programming (Top-Down with Memoization)
    
    Time: O(n)
    Space: O(n) for the memoization cache
    """
    # Create a set of travel days for quick lookup
    travel_days = set(days)
    
    # Memoization cache
    memo = {}
    
    def dp(day):
        # Base case: beyond the last travel day
        if day > days[-1]:
            return 0
        
        # If not a travel day, skip to the next day
        if day not in travel_days:
            return dp(day + 1)
        
        # Check memoization cache
        if day in memo:
            return memo[day]
        
        # Try each pass option
        memo[day] = min(
            costs[0] + dp(day + 1),    # 1-day pass
            costs[1] + dp(day + 7),    # 7-day pass
            costs[2] + dp(day + 30)    # 30-day pass
        )
        
        return memo[day]
    
    return dp(1)  # Start from day 1


# Test cases
print("\n" + "=" * 70)
print("Problem 24: LeetCode 983 - Minimum Cost For Tickets")
print("=" * 70)

test_cases_983 = [
    ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
    ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17)
]

for days, costs, expected in test_cases_983:
    result = mincostTickets(days, costs)
    status = "✅" if result == expected else "❌"
    print(f"days={days}, costs={costs} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 25: LeetCode 740 - Delete and Earn (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are given an integer array nums. You want to maximize the number of points you get
by performing the following operation any number of times:

- Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete
  every element equal to nums[i] - 1 and every element equal to nums[i] + 1.

Return the maximum number of points you can earn by applying the above operation some
number of times.

Example 1:
Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Example 2:
Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 1 <= nums[i] <= 10^4
"""

def deleteAndEarn(nums):
    """
    Approach: Dynamic Programming (Reduced to House Robber problem)
    
    Key Insight:
    - For any number n, we can either take all instances of n or none
    - If we take n, we earn n * (count of n in nums) points
    - If we take n, we cannot take n-1 or n+1
    - This is similar to the House Robber problem, where we decide whether to rob adjacent houses
    
    DP State:
    - dp[i] = maximum points earned up to number i
    
    DP Recurrence:
    - dp[i] = max(dp[i-1], dp[i-2] + i * count[i])
    
    Pattern Recognition:
    - Problem transformation (reduce to a familiar problem)
    - House Robber pattern
    - Counting and grouping elements
    
    Time: O(n + m) where n is the length of nums and m is the range of values
    Space: O(m) for the DP array and counts
    """
    if not nums:
        return 0
    
    # Find the maximum value to determine the size of our arrays
    max_num = max(nums)
    
    # Count occurrences of each number
    counts = [0] * (max_num + 1)
    for num in nums:
        counts[num] += num  # Directly store the total points for this number
    
    # Initialize DP array
    dp = [0] * (max_num + 1)
    dp[1] = counts[1]  # Base case
    
    # Fill the DP array
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i-1], dp[i-2] + counts[i])
    
    return dp[max_num]


# Space-optimized solution
def deleteAndEarn_optimized(nums):
    """
    Space-optimized solution using just two variables
    
    Time: O(n + m)
    Space: O(m) for counts, O(1) for DP variables
    """
    if not nums:
        return 0
    
    # Count the points for each number
    points = {}
    for num in nums:
        points[num] = points.get(num, 0) + num
    
    # Get sorted unique numbers
    sorted_nums = sorted(points.keys())
    
    # Initialize with the first number
    prev2 = 0  # Max points two numbers ago
    prev1 = points.get(sorted_nums[0], 0)  # Max points one number ago
    
    # Fill in the DP values
    for i in range(1, len(sorted_nums)):
        current = sorted_nums[i]
        prev = sorted_nums[i-1]
        
        # If current and prev are adjacent, we have a "house robber" decision
        if current == prev + 1:
            # Either take current (and skip prev) or skip current (keep prev)
            temp = prev1
            prev1 = max(prev1, prev2 + points[current])
            prev2 = temp
        else:
            # If not adjacent, we can take both
            prev2 = prev1
            prev1 = prev1 + points[current]
    
    return prev1


# Test cases
print("\n" + "=" * 70)
print("Problem 25: LeetCode 740 - Delete and Earn")
print("=" * 70)

test_cases_740 = [
    ([3, 4, 2], 6),
    ([2, 2, 3, 3, 3, 4], 9),
    ([1, 1, 1, 2, 4, 5, 5, 5, 6], 18),
    ([8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1, 4], 61),
    ([1], 1)
]

for nums, expected in test_cases_740:
    result = deleteAndEarn_optimized(nums)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 26: LeetCode 1105 - Filling Bookcase Shelves (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are given an array of books where books[i] = [thicknessi, heighti] indicates the thickness and height
of the ith book. You are also given an integer shelfWidth.

We want to place these books in order onto bookcase shelves that have a total width shelfWidth.

We choose some of the books to place on this shelf such that the sum of their thickness is <= shelfWidth,
then build another level of the shelf of the bookcase so that the total height of the bookcase has increased 
by the maximum height of the books we just put down. We repeat this process until there are no more books to place.

Note that at each step of the above process, the order of the books we place is the same order as the given 
sequence of books.

For example, if we have an ordered list of 5 books, we might place the first and second book onto the first shelf, 
the third book on the second shelf, and the fourth and fifth book on the last shelf.
Return the minimum possible height that the total bookshelf can be after placing shelves in this manner.

Example 1:
Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,2]], shelfWidth = 4
Output: 6
Explanation: The sum of the heights of the 3 shelves is 1 + 3 + 2 = 6.
Notice that book number 2 does not have to be on the first shelf.

Example 2:
Input: books = [[1,3],[2,4],[3,2]], shelfWidth = 6
Output: 4

Constraints:
- 1 <= books.length <= 1000
- 1 <= thicknessi <= shelfWidth <= 1000
- 1 <= heighti <= 1000
"""

def minHeightShelves(books, shelfWidth):
    """
    Approach: Dynamic Programming with Greedy Shelf Filling
    
    Key Insight:
    - For each book, we have two choices:
      1. Put it on a new shelf by itself
      2. Put it on the current shelf with previous books
    - For option 2, we can consider different "breakpoints" for the shelf
    
    DP State:
    - dp[i] = minimum height of bookshelf for books[0...i-1]
    
    DP Recurrence:
    - dp[i] = min(dp[j] + max_height(books[j...i-1])) for all valid j
    
    Pattern Recognition:
    - Partition optimization
    - Layout/packing problem
    - Greedy within DP
    
    Time: O(n²) where n is the number of books
    Space: O(n) for the DP array
    """
    n = len(books)
    
    # Initialize DP array
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # Base case: no books means 0 height
    
    for i in range(1, n + 1):
        width = 0  # Current shelf width
        max_height = 0  # Maximum height of books on current shelf
        
        # Try different breakpoints for the shelf
        # j = i means the current book starts a new shelf
        # j < i means we place books[j:i] on the same shelf
        for j in range(i, 0, -1):
            width += books[j-1][0]  # Add book thickness
            
            # If shelf width is exceeded, we can't put more books on this shelf
            if width > shelfWidth:
                break
            
            # Update max height of current shelf
            max_height = max(max_height, books[j-1][1])
            
            # Update minimum height for books[0...i-1]
            # dp[j-1] = height of shelves for books[0...j-2]
            # max_height = height of current shelf with books[j-1...i-1]
            dp[i] = min(dp[i], dp[j-1] + max_height)
    
    return dp[n]


# Test cases
print("\n" + "=" * 70)
print("Problem 26: LeetCode 1105 - Filling Bookcase Shelves")
print("=" * 70)

test_cases_1105 = [
    ([[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 2]], 4, 6),
    ([[1, 3], [2, 4], [3, 2]], 6, 4),
    ([[7, 3], [8, 7], [2, 7], [2, 5]], 10, 15),
    ([[1, 1], [2, 2], [3, 3]], 3, 3)
]

for books, shelfWidth, expected in test_cases_1105:
    result = minHeightShelves(books, shelfWidth)
    status = "✅" if result == expected else "❌"
    print(f"books={books}, shelfWidth={shelfWidth} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 27: LeetCode 1425 - Constrained Subsequence Sum (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an integer array nums and an integer k, return the maximum sum of a non-empty 
subsequence of that array such that for every two consecutive integers in the subsequence, 
nums[i] and nums[j], where i < j, j - i <= k.

A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, 
leaving the remaining elements in their original order.

Example 1:
Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subsequence is [10, 2, 5, 20].

Example 2:
Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subsequence must be non-empty, so we choose the largest number.

Example 3:
Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subsequence is [10, -2, -5, 20].

Constraints:
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

from collections import deque

def constrainedSubsetSum(nums, k):
    """
    Approach: Dynamic Programming with Monotonic Deque
    
    Key Insight:
    - This is a maximum subsequence sum problem with an additional constraint
    - For each position, we want to find the maximum sum ending at positions [i-k, i-1]
    - We can use a monotonic deque to efficiently track the maximum values in our sliding window
    
    DP State:
    - dp[i] = maximum subsequence sum ending at position i
    
    DP Recurrence:
    - dp[i] = nums[i] + max(0, dp[i-1], dp[i-2], ..., dp[i-k])
    
    Pattern Recognition:
    - Sliding window with DP
    - Monotonic queue optimization
    - Maximum subsequence sum variation
    
    Time: O(n) where n is the length of nums
    Space: O(n) for the DP array and deque
    """
    n = len(nums)
    
    # Initialize DP array
    dp = [0] * n
    dp[0] = nums[0]
    
    # Monotonic deque to track maximum values in the sliding window
    # Stores indices of potential maximums
    deq = deque([0])  # Start with the first element
    
    for i in range(1, n):
        # Get the maximum sum within the window
        while deq and deq[0] < i - k:
            deq.popleft()  # Remove elements outside the window
        
        # Current value is the array value plus the max value in the window (if positive)
        dp[i] = nums[i] + max(0, dp[deq[0]])
        
        # Maintain monotonic decreasing property of the deque
        while deq and dp[deq[-1]] <= dp[i]:
            deq.pop()  # Remove elements smaller than current
            
        deq.append(i)  # Add current index to the deque
    
    return max(dp)


# Alternative solution without using a deque (slower but simpler)
def constrainedSubsetSum_simple(nums, k):
    """
    Standard DP approach without optimizations
    
    Time: O(n*k) - may be too slow for large inputs
    Space: O(n)
    """
    n = len(nums)
    dp = nums.copy()  # Start with the original values
    
    for i in range(1, n):
        # Check previous k elements
        for j in range(max(0, i-k), i):
            dp[i] = max(dp[i], nums[i] + dp[j])
    
    return max(dp)


# Test cases
print("\n" + "=" * 70)
print("Problem 27: LeetCode 1425 - Constrained Subsequence Sum")
print("=" * 70)

test_cases_1425 = [
    ([10, 2, -10, 5, 20], 2, 37),
    ([-1, -2, -3], 1, -1),
    ([10, -2, -10, -5, 20], 2, 23),
    ([3, 4, 3, 2], 2, 12),
    ([5, -1, -2, 3, 4, -5, 6], 3, 15)
]

for nums, k, expected in test_cases_1425:
    result = constrainedSubsetSum(nums, k)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums}, k={k} → {result} (expected: {expected}) {status}")


# ============================================================================
# FINAL CONCLUSION
# ============================================================================

"""
Summary of Additional Dynamic Programming Problems:

This comprehensive collection now covers virtually all key DP patterns:

1. Core DP Patterns:
   - Linear subsequence (LIS, LCS, Delete and Earn)
   - Grid/matrix traversal (Triangle, Dungeon Game, Minimum Path Sum)
   - Knapsack variations (Partition Equal Subset Sum, Target Sum)
   - Interval scheduling (Maximum Profit in Job Scheduling)
   - String transformation (Edit Distance, Longest String Chain)

2. Advanced Techniques:
   - Monotonic queue optimization (Constrained Subsequence Sum)
   - Recursive DP with constraints (Frog Jump, Super Egg Drop)
   - Calendar-based optimization (Minimum Cost For Tickets)
   - Layout optimization (Filling Bookcase Shelves)
   - State-machine transitions (Stock trading problems)

These problems represent the most common and important dynamic programming
patterns seen in technical interviews at top tech companies.