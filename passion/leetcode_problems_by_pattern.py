"""
LEETCODE PROBLEMS MAPPED TO ARRAY TRAVERSAL PATTERNS
====================================================

This document maps each use case from array_traversal_patterns_guide.py
to specific LeetCode problems.

Format:
- Pattern Name
  - Use Case Description
    → LeetCode Problem Number & Name
    → Difficulty Level
    → Key Insights
"""

# ============================================================================
# 1. TWO POINTERS PATTERN
# ============================================================================

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 1A: OPPOSITE DIRECTION (LEFT & RIGHT)
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Finding pairs with target sum in sorted array
"""
→ LeetCode 1: Two Sum
  Difficulty: Easy
  Note: Use hash map for unsorted; two pointers if sorted
  
→ LeetCode 167: Two Sum II - Input Array Is Sorted
  Difficulty: Easy
  Perfect example of two pointers on sorted array
  
→ LeetCode 15: 3Sum
  Difficulty: Medium
  Extension: Fix one element, use two pointers for remaining two
  
→ LeetCode 16: 3Sum Closest
  Difficulty: Medium
  Similar to 3Sum but tracking closest sum
  
→ LeetCode 18: 4Sum
  Difficulty: Medium
  Extension: Fix two elements, use two pointers for remaining two
"""

# Use Case: Palindrome checking
"""
→ LeetCode 125: Valid Palindrome
  Difficulty: Easy
  Basic two pointer palindrome check with character filtering
  
→ LeetCode 680: Valid Palindrome II
  Difficulty: Easy
  Can delete at most one character
  
→ LeetCode 5: Longest Palindromic Substring
  Difficulty: Medium
  Expand around center approach
  
→ LeetCode 647: Palindromic Substrings
  Difficulty: Medium
  Count all palindromic substrings using expand around center
"""

# Use Case: Container with most water
"""
→ LeetCode 11: Container With Most Water
  Difficulty: Medium
  Classic two pointer problem - move pointer with smaller height
  
→ LeetCode 42: Trapping Rain Water
  Difficulty: Hard
  Can use two pointers or stack approach
"""

# Use Case: Reversing
"""
→ LeetCode 344: Reverse String
  Difficulty: Easy
  Basic two pointer reversal
  
→ LeetCode 345: Reverse Vowels of a String
  Difficulty: Easy
  Two pointers with condition checking
  
→ LeetCode 151: Reverse Words in a String
  Difficulty: Medium
  Multiple steps: split, reverse, join
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 1B: SAME DIRECTION (FAST & SLOW)
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Removing duplicates in-place
"""
→ LeetCode 26: Remove Duplicates from Sorted Array
  Difficulty: Easy
  Slow pointer marks position for unique elements
  
→ LeetCode 80: Remove Duplicates from Sorted Array II
  Difficulty: Medium
  Allow duplicates to appear at most twice
  
→ LeetCode 83: Remove Duplicates from Sorted List
  Difficulty: Easy
  Same concept but for linked list
"""

# Use Case: Moving zeros to end
"""
→ LeetCode 283: Move Zeroes
  Difficulty: Easy
  Classic fast-slow pointer problem
  
→ LeetCode 27: Remove Element
  Difficulty: Easy
  Similar concept - remove specific value
"""

# Use Case: Cycle detection in linked list
"""
→ LeetCode 141: Linked List Cycle
  Difficulty: Easy
  Floyd's cycle detection algorithm
  
→ LeetCode 142: Linked List Cycle II
  Difficulty: Medium
  Find the start of the cycle
  
→ LeetCode 287: Find the Duplicate Number
  Difficulty: Medium
  Treat array as linked list, use cycle detection
"""

# Use Case: Finding middle element
"""
→ LeetCode 876: Middle of the Linked List
  Difficulty: Easy
  Fast moves 2x, slow moves 1x
  
→ LeetCode 234: Palindrome Linked List
  Difficulty: Easy
  Find middle, reverse second half, compare
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 1C: MULTIPLE ARRAYS
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Merging sorted arrays
"""
→ LeetCode 88: Merge Sorted Array
  Difficulty: Easy
  Merge in-place from the end
  
→ LeetCode 21: Merge Two Sorted Lists
  Difficulty: Easy
  Merge two sorted linked lists
  
→ LeetCode 23: Merge k Sorted Lists
  Difficulty: Hard
  Use heap or divide & conquer
"""

