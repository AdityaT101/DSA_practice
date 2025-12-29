"""
ARRAY TRAVERSAL PATTERNS - COMPREHENSIVE GUIDE
===============================================

This guide covers fundamental patterns for array/string problems:
1. Two Pointers
2. Sliding Window
3. Prefix Sums / Range Queries
4. Subarray Problems
5. String Manipulation & Pattern Matching

Each section includes:
- Pattern explanation
- When to use it
- Time/Space complexity
- Basic implementation template
"""

# ============================================================================
# 1. TWO POINTERS PATTERN
# ============================================================================

"""
CONCEPT:
--------
Use two pointers to traverse array from different positions/directions.
Reduces nested loops from O(n²) to O(n).

TYPES:
------
a) Opposite Direction (Left & Right)
b) Same Direction (Fast & Slow)
c) Multiple Arrays

WHEN TO USE:
------------
- Sorted arrays
- Finding pairs/triplets with specific sum
- Removing duplicates
- Reversing
- Detecting cycles
- Merging sorted arrays

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""

# Pattern 1a: Opposite Direction (Left & Right)
def two_pointers_opposite_direction(arr):
    """
    Pointers move towards each other from opposite ends.
    
    Use cases:
    - Finding pairs with target sum in sorted array
    - Palindrome checking
    - Container with most water
    """
    left = 0
    right = len(arr) - 1
    
    # while left < right:
    #     # Process elements at both pointers
    #     left_val = arr[left]
    #     right_val = arr[right]
    #
    #     # Decision logic determines which pointer moves
    #     # Example: if sum is too small, move left++
    #     #          if sum is too large, move right--
    #
    #     # Move pointers based on condition
    #     if some_condition:
    #         left += 1
    #     else:
    #         right -= 1
    #
    # return result


# Pattern 1b: Same Direction (Fast & Slow)
def two_pointers_same_direction(arr):
    """
    Both pointers move in same direction at different speeds.
    
    Use cases:
    - Removing duplicates in-place
    - Moving zeros to end
    - Cycle detection in linked list
    - Finding middle element
    """
    slow = 0
    fast = 0
    
    while fast < len(arr):
        # Fast pointer explores ahead
        # Slow pointer marks valid position
        
        if arr[fast]: #meets_condition:
            # Swap or assign
            arr[slow] = arr[fast]
            slow += 1
        
        fast += 1
    
    return slow  # Often returns new length or position


# Pattern 1c: Multiple Arrays
def two_pointers_multiple_arrays(arr1, arr2):
    """
    One pointer per array, merge or compare.
    
    Use cases:
    - Merging sorted arrays
    - Finding intersection
    - Comparing sequences
    """
    i = 0  # Pointer for arr1
    j = 0  # Pointer for arr2
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Handle remaining elements
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    
    return result


# ============================================================================
# 2. SLIDING WINDOW PATTERN
# ============================================================================

"""
CONCEPT:
--------
Maintain a window (subarray) that slides through the array.
Avoids recalculating from scratch for each position.

TYPES:
------
a) Fixed Window Size
b) Variable Window Size

WHEN TO USE:
------------
- Finding subarrays with specific properties
- Maximum/minimum in subarrays
- Substring problems
- Consecutive elements

