"""
SLIDING WINDOW - FIXED WINDOW SIZE
===================================
Complete solutions for LeetCode problems using fixed-size sliding window pattern

Pattern Template (While Loop):
-------------------------------
if len(array) < k:
    return None  # or appropriate default

# Step 1: Initialize first window
window_state = calculate_first_window(array[:k])
result = window_state  # or other initialization

left = 0
right = k

# Step 2: Slide the window
while right < len(array):
    # Add new element from right
    window_state += array[right]
    
    # Remove old element from left
    window_state -= array[left]
    
    # Update result
    result = update_result(window_state)
    
    # Move pointers
    left += 1
    right += 1

return result

Key Characteristics:
-------------------
1. Window size is FIXED and known beforehand
2. Slide by removing left element and adding right element
3. Each element visited exactly once → O(n)
4. Common in: substring matching, anagram detection, word concatenation

Time Complexity: O(n) where n = length of input
Space Complexity: O(k) where k = window size or alphabet size
"""

# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 1: LeetCode 438 - Find All Anagrams in a String
# ============================================================================

"""
Problem:
--------
Given two strings s and p, return an array of all the start indices of 
p's anagrams in s.

An Anagram is a word formed by rearranging the letters of a different word.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation: 
The substring "cba" at index 0 is an anagram of "abc"
The substring "bac" at index 6 is an anagram of "abc"

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]

Constraints:
- 1 <= s.length, p.length <= 3 * 10^4
- s and p consist of lowercase English letters
"""

def findAnagrams(s, p):
    """
    Approach: Fixed sliding window with frequency map
    
    Key Insight:
    - An anagram has the SAME character frequencies as the original
    - Use a FIXED window of size len(p) and slide it across s
    - Compare character frequencies in the window with p's frequencies
    - Use two hashmaps: one for p (target), one for current window
    - Use a counter to track how many unique characters are satisfied
    - When all characters are satisfied, we found an anagram!
    - Record the starting index of each valid window
    - The key is: maintain FIXED window size = len(p), check if frequencies match
    
    Time: O(|s|)
    Space: O(1) - at most 26 letters
    """
    if len(s) < len(p):
        return []
    
    k = len(p)
    
    # Count frequencies in p (target)
    target_hashmap = {}
    for char in p:
        target_hashmap[char] = target_hashmap.get(char, 0) + 1
    
    # Initialize first window
    source_hashmap = {}
    for char in s[:k]:
        source_hashmap[char] = source_hashmap.get(char, 0) + 1
    
    result = []
    required = len(target_hashmap)
    
    # Check if first window is an anagram
    formed = sum(1 for char in target_hashmap if source_hashmap.get(char, 0) == target_hashmap[char])
    if formed == required:
        result.append(0)
    
    left = 0
    right = k
    
    # Slide the window
    while right < len(s):
        # Add new character from right
        source_hashmap[s[right]] = source_hashmap.get(s[right], 0) + 1
        
        # Check if right character now matches target frequency
        if s[right] in target_hashmap and source_hashmap[s[right]] == target_hashmap[s[right]]:
            formed += 1
        elif s[right] in target_hashmap and source_hashmap[s[right]] == target_hashmap[s[right]] + 1:
            formed -= 1
        
        # Remove character from left
        if s[left] in target_hashmap and source_hashmap[s[left]] == target_hashmap[s[left]]:
            formed -= 1
        elif s[left] in target_hashmap and source_hashmap[s[left]] == target_hashmap[s[left]] + 1:
            formed += 1
        
        source_hashmap[s[left]] -= 1
        if source_hashmap[s[left]] == 0:
            del source_hashmap[s[left]]
        
        # Check if current window is an anagram
        if formed == required:
            result.append(left + 1)
        
        left += 1
        right += 1
    
    return result


# Test cases
print("=" * 70)
print("Problem 1: LeetCode 438 - Find All Anagrams in a String")
print("=" * 70)
test_cases_438 = [
    ("cbaebabacd", "abc"),
    ("abab", "ab"),
    ("baa", "aa"),
    ("aaaaaaaaaa", "aaaaaaaaaaaaa")
]

for s, p in test_cases_438:
    result = findAnagrams(s, p)
    print(f"s: '{s}', p: '{p}'")
    print(f"Result: {result}\n")


# HIGHEST FREQUENCY (Must Know for Interviews)
# ============================================================================
# PROBLEM 2: LeetCode 567 - Permutation in String
# ============================================================================

"""
Problem:
--------
Given two strings s1 and s2, return true if s2 contains a permutation 
of s1, or false otherwise.

A permutation is a rearrangement of all the characters of a string.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains "ba" which is a permutation of "ab"

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
- 1 <= s1.length, s2.length <= 10^4
- s1 and s2 consist of lowercase English letters
"""

