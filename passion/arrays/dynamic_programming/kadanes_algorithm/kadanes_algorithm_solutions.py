"""
================================================================================
KADANE'S ALGORITHM - COMPREHENSIVE PROBLEM SET
================================================================================

This file contains a comprehensive collection of Kadane's Algorithm problems
ranging from Easy to Hard difficulty, including FAANG and high-frequency
interview questions.

Topics Covered:
1. Classic Maximum Subarray Problems
2. Circular Array Variations
3. Maximum Product Subarray
4. Stock Buy/Sell Problems (Kadane's Variations)
5. Advanced Applications

Each problem includes:
- Detailed problem statement with examples
- Key Insights (pattern recognition and approach)
- Multiple solution approaches where applicable
- Time and Space Complexity Analysis
- Test cases with expected outputs

Author: DSA Practice Collection
Last Updated: December 2025
================================================================================
"""


# ============================================================================
# KADANE'S ALGORITHM - PATTERN TEMPLATE
# ============================================================================

def kadane_template(arr):
    """
    Template for maximum subarray and related problems
    
    Pattern:
    1. Track current_sum and max_sum
    2. At each position, decide whether to extend previous subarray or start a new one
    3. Update max_sum if current_sum is larger
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0
    
    current_sum = max_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Decision: extend previous subarray or start a new one
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update maximum sum found so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# ============================================================================
# PROBLEM 1: Maximum Subarray (LC 53)
# Difficulty: Medium
# FAANG Frequency: Very High (Amazon, Google, Microsoft, Meta, Apple)
# ============================================================================

"""
Problem Statement:
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - Need to find maximum sum of contiguous subarray
   - Classic Kadane's algorithm problem
   - Greedy approach: at each position, decide to extend or start new

2. CORE INTUITION:
   - If current_sum becomes negative, it's better to start fresh
   - Keep track of maximum sum seen so far
   - Local optimum leads to global optimum

3. DECISION AT EACH STEP:
   - current_sum + nums[i] vs nums[i]
   - If adding current element increases sum, extend subarray
   - Otherwise, start new subarray from current element

4. WHY IT WORKS:
   - A negative prefix will never help maximize the sum
   - We're essentially choosing the best starting point dynamically
   - Greedy choice property holds: local max leads to global max

5. EDGE CASES:
   - All negative numbers: return the largest (least negative)
   - Single element: return that element
   - All positive: return sum of entire array
"""

def maxSubArray_kadane(nums):
    """
    Approach 1: Classic Kadane's Algorithm
    
    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only two variables
    """
    if not nums:
        return 0
    
    current_sum = max_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Extend current subarray or start new one
        current_sum = max(nums[i], current_sum + nums[i])
        
        # Update global maximum
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def maxSubArray_with_indices(nums):
    """
    Approach 2: Kadane's with tracking start and end indices
    
    Returns: (max_sum, start_index, end_index)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0, -1, -1
    
    current_sum = max_sum = nums[0]
    start = end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        # If starting fresh, update temp_start
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum = current_sum + nums[i]
        
        # Update global maximum and indices
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return max_sum, start, end