KEY INSIGHT: Add new element, remove old element, update result
"""

# Pattern 2a: Fixed Window Size
def sliding_window_fixed(arr, k):
    """
    Window size is constant (k elements).
    
    Use cases:
    - Maximum sum of k consecutive elements
    - Average of subarrays of size k
    - First negative in every window of size k
    
    TIME: O(n)
    SPACE: O(1)
    """
    if len(arr) < k:
        return None
    
    # Calculate first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        # Remove leftmost element of previous window
        window_sum -= arr[i - k]
        
        # Add new element (rightmost of current window)
        window_sum += arr[i]
        
        # Update result
        max_sum = max(max_sum, window_sum)
    
    return max_sum


# Pattern 2b: Variable Window Size
def sliding_window_variable(arr, target):
    """
    Window size changes based on condition.
    
    Use cases:
    - Smallest subarray with sum >= target
    - Longest substring with k unique characters
    - Longest subarray with sum <= target
    
    TIME: O(n)
    SPACE: O(1) or O(k) for tracking window contents
    """
    left = 0
    right = 0
    current_sum = 0
    min_length = float('inf')
    
    while right < len(arr):
        # Expand window: add right element
        current_sum += arr[right]
        
        # Contract window: remove left elements while condition met
        while current_sum >= target:
            # Update result
            min_length = min(min_length, right - left + 1)
            
            # Shrink from left
            current_sum -= arr[left]
            left += 1
        
        # Move right pointer
        right += 1
    
    return min_length if min_length != float('inf') else 0


# Template for tracking window contents (for string problems)
def sliding_window_with_map(s, k):
    """
    Track elements in window using hash map.
    
    Use cases:
    - Longest substring with at most k distinct characters
    - Substring with all unique characters
    """
    left = 0
    char_count = {}  # Track frequency of characters in window
    max_length = 0
    
    for right in range(len(s)):
        # Add right character to window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Shrink window if condition violated
        while len(char_count) > k:  # Example: too many distinct chars
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ============================================================================
# 3. PREFIX SUMS / RANGE QUERIES
# ============================================================================

"""
CONCEPT:
--------
Precompute cumulative sums to answer range queries in O(1).
prefix[i] = sum of elements from index 0 to i

FORMULA:
--------
sum(arr[i:j+1]) = prefix[j] - prefix[i-1]

WHEN TO USE:
------------
- Multiple range sum queries
- Subarray sum problems
- Finding subarrays with specific sum
- 2D matrix range queries

TIME: O(n) preprocessing, O(1) per query
SPACE: O(n)
"""

# Pattern 3a: Basic Prefix Sum
def build_prefix_sum(arr):
    """
    Build prefix sum array.
    prefix[i] = sum of arr[0] to arr[i]
    """
    n = len(arr)
    prefix = [0] * n
    
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    
    return prefix


def range_sum_query(prefix, left, right):
    """
    Get sum of elements from index left to right (inclusive).
    
    TIME: O(1)
    """
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


# Pattern 3b: Prefix Sum with Hash Map
def prefix_sum_with_hashmap(arr, target):
    """
    Find count of subarrays with sum equal to target.
    
    KEY INSIGHT: If prefix[j] - prefix[i] = target,
                 then subarray from i+1 to j has sum = target
    
    Use cases:
    - Count subarrays with given sum
    - Continuous subarray sum
    - Subarray sum divisible by k
    
    TIME: O(n)
    SPACE: O(n)
    """
    prefix_sum = 0
    count = 0
    # Map: prefix_sum -> frequency
    sum_count = {0: 1}  # Initialize with 0 for subarrays starting at index 0
    
    for num in arr:
        prefix_sum += num
        
        # Check if (prefix_sum - target) exists
        # If yes, we found subarray(s) with sum = target
        if (prefix_sum - target) in sum_count:
            count += sum_count[prefix_sum - target]
        
        # Add current prefix_sum to map
        sum_count[prefix_sum] = sum_count.get(prefix_sum, 0) + 1
    
    return count


# Pattern 3c: 2D Prefix Sum (Matrix)
def build_2d_prefix_sum(matrix):
    """
    Build 2D prefix sum for matrix range queries.
    
    prefix[i][j] = sum of all elements in rectangle from (0,0) to (i,j)
    """
    if not matrix:
        return []
    
    rows, cols = len(matrix), len(matrix[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = (matrix[i-1][j-1] + 
                           prefix[i-1][j] + 
                           prefix[i][j-1] - 
                           prefix[i-1][j-1])
    
    return prefix


def range_sum_2d(prefix, row1, col1, row2, col2):
    """
    Get sum of rectangle from (row1, col1) to (row2, col2).
    
    TIME: O(1)
    """
    return (prefix[row2+1][col2+1] - 
            prefix[row1][col2+1] - 
            prefix[row2+1][col1] + 
            prefix[row1][col1])


# ============================================================================
# 4. SUBARRAY PROBLEMS
# ============================================================================

"""
CONCEPT:
--------
Problems involving contiguous elements in array.
Often combined with other patterns.

