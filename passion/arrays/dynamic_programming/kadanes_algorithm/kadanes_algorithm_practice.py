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


def maxSubArray_kadane(arr):
    """
    Approach 1: Classic Kadane's Algorithm

    Time Complexity: O(n) - single pass through array
    Space Complexity: O(1) - only two variables
    """
    if not arr:
        return 0

    current_sum = arr[0]
    global_max = max( float ('-inf'), current_sum )
    i = 1

    while i < len(arr) :
        current_sum = max( current_sum+arr[i] , arr[i])

        global_max = max( global_max, current_sum)

        i+=1

    return global_max


def maxSubArray_with_indices(arr):
    """
    Approach 2: Kadane's with tracking start and end indices

    Returns: (max_sum, start_index, end_index)

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0, -1, -1

    return_array = [0,0,0]

    left = 0
    right = 1
    current_sum = arr[0]
    global_max_sum = current_sum

    while( right < len(arr)):
        current_sum = arr[right] + current_sum

        if arr[right] > current_sum:
            current_sum = arr[right]
            left = right

        if current_sum > global_max_sum:
            global_max_sum = current_sum
            return_array = [ global_max_sum, left , right ]

        right+=1

    # print(return_array)
    return return_array


# Test cases for Problem 1
def test_maximum_subarray():
    print("Testing Problem 1: Maximum Subarray")
    print("=" * 60)

    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "Mixed positive and negative"),
        ([1], 1, "Single element"),
        ([5, 4, -1, 7, 8], 23, "Mostly positive"),
        ([-1], -1, "Single negative"),
        ([-2, -1], -1, "All negative"),
        ([1, -2, 3, -2], 3, " "),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "Example from problem"),
    ]

    for nums, expected, description in test_cases:
        #     result = maxSubArray_kadane(nums)
        #     status = "✓" if result == expected else "✗"
        #     print(f"{status} {description}")
        #     print(f"  Input: {nums}")
        #     print(f"  Expected: {expected}, Got: {result}")

        # Also test with indices
        max_sum, start, end = maxSubArray_with_indices(nums)
        print(f"  Subarray: {nums[start:end + 1]} (indices {start} to {end})")
        print()




# ============================================================================
# PROBLEM 2: Maximum Sum Circular Subarray (LC 918)
# Difficulty: Medium
# FAANG Frequency: High (Google, Amazon, Meta)
# ============================================================================

"""
Problem Statement:
Given a circular arr of length n, return the maximum possible sum 
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

def max_kadanes_subarray_sum(arr):
    left = 0
    right = 1
    global_max_sum = arr[0]
    current_subarray_sum = arr[0]
    result = [arr[0], 0, 0]

    while( right < len(arr) ):
        # as the name suggests , find out current_subarray_sum = current_subarray_sum + arr[right]
        current_subarray_sum += arr[right]

        # compare the value of current element vs current subarray sum
        # and then adjust the left pointer -> as soon as we find a number > current_subarray_sum, we move the left pointer to current element/value.
        if arr[right] > current_subarray_sum:
            current_subarray_sum = arr[right]
            left = right

        # since there can be multiple local maxima , keep a track of the global_max_sum in a separate variable.
        if current_subarray_sum > global_max_sum :
            global_max_sum = current_subarray_sum
            result = [ global_max_sum, left, right ]

        right+=1

    return result



def min_kadanes_subarray_sum(arr):
    left = 0
    right = 1
    global_min_sum = arr[0]
    current_subarray_sum = arr[0]
    result = [arr[0], 0, 0]

    while (right < len(arr)):
        # as the name suggests , find out current_subarray_sum = current_subarray_sum + arr[right]
        current_subarray_sum += arr[right]

        # compare the value of current element vs current subarray sum
        # and then adjust the left pointer -> as soon as we find a number < current_subarray_sum, we move the left pointer to current element/value.
        if arr[right] < current_subarray_sum:
            current_subarray_sum = arr[right]
            left = right

        # since there can be multiple local minima, keep a track of the global_min_sum in a separate variable.
        if current_subarray_sum < global_min_sum:
            global_min_sum = current_subarray_sum
            result = [global_min_sum, left, right]

        right += 1

    return result


