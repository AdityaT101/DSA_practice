"""
================================================================================
UNIFIED STATE MACHINE TEMPLATE FOR STOCK BUY/SELL PROBLEMS
================================================================================

This template provides a consistent pattern for solving all Stock Buy/Sell 
problems (LC 121, 122, 123, 188) using a state machine approach.

Author: DSA Practice Collection
Last Updated: December 2025
================================================================================
"""


# ============================================================================
# CORE TEMPLATE PATTERN
# ============================================================================

"""
UNIVERSAL STATE MACHINE TEMPLATE
=================================

Concept:
--------
For k transactions, track 2k states:
- buy[0], buy[1], ..., buy[k-1]: Max profit after each buy
- sell[0], sell[1], ..., sell[k-1]: Max profit after each sell

Template Code:
--------------
"""

def stock_template(k, arr):
    """
    Universal template for k transactions
    
    Args:
        k: Number of allowed transactions
        arr: Array of stock prices
    
    Returns:
        Maximum profit achievable
    """
    if not arr or k == 0:
        return 0
    
    # Initialize states
    buy = [float('-inf')] * k   # Haven't bought yet
    sell = [0] * k               # No profit yet
    
    # Process each price
    right = 0
    while right < len(arr):
        price = arr[right]
        i = 0
        while i < k:
            # State transitions
            if i == 0:
                # First transaction: use initial capital (0)
                buy[i] = max(buy[i], 0 - price)
            else:
                # Subsequent transactions: use profit from previous sell
                buy[i] = max(buy[i], sell[i-1] - price)
            
            # Sell after current buy
            sell[i] = max(sell[i], buy[i] + price)
            i += 1
        right += 1
    
    return sell[k-1]


# ============================================================================
# PROBLEM-SPECIFIC IMPLEMENTATIONS
# ============================================================================

"""
PROBLEM 1: Best Time to Buy and Sell Stock (LC 121)
====================================================
Constraint: k = 1 (single transaction)
"""

def maxProfit_I(arr):
    """
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
        max_profit = max( max_profit , arr[right] - min_buy ) # calculate profit first
        min_buy = min(min_buy, arr[right])  # update min_buy

        right += 1
    
    return max_profit


"""
PROBLEM 2: Best Time to Buy and Sell Stock II (LC 122)
=======================================================
Constraint: k = ∞ (unlimited transactions)
"""

def maxProfit_II(arr):
    """
    Stock II: Unlimited transactions (k=∞)
    
    Template application:
    - buy: Max profit in "holding stock" state
    - sell: Max profit in "not holding stock" state
    - Key: Can reuse sell profit for next buy
    """
    if not arr:
        return 0
    
    # k=∞: Can buy and sell multiple times
    buy = float('-inf')
    max_profit = 0
    
    right = 0
    while right < len(arr):
        prev_buy = buy
        buy = max(buy, max_profit - arr[right])              # Can use sell profit
        max_profit = max(max_profit, prev_buy + arr[right])  # Sell after buy
        right += 1
    
    return max_profit


def maxProfit_II_greedy(arr):
    """
    Alternative: Greedy approach (more intuitive for unlimited transactions)
    Capture every price increase
    """
    max_profit = 0
    right = 1
    while right < len(arr):
        if arr[right] > arr[right-1]:
            max_profit += arr[right] - arr[right-1]
        right += 1
    return max_profit


"""
PROBLEM 3: Best Time to Buy and Sell Stock III (LC 123)
========================================================
Constraint: k = 2 (at most 2 transactions)
"""

def maxProfit_III(arr):
    """
    Stock III: Two transactions (k=2)
    
    Pattern application (similar to Stock I):
    - min_buy1: Minimum price for first buy
    - max_profit1: Maximum profit after first transaction
    - min_buy2: Minimum effective price for second buy (after using profit1)
    - max_profit2: Maximum profit after second transaction
    """
    if not arr:
        return 0
    
    # k=2: Track two transactions
    min_buy1 = arr[0]
    max_profit1 = 0
    min_buy2 = arr[0]  # Effective price for 2nd buy (will be adjusted by profit1)
    max_profit2 = 0
    
    right = 1
    while right < len(arr):
        # Transaction 1: Same pattern as Stock I
        max_profit1 = max(max_profit1, arr[right] - min_buy1)
        min_buy1 = min(min_buy1, arr[right])
        
        # Transaction 2: Use profit from transaction 1
        # min_buy2 tracks: arr[right] - max_profit1 (effective cost after using profit1)
        max_profit2 = max(max_profit2, arr[right] - min_buy2)
        min_buy2 = min(min_buy2, arr[right] - max_profit1)
        
        right += 1
    
    return max_profit2


"""
PROBLEM 4: Best Time to Buy and Sell Stock IV (LC 188)
=======================================================
Constraint: k = k (at most k transactions)
"""

def maxProfit_IV(k, arr):
    """
    Stock IV: K transactions (generalized)
    
    Pattern application (similar to Stock I):
    - min_buy[i]: Minimum effective price for transaction i
    - max_profit[i]: Maximum profit after transaction i
    - Each transaction uses profit from previous transaction
    """
    if not arr or k == 0:
        return 0
    
    n = len(arr)
    
    # Optimization: k >= n/2 means unlimited transactions
    if k >= n // 2:
        return maxProfit_II_greedy(arr)
    
    # k transactions: Track min_buy and max_profit for each transaction
    min_buy = [arr[0]] * k      # Initialize with first price
    max_profit = [0] * k         # No profit initially
    
    right = 1
    while right < len(arr):
        i = 0
        while i < k:
            max_profit[i] = max( max_profit[i], arr[right]-min_buy[i] )
            if i == 0:
                # Transaction 0: Same pattern as Stock I
                min_buy[i] = min( min_buy[i], arr[right] )
            else:
                # Transaction i: Use profit from transaction i-1
                # min_buy[i] tracks: arr[right] - max_profit[i-1]
                min_buy[i] = min( min_buy[i], arr[right]-max_profit[i-1] )
            i += 1
        right += 1
    
    return max_profit[k-1]


# ============================================================================
# KEY INSIGHTS AND PATTERNS
# ============================================================================

"""
WHY THIS TEMPLATE WORKS
========================