COMMON TECHNIQUES:
------------------
a) Kadane's Algorithm (Maximum Subarray)
b) Hash Map + Prefix Sum
c) Sliding Window
d) Two Pointers

TYPES:
------
- Maximum/minimum sum subarray
- Subarray with given sum
- Longest subarray with condition
- Count of subarrays
"""

# Pattern 4a: Kadane's Algorithm
def kadanes_algorithm(arr):
    """
    Find maximum sum of contiguous subarray.
    
    KEY INSIGHT: At each position, decide:
                 - Extend current subarray, OR
                 - Start new subarray from current element
    
    TIME: O(n)
    SPACE: O(1)
    """
    max_sum = arr[0]
    current_sum = arr[0]
    
    for i in range(1, len(arr)):
        # Either extend current subarray or start fresh
        current_sum = max(arr[i], current_sum + arr[i])
        
        # Update global maximum
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Pattern 4b: Subarray with Given Sum (using prefix sum + hash map)
def subarray_sum_equals_k(arr, k):
    """
    Count subarrays with sum equal to k.
    
    Combines prefix sum with hash map.
    """
    count = 0
    prefix_sum = 0
    sum_freq = {0: 1}
    
    for num in arr:
        prefix_sum += num
        
        # If (prefix_sum - k) exists, found subarray(s)
        if (prefix_sum - k) in sum_freq:
            count += sum_freq[prefix_sum - k]
        
        sum_freq[prefix_sum] = sum_freq.get(prefix_sum, 0) + 1
    
    return count


# Pattern 4c: Longest Subarray with Condition
def longest_subarray_with_sum_at_most_k(arr, k):
    """
    Find length of longest subarray with sum <= k.
    
    Uses sliding window.
    """
    left = 0
    current_sum = 0
    max_length = 0
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        # Shrink window if sum exceeds k
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


# ============================================================================
# 5. STRING MANIPULATION & PATTERN MATCHING
# ============================================================================

"""
CONCEPT:
--------
String-specific algorithms and patterns.

COMMON PATTERNS:
----------------
a) Character frequency (Hash Map)
b) Sliding Window for substrings
c) Two Pointers for palindromes
d) Pattern matching algorithms

TECHNIQUES:
-----------
- Hash map for character counting
- Sliding window for substring problems
- Two pointers for palindrome/reversal
- KMP/Rabin-Karp for pattern matching (advanced)
"""

# Pattern 5a: Character Frequency with Hash Map
def character_frequency_pattern(s):
    """
    Track character frequencies.
    
    Use cases:
    - Anagram checking
    - Valid anagram
    - Group anagrams
    - First unique character
    """
    freq = {}
    
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    return freq


def are_anagrams(s1, s2):
    """Check if two strings are anagrams."""
    if len(s1) != len(s2):
        return False
    
    return character_frequency_pattern(s1) == character_frequency_pattern(s2)


# Pattern 5b: Sliding Window for Substring
def longest_substring_with_k_distinct(s, k):
    """
    Find longest substring with at most k distinct characters.
    
    TIME: O(n)
    SPACE: O(k)
    """
    left = 0
    char_count = {}
    max_length = 0
    
    for right in range(len(s)):
        # Expand window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Contract window if too many distinct characters
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Pattern 5c: Two Pointers for Palindrome
def is_palindrome(s):
    """
    Check if string is palindrome.
    
    TIME: O(n)
    SPACE: O(1)
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