# Test cases for Problem 1
def test_maximum_subarray():
    print("Testing Problem 1: Maximum Subarray")
    print("=" * 60)
    
    test_cases = [
        ([-2,1,-3,4,-1,2,1,-5,4], 6, "Mixed positive and negative"),
        ([1], 1, "Single element"),
        ([5,4,-1,7,8], 23, "Mostly positive"),
        ([-1], -1, "Single negative"),
        ([-2,-1], -1, "All negative"),
        ([1,2,3,4,5], 15, "All positive"),
        ([-2,1,-3,4,-1,2,1,-5,4], 6, "Example from problem"),
    ]
    
    for nums, expected, description in test_cases:
        result = maxSubArray_kadane(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        
        # Also test with indices
        max_sum, start, end = maxSubArray_with_indices(nums)
        print(f"  Subarray: {nums[start:end+1]} (indices {start} to {end})")
        print()


# ============================================================================
# PROBLEM 2: Maximum Sum Circular Subarray (LC 918)
# Difficulty: Medium
# FAANG Frequency: High (Google, Amazon, Meta)
# ============================================================================

"""
Problem Statement:
Given a circular integer array nums of length n, return the maximum possible sum 
of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array.
Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element 
of nums[i] is nums[(i - 1 + n) % n].

Example 1:
Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.

Example 2:
Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Example 3:
Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.

Constraints:
- n == nums.length
- 1 <= n <= 3 * 10^4
- -3 * 10^4 <= nums[i] <= 3 * 10^4
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - Circular array adds complexity to standard Kadane's
   - Maximum subarray can be in two forms:
     a) Normal subarray (doesn't wrap around)
     b) Circular subarray (wraps around)

2. BRILLIANT INSIGHT:
   - Case 1: Max subarray doesn't wrap → Standard Kadane's
   - Case 2: Max subarray wraps around → 
     * This is equivalent to: Total Sum - Min Subarray
     * The middle part (min subarray) is excluded
     * Wrapping part = Total - (what we exclude)

3. ALGORITHM:
   - Calculate max_kadane (normal maximum subarray)
   - Calculate min_kadane (minimum subarray to exclude)
   - Calculate total_sum
   - Answer = max(max_kadane, total_sum - min_kadane)

4. EDGE CASE:
   - If all numbers are negative:
     * total_sum - min_kadane would give 0 (excluding everything)
     * But we need non-empty subarray
     * Return max_kadane in this case

5. WHY THIS WORKS:
   - Wrapping around means we take prefix + suffix
   - Excluding middle = taking prefix + suffix
   - Min subarray in middle = what we want to exclude
"""

def maxSubarraySumCircular(nums):
    """
    Approach: Two Kadane's - Max and Min
    
    Time Complexity: O(n) - three passes (max, min, sum)
    Space Complexity: O(1)
    """
    def kadane_max(arr):
        current_sum = max_sum = arr[0]
        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
    
    def kadane_min(arr):
        current_sum = min_sum = arr[0]
        for i in range(1, len(arr)):
            current_sum = min(arr[i], current_sum + arr[i])
            min_sum = min(min_sum, current_sum)
        return min_sum
    
    max_kadane = kadane_max(nums)
    min_kadane = kadane_min(nums)
    total_sum = sum(nums)
    
    # Edge case: all negative numbers
    if max_kadane < 0:
        return max_kadane
    
    # Max of: normal subarray OR circular subarray
    return max(max_kadane, total_sum - min_kadane)


def maxSubarraySumCircular_single_pass(nums):
    """
    Approach 2: Single pass optimization
    Calculate max and min Kadane's in one pass
    
    Time Complexity: O(n) - single pass
    Space Complexity: O(1)
    """
    current_max = current_min = 0
    max_sum = min_sum = nums[0]
    total_sum = 0
    
    for num in nums:
        current_max = max(current_max + num, num)
        max_sum = max(max_sum, current_max)
        
        current_min = min(current_min + num, num)
        min_sum = min(min_sum, current_min)
        
        total_sum += num
    
    # Edge case: all negative
    if max_sum < 0:
        return max_sum
    
    return max(max_sum, total_sum - min_sum)


# Test cases for Problem 2
def test_circular_subarray():
    print("\nTesting Problem 2: Maximum Sum Circular Subarray")
    print("=" * 60)
    
    test_cases = [
        ([1,-2,3,-2], 3, "Simple case - no wrap"),
        ([5,-3,5], 10, "Wrap around case"),
        ([-3,-2,-3], -2, "All negative"),
        ([3,-1,2,-1], 4, "Wrap gives better result"),
        ([1,2,3,4,5], 15, "All positive"),
        ([-2,-3,-1], -1, "All negative, pick largest"),
    ]
    
    for nums, expected, description in test_cases:
        result = maxSubarraySumCircular(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# PROBLEM 3: Maximum Absolute Sum of Any Subarray (LC 1749)
# Difficulty: Medium
# FAANG Frequency: Medium (Google, Amazon)
# ============================================================================

"""
Problem Statement:
You are given an integer array nums. The absolute sum of a subarray 
[numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - Need maximum absolute value of subarray sum
   - Absolute value means we care about both max and min
   - |x| = max(x, -x)

2. KEY INSIGHT:
   - Maximum absolute sum = max(max_subarray_sum, |min_subarray_sum|)
   - Run Kadane's twice:
     a) Once for maximum sum
     b) Once for minimum sum
   - Return max of (max_sum, abs(min_sum))

3. WHY THIS WORKS:
   - Absolute value of negative number becomes positive
   - Most negative sum has largest absolute value among negatives
   - Compare largest positive sum vs largest negative sum (as positive)

4. ALGORITHM:
   - Apply standard Kadane's for maximum
   - Apply Kadane's for minimum (flip the logic)
   - Return max(max_sum, abs(min_sum))

5. OPTIMIZATION:
   - Can do both in single pass
   - Track both max and min simultaneously
"""

def maxAbsoluteSum(nums):
    """
    Approach: Two Kadane's - Max and Min
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Find maximum subarray sum
    current_max = max_sum = 0
    for num in nums:
        current_max = max(0, current_max + num)
        max_sum = max(max_sum, current_max)
    
    # Find minimum subarray sum
    current_min = min_sum = 0
    for num in nums:
        current_min = min(0, current_min + num)
        min_sum = min(min_sum, current_min)
    
    # Maximum absolute sum
    return max(max_sum, abs(min_sum))


def maxAbsoluteSum_single_pass(nums):
    """
    Approach 2: Single pass optimization
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    current_max = current_min = 0
    max_sum = min_sum = 0
    
    for num in nums:
        current_max = max(0, current_max + num)
        max_sum = max(max_sum, current_max)
        
        current_min = min(0, current_min + num)
        min_sum = min(min_sum, current_min)
    
    return max(max_sum, abs(min_sum))


# Test cases for Problem 3
def test_max_absolute_sum():
    print("\nTesting Problem 3: Maximum Absolute Sum")
    print("=" * 60)
    
    test_cases = [
        ([1,-3,2,3,-4], 5, "Mixed values"),
        ([2,-5,1,-4,3,-2], 8, "Large negative sum"),
        ([1,2,3,4], 10, "All positive"),
        ([-1,-2,-3,-4], 10, "All negative"),
        ([0], 0, "Single zero"),
    ]
    
    for nums, expected, description in test_cases:
        result = maxAbsoluteSum(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# PROBLEM 4: Maximum Product Subarray (LC 152)
# Difficulty: Medium
# FAANG Frequency: Very High (Amazon, Microsoft, Meta, Apple)
# ============================================================================

"""
Problem Statement:
Given an integer array nums, find a subarray that has the largest product, 
and return the product.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Example 3:
Input: nums = [-2,3,-4]
Output: 24
Explanation: [-2,3,-4] has the largest product 24.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - Similar to maximum sum subarray but with multiplication
   - Key difference: negative numbers can flip signs
   - Two negatives make a positive!

2. CRITICAL INSIGHT:
   - Need to track BOTH maximum and minimum
   - Why? A negative number can turn:
     * Small negative (min) → Large positive (new max)
     * Large positive (max) → Small negative (new min)

3. STATE TRANSITIONS:
   At each position, three choices:
   a) Start fresh with current number
   b) Multiply with previous max (if current is positive)
   c) Multiply with previous min (if current is negative)

4. ALGORITHM:
   - Track max_prod and min_prod at each step
   - When we see a negative number:
     * Swap max_prod and min_prod (signs flip)
   - Update: max_prod = max(num, max_prod * num, min_prod * num)
   - Update: min_prod = min(num, max_prod * num, min_prod * num)

5. EDGE CASES:
   - Zero resets both max and min to 0
   - Single negative number
   - Even number of negatives (all multiply to positive)
   - Odd number of negatives (need to exclude one)
"""

def maxProduct(nums):
    """
    Approach 1: Track both max and min products
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        num = nums[i]
        
        # If negative, swap max and min
        if num < 0:
            max_prod, min_prod = min_prod, max_prod
        
        # Update max and min
        max_prod = max(num, max_prod * num)
        min_prod = min(num, min_prod * num)
        
        # Update global result
        result = max(result, max_prod)
    
    return result


def maxProduct_no_swap(nums):
    """
    Approach 2: Without swapping (more explicit)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        num = nums[i]
        
        # Store previous values
        temp_max = max_prod
        
        # Calculate new max and min
        max_prod = max(num, max(temp_max * num, min_prod * num))
        min_prod = min(num, min(temp_max * num, min_prod * num))
        
        result = max(result, max_prod)
    
    return result


def maxProduct_two_passes(nums):
    """
    Approach 3: Two passes (left to right, right to left)
    Elegant alternative approach
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    result = nums[0]
    
    # Left to right
    product = 1
    for num in nums:
        product *= num
        result = max(result, product)
        if product == 0:
            product = 1
    
    # Right to left
    product = 1
    for i in range(len(nums) - 1, -1, -1):
        product *= nums[i]
        result = max(result, product)
        if product == 0:
            product = 1
    
    return result


# Test cases for Problem 4
def test_max_product():
    print("\nTesting Problem 4: Maximum Product Subarray")
    print("=" * 60)
    
    test_cases = [
        ([2,3,-2,4], 6, "Mixed with negative"),
        ([-2,0,-1], 0, "Contains zero"),
        ([-2,3,-4], 24, "All multiply to positive"),
        ([2,-5,-2,-4,3], 24, "Multiple negatives"),
        ([-2], -2, "Single negative"),
        ([0,2], 2, "Zero at start"),
        ([2,3,4], 24, "All positive"),
        ([-1,-2,-3,-4], 24, "All negative, even count"),
    ]
    
    for nums, expected, description in test_cases:
        result = maxProduct(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# UNIFIED STATE MACHINE TEMPLATE FOR STOCK BUY/SELL PROBLEMS
# ============================================================================

"""
TEMPLATE PATTERN FOR ALL STOCK PROBLEMS (I, II, III, IV)
=========================================================

Core Concept: State Machine with Buy/Sell States
-------------------------------------------------

For k transactions, we track 2k states:
- buy[i]: Max profit after ith buy (i = 0 to k-1)
- sell[i]: Max profit after ith sell (i = 0 to k-1)

Universal Template:
-------------------
for price in prices:
    for i in range(k):
        if i == 0:
            buy[i] = max(buy[i], 0 - price)           # First buy: use initial capital
        else:
            buy[i] = max(buy[i], sell[i-1] - price)   # Subsequent buy: use previous sell profit
        
        sell[i] = max(sell[i], buy[i] + price)        # Sell after current buy

Initialization:
---------------
buy[i] = float('-inf')  # Haven't bought yet (impossible state initially)
sell[i] = 0             # No profit yet (starting state)

Problem Variations:
-------------------
1. Stock I (LC 121):   k = 1 transaction
2. Stock II (LC 122):  k = ∞ (unlimited), use greedy or state machine
3. Stock III (LC 123): k = 2 transactions
4. Stock IV (LC 188):  k = k transactions (generalized)

State Transition Logic:
-----------------------
- buy[i] = max(keep_previous_buy, make_new_buy_using_previous_sell_profit)
- sell[i] = max(keep_previous_sell, make_new_sell_using_current_buy)

This ensures we always track the MAXIMUM profit at each state.
"""


# ============================================================================
# PROBLEM 5: Best Time to Buy and Sell Stock (LC 121)
# Difficulty: Easy
# FAANG Frequency: Very High (All FAANG companies)
# ============================================================================

"""
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing 
a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve 
any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - This is a Kadane's algorithm variation!
   - Instead of sum, we track profit (difference)
   - Convert to: max difference between future and past elements

2. KEY INSIGHT:
   - Track minimum price seen so far
   - At each day, calculate profit if we sell today
   - Profit = current_price - min_price_so_far
   - Keep track of maximum profit

3. CONNECTION TO KADANE'S:
   - If we compute daily price differences: diff[i] = prices[i] - prices[i-1]
   - Maximum profit = maximum subarray sum of differences
   - This is exactly Kadane's algorithm!

4. ALGORITHM (Two approaches):
   Approach 1: Track min price
   - Keep track of minimum price seen so far
   - Calculate profit at each step
   - Update max profit
   
   Approach 2: Convert to Kadane's
   - Create difference array
   - Apply Kadane's algorithm

5. WHY IT WORKS:
   - We need to buy before we sell (past < future)
   - Tracking min price ensures we buy at best time
   - Checking profit at each point ensures we sell at best time
"""

def maxProfit_stock(arr):
    """
    Approach 1: State Machine Template (k=1 transaction)

    States:
    - buy: Max profit after buying (negative, since we spent money)
    - sell: Max profit after selling

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0

    # Initialize states
    buy = float('-inf')  # Haven't bought yet
    sell = 0             # No profit yet

    idx = 0
    while idx < len(arr):
        price = arr[idx]
        # State transitions
        buy = max(buy, -price)        # Buy stock (spend money)
        sell = max(sell, buy + price) # Sell stock (gain profit)
        idx += 1

    return sell


def maxProfit_min_price_tracking(arr):
    """
    Approach 2: Track minimum price (alternative intuitive approach)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0
    
    min_price = arr[0]
    max_profit = 0
    
    idx = 0
    while idx < len(arr):
        price = arr[idx]
        # Update minimum price seen so far
        min_price = min(min_price, price)
        
        # Calculate profit if we sell today
        profit = price - min_price
        
        # Update maximum profit
        max_profit = max(max_profit, profit)
        idx += 1
    
    return max_profit


# Test cases for Problem 5
def test_stock_profit():
    print("\nTesting Problem 5: Best Time to Buy and Sell Stock")
    print("=" * 60)
    
    test_cases = [
        ([7,1,5,3,6,4], 5, "Buy at 1, sell at 6"),
        ([7,6,4,3,1], 0, "Decreasing prices"),
        ([1,2,3,4,5], 4, "Increasing prices"),
        ([2,4,1], 2, "Peak in middle"),
        ([3,3,3,3], 0, "All same price"),
    ]
    
    for prices, expected, description in test_cases:
        result = maxProfit_stock(prices)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {prices}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# PROBLEM 6: Best Time to Buy and Sell Stock II (LC 122)
# Difficulty: Medium
# FAANG Frequency: High (Amazon, Microsoft, Meta)
# ============================================================================

"""
Problem Statement:
You are given an integer array prices where prices[i] is the price of a given stock 
on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most 
one share of the stock at any time. However, you can buy it then immediately sell it 
on the same day.

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
Explanation: There is no way to make a positive profit.

Constraints:
- 1 <= prices.length <= 3 * 10^4
- 0 <= prices[i] <= 10^4
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - Multiple transactions allowed
   - Can buy and sell on same day
   - Greedy approach works!

2. KEY INSIGHT:
   - Capture every upward price movement
   - If prices[i+1] > prices[i], we profit by (prices[i+1] - prices[i])
   - Sum all positive differences

3. WHY THIS WORKS:
   - We can make as many transactions as we want
   - Every increase in price is an opportunity
   - Example: [1,3,5] = (3-1) + (5-3) = 2 + 2 = 4
   - Same as buying at 1, selling at 5: 5-1 = 4

4. ALGORITHM:
   - Iterate through prices
   - If price increases from previous day, add difference to profit
   - This is equivalent to buying at valleys and selling at peaks

5. MATHEMATICAL PROOF:
   If prices go: a → b → c where a < b < c
   - Multiple transactions: (b-a) + (c-b) = c-a
   - Single transaction: c-a
   - They're equal! So we can capture all increases.
"""

def maxProfit_multiple_transactions(arr):
    """
    Approach 1: State Machine Template (k=∞ unlimited transactions)
    
    States:
    - buy: Max profit after buying (can buy multiple times)
    - sell: Max profit after selling (can sell multiple times)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0
    
    # Initialize states
    buy = float('-inf')  # Haven't bought yet
    sell = 0             # No profit yet
    
    idx = 0
    while idx < len(arr):
        price = arr[idx]
        # State transitions (can use previous sell profit for next buy)
        prev_buy = buy
        buy = max(buy, sell - price)   # Buy stock (can reuse sell profit)
        sell = max(sell, prev_buy + price)  # Sell stock (gain profit)
        idx += 1
    
    return sell


def maxProfit_greedy(arr):
    """
    Approach 2: Greedy - capture all increases (alternative intuitive approach)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr or len(arr) < 2:
        return 0
    
    max_profit = 0
    
    i = 1
    while i < len(arr):
        # If price increased, capture the profit
        if arr[i] > arr[i-1]:
            max_profit += arr[i] - arr[i-1]
        i += 1
    
    return max_profit


# Test cases for Problem 6
def test_stock_profit_multiple():
    print("\nTesting Problem 6: Best Time to Buy and Sell Stock II")
    print("=" * 60)
    
    test_cases = [
        ([7,1,5,3,6,4], 7, "Multiple transactions"),
        ([1,2,3,4,5], 4, "Continuous increase"),
        ([7,6,4,3,1], 0, "Continuous decrease"),
        ([1,2,1,2,1,2], 3, "Multiple small profits"),
        ([3,3,3,3], 0, "No change"),
    ]
    
    for prices, expected, description in test_cases:
        result = maxProfit_multiple_transactions(prices)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {prices}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# RUN ALL TESTS
# ============================================================================

if __name__ == "__main__":
    print("\n" + "="*80)
    print("KADANE'S ALGORITHM - COMPREHENSIVE TEST SUITE")
    print("="*80)
    
    test_maximum_subarray()
    test_circular_subarray()
    test_max_absolute_sum()
    test_max_product()
    test_stock_profit()
    test_stock_profit_multiple()
    
    print("\n" + "="*80)
    print("ALL TESTS COMPLETED!")
    print("="*80)
    print("\nProblems covered:")
    print("1. LC 53  - Maximum Subarray (Classic Kadane's)")
    print("2. LC 918 - Maximum Sum Circular Subarray")
    print("3. LC 1749 - Maximum Absolute Sum")
    print("4. LC 152 - Maximum Product Subarray")
    print("5. LC 121 - Best Time to Buy/Sell Stock")
    print("6. LC 122 - Best Time to Buy/Sell Stock II")
    print("\nNext: Practice more advanced variations!")


# ============================================================================
# PROBLEM 7: Best Time to Buy and Sell Stock III (LC 123)
# Difficulty: Hard
# FAANG Frequency: Very High (Amazon, Microsoft, Google)
# ============================================================================

"""
Problem Statement:
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell 
the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are 
engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^5
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - Extension of stock problem with transaction limit
   - Need to track state: how many transactions completed
   - Dynamic programming with state machine

2. STATE MACHINE APPROACH:
   Four states to track:
   - buy1: Max profit after first buy
   - sell1: Max profit after first sell
   - buy2: Max profit after second buy
   - sell2: Max profit after second sell

3. STATE TRANSITIONS:
   - buy1 = max(buy1, -price)  # Buy first stock
   - sell1 = max(sell1, buy1 + price)  # Sell first stock
   - buy2 = max(buy2, sell1 - price)  # Buy second stock
   - sell2 = max(sell2, buy2 + price)  # Sell second stock

4. WHY THIS WORKS:
   - Each state represents best profit at that stage
   - buy1 tracks best time to buy first stock
   - sell1 tracks best profit after completing first transaction
   - buy2 uses profit from sell1 to buy second stock
   - sell2 gives final maximum profit

5. INITIALIZATION:
   - buy1 = buy2 = -infinity (haven't bought yet)
   - sell1 = sell2 = 0 (no profit yet)

6. ALTERNATIVE APPROACH:
   - Split array at each point
   - Max profit = max(left_profit[i] + right_profit[i])
   - Use Kadane's for left and right parts
"""

def maxProfit_two_transactions(arr):
    """
    Approach 1: State Machine Template (k=2 transactions)
    
    States (for 2 transactions):
    - buy1: Max profit after 1st buy
    - sell1: Max profit after 1st sell
    - buy2: Max profit after 2nd buy (uses profit from sell1)
    - sell2: Max profit after 2nd sell
    
    Template Pattern:
    For each transaction i:
      buy[i] = max(buy[i], sell[i-1] - price)
      sell[i] = max(sell[i], buy[i] + price)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    k = 2

    if not arr or k == 0:
        return 0

    # k transactions: Track min_buy and max_profit for each transaction
    min_buy = [arr[0]] * k  # Initialize with first price
    max_profit = [0] * k  # No profit initially

    right = 1
    while right < len(arr):
        i = 0
        while i < k:
            max_profit[i] = max(max_profit[i], arr[right] - min_buy[i])
            if i == 0:
                min_buy[i] = min(min_buy[i], arr[right])
            else:
                min_buy[i] = min(min_buy[i], arr[right] - max_profit[i - 1])
            i += 1
        right += 1

    return max_profit[k - 1]


# Test cases for Problem 7
def test_stock_two_transactions():
    print("\nTesting Problem 7: Best Time to Buy and Sell Stock III")
    print("=" * 60)
    
    test_cases = [
        ([3,3,5,0,0,3,1,4], 6, "Two separate transactions"),
        ([1,2,3,4,5], 4, "Single transaction better"),
        ([7,6,4,3,1], 0, "No profit possible"),
        ([1,2,4,2,5,7,2,4,9,0], 13, "Complex case"),
        ([2,1,2,0,1], 1, "Small profits"),
    ]
    
    for prices, expected, description in test_cases:
        result = maxProfit_two_transactions(prices)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {prices}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# PROBLEM 8: Best Time to Buy and Sell Stock IV (LC 188)
# Difficulty: Hard
# FAANG Frequency: High (Amazon, Google)
# ============================================================================

"""
Problem Statement:
You are given an integer array prices where prices[i] is the price of a given stock 
on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell 
the stock before you buy again).

Example 1:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. 
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

Constraints:
- 1 <= k <= 100
- 1 <= prices.length <= 1000
- 0 <= prices[i] <= 1000
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - Generalization of at most 2 transactions
   - Need to track k different transaction states
   - DP with transaction count dimension

2. KEY INSIGHT - OPTIMIZATION:
   - If k >= n/2, we can make unlimited transactions
   - Why? Maximum possible transactions = n/2 (buy-sell pairs)
   - If k >= n/2, use greedy approach (Problem 6)

3. DP STATE:
   - buy[i] = max profit after ith buy
   - sell[i] = max profit after ith sell
   - For each transaction i: 0 to k-1

4. STATE TRANSITIONS:
   For each price:
   - buy[i] = max(buy[i], sell[i-1] - price)
   - sell[i] = max(sell[i], buy[i] + price)

5. SPACE OPTIMIZATION:
   - Can use 1D arrays instead of 2D
   - Only need previous state, not entire history

6. EDGE CASES:
   - k = 0: no transactions, profit = 0
   - k >= n/2: unlimited transactions
   - Single price: no transaction possible
"""

def maxProfit_k_transactions(k, arr):
    """
    Approach: State Machine Template (k transactions)
    
    States (for k transactions):
    - buy[i]: Max profit after ith buy
    - sell[i]: Max profit after ith sell
    
    Template Pattern (generalized for k transactions):
    For each transaction i (0 to k-1):
      if i == 0:
        buy[i] = max(buy[i], 0 - price)           # First buy uses initial capital
      else:
        buy[i] = max(buy[i], sell[i-1] - price)   # Use profit from previous sell
      sell[i] = max(sell[i], buy[i] + price)      # Sell after current buy
    
    Time Complexity: O(n*k) or O(n) if k >= n/2
    Space Complexity: O(k)
    """

    if not arr or k == 0:
        return 0

    # k transactions: Track min_buy and max_profit for each transaction
    min_buy = [arr[0]] * k  # Initialize with first price
    max_profit = [0] * k  # No profit initially

    right = 1
    while right < len(arr):
        i = 0
        while i < k:
            max_profit[i] = max(max_profit[i], arr[right] - min_buy[i])
            if i == 0:
                min_buy[i] = min(min_buy[i], arr[right])
            else:
                min_buy[i] = min(min_buy[i], arr[right] - max_profit[i - 1])
            i += 1
        right += 1

    return max_profit[k - 1]


# Test cases for Problem 8
def test_stock_k_transactions():
    print("\nTesting Problem 8: Best Time to Buy and Sell Stock IV")
    print("=" * 60)
    
    test_cases = [
        (2, [2,4,1], 2, "k=2, simple case"),
        (2, [3,2,6,5,0,3], 7, "k=2, two transactions"),
        (1, [1,2,3,4,5], 4, "k=1, single transaction"),
        (3, [1,2,4,2,5,7,2,4,9,0], 15, "k=3, multiple opportunities"),
        (2, [7,6,4,3,1], 0, "Decreasing prices"),
        (100, [1,2,3,4,5], 4, "k > n/2, unlimited"),
    ]
    
    for k, prices, expected, description in test_cases:
        result = maxProfit_k_transactions(k, prices)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  k={k}, prices={prices}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# PROBLEM 9: Maximum Subarray Sum After One Operation (LC 1746)
# Difficulty: Medium
# FAANG Frequency: Medium (Google, Amazon)
# ============================================================================

"""
Problem Statement:
You are given an integer array nums. You must perform exactly one operation where you 
can replace one element nums[i] with nums[i] * nums[i].

Return the maximum possible subarray sum after performing exactly one operation.

Example 1:
Input: nums = [2,-1,-4,-3]
Output: 17
Explanation: You can perform the operation on index 2 (0-indexed) to make 
nums = [2,-1,16,-3]. Now, the maximum subarray sum is 2 + -1 + 16 = 17.

Example 2:
Input: nums = [1,-1,1,1,-1,-1,1]
Output: 4
Explanation: You can perform the operation on index 1 (0-indexed) to make 
nums = [1,1,1,1,-1,-1,1]. Now, the maximum subarray sum is 1 + 1 + 1 + 1 = 4.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - Kadane's with a twist: must square exactly one element
   - Need to track two states: with and without operation

2. KEY INSIGHT:
   - Track two Kadane's simultaneously:
     a) max_without_op: max sum without using operation yet
     b) max_with_op: max sum after using operation

3. STATE TRANSITIONS:
   At each position i:
   - max_without_op: standard Kadane's
   - max_with_op: either
     * Use operation on current element: max_without_op[i-1] + nums[i]^2
     * Already used operation: max_with_op[i-1] + nums[i]

4. ALGORITHM:
   - current_without = max(nums[i], current_without + nums[i])
   - current_with = max(
       nums[i] * nums[i],  # Start new with operation
       current_without + nums[i] * nums[i],  # Use operation now
       current_with + nums[i]  # Already used operation
     )

5. WHY THIS WORKS:
   - We must use operation exactly once
   - Track best sum with and without operation
   - Operation can be used at any point in the subarray
"""

def maxSumAfterOperation(nums):
    """
    Approach: Two-state Kadane's
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    # current_without: max sum without using operation
    # current_with: max sum with operation used
    current_without = 0
    current_with = 0
    result = float('-inf')
    
    for num in nums:
        # Update with operation (must use it at some point)
        current_with = max(
            num * num,  # Start new subarray with operation
            current_without + num * num,  # Use operation now
            current_with + num  # Already used operation before
        )
        
        # Update without operation (standard Kadane's)
        current_without = max(num, current_without + num)
        
        # Update result (must have used operation)
        result = max(result, current_with)
    
    return result


def maxSumAfterOperation_explicit(nums):
    """
    Approach 2: More explicit state tracking
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    
    max_without_op = 0  # Max sum without using operation
    max_with_op = nums[0] * nums[0]  # Max sum with operation used
    result = max_with_op
    
    for i in range(1, len(nums)):
        num = nums[i]
        squared = num * num
        
        # New max with operation
        new_with_op = max(
            squared,  # Start fresh with operation
            max_without_op + squared,  # Use operation now
            max_with_op + num  # Continue after operation
        )
        
        # New max without operation
        new_without_op = max(num, max_without_op + num)
        
        max_with_op = new_with_op
        max_without_op = new_without_op
        result = max(result, max_with_op)
    
    return result


# Test cases for Problem 9
def test_max_sum_after_operation():
    print("\nTesting Problem 9: Maximum Subarray Sum After One Operation")
    print("=" * 60)
    
    test_cases = [
        ([2,-1,-4,-3], 17, "Square negative to positive"),
        ([1,-1,1,1,-1,-1,1], 4, "Square -1 to 1"),
        ([1,2,3], 14, "All positive, square largest"),
        ([-1,-2,-3], 1, "All negative, square smallest"),
        ([5], 25, "Single element"),
    ]
    
    for nums, expected, description in test_cases:
        result = maxSumAfterOperation(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# PROBLEM 10: Maximum Score After Splitting a String (LC 1422)
# Difficulty: Easy
# FAANG Frequency: Medium (Amazon)
# ============================================================================

"""
Problem Statement:
Given a string s of zeros and ones, return the maximum score after splitting the 
string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring 
plus the number of ones in the right substring.

Example 1:
Input: s = "011101"
Output: 5
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
Input: s = "1111"
Output: 3

Constraints:
- 2 <= s.length <= 500
- The string s consists of characters '0' and '1' only.
"""

# KEY INSIGHTS:
"""
1. PATTERN RECOGNITION:
   - Similar to Kadane's: track running sum
   - Need to find optimal split point
   - Treat '0' as +1 for left, '1' as +1 for right

2. KEY INSIGHT:
   - Score = zeros_in_left + ones_in_right
   - ones_in_right = total_ones - ones_in_left
   - Score = zeros_in_left + total_ones - ones_in_left
   - Maximize: zeros_in_left - ones_in_left + total_ones
   - Since total_ones is constant, maximize: zeros_in_left - ones_in_left

3. KADANE'S CONNECTION:
   - Treat '0' as +1, '1' as -1
   - Find maximum prefix sum (but not including last element)
   - Add total number of ones

4. ALGORITHM:
   - Count total ones
   - Iterate through string (except last position)
   - Track: zeros_left - ones_left
   - Find maximum of this value
   - Add total_ones to get final score

5. WHY WE EXCLUDE LAST POSITION:
   - Both substrings must be non-empty
   - Right substring needs at least one character
"""

def maxScore_split_string(s):
    """
    Approach 1: Track zeros and ones
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(s) < 2:
        return 0
    
    total_ones = s.count('1')
    
    zeros_left = 0
    ones_left = 0
    max_score = 0
    
    # Iterate through all valid split points (not including last)
    for i in range(len(s) - 1):
        if s[i] == '0':
            zeros_left += 1
        else:
            ones_left += 1
        
        ones_right = total_ones - ones_left
        score = zeros_left + ones_right
        max_score = max(max_score, score)
    
    return max_score


def maxScore_kadane_style(s):
    """
    Approach 2: Kadane's style (treat 0 as +1, 1 as -1)
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(s) < 2:
        return 0
    
    total_ones = s.count('1')
    
    # Find max of (zeros_left - ones_left)
    current_diff = 0
    max_diff = float('-inf')
    
    for i in range(len(s) - 1):
        if s[i] == '0':
            current_diff += 1
        else:
            current_diff -= 1
        max_diff = max(max_diff, current_diff)
    
    return max_diff + total_ones


# Test cases for Problem 10
def test_max_score_split():
    print("\nTesting Problem 10: Maximum Score After Splitting String")
    print("=" * 60)
    
    test_cases = [
        ("011101", 5, "Mixed zeros and ones"),
        ("00111", 5, "Zeros at start"),
        ("1111", 3, "All ones"),
        ("00", 1, "All zeros"),
        ("01", 2, "Simple split"),
    ]
    
    for s, expected, description in test_cases:
        result = maxScore_split_string(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {s}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# UPDATE TEST RUNNER
# ============================================================================

def run_all_tests():
    """Run all test suites"""
    print("\n" + "="*80)
    print("KADANE'S ALGORITHM - COMPREHENSIVE TEST SUITE")
    print("="*80)
    
    test_maximum_subarray()
    test_circular_subarray()
    test_max_absolute_sum()
    test_max_product()
    test_stock_profit()
    test_stock_profit_multiple()
    test_stock_two_transactions()
    test_stock_k_transactions()
    test_max_sum_after_operation()
    test_max_score_split()
    
    print("\n" + "="*80)
    print("ALL TESTS COMPLETED!")
    print("="*80)
    print("\nProblems covered:")
    print("1. LC 53   - Maximum Subarray (Classic Kadane's)")
    print("2. LC 918  - Maximum Sum Circular Subarray")
    print("3. LC 1749 - Maximum Absolute Sum")
    print("4. LC 152  - Maximum Product Subarray")
    print("5. LC 121  - Best Time to Buy/Sell Stock")
    print("6. LC 122  - Best Time to Buy/Sell Stock II")
    print("7. LC 123  - Best Time to Buy/Sell Stock III (Hard)")
    print("8. LC 188  - Best Time to Buy/Sell Stock IV (Hard)")
    print("9. LC 1746 - Maximum Subarray Sum After One Operation")
    print("10. LC 1422 - Maximum Score After Splitting String")
    print("\n" + "="*80)
    print("DIFFICULTY BREAKDOWN:")
    print("Easy: 2 problems (LC 121, LC 1422)")
    print("Medium: 6 problems (LC 53, LC 918, LC 1749, LC 152, LC 122, LC 1746)")
    print("Hard: 2 problems (LC 123, LC 188)")
    print("\nAll problems include detailed Key Insights!")
    print("="*80)


if __name__ == "__main__":
    run_all_tests()