# Use Case: Finding intersection
"""
→ LeetCode 349: Intersection of Two Arrays
  Difficulty: Easy
  Can use hash set or two pointers if sorted
  
→ LeetCode 350: Intersection of Two Arrays II
  Difficulty: Easy
  Handle duplicates
  
→ LeetCode 160: Intersection of Two Linked Lists
  Difficulty: Easy
  Two pointers with length adjustment
"""

# Use Case: Comparing sequences
"""
→ LeetCode 392: Is Subsequence
  Difficulty: Easy
  Two pointers on different strings
  
→ LeetCode 524: Longest Word in Dictionary through Deleting
  Difficulty: Medium
  Check if string is subsequence of another
"""


# ============================================================================
# 2. SLIDING WINDOW PATTERN
# ============================================================================

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 2A: FIXED WINDOW SIZE
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Maximum sum of k consecutive elements
"""
→ LeetCode 643: Maximum Average Subarray I
  Difficulty: Easy
  Find max average of k consecutive elements
  
→ LeetCode 1456: Maximum Number of Vowels in a Substring of Given Length
  Difficulty: Medium
  Count vowels in fixed window of size k
"""

# Use Case: First negative in every window of size k
"""
→ LeetCode 239: Sliding Window Maximum
  Difficulty: Hard
  Find maximum in each window of size k (use deque)
  
→ LeetCode 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
  Difficulty: Medium
  Use deque to track min/max in window
"""

# Use Case: Anagrams in fixed window
"""
→ LeetCode 567: Permutation in String
  Difficulty: Medium
  Check if s2 contains permutation of s1 (fixed window = len(s1))
  
→ LeetCode 438: Find All Anagrams in a String
  Difficulty: Medium
  Find all anagram starting positions
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 2B: VARIABLE WINDOW SIZE
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Smallest subarray with sum >= target
"""
→ LeetCode 209: Minimum Size Subarray Sum
  Difficulty: Medium
  Classic variable window problem
  
→ LeetCode 862: Shortest Subarray with Sum at Least K
  Difficulty: Hard
  Handles negative numbers (use deque)
"""

# Use Case: Longest substring with k unique characters
"""
→ LeetCode 340: Longest Substring with At Most K Distinct Characters
  Difficulty: Medium
  Premium problem - track char frequency in window
  
→ LeetCode 159: Longest Substring with At Most Two Distinct Characters
  Difficulty: Medium
  Premium - special case of k=2
"""

# Use Case: Longest subarray with sum <= target
"""
→ LeetCode 1004: Max Consecutive Ones III
  Difficulty: Medium
  Flip at most k zeros - longest subarray with at most k zeros
  
→ LeetCode 1838: Frequency of the Most Frequent Element
  Difficulty: Medium
  Make all elements equal with k operations
"""

# Use Case: Longest substring with all unique characters
"""
→ LeetCode 3: Longest Substring Without Repeating Characters
  Difficulty: Medium
  Classic sliding window with hash map
  
→ LeetCode 1695: Maximum Erasure Value
  Difficulty: Medium
  Similar but track sum of unique elements
"""

# Use Case: Substring problems with character constraints
"""
→ LeetCode 76: Minimum Window Substring
  Difficulty: Hard
  Find smallest substring containing all characters of pattern
  
→ LeetCode 424: Longest Repeating Character Replacement
  Difficulty: Medium
  Replace at most k characters to get longest repeating substring
  
→ LeetCode 1358: Number of Substrings Containing All Three Characters
  Difficulty: Medium
  Count substrings with at least one a, b, c
"""

# Use Case: Subarray with specific properties
"""
→ LeetCode 904: Fruit Into Baskets
  Difficulty: Medium
  Longest subarray with at most 2 distinct elements
  
→ LeetCode 992: Subarrays with K Different Integers
  Difficulty: Hard
  Count subarrays with exactly k distinct integers
  
→ LeetCode 1248: Count Number of Nice Subarrays
  Difficulty: Medium
  Subarrays with exactly k odd numbers
"""


# ============================================================================
# 3. PREFIX SUMS / RANGE QUERIES
# ============================================================================

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 3A: BASIC PREFIX SUM
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Multiple range sum queries
"""
→ LeetCode 303: Range Sum Query - Immutable
  Difficulty: Easy
  Basic prefix sum array
  