def expand_around_center(s, left, right):
    """
    Expand around center to find palindrome.
    
    Use cases:
    - Longest palindromic substring
    - Count palindromic substrings
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        # Current substring s[left:right+1] is palindrome
        left -= 1
        right += 1
    
    # Return length of palindrome
    return right - left - 1


# Pattern 5d: Pattern Matching Template
def find_pattern_positions(text, pattern):
    """
    Find all positions where pattern occurs in text.
    (Naive approach - O(n*m))
    
    For better performance, use:
    - KMP Algorithm: O(n+m)
    - Rabin-Karp: O(n+m) average
    - Boyer-Moore: O(n/m) best case
    """
    positions = []
    n, m = len(text), len(pattern)
    
    for i in range(n - m + 1):
        # Check if pattern matches at position i
        if text[i:i+m] == pattern:
            positions.append(i)
    
    return positions


# Pattern 5e: Sliding Window with Character Map (Advanced)
def min_window_substring_template(s, t):
    """
    Template for minimum window substring problems.
    
    Find smallest substring of s containing all characters of t.
    
    TIME: O(n + m)
    SPACE: O(m)
    """
    if not s or not t:
        return ""
    
    # Count characters needed
    target_count = {}
    for char in t:
        target_count[char] = target_count.get(char, 0) + 1
    
    required = len(target_count)  # Unique characters needed
    formed = 0  # Unique characters matched with desired frequency
    
    window_count = {}
    left = 0
    min_len = float('inf')
    min_window = (0, 0)
    
    for right in range(len(s)):
        # Add character from right
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        
        # Check if frequency matches
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1
        
        # Try to contract window
        while formed == required and left <= right:
            # Update result
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)
            
            # Remove from left
            char = s[left]
            window_count[char] -= 1
            if char in target_count and window_count[char] < target_count[char]:
                formed -= 1
            
            left += 1
    
    return "" if min_len == float('inf') else s[min_window[0]:min_window[1]+1]


# ============================================================================
# PATTERN SELECTION GUIDE
# ============================================================================

"""
HOW TO CHOOSE THE RIGHT PATTERN:
---------------------------------

1. TWO POINTERS:
   - Array is sorted
   - Need to find pairs/triplets
   - Need O(1) space
   - Keywords: "pair", "triplet", "sorted", "opposite ends"

2. SLIDING WINDOW:
   - Contiguous subarray/substring
   - Need to track window contents
   - Keywords: "substring", "subarray", "consecutive", "window"

3. PREFIX SUM:
   - Multiple range queries
   - Subarray sum problems
   - Keywords: "range sum", "subarray sum", "multiple queries"

4. KADANE'S (Subarray):
   - Maximum/minimum subarray sum
   - Keywords: "maximum sum", "contiguous", "subarray"

5. HASH MAP:
   - Need to track frequencies
   - Need O(1) lookup
   - Keywords: "frequency", "count", "anagram", "duplicate"

6. STRING PATTERNS:
   - Character manipulation
   - Pattern matching
   - Palindromes
   - Keywords: "substring", "pattern", "palindrome", "anagram"

COMPLEXITY GOALS:
-----------------
- Two Pointers: O(n) time, O(1) space
- Sliding Window: O(n) time, O(k) space (k = window tracking)
- Prefix Sum: O(n) preprocessing, O(1) query
- Kadane's: O(n) time, O(1) space
- Hash Map: O(n) time, O(n) space
"""


# ============================================================================
# PRACTICE TEMPLATE
# ============================================================================

def problem_solving_template(arr):
    """
    General approach to array/string problems:
    
    1. UNDERSTAND:
       - What is the input? (sorted? duplicates? size?)
       - What is the output? (value? index? count? length?)
       - What are constraints? (time? space?)
    
    2. IDENTIFY PATTERN:
       - Is it about pairs/triplets? → Two Pointers
       - Is it about subarrays/substrings? → Sliding Window
       - Is it about range queries? → Prefix Sum
       - Is it about max/min subarray? → Kadane's
       - Need frequency tracking? → Hash Map
    
    3. EDGE CASES:
       - Empty array/string
       - Single element
       - All same elements
       - No valid answer
    
    4. OPTIMIZE:
       - Can we do better than O(n²)?
       - Can we reduce space?
       - Can we avoid sorting?
    """
    pass


if __name__ == "__main__":
    print("Array Traversal Patterns Guide")
    print("=" * 50)
    print("\nThis file contains templates and explanations for:")
    print("1. Two Pointers")
    print("2. Sliding Window")
    print("3. Prefix Sums / Range Queries")
    print("4. Subarray Problems")
    print("5. String Manipulation & Pattern Matching")
    print("\nRefer to each section for detailed explanations and templates.")