def checkInclusion(s1, s2):
    """
    Approach: Fixed sliding window with frequency map
    
    Key Insight:
    - A permutation has the SAME character frequencies as the original
    - This is similar to "Find All Anagrams" but we only need to find ONE
    - Use a FIXED window of size len(s1) and slide it across s2
    - Compare character frequencies in the window with s1's frequencies
    - As soon as we find a match, return True
    - If we finish scanning s2 without finding a match, return False
    - The key is: maintain FIXED window size = len(s1), check if frequencies match
    
    Time: O(|s2|)
    Space: O(1) - at most 26 letters
    """
    if len(s2) < len(s1):
        return False
    
    k = len(s1)
    
    # Count frequencies in s1 (target)
    s1_count = {}
    for char in s1:
        s1_count[char] = s1_count.get(char, 0) + 1
    
    # Initialize first window
    source_hashmap = {}
    for char in s2[:k]:
        source_hashmap[char] = source_hashmap.get(char, 0) + 1
    
    required = len(s1_count)
    
    # Check if first window is a permutation
    formed = sum(1 for char in s1_count if source_hashmap.get(char, 0) == s1_count[char])
    if formed == required:
        return True
    
    left = 0
    right = k
    
    # Slide the window
    while right < len(s2):
        # Add new character from right
        source_hashmap[s2[right]] = source_hashmap.get(s2[right], 0) + 1
        
        # Check if right character now matches target frequency
        if s2[right] in s1_count and source_hashmap[s2[right]] == s1_count[s2[right]]:
            formed += 1
        elif s2[right] in s1_count and source_hashmap[s2[right]] == s1_count[s2[right]] + 1:
            formed -= 1
        
        # Remove character from left
        if s2[left] in s1_count and source_hashmap[s2[left]] == s1_count[s2[left]]:
            formed -= 1
        elif s2[left] in s1_count and source_hashmap[s2[left]] == s1_count[s2[left]] + 1:
            formed += 1
        
        source_hashmap[s2[left]] -= 1
        if source_hashmap[s2[left]] == 0:
            del source_hashmap[s2[left]]
        
        # Check if current window is a permutation
        if formed == required:
            return True
        
        left += 1
        right += 1
    
    return False


# Test cases
print("=" * 70)
print("Problem 2: LeetCode 567 - Permutation in String")
print("=" * 70)
test_cases_567 = [
    ("ab", "eidbaooo"),
    ("ab", "eidboaoo"),
    ("adc", "dcda"),
    ("hello", "ooolleoooleh")
]

for s1, s2 in test_cases_567:
    result = checkInclusion(s1, s2)
    print(f"s1: '{s1}', s2: '{s2}'")
    print(f"Result: {result}\n")


# HIGHEST FREQUENCY (Must Know for Interviews) - FAANG HARD PROBLEMS
# ============================================================================
# PROBLEM 3: LeetCode 30 - Substring with Concatenation of All Words
# ============================================================================

"""
Problem:
--------
You are given a string s and an array of strings words. All the strings 
of words are of the same length.

A concatenated substring in s is a substring that contains all the 
strings of any permutation of words concatenated.

Return the starting indices of all the concatenated substrings in s.

Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: 
Substrings starting at index 0 is "barfoo" (permutation of ["bar","foo"])
Substrings starting at index 9 is "foobar" (permutation of ["foo","bar"])

Example 2:
Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:
Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]

Constraints:
- 1 <= s.length <= 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 30
- s and words[i] consist of lowercase English letters
"""

def findSubstring(s, target):
    """
    Approach: Fixed sliding window with word-level frequency matching
    
    Key Insight:
    - This is like "Find All Anagrams" but with WORDS instead of characters
    - Each word has the same length, so we can treat them as units
    - We need to find all substrings that contain ALL words (in any order)
    - Use a hashmap to track required word frequencies
    - Use another hashmap to track current window word frequencies
    - Window size is FIXED: len(words) * word_length
    - Slide the window word by word (not character by character)
    - For efficiency, we try starting from each position in [0, word_length)
    - The key is: treat words as atomic units, match their frequencies with FIXED window
    
    Time: O(n * word_length) where n = len(s)
    Space: O(m) where m = number of unique words
    """
    if not s or not target:
        return []
    
    word_len = len(target[0])
    word_count = len(target)
    total_len = word_len * word_count
    
    if len(s) < total_len:
        return []
    
    # Build word frequency map
    target_hmap = {}
    for word in target:
        target_hmap[word] = target_hmap.get(word, 0) + 1
    
    result = []
    
    # Try starting from each position in [0, word_len)
    for i in range(word_len):
        left = i
        right = i
        source_hmap = {}
        count = 0  # Number of target matched
        
        # Slide window word by word
        while right + word_len <= len(s):
            # Get the word at right pointer
            word = s[right:right + word_len]
            right += word_len
            
            if word in target_hmap:
                source_hmap[word] = source_hmap.get(word, 0) + 1
                count += 1
                
                # If we have too many of this word, shrink from left
                while source_hmap[word] > target_hmap[word]:
                    left_word = s[left:left + word_len]
                    source_hmap[left_word] -= 1
                    count -= 1
                    left += word_len
                
                # If we matched all target, record the starting index
                if count == word_count:
                    result.append(left)
                    # Shrink window by one word to continue searching
                    left_word = s[left:left + word_len]
                    source_hmap[left_word] -= 1
                    count -= 1
                    left += word_len
            else:
                # Word not in target list, reset window
                source_hmap.clear()
                count = 0
                left = right
    
    return result