def maxSubarraySumCircular(arr):
    """
    Approach: Two Kadane's - Max and Min

    Time Complexity: O(n) - three passes (max, min, sum)
    Space Complexity: O(1)
    """
    # Step 1: Get total sum
    total_sum = sum(arr)

    # Step 2: Find max subarray (normal case - no wrap)
    max_sum = max_kadanes_subarray_sum(arr)[0]

    # Step 3: Find min subarray (to exclude from circular)
    min_sum = min_kadanes_subarray_sum(arr)[0]

    # Step 4: Edge case check and return
    # If all negative, max_sum will be negative
    if max_sum < 0:
        return max_sum  # Can't use circular (would be empty)

    # Otherwise, compare normal vs circular
    circular_max = total_sum - min_sum
    return max(max_sum, circular_max)


# Test cases for Problem 2
def test_circular_subarray():
    print("\nTesting Problem 2: Maximum Sum Circular Subarray")
    print("=" * 60)

    test_cases = [
        # ([1, -2, 3, -2], 3, "Simple case - no wrap"),
        # ([5, -3, 5], 10, "Wrap around case"),
        ([-3, -2, -3], -2, "All negative"),
        ([3, -1, 2, -1], 4, "Wrap gives better result"),
        ([1, 2, 3, 4, 5], 15, "All positive"),
        ([-2, -3, -1], -1, "All negative, pick largest"),
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




# Test cases for Problem 3
# def test_max_absolute_sum():
#     print("\nTesting Problem 3: Maximum Absolute Sum")
#     print("=" * 60)
#
#     test_cases = [
#         ([1, -3, 2, 3, -4], 5, "Mixed values"),
#         ([2, -5, 1, -4, 3, -2], 8, "Large negative sum"),
#         ([1, 2, 3, 4], 10, "All positive"),
#         ([-1, -2, -3, -4], 10, "All negative"),
#         ([0], 0, "Single zero"),
#     ]
#
#     for nums, expected, description in test_cases:
#         result = maxAbsoluteSum(nums)
#         status = "✓" if result == expected else "✗"
#         print(f"{status} {description}")
#         print(f"  Input: {nums}")
#         print(f"  Expected: {expected}, Got: {result}")
#         print()



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


def maxProduct(arr):
    """
    Approach 1: Track both max and min products

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0

    left = 0
    right = 1

    max_product = min_product = arr[0]
    global_max_product = arr[0]

    print(f" iteration : - {0}, min_product :- {min_product}, max_product :- {max_product} ")

    while right < len(arr):

        if arr[right] < 0 :
            max_product, min_product = min_product, max_product

        max_product = max( arr[right] , max_product * arr[right])
        min_product = min( arr[right] , min_product * arr[right])

        global_max_product = max(global_max_product, max_product, min_product )

        print( f" iteration : - {right}, min_product :- {min_product}, max_product :- {max_product} ")

        right+=1


    return global_max_product


# Test cases for Problem 4
def test_max_product():
    print("\nTesting Problem 4: Maximum Product Subarray")
    print("=" * 60)

    test_cases = [
        ([2, 3, -2, 4], 6, "Mixed with negative"),
        ([-2, 0, -1], 0, "Contains zero"),
        ([-2, 3, -4], 24, "All multiply to positive"),
        ([2, -5, -2, -4, 3], 24, "Multiple negatives"),
        ([-2], -2, "Single negative"),
        ([0, 2], 2, "Zero at start"),
        ([2, 3, 4], 24, "All positive"),
        ([-1, -2, -3, -4], 24, "All negative, even count"),
    ]

    # for nums, expected, description in test_cases:
    #     result = maxProduct(nums)
    #     status = "✓" if result == expected else "✗"
    #     print(f"{status} {description}")
    #     print(f"  Input: {nums}")
    #     print(f"  Expected: {expected}, Got: {result}")
    #     print()



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
    Approach 1: Track minimum price

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = 1
    min_price = arr[0]
    max_diff = float('-inf')

    while( right < len(arr)):
        max_diff = max(max_diff, arr[right] - min_price)
        min_price = min( min_price, arr[right])
        right+=1

    return max_diff


def maxProfit_DP(arr):
    """
    Approach 2: Using DP algorithm on differences

    Time Complexity: O(n)
    Space Complexity: O(1)

    Stock I: Single transaction (k=1)

    Template application:
    - buy: Max profit after buying once
    - sell: Max profit after selling once
    """
    if not arr:
        return 0

    # k=1: Single buy and sell state
    min_buy = arr[0]
    max_profit = 0

    right = 1
    while right < len(arr):
        max_profit = max(max_profit, arr[right] - min_buy)  # calculate profit first
        min_buy = min(min_buy, arr[right])                  # update min_buy

        right += 1

    return max_profit



# Test cases for Problem 5
def test_stock_profit():
    print("\nTesting Problem 5: Best Time to Buy and Sell Stock")
    print("=" * 60)

    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5, "Buy at 1, sell at 6"),
        ([7, 6, 4, 3, 1], 0, "Decreasing prices"),
        ([1, 2, 3, 4, 5], 4, "Increasing prices"),
        ([2, 4, 1], 2, "Peak in middle"),
        ([3, 3, 3, 3], 0, "All same price"),
    ]

    for prices, expected, description in test_cases:
        result = maxProfit_DP(prices)
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
    k=2

    if not arr or k == 0:
        return 0

    # k transactions: Track min_buy and max_profit for each transaction
    min_buy = [arr[0]] * k  # Initialize with first price
    max_profit = [0] * k    # No profit initially

    right = 1
    while right < len(arr):
        i = 0
        while i < k:
            max_profit[i] = max( max_profit[i], arr[right]-min_buy[i])
            if i == 0:
                min_buy[i] = min( min_buy[i], arr[right])
            else:
                # min_buy[i] tracks: arr[right] - max_profit[i-1]
                min_buy[i] = min( min_buy[i], arr[right]-max_profit[i-1])
            i += 1
        right += 1

    return max_profit[k-1]


# Test cases for Problem 6
def test_stock_profit_multiple():
    print("\nTesting Problem 6: Best Time to Buy and Sell Stock II")
    print("=" * 60)

    test_cases = [
        ([7, 1, 5, 3, 6, 4], 7, "Multiple transactions"),
        ([1, 2, 3, 4, 5], 4, "Continuous increase"),
        ([7, 6, 4, 3, 1], 0, "Continuous decrease"),
        ([1, 2, 1, 2, 1, 2], 3, "Multiple small profits"),
        ([3, 3, 3, 3], 0, "No change"),
    ]

    for prices, expected, description in test_cases:
        result = maxProfit_multiple_transactions(prices)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {prices}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


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
        # Original test cases
        ([3, 3, 5, 0, 0, 3, 1, 4], 6, "Two separate transactions"),
        # ([1, 2, 3, 4, 5], 4, "Single transaction better"),
        # ([7, 6, 4, 3, 1], 0, "No profit possible"),
        # ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 13, "Complex case"),
        # ([2, 1, 2, 0, 1], 2, "Small profits"),
        #
        # # Edge cases
        # ([1], 0, "Single element"),
        # ([1, 1], 0, "Two same elements"),
        # ([2, 1], 0, "Two elements decreasing"),
        # ([1, 2], 1, "Two elements increasing"),
        #
        # # All same prices
        # ([5, 5, 5, 5, 5], 0, "All same prices"),
        #
        # # Large gap scenarios
        # ([1, 100, 1, 100], 198, "Two perfect transactions"),
        # ([1, 10, 1, 10, 1, 10], 18, "Three opportunities, pick best two"),
        #
        # # Overlapping vs separate transactions
        # ([1, 5, 0, 5], 9, "Better to do two separate"),
        # ([1, 4, 2, 5], 6, "Overlapping transactions"),
        #
        # # Peak in middle
        # ([1, 2, 10, 9, 8, 7], 9, "Peak in middle, single transaction"),
        # ([1, 2, 10, 1, 2, 10], 18, "Two identical peaks"),
        #
        # # Valley in middle
        # ([10, 9, 1, 2, 3], 2, "Valley in middle"),
        # ([10, 1, 10, 1, 10], 18, "Multiple valleys"),
        #
        # # Gradual increase then decrease
        # ([1, 2, 3, 4, 3, 2, 1], 3, "Gradual up then down"),
        #
        # # Complex real-world scenarios
        # ([6, 1, 3, 2, 4, 7], 7, "Buy at 1, sell at 7"),
        # ([2, 4, 1, 7, 5, 11], 12, "Two non-overlapping transactions"),
        # ([5, 11, 3, 50, 60, 90], 93, "Large gains possible"),
        #
        # # Stress test with many elements
        # ([1, 2, 1, 2, 1, 2, 1, 2], 2, "Many small opportunities"),
        #
        # # Zero profit scenarios
        # ([100, 90, 80, 70, 60], 0, "Continuous decline"),
        # ([50, 50, 50], 0, "Flat prices"),
        #
        # # Maximum two transactions needed
        # ([3, 2, 6, 5, 0, 3], 7, "LC example case"),
        # ([1, 2, 3, 0, 2], 4, "Simple two transactions"),
    ]


    for prices, expected, description in test_cases:
        result = maxProfit_two_transactions(prices)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {prices}")
        print(f"  Expected: {expected}, Got: {result}")
        if result != expected:
            print(f"  ⚠️  MISMATCH DETECTED!")
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
        (2, [2, 4, 1], 2, "k=2, simple case"),
        (2, [3, 2, 6, 5, 0, 3], 7, "k=2, two transactions"),
        (1, [1, 2, 3, 4, 5], 4, "k=1, single transaction"),
        (3, [1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 15, "k=3, multiple opportunities"),
        (2, [7, 6, 4, 3, 1], 0, "Decreasing prices"),
        (100, [1, 2, 3, 4, 5], 4, "k > n/2, unlimited"),
    ]

    for k, prices, expected, description in test_cases:
        result = maxProfit_k_transactions(k, prices)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  k={k}, prices={prices}")
        print(f"  Expected: {expected}, Got: {result}")
        print()


# ============================================================================
# UPDATE TEST RUNNER
# ============================================================================


def run_all_tests():
    """Run all test suites"""
    print("\n" + "=" * 80)
    print("KADANE'S ALGORITHM - COMPREHENSIVE TEST SUITE")
    print("=" * 80)

    # test_maximum_subarray()
    # test_circular_subarray()
    # test_max_absolute_sum()
    # test_max_product()
    # test_stock_profit()
    # test_stock_profit_multiple()
    # test_stock_two_transactions()
    test_stock_k_transactions()
    # test_max_sum_after_operation()
    # test_max_score_split()

    print("\n" + "=" * 80)
    print("ALL TESTS COMPLETED!")
    print("=" * 80)
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
    print("\n" + "=" * 80)
    print("DIFFICULTY BREAKDOWN:")
    print("Easy: 2 problems (LC 121, LC 1422)")
    print("Medium: 6 problems (LC 53, LC 918, LC 1749, LC 152, LC 122, LC 1746)")
    print("Hard: 2 problems (LC 123, LC 188)")
    print("\nAll problems include detailed Key Insights!")
    print("=" * 80)


if __name__ == "__main__":
    run_all_tests()