1. STATE MACHINE CONCEPT:
   - Each buy/sell represents a state in the transaction process
   - We track the MAXIMUM profit achievable at each state
   - States transition as we process each price

2. STATE TRANSITIONS:
   - buy[i] = max(keep_previous, make_new_buy)
     * keep_previous: Don't buy at this price
     * make_new_buy: Buy at this price using available capital
   
   - sell[i] = max(keep_previous, make_new_sell)
     * keep_previous: Don't sell at this price
     * make_new_sell: Sell at this price after buying

3. CAPITAL FLOW:
   - First buy (buy[0]): Uses initial capital (0)
   - Subsequent buys (buy[i]): Use profit from previous sell (sell[i-1])
   - This ensures transactions are sequential and don't overlap

4. INITIALIZATION:
   - buy[i] = float('-inf'): Impossible state initially (can't have bought)
   - sell[i] = 0: Starting state (no transactions, no profit)

5. WHY MAX()?
   - We want the BEST decision at each step
   - max() ensures we keep the most profitable path
   - This is the "greedy" aspect within the DP framework


PATTERN RECOGNITION
===================

When you see a Stock Buy/Sell problem:

1. Identify k (number of transactions allowed):
   - k = 1 → Stock I
   - k = ∞ → Stock II
   - k = 2 → Stock III
   - k = k → Stock IV

2. Apply the template:
   - Create k buy states and k sell states
   - Initialize: buy = -∞, sell = 0
   - For each price, update all states
   - Return sell[k-1]

3. Optimization:
   - If k >= n/2, use greedy (Stock II approach)
   - For k=1 or k=2, can unroll the loop for clarity


TIME & SPACE COMPLEXITY
========================

Stock I (k=1):
- Time: O(n)
- Space: O(1)

Stock II (k=∞):
- Time: O(n)
- Space: O(1)

Stock III (k=2):
- Time: O(n)
- Space: O(1)

Stock IV (k=k):
- Time: O(n*k) or O(n) if k >= n/2
- Space: O(k)


COMMON MISTAKES TO AVOID
=========================

1. ❌ Forgetting to use sell[i-1] for buy[i]
   ✓ buy[i] must use profit from previous transaction

2. ❌ Initializing buy to 0 instead of -∞
   ✓ buy = -∞ represents "haven't bought yet"

3. ❌ Returning buy[k-1] instead of sell[k-1]
   ✓ Final state should be "sold" (holding no stock)

4. ❌ Not handling k >= n/2 optimization in Stock IV
   ✓ Use greedy approach when k is large enough

5. ❌ Overlapping transactions
   ✓ Must sell before buying again (template ensures this)
"""


# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================

def test_all_stock_problems():
    """Test all stock problem implementations"""
    
    print("="*80)
    print("STOCK PROBLEMS - UNIFIED TEMPLATE TESTING")
    print("="*80)
    
    # Test data
    arr1 = [7,1,5,3,6,4]
    arr2 = [7,6,4,3,1]
    arr3 = [3,3,5,0,0,3,1,4]
    
    print("\n--- Stock I (k=1) ---")
    print(f"Array: {arr1}")
    print(f"Max Profit: {maxProfit_I(arr1)}")  # Expected: 5
    
    print("\n--- Stock II (k=∞) ---")
    print(f"Array: {arr1}")
    print(f"Max Profit: {maxProfit_II(arr1)}")  # Expected: 7
    
    print("\n--- Stock III (k=2) ---")
    print(f"Array: {arr3}")
    print(f"Max Profit: {maxProfit_III(arr3)}")  # Expected: 6
    
    print("\n--- Stock IV (k=2) ---")
    print(f"Array: {arr3}")
    print(f"Max Profit: {maxProfit_IV(2, arr3)}")  # Expected: 6
    
    print("\n" + "="*80)
    print("All tests completed!")
    print("="*80)


if __name__ == "__main__":
    test_all_stock_problems()