# Test cases
print("=" * 70)
print("Problem 3: LeetCode 30 - Substring with Concatenation of All Words (HARD)")
print("=" * 70)
test_cases_30 = [
    ("barfoothefoobarman", ["foo", "bar"]),
    ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]),
    ("barfoofoobarthefoobarman", ["bar", "foo", "the"]),
    ("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"])
]

for s, words in test_cases_30:
    result = findSubstring(s, words)
    print(f"s: '{s}'")
    print(f"words: {words}")
    print(f"Result: {result}\n")


# ============================================================================
# SUMMARY & PATTERN RECOGNITION
# ============================================================================

"""
FIXED WINDOW SIZE - PATTERN RECOGNITION:
=========================================

When to Use Fixed Window:
--------------------------
✓ Window size is known beforehand (e.g., len(pattern))
✓ "Find all occurrences of pattern"
✓ "Check if permutation/anagram exists"
✓ "Substring matching with fixed length"

Key Characteristics:
-------------------
1. Window size is CONSTANT throughout
2. Slide by: remove left, add right
3. Each element visited exactly once → O(n)
4. Simpler than variable window (no while loop for contraction)

Template Structure:
------------------
window_size = k
state = initialize()

for right in range(len(array)):
    # Add right element
    add array[right] to state
    
    # If window exceeds size, remove left
    if right >= window_size:
        remove array[right - window_size] from state
    
    # Check if window is valid
    if right >= window_size - 1:
        if window_is_valid(state):
            record_result()

Common Use Cases:
-----------------
1. Anagram Detection: LC 438, 567
2. Word Concatenation: LC 30
3. Fixed-size subarray problems

Difference from Variable Window:
--------------------------------
FIXED:
- Window size = constant
- Slide by removing left, adding right
- No while loop for contraction
- Simpler logic

VARIABLE:
- Window size = changes dynamically
- Expand right, contract left when invalid
- While loop for contraction
- More complex logic

Problem Categories:
------------------
1. Character Anagrams: LC 438, 567
2. Word Concatenations: LC 30

Time Complexity: O(n) for all
Space Complexity: O(k) where k = alphabet size or number of unique words
"""

# ============================================================================
# BEGINNER PROBLEMS - Start Here!
# ============================================================================

# ============================================================================
# PROBLEM 4: LeetCode 643 - Maximum Average Subarray I (EASY)
# ============================================================================

"""
Problem:
--------
You are given an integer array nums consisting of n elements, and an 
integer k.

Find a contiguous subarray whose length is equal to k that has the 
maximum average value and return this value.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
- n == nums.length
- 1 <= k <= n <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

def findMaxAverage(nums, k):
    """
    Approach: Fixed sliding window with sum tracking
    
    Key Insight:
    - This is the SIMPLEST fixed window problem - perfect for beginners!
    - We need to find the maximum sum of any k consecutive elements
    - Then divide by k to get the average
    - Use a fixed window of size k and slide it across the array
    - Track the current sum by adding right element and removing left element
    - Keep track of the maximum sum seen
    - The key is: maintain FIXED window size = k, track sum efficiently
    
    Time: O(n)
    Space: O(1)
    """
    if len(nums) < k:
        return None
    
    # Initialize first window
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    left = 0
    right = k
    
    # Slide the window
    while right < len(nums):
        window_sum += nums[right]
        window_sum -= nums[left]
        max_sum = max(max_sum, window_sum)
        left += 1
        right += 1
    
    return max_sum / k


# Test cases
print("=" * 70)
print("Problem 4: LeetCode 643 - Maximum Average Subarray I (EASY)")
print("=" * 70)
test_cases_643 = [
    ([1, 12, -5, -6, 50, 3], 4),
    ([5], 1),
    ([0, 4, 0, 3, 2], 1),
    ([4, 0, 4, 3, 3], 5)
]

for nums, k in test_cases_643:
    result = findMaxAverage(nums, k)
    print(f"nums: {nums}, k: {k}")
    print(f"Result: {result:.5f}\n")


# ============================================================================
# PROBLEM 5: LeetCode 1456 - Maximum Number of Vowels in a Substring (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a string s and an integer k, return the maximum number of vowel 
letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:
Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.

Example 2:
Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.

Example 3:
Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters
- 1 <= k <= s.length
"""

def maxVowels(s, k):
    """
    Approach: Fixed sliding window with vowel counting
    
    Key Insight:
    - We need to find the maximum count of vowels in any k consecutive characters
    - Use a fixed window of size k and slide it across the string
    - Track the current vowel count by adding/removing characters
    - Keep track of the maximum vowel count seen
    - The key is: maintain FIXED window size = k, count vowels efficiently
    
    Time: O(n)
    Space: O(1)
    """
    if len(s) < k:
        return 0
    
    vowels = set('aeiou')
    
    # Initialize first window
    vowel_count = sum(1 for char in s[:k] if char in vowels)
    max_vowels = vowel_count
    
    left = 0
    right = k
    
    # Slide the window
    while right < len(s):
        # Add new character
        if s[right] in vowels:
            vowel_count += 1
        # Remove leftmost character
        if s[left] in vowels:
            vowel_count -= 1
        
        max_vowels = max(max_vowels, vowel_count)
        left += 1
        right += 1
    
    return max_vowels