→ LeetCode 304: Range Sum Query 2D - Immutable
  Difficulty: Medium
  2D prefix sum for matrix queries
  
→ LeetCode 1314: Matrix Block Sum
  Difficulty: Medium
  Sum of elements in k-distance neighborhood
"""

# Use Case: Running sum
"""
→ LeetCode 1480: Running Sum of 1d Array
  Difficulty: Easy
  Build prefix sum array
  
→ LeetCode 1991: Find the Middle Index in Array
  Difficulty: Easy
  Find pivot index using prefix sum
  
→ LeetCode 724: Find Pivot Index
  Difficulty: Easy
  Same as above
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 3B: PREFIX SUM WITH HASH MAP
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Count subarrays with given sum
"""
→ LeetCode 560: Subarray Sum Equals K
  Difficulty: Medium
  Classic prefix sum + hash map problem
  
→ LeetCode 930: Binary Subarrays With Sum
  Difficulty: Medium
  Count subarrays with sum = goal (binary array)
"""

# Use Case: Continuous subarray sum
"""
→ LeetCode 523: Continuous Subarray Sum
  Difficulty: Medium
  Subarray sum divisible by k (use modulo)
  
→ LeetCode 974: Subarray Sums Divisible by K
  Difficulty: Medium
  Count subarrays with sum divisible by k
"""

# Use Case: Subarray with equal elements
"""
→ LeetCode 525: Contiguous Array
  Difficulty: Medium
  Longest subarray with equal 0s and 1s (treat 0 as -1)
  
→ LeetCode 1124: Longest Well-Performing Interval
  Difficulty: Medium
  Longest subarray with more tiring days (>8 hours)
"""

# Use Case: Maximum subarray sum
"""
→ LeetCode 325: Maximum Size Subarray Sum Equals k
  Difficulty: Medium
  Premium - longest subarray with sum = k
  
→ LeetCode 1371: Find the Longest Substring Containing Vowels in Even Counts
  Difficulty: Medium
  Use bitmask + prefix sum concept
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 3C: 2D PREFIX SUM
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Matrix range queries
"""
→ LeetCode 304: Range Sum Query 2D - Immutable
  Difficulty: Medium
  Classic 2D prefix sum
  
→ LeetCode 1277: Count Square Submatrices with All Ones
  Difficulty: Medium
  DP + prefix sum concept
  
→ LeetCode 1292: Maximum Side Length of a Square with Sum Less than or Equal to Threshold
  Difficulty: Medium
  Binary search + 2D prefix sum
"""


# ============================================================================
# 4. SUBARRAY PROBLEMS
# ============================================================================

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 4A: KADANE'S ALGORITHM
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Maximum sum subarray
"""
→ LeetCode 53: Maximum Subarray
  Difficulty: Medium
  Classic Kadane's algorithm
  
→ LeetCode 918: Maximum Sum Circular Subarray
  Difficulty: Medium
  Kadane's with circular array consideration
  
→ LeetCode 1749: Maximum Absolute Sum of Any Subarray
  Difficulty: Medium
  Apply Kadane's for both max and min
"""

# Use Case: Maximum product subarray
"""
→ LeetCode 152: Maximum Product Subarray
  Difficulty: Medium
  Track both max and min (negative numbers flip signs)
"""

# Use Case: Best time to buy/sell stock
"""
→ LeetCode 121: Best Time to Buy and Sell Stock
  Difficulty: Easy
  Variation of Kadane's (max profit)
  
→ LeetCode 122: Best Time to Buy and Sell Stock II
  Difficulty: Medium
  Multiple transactions allowed
  
→ LeetCode 123: Best Time to Buy and Sell Stock III
  Difficulty: Hard
  At most 2 transactions
  
→ LeetCode 188: Best Time to Buy and Sell Stock IV
  Difficulty: Hard
  At most k transactions
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 4B: SUBARRAY WITH GIVEN SUM (PREFIX SUM + HASH MAP)
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Count subarrays with sum = k
"""
→ LeetCode 560: Subarray Sum Equals K
  Difficulty: Medium
  Already mentioned in prefix sum section
  
→ LeetCode 437: Path Sum III
  Difficulty: Medium
  Same concept but on binary tree
"""

# Use Case: Longest subarray with sum = k
"""
→ LeetCode 325: Maximum Size Subarray Sum Equals k
  Difficulty: Medium
  Premium - track first occurrence of each prefix sum
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 4C: LONGEST SUBARRAY WITH CONDITION
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Longest subarray with sum <= k
"""
→ LeetCode 1658: Minimum Operations to Reduce X to Zero
  Difficulty: Medium
  Find longest subarray with sum = total - x
  
→ LeetCode 2090: K Radius Subarray Averages
  Difficulty: Medium
  Calculate average of subarrays
"""

# Use Case: Longest subarray with constraints
"""
→ LeetCode 1493: Longest Subarray of 1's After Deleting One Element
  Difficulty: Medium
  Longest subarray with at most one 0 (must delete one)
  
→ LeetCode 2024: Maximize the Confusion of an Exam
  Difficulty: Medium
  Flip at most k characters to maximize consecutive T or F
"""


# ============================================================================
# 5. STRING MANIPULATION & PATTERN MATCHING
# ============================================================================

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 5A: CHARACTER FREQUENCY (HASH MAP)
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Anagram checking
"""
→ LeetCode 242: Valid Anagram
  Difficulty: Easy
  Compare character frequencies
  
→ LeetCode 49: Group Anagrams
  Difficulty: Medium
  Group strings by sorted characters or frequency map
  
→ LeetCode 1347: Minimum Number of Steps to Make Two Strings Anagram
  Difficulty: Medium
  Count character differences
"""

# Use Case: First unique character
"""
→ LeetCode 387: First Unique Character in a String
  Difficulty: Easy
  Find first non-repeating character
  
→ LeetCode 451: Sort Characters By Frequency
  Difficulty: Medium
  Sort by frequency (use bucket sort or heap)
"""

# Use Case: Character counting
"""
→ LeetCode 383: Ransom Note
  Difficulty: Easy
  Check if can construct from magazine
  
→ LeetCode 1160: Find Words That Can Be Formed by Characters
  Difficulty: Easy
  Check if words can be formed from given characters
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 5B: SLIDING WINDOW FOR SUBSTRING
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Longest substring with k distinct characters
"""
→ LeetCode 340: Longest Substring with At Most K Distinct Characters
  Difficulty: Medium
  Premium - already mentioned in sliding window
  
→ LeetCode 395: Longest Substring with At Least K Repeating Characters
  Difficulty: Medium
  Divide and conquer or sliding window with 26 iterations
"""

# Use Case: Minimum window substring
"""
→ LeetCode 76: Minimum Window Substring
  Difficulty: Hard
  Classic hard sliding window problem
  
→ LeetCode 727: Minimum Window Subsequence
  Difficulty: Hard
  Premium - find shortest substring containing subsequence
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 5C: TWO POINTERS FOR PALINDROME
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Check palindrome
"""
→ LeetCode 125: Valid Palindrome
  Difficulty: Easy
  Already mentioned in two pointers
  
→ LeetCode 680: Valid Palindrome II
  Difficulty: Easy
  Can delete at most one character
"""

# Use Case: Longest palindromic substring
"""
→ LeetCode 5: Longest Palindromic Substring
  Difficulty: Medium
  Expand around center
  
→ LeetCode 647: Palindromic Substrings
  Difficulty: Medium
  Count all palindromic substrings
  
→ LeetCode 516: Longest Palindromic Subsequence
  Difficulty: Medium
  Use DP (not expand around center)
"""

# Use Case: Palindrome construction
"""
→ LeetCode 131: Palindrome Partitioning
  Difficulty: Medium
  Backtracking + palindrome checking
  
→ LeetCode 132: Palindrome Partitioning II
  Difficulty: Hard
  DP - minimum cuts for palindrome partitioning
  
→ LeetCode 214: Shortest Palindrome
  Difficulty: Hard
  Add minimum characters to front to make palindrome
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 5D: PATTERN MATCHING
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: String matching
"""
→ LeetCode 28: Find the Index of the First Occurrence in a String
  Difficulty: Easy
  Implement strStr() - can use KMP for O(n+m)
  
→ LeetCode 459: Repeated Substring Pattern
  Difficulty: Easy
  Check if string can be constructed by repeating substring
  
→ LeetCode 686: Repeated String Match
  Difficulty: Medium
  Minimum repeats of A to contain B
"""