# Test cases
print("=" * 70)
print("Problem 5: LeetCode 1456 - Maximum Number of Vowels (MEDIUM)")
print("=" * 70)
test_cases_1456 = [
    ("abciiidef", 3),
    ("aeiou", 2),
    ("leetcode", 3),
    ("rhythms", 4)
]

for s, k in test_cases_1456:
    result = maxVowels(s, k)
    print(f"s: '{s}', k: {k}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 6: LeetCode 1343 - Number of Sub-arrays of Size K and Average >= Threshold (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given an array of integers arr and two integers k and threshold, return 
the number of sub-arrays of size k and average greater than or equal to 
threshold.

Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6.

Example 2:
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^4
- 1 <= k <= arr.length
- 0 <= threshold <= 10^4
"""

def numOfSubarrays(arr, k, threshold):
    """
    Approach: Fixed sliding window with sum tracking and counting
    
    Key Insight:
    - Similar to LC 643 but we COUNT how many windows meet the threshold
    - Use a fixed window of size k and slide it across the array
    - Track the current sum by adding/removing elements
    - Check if average (sum / k) >= threshold, which is same as sum >= threshold * k
    - Count how many windows satisfy the condition
    - The key is: maintain FIXED window size = k, count valid windows
    
    Time: O(n)
    Space: O(1)
    """
    if len(arr) < k:
        return 0
    
    target_sum = threshold * k
    
    # Initialize first window
    window_sum = sum(arr[:k])
    count = 1 if window_sum >= target_sum else 0
    
    left = 0
    right = k
    
    # Slide the window
    while right < len(arr):
        window_sum += arr[right]
        window_sum -= arr[left]
        
        if window_sum >= target_sum:
            count += 1
        
        left += 1
        right += 1
    
    return count


# Test cases
print("=" * 70)
print("Problem 6: LeetCode 1343 - Sub-arrays with Average >= Threshold (MEDIUM)")
print("=" * 70)
test_cases_1343 = [
    ([2, 2, 2, 2, 5, 5, 5, 8], 3, 4),
    ([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5),
    ([1, 1, 1, 1, 1], 1, 0)
]

for arr, k, threshold in test_cases_1343:
    result = numOfSubarrays(arr, k, threshold)
    print(f"arr: {arr}, k: {k}, threshold: {threshold}")
    print(f"Result: {result}\n")

# ============================================================================



# ============================================================================
# HIGH-FREQUENCY PROBLEMS
# ============================================================================

# HIGHEST FREQUENCY (Must Know for Interviews) - FAANG FAVORITE
# ============================================================================
# PROBLEM 7: LeetCode 239 - Sliding Window Maximum (HARD)
# ============================================================================

"""
Problem:
--------
You are given an array of integers nums, there is a sliding window of 
size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding 
window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

from collections import deque

def maxSlidingWindow(nums, k):
    """
    Approach: Fixed sliding window with monotonic deque
    
    Key Insight:
    - We need to find the MAXIMUM in each window of size k
    - Naive approach: recalculate max for each window → O(n*k)
    - Optimized: use a MONOTONIC DECREASING DEQUE
    - Deque stores INDICES (not values) in decreasing order of their values
    - Front of deque always has index of maximum element in current window
    - When sliding: remove indices outside window, remove smaller elements from back
    - The key is: maintain deque with potential maximums, discard useless elements
    
    Time: O(n) - each element added and removed at most once
    Space: O(k) - deque size at most k
    """
    if not nums or k == 0:
        return []
    if len(nums) < k:
        return []
    
    dq = deque()  # Stores indices
    result = []
    
    # Initialize first window
    for i in range(k):
        # Remove smaller elements from back
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
    
    # First window's maximum
    result.append(nums[dq[0]])
    
    left = 0
    right = k
    
    # Slide the window
    while right < len(nums):
        # Remove indices outside the window from front
        while dq and dq[0] <= left:
            dq.popleft()
        
        # Remove indices of smaller elements from back
        while dq and nums[dq[-1]] < nums[right]:
            dq.pop()
        
        # Add current index
        dq.append(right)
        
        # Record maximum for this window
        result.append(nums[dq[0]])
        
        left += 1
        right += 1
    
    return result


# Test cases
print("=" * 70)
print("Problem 7: LeetCode 239 - Sliding Window Maximum (HARD)")
print("=" * 70)
test_cases_239 = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3),
    ([1], 1),
    ([1, -1], 1),
    ([9, 11], 2),
    ([4, -2], 2)
]

for nums, k in test_cases_239:
    result = maxSlidingWindow(nums, k)
    print(f"nums: {nums}, k: {k}")
    print(f"Result: {result}\n")