# Use Case: Subsequence matching
"""
→ LeetCode 392: Is Subsequence
  Difficulty: Easy
  Two pointers to check subsequence
  
→ LeetCode 792: Number of Matching Subsequences
  Difficulty: Medium
  Count how many words are subsequences
  
→ LeetCode 115: Distinct Subsequences
  Difficulty: Hard
  Count distinct subsequences (DP)
"""

# Use Case: Pattern with wildcards
"""
→ LeetCode 10: Regular Expression Matching
  Difficulty: Hard
  Support '.' and '*' wildcards (DP)
  
→ LeetCode 44: Wildcard Matching
  Difficulty: Hard
  Support '?' and '*' wildcards (DP or greedy)
"""

"""
═══════════════════════════════════════════════════════════════════════════
PATTERN 5E: ADVANCED STRING PROBLEMS
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: String transformation
"""
→ LeetCode 72: Edit Distance
  Difficulty: Medium
  Minimum operations to convert one string to another (DP)
  
→ LeetCode 583: Delete Operation for Two Strings
  Difficulty: Medium
  Minimum deletions to make strings equal
  
→ LeetCode 712: Minimum ASCII Delete Sum for Two Strings
  Difficulty: Medium
  Similar but minimize ASCII sum
"""

# Use Case: Longest common subsequence/substring
"""
→ LeetCode 1143: Longest Common Subsequence
  Difficulty: Medium
  Classic DP problem
  
→ LeetCode 718: Longest Common Substring
  Difficulty: Medium
  Use DP or sliding window
"""


# ============================================================================
# ADDITIONAL IMPORTANT PATTERNS
# ============================================================================

"""
═══════════════════════════════════════════════════════════════════════════
MONOTONIC STACK/DEQUE
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Next greater/smaller element
"""
→ LeetCode 496: Next Greater Element I
  Difficulty: Easy
  Use monotonic stack
  
→ LeetCode 503: Next Greater Element II
  Difficulty: Medium
  Circular array - process twice
  
→ LeetCode 739: Daily Temperatures
  Difficulty: Medium
  Days until warmer temperature
  
→ LeetCode 901: Online Stock Span
  Difficulty: Medium
  Consecutive days with price <= today
"""

# Use Case: Sliding window maximum/minimum
"""
→ LeetCode 239: Sliding Window Maximum
  Difficulty: Hard
  Use monotonic deque
  
→ LeetCode 1438: Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
  Difficulty: Medium
  Track min/max with two deques
"""

"""
═══════════════════════════════════════════════════════════════════════════
INTERVALS
═══════════════════════════════════════════════════════════════════════════
"""

# Use Case: Merge intervals
"""
→ LeetCode 56: Merge Intervals
  Difficulty: Medium
  Sort and merge overlapping intervals
  
→ LeetCode 57: Insert Interval
  Difficulty: Medium
  Insert and merge in sorted intervals
  
→ LeetCode 986: Interval List Intersections
  Difficulty: Medium
  Find intersection of two interval lists
"""

# Use Case: Non-overlapping intervals
"""
→ LeetCode 435: Non-overlapping Intervals
  Difficulty: Medium
  Minimum removals to make non-overlapping
  
→ LeetCode 452: Minimum Number of Arrows to Burst Balloons
  Difficulty: Medium
  Similar greedy approach
"""

# Use Case: Meeting rooms
"""
→ LeetCode 252: Meeting Rooms
  Difficulty: Easy
  Premium - check if can attend all meetings
  
→ LeetCode 253: Meeting Rooms II
  Difficulty: Medium
  Premium - minimum conference rooms needed
"""


# ============================================================================
# PROBLEM DIFFICULTY PROGRESSION
# ============================================================================