# ============================================================================
# ALTERNATIVE APPROACH: Using Priority Queue (Heap) - SLOWER!
# ============================================================================

"""
COMPARISON: Deque vs Priority Queue for Sliding Window Maximum

This section shows an ALTERNATIVE implementation using a priority queue (heap).
While it works correctly, it's SLOWER than the deque approach.

Time Complexity Comparison:
- Deque (Monotonic): O(n) ✅ OPTIMAL
- Priority Queue: O(n log k) ⚠️ SLOWER

Why is heap slower?
- Heap operations (push/pop) are O(log k)
- Need "lazy deletion" (can't efficiently remove arbitrary elements)
- Heap can grow larger than k elements

When to use heap vs deque:
- Use DEQUE for sliding window max/min (optimal)
- Use HEAP for top K problems (not sliding window)
"""

import heapq

def maxSlidingWindow_heap(nums, k):
    """
    Alternative Approach: Priority Queue (Max-Heap) with Lazy Deletion
    
    Key Insight:
    - Use a max-heap to track potential maximums
    - Store (-value, index) tuples (negate for max-heap)
    - Use "lazy deletion": keep invalid indices in heap, skip when encountered
    - When we need the max, check if top element is still in window
    - If not, remove it and check next element
    
    Pros:
    - Simpler logic (no need to maintain monotonic property)
    - Works for finding max in any range
    
    Cons:
    - Slower: O(n log k) vs O(n) for deque
    - Heap can grow larger than k (lazy deletion)
    - More memory overhead
    
    Time: O(n log k) - each push/pop is O(log k)
    Space: O(k) - heap size can be up to k (or more with lazy deletion)
    """
    if not nums or k == 0:
        return []
    if len(nums) < k:
        return []
    
    heap = []  # Max-heap: store (-value, index)
    result = []
    
    # Initialize first window
    for i in range(k):
        heapq.heappush(heap, (-nums[i], i))  # O(log k)
    
    # Get max for first window (with lazy deletion)
    while heap and heap[0][1] < 0:  # Index outside window
        heapq.heappop(heap)
    result.append(-heap[0][0])  # Negate to get original value
    
    left = 0
    right = k
    
    # Slide the window
    while right < len(nums):
        # Add new element to heap
        heapq.heappush(heap, (-nums[right], right))  # O(log k)
        
        # Lazy deletion: remove elements outside current window
        # Only remove from top when we need the max
        while heap and heap[0][1] <= left:
            heapq.heappop(heap)  # O(log k)
        
        # Get maximum for this window
        result.append(-heap[0][0])
        
        left += 1
        right += 1
    
    return result


# Test cases - Compare both approaches
print("=" * 70)
print("COMPARISON: Deque vs Priority Queue (Heap)")
print("=" * 70)
print("\nTesting both implementations on the same test cases:\n")

test_cases_comparison = [
    ([1, 3, -1, -3, 5, 3, 6, 7], 3),
    ([1], 1),
    ([1, -1], 1),
    ([9, 11], 2),
]

for nums, k in test_cases_comparison:
    result_deque = maxSlidingWindow(nums, k)
    result_heap = maxSlidingWindow_heap(nums, k)
    
    match = "✅ MATCH" if result_deque == result_heap else "❌ MISMATCH"
    
    print(f"nums: {nums}, k: {k}")
    print(f"Deque result:  {result_deque}")
    print(f"Heap result:   {result_heap}")
    print(f"Status: {match}\n")

print("=" * 70)
print("CONCLUSION:")
print("=" * 70)
print("Both approaches produce the same results!")
print("However, DEQUE is FASTER: O(n) vs O(n log k)")
print("Use DEQUE for sliding window maximum problems!")
print("Use HEAP for top K problems (not sliding window)")
print("=" * 70)
print()


# ============================================================================
# CONTAINS DUPLICATE SERIES - Building Up Complexity
# ============================================================================

"""
This section covers the "Contains Duplicate" series of problems.
They progressively increase in difficulty and introduce different concepts:

1. LC 217 - Contains Duplicate I (EASY)
   - Check if ANY duplicate exists
   - Use: Hash Set
   - Time: O(n), Space: O(n)

2. LC 219 - Contains Duplicate II (EASY)
   - Check if duplicate exists within distance k
   - Use: Fixed Sliding Window + Hash Set
   - Time: O(n), Space: O(k)

3. LC 220 - Contains Duplicate III (HARD)
   - Check if near-duplicate exists (value difference <= valueDiff)
   - Use: Fixed Sliding Window + Set/Bucket
   - Time: O(n*k), Space: O(k)
"""


# ============================================================================
# PROBLEM 9A: LeetCode 217 - Contains Duplicate I (EASY)
# ============================================================================

"""
Problem:
--------
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def containsDuplicate(nums):
    """
    Approach: Hash Set
    
    Key Insight:
    - Simply check if we've seen each number before
    - Use a set to track seen numbers
    - If we encounter a number already in set, we found a duplicate
    - This is NOT a sliding window problem - just hash set usage
    
    Time: O(n)
    Space: O(n)
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False