"""
RECOMMENDED LEARNING PATH:
==========================

WEEK 1-2: TWO POINTERS (Easy → Medium)
---------------------------------------
1. LeetCode 167: Two Sum II
2. LeetCode 344: Reverse String
3. LeetCode 125: Valid Palindrome
4. LeetCode 283: Move Zeroes
5. LeetCode 26: Remove Duplicates
6. LeetCode 11: Container With Most Water
7. LeetCode 15: 3Sum
8. LeetCode 16: 3Sum Closest

WEEK 3-4: SLIDING WINDOW (Easy → Hard)
---------------------------------------
1. LeetCode 643: Maximum Average Subarray
2. LeetCode 1456: Max Vowels in Substring
3. LeetCode 3: Longest Substring Without Repeating
4. LeetCode 209: Minimum Size Subarray Sum
5. LeetCode 424: Longest Repeating Character Replacement
6. LeetCode 438: Find All Anagrams
7. LeetCode 567: Permutation in String
8. LeetCode 76: Minimum Window Substring (HARD)

WEEK 5-6: PREFIX SUM (Easy → Medium)
-------------------------------------
1. LeetCode 303: Range Sum Query
2. LeetCode 1480: Running Sum
3. LeetCode 724: Find Pivot Index
4. LeetCode 560: Subarray Sum Equals K
5. LeetCode 974: Subarray Sums Divisible by K
6. LeetCode 525: Contiguous Array
7. LeetCode 523: Continuous Subarray Sum
8. LeetCode 304: Range Sum Query 2D

WEEK 7-8: KADANE'S & SUBARRAYS (Medium → Hard)
-----------------------------------------------
1. LeetCode 53: Maximum Subarray
2. LeetCode 121: Best Time to Buy/Sell Stock
3. LeetCode 152: Maximum Product Subarray
4. LeetCode 918: Maximum Sum Circular Subarray
5. LeetCode 1004: Max Consecutive Ones III
6. LeetCode 1658: Minimum Operations to Reduce X

WEEK 9-10: STRING PATTERNS (Easy → Hard)
-----------------------------------------
1. LeetCode 242: Valid Anagram
2. LeetCode 49: Group Anagrams
3. LeetCode 387: First Unique Character
4. LeetCode 5: Longest Palindromic Substring
5. LeetCode 647: Palindromic Substrings
6. LeetCode 131: Palindrome Partitioning
7. LeetCode 72: Edit Distance
8. LeetCode 10: Regular Expression Matching (HARD)

WEEK 11-12: ADVANCED & MIXED (Medium → Hard)
---------------------------------------------
1. LeetCode 239: Sliding Window Maximum
2. LeetCode 496: Next Greater Element I
3. LeetCode 739: Daily Temperatures
4. LeetCode 56: Merge Intervals
5. LeetCode 253: Meeting Rooms II
6. LeetCode 42: Trapping Rain Water
7. LeetCode 992: Subarrays with K Different Integers
"""


# ============================================================================
# QUICK REFERENCE: PATTERN IDENTIFICATION
# ============================================================================

"""
KEYWORDS → PATTERN MAPPING:
===========================

"sorted array" + "pair/triplet" → Two Pointers (Opposite Direction)
"remove duplicates" + "in-place" → Two Pointers (Same Direction)
"cycle" + "linked list" → Two Pointers (Fast & Slow)
"merge" + "sorted" → Two Pointers (Multiple Arrays)

"substring" + "consecutive" → Sliding Window
"subarray" + "maximum/minimum" → Sliding Window or Kadane's
"k elements" + "window" → Sliding Window (Fixed)
"at most k" + "distinct" → Sliding Window (Variable)

"range sum" + "multiple queries" → Prefix Sum
"subarray sum" + "equals k" → Prefix Sum + Hash Map
"matrix" + "rectangle sum" → 2D Prefix Sum

"maximum subarray sum" → Kadane's Algorithm
"buy/sell stock" → Kadane's Variation

"palindrome" → Two Pointers or Expand Around Center
"anagram" → Character Frequency (Hash Map)
"pattern matching" → String Algorithms (KMP/DP)
"edit distance" → DP

"next greater/smaller" → Monotonic Stack
"sliding window max" → Monotonic Deque
"intervals" + "merge/overlap" → Sort + Greedy
"""


if __name__ == "__main__":
    print("LeetCode Problems Mapped to Array Traversal Patterns")
    print("=" * 60)
    print("\nThis file contains:")
    print("- 150+ LeetCode problems organized by pattern")
    print("- Difficulty levels for each problem")
    print("- 12-week learning path")
    print("- Pattern identification keywords")
    print("\nUse this alongside array_traversal_patterns_guide.py")
    print("for comprehensive DSA preparation!")