# Test cases
print("=" * 70)
print("Problem 9A: LeetCode 217 - Contains Duplicate I (EASY)")
print("=" * 70)
test_cases_217 = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
]

for nums in test_cases_217:
    result = containsDuplicate(nums)
    print(f"nums: {nums}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 9B: LeetCode 219 - Contains Duplicate II (EASY)
# ============================================================================

"""
Problem:
--------
Given an integer array nums and an integer k, return true if there are 
two distinct indices i and j in the array such that nums[i] == nums[j] 
and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Explanation: nums[0] = nums[3] = 1, and 0 - 3 = 3 <= k

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Explanation: nums[2] = nums[3] = 1, and 3 - 2 = 1 <= k

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
Explanation: No duplicates within distance 2

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5
"""

def containsNearbyDuplicate(nums, k):
    """
    Approach: Fixed sliding window with hash set
    
    Key Insight:
    - We need to check if duplicate exists within a window of size k
    - Use a fixed window of size k and maintain a set of elements in window
    - For each new element, check if it's already in the window set
    - If yes, we found a duplicate within distance k
    - Slide the window by removing leftmost element and adding new element
    - The key is: maintain FIXED window size = k, check for duplicates in set
    
    Time: O(n)
    Space: O(min(n, k))
    """
    if k == 0:
        return False
    
    window = set()
    
    for i in range(len(nums)):
        # Check if current element is in window
        if nums[i] in window:
            return True
        
        # Add current element to window
        window.add(nums[i])
        
        # Maintain window size of k
        if len(window) > k:
            window.remove(nums[i - k])
    
    return False


# Test cases
print("=" * 70)
print("Problem 9B: LeetCode 219 - Contains Duplicate II (EASY)")
print("=" * 70)
test_cases_219 = [
    ([1, 2, 3, 1], 3),
    ([1, 0, 1, 1], 1),
    ([1, 2, 3, 1, 2, 3], 2),
    ([99, 99], 2)
]

for nums, k in test_cases_219:
    result = containsNearbyDuplicate(nums, k)
    print(f"nums: {nums}, k: {k}")
    print(f"Result: {result}\n")


# ============================================================================
# PROBLEM 9C: LeetCode 220 - Contains Duplicate III (HARD)
# ============================================================================

"""
Problem:
--------
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:
- i != j,
- abs(i - j) <= indexDiff  (indices are close)
- abs(nums[i] - nums[j]) <= valueDiff  (values are close)

Return true if such pair exists or false otherwise.

Example 1:
Input: nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output: true
Explanation: i = 0 and j = 3, abs(0 - 3) = 3, abs(1 - 1) = 0
             Indices 0 and 3 are within distance 3, and values are identical (diff = 0)

Example 2:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output: false
Explanation: No two elements within distance 2 have value difference <= 3

Example 3:
Input: nums = [1,3,1], indexDiff = 1, valueDiff = 1
Output: false
Explanation: 
  - indices 0,1: distance = 1 ✅, value diff = |1-3| = 2 ❌ (> 1)
  - indices 1,2: distance = 1 ✅, value diff = |3-1| = 2 ❌ (> 1)
  - indices 0,2: distance = 2 ❌ (> indexDiff=1)

Example 4:
Input: nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 4
Output: true
Explanation: i = 0 and j = 1, abs(0 - 1) = 1 <= 2, abs(1 - 5) = 4 <= 4

Example 5:
Input: nums = [2,4], indexDiff = 1, valueDiff = 1
Output: false
Explanation: Only pair (0,1): distance = 1 ✅, value diff = |2-4| = 2 ❌ (> 1)

Constraints:
- 2 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 1 <= indexDiff <= nums.length
- 0 <= valueDiff <= 10^9

DETAILED WALKTHROUGH:
---------------------

Example: nums = [1, 5, 9, 1, 5, 9], indexDiff = 2, valueDiff = 3

Step-by-step with window of size indexDiff = 2:

i=0, num=1:
  Window: [1]
  Check: No previous elements
  Result: Continue

i=1, num=5:
  Window: [1, 5]
  Check: Is there any num in window where |5 - num| <= 3?
    - |5 - 1| = 4 > 3 ❌
  Result: Continue

i=2, num=9:
  Window: [1, 5, 9]  (size > indexDiff, so remove oldest)
  Window after removal: [5, 9]
  Check: Is there any num in window where |9 - num| <= 3?
    - |9 - 5| = 4 > 3 ❌
  Result: Continue

i=3, num=1:
  Window: [5, 9, 1]  (size > indexDiff, so remove oldest)
  Window after removal: [9, 1]
  Check: Is there any num in window where |1 - num| <= 3?
    - |1 - 9| = 8 > 3 ❌
  Result: Continue

i=4, num=5:
  Window: [9, 1, 5]  (size > indexDiff, so remove oldest)
  Window after removal: [1, 5]
  Check: Is there any num in window where |5 - num| <= 3?
    - |5 - 1| = 4 > 3 ❌
  Result: Continue

i=5, num=9:
  Window: [1, 5, 9]  (size > indexDiff, so remove oldest)
  Window after removal: [5, 9]
  Check: Is there any num in window where |9 - num| <= 3?
    - |9 - 5| = 4 > 3 ❌
  Result: Continue

Final: No pair found → return False


Example: nums = [1, 2, 3, 1], indexDiff = 3, valueDiff = 0

i=0, num=1:
  Window: [1]
  Check: No previous elements
  Result: Continue

i=1, num=2:
  Window: [1, 2]
  Check: Is there any num in window where |2 - num| <= 0?
    - |2 - 1| = 1 > 0 ❌
  Result: Continue

i=2, num=3:
  Window: [1, 2, 3]
  Check: Is there any num in window where |3 - num| <= 0?
    - |3 - 1| = 2 > 0 ❌
    - |3 - 2| = 1 > 0 ❌
  Result: Continue

i=3, num=1:
  Window: [1, 2, 3, 1]  (size = indexDiff + 1)
  Check: Is there any num in window where |1 - num| <= 0?
    - |1 - 1| = 0 <= 0 ✅ FOUND!
  Result: return True

Final: Pair found at indices (0, 3) → return True
"""

def containsNearbyAlmostDuplicate(arr, indexDiff, valueDiff):
    """
    Approach: Fixed sliding window with bucket/set approach
    
    Key Insight:
    - We need to check if there exist two numbers within indexDiff distance
      that have at most valueDiff difference in value
    - Use a fixed window of size indexDiff
    - For each position, check if there's a number in the window within valueDiff range
    - Use a set to store numbers in current window
    - For each new number, check if any number in [num - valueDiff, num + valueDiff] exists
    - The key is: maintain FIXED window size = indexDiff, check value range
    
    Time: O(n * indexDiff) in worst case, O(n) average with optimizations
    Space: O(min(n, indexDiff))
    """
    if indexDiff < 1 or valueDiff < 0:
        return False
    if len(arr) < 2:
        return False
    
    hset = set()
    i = 0
    
    # Initialize first window (size = min(indexDiff, len(arr)-1))
    while i < min(indexDiff, len(arr)):
        # Check if any element in hset is within valueDiff range
        for num in hset:
            if abs(arr[i] - num) <= valueDiff:
                return True
        
        hset.add(arr[i])
        i += 1
    
    left = 0
    right = min(indexDiff, len(arr))
    
    # Slide the window
    while right < len(arr):
        # Check if any element in hset is within valueDiff range
        for num in hset:
            if abs(arr[right] - num) <= valueDiff:
                return True
        
        # Add new element
        hset.add(arr[right])
        
        # Remove leftmost element
        hset.remove(arr[left])
        
        left += 1
        right += 1
    
    return False


# Test cases with detailed explanations
print("=" * 70)
print("Problem 9C: LeetCode 220 - Contains Duplicate III (HARD)")
print("=" * 70)
print("\nDetailed Test Cases:\n")

test_cases_220_detailed = [
    {
        'nums': [1, 2, 3, 1],
        'indexDiff': 3,
        'valueDiff': 0,
        'expected': True,
        'explanation': 'Exact duplicate: indices (0,3) have same value 1, distance=3'
    },
    {
        'nums': [1, 5, 9, 1, 5, 9],
        'indexDiff': 2,
        'valueDiff': 3,
        'expected': False,
        'explanation': 'All pairs within distance 2 have value diff > 3'
    },
    {
        'nums': [1, 3, 1],
        'indexDiff': 1,
        'valueDiff': 1,
        'expected': False,
        'explanation': 'Pairs (0,1) and (1,2) both have value diff = 2 > valueDiff=1'
    },
    {
        'nums': [1, 5, 9, 1, 5, 9],
        'indexDiff': 2,
        'valueDiff': 4,
        'expected': True,
        'explanation': 'Pair (0,1): distance=1, value diff=|1-5|=4 <= valueDiff=4'
    },
    {
        'nums': [2, 4],
        'indexDiff': 1,
        'valueDiff': 1,
        'expected': False,
        'explanation': 'Only pair (0,1): value diff=|2-4|=2 > valueDiff=1'
    },
    {
        'nums': [1, 2, 1, 1],
        'indexDiff': 1,
        'valueDiff': 0,
        'expected': True,
        'explanation': 'Exact duplicate: indices (2,3) have same value 1, distance=1'
    },
    {
        'nums': [2, 2],
        'indexDiff': 3,
        'valueDiff': 0,
        'expected': True,
        'explanation': 'Exact duplicate: indices (0,1) have same value 2, distance=1'
    },
    {
        'nums': [1, 0, 1, 1],
        'indexDiff': 1,
        'valueDiff': 2,
        'expected': True,
        'explanation': 'Pair (0,1): distance=1, value diff=|1-0|=1 <= valueDiff=2'
    },
    {
        'nums': [7, 1, 3],
        'indexDiff': 2,
        'valueDiff': 3,
        'expected': True,
        'explanation': 'Pair (1,2): distance=1, value diff=|1-3|=2 <= valueDiff=3'
    },
    {
        'nums': [10, 100, 11, 9],
        'indexDiff': 1,
        'valueDiff': 2,
        'expected': True,
        'explanation': 'Pair (2,3): distance=1, value diff=|11-9|=2 <= valueDiff=2'
    }
]

for i, test in enumerate(test_cases_220_detailed, 1):
    nums = test['nums']
    indexDiff = test['indexDiff']
    valueDiff = test['valueDiff']
    expected = test['expected']
    explanation = test['explanation']
    
    result = containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    
    print(f"Test {i}:")
    print(f"  Input: nums={nums}, indexDiff={indexDiff}, valueDiff={valueDiff}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Status: {status}")
    print(f"  Explanation: {explanation}")
    print()

print("=" * 70)
print("VISUAL EXAMPLES:")
print("=" * 70)
# print("""
# Example 1: nums = [1, 2, 3, 1], indexDiff = 3, valueDiff = 0
#            Index:  0  1  2  3
# 
# Window progression:
#   i=0: [1]           → No match yet
#   i=1: [1, 2]        → |2-1|=1 > 0 ❌
#   i=2: [1, 2, 3]     → |3-1|=2 > 0 ❌, |3-2|=1 > 0 ❌
#   i=3: [1, 2, 3, 1]  → |1-1|=0 <= 0 ✅ FOUND!
#   
# Result: TRUE (found exact duplicate within distance 3)
# 
# ---
# 
# Example 2: nums = [1, 5, 9, 1, 5, 9], indexDiff = 2, valueDiff = 3
#            Index:  0  1  2  3  4  5
# 
# Window progression (size = indexDiff = 2):
#   i=0: [1]           → No match yet
#   i=1: [1, 5]        → |5-1|=4 > 3 ❌
#   i=2: [5, 9]        → |9-5|=4 > 3 ❌  (removed 1)
#   i=3: [9, 1]        → |1-9|=8 > 3 ❌  (removed 5)
#   i=4: [1, 5]        → |5-1|=4 > 3 ❌  (removed 9)
#   i=5: [5, 9]        → |9-5|=4 > 3 ❌  (removed 1)
#   
# Result: FALSE (no pair within distance 2 has value diff <= 3)
# 
# ---
# 
# Example 3: nums = [1, 5, 9, 1, 5, 9], indexDiff = 2, valueDiff = 4
#            Index:  0  1  2  3  4  5
# 
# Window progression (size = indexDiff = 2):
#   i=0: [1]           → No match yet
#   i=1: [1, 5]        → |5-1|=4 <= 4 ✅ FOUND!
#   
# Result: TRUE (pair at indices 0,1 satisfies both conditions)

# ---

# KEY INSIGHTS:
# 1. indexDiff controls WINDOW SIZE (how far apart indices can be)
# 2. valueDiff controls VALUE RANGE (how different values can be)
# 3. Both conditions must be satisfied simultaneously
# 4. Window slides to maintain indexDiff constraint
# 5. For each new element, check ALL elements in current window
# """)


print("=" * 70)
print("FIXED WINDOW SIZE PATTERN - COMPLETE!")
print("=" * 70)
print("\n🎯 FAANG-READY FIXED SLIDING WINDOW COLLECTION (9 Problems)")
print("\nProblems Covered:")
print("\n📚 BEGINNER LEVEL (Start Here!):")
print("4. LC 643  - Maximum Average Subarray I (EASY) ⭐⭐⭐")
print("5. LC 1456 - Maximum Number of Vowels (MEDIUM) ⭐⭐⭐")
print("6. LC 1343 - Sub-arrays with Average >= Threshold (MEDIUM) ⭐⭐")
print("\n🔥 CORE PROBLEMS (Must Know!):")
print("1. LC 438  - Find All Anagrams in a String ⭐⭐⭐⭐⭐")
print("2. LC 567  - Permutation in String ⭐⭐⭐⭐")
print("\n💎 ADVANCED PROBLEMS (FAANG Favorites!):")
print("3. LC 30   - Substring with Concatenation of All Words (HARD) ⭐⭐⭐⭐")
print("7. LC 239  - Sliding Window Maximum (HARD) ⭐⭐⭐⭐⭐")
print("9. LC 220  - Contains Duplicate III (HARD) ⭐⭐⭐")
print("\n⚠️  COMPARISON PROBLEM:")
print("8. LC 1004 - Max Consecutive Ones III (MEDIUM) ⭐⭐⭐")
print("   (Uses VARIABLE window - included to show the difference!)")
print("\n⭐ = Frequency Rating (More stars = Asked more often)")
print("\n📖 Study Path:")
print("   Week 1: Problems 4, 5, 6 (Build fundamentals)")
print("   Week 2: Problems 1, 2 (Master anagram detection)")
print("   Week 3: Problems 3, 7, 9 (Conquer advanced topics)")
print("\nKey Pattern:")
print("  - Fixed window size = k (known beforehand)")
print("  - Slide by removing left, adding right")
print("  - No while loop for contraction")
print("  - Simpler than variable window!")
print("\nAll solutions use O(n) or O(n*k) time complexity!")
# print("\n" + "=" * 70)
