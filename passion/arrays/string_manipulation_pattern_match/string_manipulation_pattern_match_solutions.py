"""
STRING MANIPULATION & PATTERN MATCHING - COMPLETE SOLUTIONS
============================================================

This file contains comprehensive solutions for string manipulation and pattern matching problems,
organized from EASY → MEDIUM → HARD with detailed explanations and key insights.

Covers:
- PATTERN 5A: Character Frequency (Hash Map)
- PATTERN 5B: Sliding Window for Substring
- PATTERN 5C: Two Pointers for Palindrome
- PATTERN 5D: Pattern Matching
- PATTERN 5E: Advanced String Problems

Each problem includes:
✓ Problem statement with examples
✓ Detailed key insights
✓ Step-by-step approach
✓ Optimized solution
✓ Time & space complexity
✓ Test cases with explanations
"""

# ============================================================================
# PATTERN TEMPLATES
# ============================================================================

"""
UNIVERSAL STRING MANIPULATION TEMPLATES
========================================

1. CHARACTER FREQUENCY (HASH MAP)
----------------------------------
def char_frequency_template(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

Use Case: Anagrams, character counting, frequency comparison

2. SLIDING WINDOW FOR SUBSTRING
--------------------------------
def sliding_window_substring(s, pattern):
    left = 0
    window = {}
    
    for right in range(len(s)):
        # Expand window
        char = s[right]
        window[char] = window.get(char, 0) + 1
        
        # Shrink window when condition met
        while condition_violated:
            window[s[left]] -= 1
            left += 1
        
        # Update result
        update_result()

Use Case: Minimum window, longest substring with constraints

3. TWO POINTERS FOR PALINDROME
-------------------------------
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

Use Case: Longest palindrome, count palindromes

4. PATTERN MATCHING (TWO POINTERS)
----------------------------------
def is_subsequence(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

Use Case: Subsequence checking, pattern matching

5. STRING DP (EDIT DISTANCE)
-----------------------------
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    
    return dp[m][n]

Use Case: Edit distance, LCS, string transformation
"""


# ============================================================================
# EASY PROBLEMS - FOUNDATIONAL CONCEPTS
# ============================================================================

print("=" * 70)
print("EASY PROBLEMS - MASTER THESE FIRST")
print("=" * 70)


# ============================================================================
# PROBLEM 1: LeetCode 242 - Valid Anagram (EASY)
# ============================================================================

"""
Problem:
--------
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters

Follow up: What if the inputs contain Unicode characters?
"""

def isAnagram(s, t):
    """
    Approach: Character Frequency Hash Map
    
    Key Insight:
    - Two strings are anagrams if they have EXACTLY the same character frequencies
    - We can use a hash map to count character occurrences
    - Compare the two frequency maps for equality
    - Alternative: Sort both strings and compare (O(n log n))
    - Hash map approach is O(n) which is optimal
    
    Why This Works:
    - Anagrams have same letters, just rearranged
    - If frequencies match, strings are anagrams
    - Dictionary equality in Python compares both keys and values
    
    Edge Cases:
    - Different lengths → immediately return False
    - Empty strings → both empty means True
    - Single character → check if same
    
    Algorithm:
    1. Quick check: if lengths differ, return False
    2. Build frequency map for string s
    3. Build frequency map for string t
    4. Compare the two maps
    
    Optimization:
    - Can use single map: increment for s, decrement for t
    - If all values are 0 at end, it's an anagram
    - Or use Counter from collections module
    
    Pattern Recognition:
    - "rearrange letters" → frequency counting
    - "same letters" → hash map comparison
    - "anagram" keyword → character frequency
    
    Time: O(n) where n = len(s) + len(t)
    Space: O(1) - at most 26 lowercase letters
    """
    # Quick length check
    if len(s) != len(t):
        return False
    
    # Build frequency maps
    freq_s = {}
    freq_t = {}
    
    i = 0
    while i < len(s):
        freq_s[s[i]] = freq_s.get(s[i], 0) + 1
        freq_t[t[i]] = freq_t.get(t[i], 0) + 1
        i += 1
    
    # Compare frequency maps
    return freq_s == freq_t


# Alternative: Using single map
def isAnagram_optimized(s, t):
    """
    Single pass with one frequency map
    """
    if len(s) != len(t):
        return False
    
    freq = {}
    
    i = 0
    while i < len(s):
        # Increment for s
        freq[s[i]] = freq.get(s[i], 0) + 1
        # Decrement for t
        freq[t[i]] = freq.get(t[i], 0) - 1
        i += 1
    
    # Check if all frequencies are 0
    for count in freq.values():
        if count != 0:
            return False
    
    return True


# Test cases
print("\n" + "=" * 70)
print("Problem 1: LeetCode 242 - Valid Anagram")
print("=" * 70)

test_cases_242 = [
    ("anagram", "nagaram", True),
    ("rat", "car", False),
    ("a", "a", True),
    ("ab", "ba", True),
    ("abc", "def", False)
]

for s, t, expected in test_cases_242:
    result = isAnagram(s, t)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', t='{t}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 2: LeetCode 387 - First Unique Character in a String (EASY)
# ============================================================================

"""
Problem:
--------
Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0
Explanation: 'l' is the first character that appears only once

Example 2:
Input: s = "loveleetcode"
Output: 2
Explanation: 'v' is the first non-repeating character

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters
"""

def firstUniqChar(s):
    """
    Approach: Two-Pass with Frequency Map
    
    Key Insight:
    - Need to find FIRST character that appears only once
    - Two-pass approach: count frequencies, then find first with count=1
    - Can't do in single pass because we need to know total counts
    - Hash map stores character frequencies
    - Second pass finds first character with frequency 1
    
    Why Two Passes?
    - First pass: Build complete frequency map
    - Second pass: Find first char with freq=1 in original order
    - Order matters! We need the FIRST unique character
    
    Algorithm:
    1. First pass: Count frequency of each character
    2. Second pass: Iterate through string, return index of first char with freq=1
    3. If no unique character found, return -1
    
    Alternative Approaches:
    - Use array of size 26 for lowercase letters (slightly faster)
    - Use OrderedDict to maintain insertion order
    - Use two sets: seen_once and seen_multiple
    
    Pattern Recognition:
    - "first non-repeating" → frequency map + order preservation
    - "unique character" → count occurrences
    - Need to maintain original order → iterate string, not map
    
    Time: O(n) - two passes through string
    Space: O(1) - at most 26 lowercase letters
    """
    # First pass: build frequency map
    freq = {}
    i = 0
    while i < len(s):
        freq[s[i]] = freq.get(s[i], 0) + 1
        i += 1
    
    # Second pass: find first unique character
    i = 0
    while i < len(s):
        if freq[s[i]] == 1:
            return i
        i += 1
    
    return -1


# Test cases
print("\n" + "=" * 70)
print("Problem 2: LeetCode 387 - First Unique Character in a String")
print("=" * 70)

test_cases_387 = [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1),
    ("z", 0),
    ("aabbcc", -1)
]

for s, expected in test_cases_387:
    result = firstUniqChar(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 3: LeetCode 125 - Valid Palindrome (EASY)
# ============================================================================

"""
Problem:
--------
A phrase is a palindrome if, after converting all uppercase letters into lowercase 
letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome

Example 3:
Input: s = " "
Output: true
Explanation: Empty string is palindrome

Constraints:
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters
"""

def isPalindrome(s):
    """
    Approach: Two Pointers with Character Filtering
    
    Key Insight:
    - Use two pointers from opposite ends
    - Skip non-alphanumeric characters
    - Compare characters case-insensitively
    - No need to create new string (space efficient)
    - Move pointers inward, skipping invalid chars
    
    Why Two Pointers?
    - O(n) time with O(1) space
    - Don't need to create filtered string
    - Can check on-the-fly while moving pointers
    - More efficient than reversing and comparing
    
    Algorithm:
    1. Initialize left=0, right=len(s)-1
    2. While left < right:
       a. Skip non-alphanumeric from left
       b. Skip non-alphanumeric from right
       c. Compare characters (case-insensitive)
       d. If mismatch, return False
       e. Move both pointers inward
    3. Return True if all characters matched
    
    Edge Cases:
    - Empty string → True
    - Single character → True
    - All spaces/punctuation → True
    - Mixed case → convert to same case
    
    Pattern Recognition:
    - "reads same forward and backward" → palindrome → two pointers
    - "ignore non-alphanumeric" → filtering while iterating
    - "case-insensitive" → convert to lowercase
    
    Time: O(n)
    Space: O(1)
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1
        
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


# Test cases
print("\n" + "=" * 70)
print("Problem 3: LeetCode 125 - Valid Palindrome")
print("=" * 70)

test_cases_125 = [
    ("A man, a plan, a canal: Panama", True),
    ("race a car", False),
    (" ", True),
    ("a", True),
    ("ab", False),
    (".,", True)
]

for s, expected in test_cases_125:
    result = isPalindrome(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 4: LeetCode 28 - Find the Index of the First Occurrence (EASY)
# ============================================================================

"""
Problem:
--------
Given two strings needle and haystack, return the index of the first occurrence 
of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6. First occurrence is at index 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode"

Constraints:
- 1 <= haystack.length, needle.length <= 10^4
- haystack and needle consist of only lowercase English characters
"""

def strStr(haystack, needle):
    """
    Approach: Sliding Window / Brute Force
    
    Key Insight:
    - Check every possible starting position in haystack
    - For each position, check if needle matches
    - Can use Python's built-in 'in' operator, but let's implement manually
    - Sliding window of size len(needle) through haystack
    - KMP algorithm is O(n+m) but overkill for this problem
    
    Why This Approach?
    - Simple and intuitive
    - Works well for small strings
    - Python string slicing is optimized
    - For interviews, brute force is acceptable unless asked to optimize
    
    Algorithm:
    1. Edge case: if needle is empty, return 0
    2. Iterate through haystack up to (len(haystack) - len(needle) + 1)
    3. At each position, check if substring matches needle
    4. Return index if match found
    5. Return -1 if no match
    
    Optimization:
    - Can use KMP (Knuth-Morris-Pratt) for O(n+m) worst case
    - Can use Rabin-Karp with rolling hash
    - For most cases, brute force is sufficient
    
    Pattern Recognition:
    - "find first occurrence" → sliding window or pattern matching
    - "substring search" → iterate and compare
    - Can optimize with KMP if needed
    
    Time: O(n*m) worst case, where n=len(haystack), m=len(needle)
    Space: O(1)
    """
    if not needle:
        return 0
    
    if len(needle) > len(haystack):
        return -1
    
    # Check each possible starting position
    i = 0
    while i <= len(haystack) - len(needle):
        # Check if needle matches at position i
        if haystack[i:i+len(needle)] == needle:
            return i
        i += 1
    
    return -1


# Alternative: Manual character comparison
def strStr_manual(haystack, needle):
    """
    Manual character-by-character comparison
    """
    if not needle:
        return 0
    
    if len(needle) > len(haystack):
        return -1
    
    i = 0
    while i <= len(haystack) - len(needle):
        # Check if needle matches starting at position i
        j = 0
        while j < len(needle):
            if haystack[i + j] != needle[j]:
                break
            j += 1
        
        # If we matched all characters
        if j == len(needle):
            return i
        
        i += 1
    
    return -1


# Test cases
print("\n" + "=" * 70)
print("Problem 4: LeetCode 28 - Find the Index of the First Occurrence")
print("=" * 70)

test_cases_28 = [
    ("sadbutsad", "sad", 0),
    ("leetcode", "leeto", -1),
    ("hello", "ll", 2),
    ("aaaaa", "bba", -1),
    ("", "", 0),
    ("a", "a", 0)
]

for haystack, needle, expected in test_cases_28:
    result = strStr(haystack, needle)
    status = "✅" if result == expected else "❌"
    print(f"haystack='{haystack}', needle='{needle}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 5: LeetCode 392 - Is Subsequence (EASY)
# ============================================================================

"""
Problem:
--------
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string 
by deleting some (can be none) of the characters without disturbing the relative 
positions of the remaining characters.

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
- 0 <= s.length <= 100
- 0 <= t.length <= 10^4
- s and t consist only of lowercase English letters

Follow up: If there are lots of incoming s, how would you optimize?
"""

def isSubsequence(s, t):
    """
    Approach: Two Pointers
    
    Key Insight:
    - Subsequence means characters appear in same order, but not necessarily consecutive
    - Use two pointers: one for s, one for t
    - Move pointer in t always, move pointer in s only when characters match
    - If we reach end of s, all characters were found in order
    - This is greedy: match as soon as we find the character
    
    Why Two Pointers?
    - O(n) time where n = len(t)
    - O(1) space
    - Simple and efficient
    - Greedy approach works because we just need any valid subsequence
    
    Algorithm:
    1. Initialize i=0 (pointer for s), j=0 (pointer for t)
    2. While both pointers are in bounds:
       a. If s[i] == t[j], move i forward (found match)
       b. Always move j forward
    3. Return True if i == len(s) (all characters of s found)
    
    Follow-up Optimization:
    - If many queries with different s but same t:
      - Preprocess t: build index map {char: [list of indices]}
      - For each s, use binary search on index lists
      - Time: O(m log n) per query where m=len(s), n=len(t)
    
    Pattern Recognition:
    - "subsequence" → two pointers
    - "same order" → greedy matching
    - "not consecutive" → skip characters in t
    
    Time: O(n) where n = len(t)
    Space: O(1)
    """
    i = 0  # Pointer for s
    j = 0  # Pointer for t
    
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    
    return i == len(s)


# Test cases
print("\n" + "=" * 70)
print("Problem 5: LeetCode 392 - Is Subsequence")
print("=" * 70)

test_cases_392 = [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False),
    ("", "ahbgdc", True),
    ("abc", "", False),
    ("ace", "abcde", True)
]

for s, t, expected in test_cases_392:
    result = isSubsequence(s, t)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', t='{t}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 6: LeetCode 383 - Ransom Note (EASY)
# ============================================================================

"""
Problem:
--------
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters
"""

def canConstruct(ransomNote, magazine):
    """
    Approach: Character Frequency Hash Map
    
    Key Insight:
    - Check if magazine has enough of each character for ransomNote
    - Build frequency map for magazine
    - For each character in ransomNote, check if available
    - Decrement count as we use characters
    - If any character not available, return False
    
    Why This Works:
    - Each letter can only be used once
    - Frequency map tracks available letters
    - Simple counting problem
    
    Algorithm:
    1. Build frequency map for magazine
    2. For each character in ransomNote:
       a. Check if character exists in map with count > 0
       b. If yes, decrement count
       c. If no, return False
    3. Return True if all characters found
    
    Alternative:
    - Use Counter from collections
    - Sort and compare (slower)
    
    Pattern Recognition:
    - "can construct" → frequency checking
    - "each letter used once" → count availability
    
    Time: O(m + n) where m=len(ransomNote), n=len(magazine)
    Space: O(1) - at most 26 lowercase letters
    """
    # Build frequency map for magazine
    freq = {}
    for char in magazine:
        freq[char] = freq.get(char, 0) + 1
    
    # Check if ransomNote can be constructed
    for char in ransomNote:
        if char not in freq or freq[char] == 0:
            return False
        freq[char] -= 1
    
    return True


# Test cases
print("\n" + "=" * 70)
print("Problem 6: LeetCode 383 - Ransom Note")
print("=" * 70)

test_cases_383 = [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
    ("abc", "aabbcc", True),
    ("", "abc", True)
]

for ransomNote, magazine, expected in test_cases_383:
    result = canConstruct(ransomNote, magazine)
    status = "✅" if result == expected else "❌"
    print(f"ransomNote='{ransomNote}', magazine='{magazine}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 7: LeetCode 459 - Repeated Substring Pattern (EASY)
# ============================================================================

"""
Problem:
--------
Given a string s, check if it can be constructed by taking a substring of it 
and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters
"""

def repeatedSubstringPattern(s):
    """
    Approach: String Concatenation Trick
    
    Key Insight:
    - If s is made of repeated pattern, then s exists in (s+s)[1:-1]
    - Example: s="abab", s+s="abababab", (s+s)[1:-1]="bababab"
    - "abab" is found in "bababab" at index 1
    - If s is NOT repeated pattern, it won't be found
    
    Why This Works:
    - If s = pattern * k, then s+s = pattern * 2k
    - Removing first and last char: still has pattern * (2k-2) which contains s
    - If s is not repeated, removing edges breaks the pattern
    
    Alternative Approach:
    - Try all divisors of len(s) as pattern lengths
    - Check if s[:length] repeated gives s
    - More intuitive but slower
    
    Algorithm:
    1. Create doubled = s + s
    2. Remove first and last character
    3. Check if s exists in the result
    
    Pattern Recognition:
    - "repeated substring" → pattern matching
    - "constructed by repeating" → check divisors or use trick
    
    Time: O(n) - string search is O(n)
    Space: O(n) - for concatenated string
    """
    # Trick: if s is repeated pattern, it exists in (s+s)[1:-1]
    return s in (s + s)[1:-1]


# Alternative: Check all divisors
def repeatedSubstringPattern_divisors(s):
    """
    Check all possible pattern lengths (divisors of len(s))
    """
    n = len(s)
    
    # Try all possible pattern lengths
    for length in range(1, n // 2 + 1):
        # Pattern length must divide total length
        if n % length == 0:
            pattern = s[:length]
            # Check if repeating pattern gives original string
            if pattern * (n // length) == s:
                return True
    
    return False


# Test cases
print("\n" + "=" * 70)
print("Problem 7: LeetCode 459 - Repeated Substring Pattern")
print("=" * 70)

test_cases_459 = [
    ("abab", True),
    ("aba", False),
    ("abcabcabcabc", True),
    ("a", False),
    ("aa", True)
]

for s, expected in test_cases_459:
    result = repeatedSubstringPattern(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 8: LeetCode 680 - Valid Palindrome II (EASY) ⭐⭐
# ============================================================================

"""
Problem:
--------
Given a string s, return true if the s can be palindrome after deleting at most 
one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'

Example 3:
Input: s = "abc"
Output: false

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters
"""

def validPalindrome(s):
    """
    Approach: Two Pointers with One Skip
    
    Key Insight:
    - Use two pointers from both ends
    - When mismatch found, try skipping either left or right character
    - Check if remaining substring is palindrome
    - Only one skip allowed
    - Helper function checks if substring is palindrome
    
    Why This Works:
    - If string is already palindrome, no skip needed
    - If one mismatch, try both options: skip left or skip right
    - If either option gives palindrome, return True
    - If more than one mismatch needed, return False
    
    Algorithm:
    1. Use two pointers: left=0, right=len(s)-1
    2. While left < right:
       a. If s[left] == s[right], move both inward
       b. If mismatch, check two options:
          - Is s[left+1...right] a palindrome? (skip left)
          - Is s[left...right-1] a palindrome? (skip right)
       c. Return True if either option works
    3. Return True if no mismatch found
    
    Helper Function:
    - isPalindrome(left, right): checks if substring is palindrome
    
    Pattern Recognition:
    - "delete at most one" → try both skip options
    - "palindrome" → two pointers
    - "after deleting" → check remaining substring
    
    Time: O(n)
    Space: O(1)
    """
    
    def isPalindrome(left, right):
        """Check if substring s[left...right] is palindrome"""
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            # Try skipping either left or right character
            return isPalindrome(left + 1, right) or isPalindrome(left, right - 1)
        left += 1
        right -= 1
    
    return True


# Test cases
print("\n" + "=" * 70)
print("Problem 8: LeetCode 680 - Valid Palindrome II (EASY)")
print("=" * 70)

test_cases_680 = [
    ("aba", True),
    ("abca", True),
    ("abc", False),
    ("racecar", True),
    ("deeee", True),
    ("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True)
]

for s, expected in test_cases_680:
    result = validPalindrome(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s[:20]}...' → {result} (expected: {expected}) {status}")


# ============================================================================
# MEDIUM PROBLEMS - CORE INTERVIEW QUESTIONS
# ============================================================================

print("\n\n" + "=" * 70)
print("MEDIUM PROBLEMS - FAANG FAVORITES")
print("=" * 70)


# ============================================================================
# PROBLEM 9: LeetCode 49 - Group Anagrams (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an array of strings strs, group the anagrams together. You can return 
the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters
"""

def groupAnagrams(strs):
    """
    Approach: Hash Map with Sorted String as Key
    
    Key Insight:
    - Anagrams have same characters, just rearranged
    - If we sort the characters, anagrams become identical
    - Use sorted string as key in hash map
    - All anagrams will map to same key
    - Group strings by their sorted representation
    
    Why Sorted String as Key?
    - Anagrams produce same sorted string
    - Example: "eat", "tea", "ate" all become "aet"
    - Hash map groups all strings with same sorted form
    - Alternative: Use character frequency tuple as key
    
    Algorithm:
    1. Create hash map: {sorted_string: [list of original strings]}
    2. For each string:
       a. Sort the string to get key
       b. Add original string to list for that key
    3. Return all values (lists of anagrams)
    
    Alternative Approach:
    - Use character count tuple as key
    - Count = tuple of 26 integers for a-z
    - Slightly faster than sorting for long strings
    
    Pattern Recognition:
    - "group anagrams" → hash map with canonical form
    - "same letters" → sorting or frequency counting
    - "group together" → hash map values are lists
    
    Time: O(n * k log k) where n = number of strings, k = max length
    Space: O(n * k) for storing all strings
    """
    anagram_map = {}
    
    i = 0
    while i < len(strs):
        # Sort string to get key
        sorted_str = ''.join(sorted(strs[i]))
        
        # Add to map
        if sorted_str not in anagram_map:
            anagram_map[sorted_str] = []
        anagram_map[sorted_str].append(strs[i])
        
        i += 1
    
    # Return all groups
    return list(anagram_map.values())


# Alternative: Using character count as key
def groupAnagrams_freq(strs):
    """
    Use character frequency tuple as key (faster for long strings)
    """
    anagram_map = {}
    
    for s in strs:
        # Create frequency count
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Use tuple as key (lists aren't hashable)
        key = tuple(count)
        
        if key not in anagram_map:
            anagram_map[key] = []
        anagram_map[key].append(s)
    
    return list(anagram_map.values())


# Test cases
print("\n" + "=" * 70)
print("Problem 6: LeetCode 49 - Group Anagrams (MEDIUM)")
print("=" * 70)

test_cases_49 = [
    (["eat", "tea", "tan", "ate", "nat", "bat"], 
     [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    ([""], [[""]]),
    (["a"], [["a"]])
]

for strs, expected in test_cases_49:
    result = groupAnagrams(strs)
    # Sort for comparison (order doesn't matter)
    result_sorted = [sorted(group) for group in result]
    expected_sorted = [sorted(group) for group in expected]
    result_sorted.sort()
    expected_sorted.sort()
    status = "✅" if result_sorted == expected_sorted else "❌"
    print(f"Input: {strs}")
    print(f"Output: {result} {status}")
    print()


# ============================================================================
# PROBLEM 10: LeetCode 451 - Sort Characters By Frequency (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a string s, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.

Constraints:
- 1 <= s.length <= 5 * 10^5
- s consists of uppercase and lowercase English letters and digits
"""

def frequencySort(s):
    """
    Approach: Frequency Map + Bucket Sort
    
    Key Insight:
    - Count character frequencies using hash map
    - Sort characters by frequency (descending)
    - Build result string with characters repeated by frequency
    - Can use bucket sort for O(n) time instead of O(n log n) sorting
    
    Why Bucket Sort?
    - Frequency range is [1, n] where n = len(s)
    - Create buckets for each frequency
    - Bucket[i] contains all characters with frequency i
    - Iterate buckets from high to low frequency
    
    Algorithm:
    1. Build frequency map: {char: count}
    2. Create buckets: bucket[freq] = [list of chars with this freq]
    3. Iterate buckets from len(s) down to 1
    4. For each bucket, append chars * frequency to result
    
    Alternative:
    - Sort by frequency using sorted() - O(n log n)
    - Use heap - O(n log k) where k = unique chars
    
    Pattern Recognition:
    - "sort by frequency" → frequency map + sorting
    - "decreasing order" → reverse sort
    - Can optimize with bucket sort
    
    Time: O(n) with bucket sort, O(n log n) with regular sort
    Space: O(n)
    """
    # Count frequencies
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Create buckets: bucket[i] = list of chars with frequency i
    buckets = [[] for _ in range(len(s) + 1)]
    for char, count in freq.items():
        buckets[count].append(char)
    
    # Build result from high frequency to low
    result = []
    for i in range(len(s), 0, -1):
        for char in buckets[i]:
            result.append(char * i)
    
    return ''.join(result)


# Test cases
print("\n" + "=" * 70)
print("Problem 9: LeetCode 451 - Sort Characters By Frequency")
print("=" * 70)

test_cases_451 = [
    ("tree", ["eert", "eetr"]),
    ("cccaaa", ["aaaccc", "cccaaa"]),
    ("Aabb", ["bbAa", "bbaA"]),
    ("a", ["a"])
]

for s, expected_options in test_cases_451:
    result = frequencySort(s)
    status = "✅" if result in expected_options else "❌"
    print(f"s='{s}' → '{result}' (expected one of: {expected_options}) {status}")


# ============================================================================
# PROBLEM 11: LeetCode 1347 - Minimum Steps to Make Two Strings Anagram (MEDIUM)
# ============================================================================

"""
Problem:
--------
You are given two strings of the same length s and t. In one step you can choose 
any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a 
different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with 'b', t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0

Constraints:
- 1 <= s.length <= 5 * 10^4
- s.length == t.length
- s and t consist of lowercase English letters only
"""

def minSteps(s, t):
    """
    Approach: Character Frequency Difference
    
    Key Insight:
    - Count frequency difference between s and t
    - For each character in s that appears more than in t, we need to add it to t
    - Only count positive differences (chars needed in t)
    - Sum of positive differences = minimum steps
    
    Why This Works:
    - Anagram means same character frequencies
    - If s has 3 'a's and t has 1 'a', we need 2 more 'a's in t
    - Each replacement is one step
    - Only count what's missing (positive diff)
    
    Algorithm:
    1. Build frequency map for s
    2. Build frequency map for t
    3. For each character in s:
       - If freq[s] > freq[t], add difference to steps
    4. Return total steps
    
    Optimization:
    - Can use single pass with one frequency map
    - Increment for s, decrement for t
    
    Pattern Recognition:
    - "make anagram" → frequency comparison
    - "minimum steps" → count differences
    - "replace characters" → frequency adjustment
    
    Time: O(n)
    Space: O(1) - at most 26 lowercase letters
    """
    # Count frequencies
    freq_s = {}
    freq_t = {}
    
    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1
    
    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    
    # Count steps needed
    steps = 0
    for char in freq_s:
        if freq_s[char] > freq_t.get(char, 0):
            steps += freq_s[char] - freq_t.get(char, 0)
    
    return steps


# Test cases
print("\n" + "=" * 70)
print("Problem 10: LeetCode 1347 - Minimum Steps to Make Anagram")
print("=" * 70)

test_cases_1347 = [
    ("bab", "aba", 1),
    ("leetcode", "practice", 5),
    ("anagram", "mangaar", 0),
    ("abc", "def", 3)
]

for s, t, expected in test_cases_1347:
    result = minSteps(s, t)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', t='{t}' → {result} (expected: {expected}) {status}")




# ============================================================================
# PROBLEM 13: LeetCode 5 - Longest Palindromic Substring (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
- 1 <= s.length <= 1000
- s consist of only digits and English letters
"""

def longestPalindrome(s):
    """
    Approach: Expand Around Center
    
    Key Insight:
    - A palindrome mirrors around its center
    - For each possible center, expand outward while characters match
    - Two cases: odd length (single center) and even length (two centers)
    - Check both cases for each position
    - Track the longest palindrome found
    
    Why Expand Around Center?
    - O(n²) time, O(1) space
    - Better than brute force O(n³)
    - Better space than DP O(n²)
    - Intuitive and easy to implement
    
    Algorithm:
    1. For each position i in string:
       a. Expand around single center (odd length palindromes)
       b. Expand around double center (even length palindromes)
       c. Track longest palindrome found
    2. Return the longest palindrome substring
    
    Helper Function:
    - expandAroundCenter(left, right): expands while s[left] == s[right]
    - Returns length of palindrome
    
    Alternative Approaches:
    - DP: O(n²) time and space
    - Manacher's Algorithm: O(n) time but complex
    - For interviews, expand around center is best balance
    
    Pattern Recognition:
    - "longest palindrome" → expand around center
    - "palindrome" → two pointers or DP
    - "substring" → need to track start and length
    
    Time: O(n²) - n centers, each expansion is O(n)
    Space: O(1)
    """
    
    def expandAroundCenter(left, right):
        """
        Expand while characters match and return length
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return length of palindrome
        return right - left - 1
    
    if not s:
        return ""
    
    start = 0
    max_len = 0
    
    i = 0
    while i < len(s):
        # Check odd length palindromes (single center)
        len1 = expandAroundCenter(i, i)
        
        # Check even length palindromes (double center)
        len2 = expandAroundCenter(i, i + 1)
        
        # Get maximum length
        current_len = max(len1, len2)
        
        # Update if we found longer palindrome
        if current_len > max_len:
            max_len = current_len
            # Calculate start position
            start = i - (current_len - 1) // 2
        
        i += 1
    
    return s[start:start + max_len]


# Test cases
print("\n" + "=" * 70)
print("Problem 7: LeetCode 5 - Longest Palindromic Substring (MEDIUM)")
print("=" * 70)

test_cases_5 = [
    ("babad", ["bab", "aba"]),  # Both are valid
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
# PROBLEM 14: LeetCode 647 - Palindromic Substrings (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c"

Example 2:
Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa"

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase English letters
"""

def countSubstrings(s):
    """
    Approach: Expand Around Center
    
    Key Insight:
    - Similar to "Longest Palindromic Substring"
    - For each center, expand and count palindromes
    - Two cases: odd length and even length palindromes
    - Each expansion that maintains palindrome property adds to count
    - Don't need to track the palindromes, just count them
    
    Why Expand Around Center?
    - O(n²) time, O(1) space
    - Simple to implement
    - Count palindromes as we expand
    - Each valid expansion is a palindrome
    
    Algorithm:
    1. For each position i:
       a. Expand around single center (odd length)
       b. Expand around double center (even length)
       c. Count all valid palindromes found
    2. Return total count
    
    Helper Function:
    - countPalindromes(left, right): expands and counts
    - Returns number of palindromes with this center
    
    Alternative:
    - DP approach: O(n²) time and space
    - For each substring, check if palindrome
    - Expand around center is more space efficient
    
    Pattern Recognition:
    - "count palindromes" → expand around center
    - "all palindromic substrings" → check all centers
    - Similar to longest palindrome but counting instead
    
    Time: O(n²)
    Space: O(1)
    """
    
    def countPalindromes(left, right):
        """
        Expand around center and count palindromes
        """
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    total_count = 0
    
    i = 0
    while i < len(s):
        # Count odd length palindromes
        total_count += countPalindromes(i, i)
        
        # Count even length palindromes
        total_count += countPalindromes(i, i + 1)
        
        i += 1
    
    return total_count


# Test cases
print("\n" + "=" * 70)
print("Problem 9: LeetCode 647 - Palindromic Substrings")
print("=" * 70)

test_cases_647 = [
    ("abc", 3),
    ("aaa", 6),
    ("a", 1),
    ("aba", 4),
    ("racecar", 10)
]

for s, expected in test_cases_647:
    result = countSubstrings(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} (expected: {expected}) {status}")




# ============================================================================
# HARD PROBLEMS - ADVANCED TECHNIQUES
# ============================================================================

print("\n\n" + "=" * 70)
print("HARD PROBLEMS - MASTER LEVEL")
print("=" * 70)


# ============================================================================
# PROBLEM 17: LeetCode 131 - Palindrome Partitioning (MEDIUM) ⭐⭐
# ============================================================================

"""
Problem:
--------
Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2.

You have the following three operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
- 0 <= word1.length, word2.length <= 500
- word1 and word2 consist of lowercase English letters
"""

def minDistance(word1, word2):
    """
    Approach: Dynamic Programming (2D DP)
    
    Key Insight:
    - Classic DP problem (Levenshtein distance)
    - dp[i][j] = min operations to convert word1[0...i-1] to word2[0...j-1]
    - Three operations: insert, delete, replace
    - If characters match, no operation needed
    - If characters differ, take min of three operations
    
    Why DP?
    - Optimal substructure: solution depends on smaller subproblems
    - Overlapping subproblems: same subproblems solved multiple times
    - Bottom-up approach builds solution from base cases
    
    DP Recurrence:
    - If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
    - Else: dp[i][j] = 1 + min(
        dp[i-1][j],    # Delete from word1
        dp[i][j-1],    # Insert into word1
        dp[i-1][j-1]   # Replace in word1
      )
    
    Base Cases:
    - dp[0][j] = j (insert j characters)
    - dp[i][0] = i (delete i characters)
    
    Algorithm:
    1. Create (m+1) x (n+1) DP table
    2. Initialize base cases
    3. Fill table using recurrence relation
    4. Return dp[m][n]
    
    Optimization:
    - Can use 1D DP with O(n) space
    - Only need previous row to compute current row
    
    Pattern Recognition:
    - "minimum operations" → DP
    - "convert string" → edit distance
    - "insert/delete/replace" → classic DP problem
    
    Time: O(m * n)
    Space: O(m * n)
    """
    m, n = len(word1), len(word2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take minimum of three operations
                dp[i][j] = 1 + min(
                    dp[i-1][j],      # Delete
                    dp[i][j-1],      # Insert
                    dp[i-1][j-1]     # Replace
                )
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 11: LeetCode 72 - Edit Distance (HARD)")
print("=" * 70)

test_cases_72 = [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
    ("", "", 0),
    ("a", "b", 1),
    ("abc", "abc", 0)
]

for word1, word2, expected in test_cases_72:
    result = minDistance(word1, word2)
    status = "✅" if result == expected else "❌"
    print(f"word1='{word1}', word2='{word2}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 18: LeetCode 686 - Repeated String Match (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given two strings text1 and text2, return the length of their longest common subsequence. 
If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some 
characters (can be none) deleted without changing the relative order of the remaining characters.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters
"""

def longestCommonSubsequence(text1, text2):
    """
    Approach: Dynamic Programming (2D DP)
    
    Key Insight:
    - Classic DP problem
    - dp[i][j] = length of LCS of text1[0...i-1] and text2[0...j-1]
    - If characters match, extend LCS by 1
    - If characters differ, take max of excluding one character
    
    Why DP?
    - Optimal substructure: LCS of strings depends on LCS of substrings
    - Overlapping subproblems: same subproblems computed multiple times
    - Build solution bottom-up from smaller subproblems
    
    DP Recurrence:
    - If text1[i-1] == text2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
    - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    Base Cases:
    - dp[0][j] = 0 (empty text1)
    - dp[i][0] = 0 (empty text2)
    
    Algorithm:
    1. Create (m+1) x (n+1) DP table
    2. Initialize base cases (first row and column = 0)
    3. Fill table using recurrence relation
    4. Return dp[m][n]
    
    Optimization:
    - Can use 1D DP with O(n) space
    - Only need previous row to compute current row
    
    Pattern Recognition:
    - "longest common subsequence" → classic DP
    - "subsequence" (not substring) → DP, not sliding window
    - Similar to edit distance but simpler
    
    Time: O(m * n)
    Space: O(m * n)
    """
    m, n = len(text1), len(text2)
    
    # Create DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                # Characters match, extend LCS
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                # Take max of excluding one character
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 12: LeetCode 1143 - Longest Common Subsequence")
print("=" * 70)

test_cases_1143 = [
    ("abcde", "ace", 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
    ("", "abc", 0),
    ("bl", "yby", 1)
]

for text1, text2, expected in test_cases_1143:
    result = longestCommonSubsequence(text1, text2)
    status = "✅" if result == expected else "❌"
    print(f"text1='{text1}', text2='{text2}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 19: LeetCode 792 - Number of Matching Subsequences (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting 
some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb"

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb"

Constraints:
- 1 <= s.length <= 1000
- s consists only of lowercase English letters
"""

def longestPalindromeSubseq(s):
    """
    Approach: Dynamic Programming (2D DP)
    
    Key Insight:
    - Similar to LCS but find LCS of s and reverse(s)
    - Or use DP directly: dp[i][j] = longest palindrome in s[i...j]
    - If s[i] == s[j], include both: dp[i][j] = 2 + dp[i+1][j-1]
    - If s[i] != s[j], exclude one: dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    Why DP?
    - Palindrome subsequence has optimal substructure
    - Can build from smaller subproblems
    - Different from longest palindrome substring (contiguous)
    
    Algorithm:
    1. Create n x n DP table
    2. Base case: dp[i][i] = 1 (single character)
    3. Fill table for increasing lengths
    4. Return dp[0][n-1]
    
    Alternative:
    - Find LCS of s and reverse(s)
    - Same result, different approach
    
    Pattern Recognition:
    - "palindromic subsequence" → DP
    - "subsequence" (not substring) → DP
    - Similar to LCS problem
    
    Time: O(n²)
    Space: O(n²)
    """
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Base case: single characters
    for i in range(n):
        dp[i][i] = 1
    
    # Fill for increasing lengths
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + (dp[i+1][j-1] if length > 2 else 0)
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]


# Test cases
print("\n" + "=" * 70)
print("Problem 13: LeetCode 516 - Longest Palindromic Subsequence")
print("=" * 70)

test_cases_516 = [
    ("bbbab", 4),
    ("cbbd", 2),
    ("a", 1),
    ("racecar", 7)
]

for s, expected in test_cases_516:
    result = longestPalindromeSubseq(s)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 20: LeetCode 1143 - Longest Common Subsequence (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Constraints:
- 1 <= s.length <= 16
- s contains only lowercase English letters
"""

def partition(s):
    """
    Approach: Backtracking + Palindrome Checking
    
    Key Insight:
    - Use backtracking to try all possible partitions
    - At each position, try all possible palindrome substrings
    - Recursively partition the remaining string
    - Collect all valid partitions
    
    Why Backtracking?
    - Need to explore all possible partitions
    - Decision tree: at each position, choose partition point
    - Prune invalid branches (non-palindrome substrings)
    
    Algorithm:
    1. Use backtracking with current partition path
    2. At each position, try all substrings starting from that position
    3. If substring is palindrome, add to path and recurse
    4. When reach end of string, add current path to result
    5. Backtrack and try other options
    
    Optimization:
    - Precompute palindrome DP table
    - dp[i][j] = True if s[i...j] is palindrome
    - Avoids repeated palindrome checks
    
    Pattern Recognition:
    - "all possible" → backtracking
    - "partition" → decision tree
    - "palindrome" → helper function or DP
    
    Time: O(n * 2^n) - exponential
    Space: O(n) for recursion stack
    """
    
    def isPalindrome(start, end):
        """Check if s[start...end] is palindrome"""
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def backtrack(start, path):
        """Backtrack to find all partitions"""
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start, len(s)):
            if isPalindrome(start, end):
                path.append(s[start:end+1])
                backtrack(end + 1, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result


# Test cases
print("\n" + "=" * 70)
print("Problem 14: LeetCode 131 - Palindrome Partitioning")
print("=" * 70)

test_cases_131 = [
    ("aab", [["a","a","b"],["aa","b"]]),
    ("a", [["a"]])
]

for s, expected in test_cases_131:
    result = partition(s)
    result.sort()
    expected.sort()
    status = "✅" if result == expected else "❌"
    print(f"s='{s}' → {result} {status}")


# ============================================================================
# PROBLEM 21: LeetCode 583 - Delete Operation for Two Strings (MEDIUM)
# ============================================================================

"""
Problem:
--------
Given two strings a and b, return the minimum number of times you should repeat 
string a so that string b is a substring of it. If it is impossible for b​​​​​​ to 
be a substring of a after repeating it, return -1.

Example 1:
Input: a = "abcd", b = "cdabcdab"
Output: 3
Explanation: We return 3 because by repeating a three times "abcdabcdabcd", b is a substring of it.

Example 2:
Input: a = "a", b = "aa"
Output: 2

Constraints:
- 1 <= a.length, b.length <= 10^4
- a and b consist of lowercase English letters
"""

def repeatedStringMatch(a, b):
    """
    Approach: Calculate Minimum Repeats
    
    Key Insight:
    - Minimum repeats needed: ceil(len(b) / len(a))
    - But might need one more repeat if b spans across boundary
    - Try minimum repeats and minimum + 1
    - If neither works, impossible
    
    Why This Works:
    - If b is substring of repeated a, it needs at least len(b)/len(a) repeats
    - Might need one extra if b starts in middle of a
    - More than that is unnecessary
    
    Algorithm:
    1. Calculate min_repeats = ceil(len(b) / len(a))
    2. Try min_repeats: check if b in a * min_repeats
    3. Try min_repeats + 1: check if b in a * (min_repeats + 1)
    4. Return repeats if found, else -1
    
    Pattern Recognition:
    - "minimum repeats" → calculate based on lengths
    - "substring" → use 'in' operator or KMP
    
    Time: O(n * m) where n = len(a) * repeats, m = len(b)
    Space: O(n) for repeated string
    """
    import math
    
    # Calculate minimum possible repeats
    min_repeats = math.ceil(len(b) / len(a))
    
    # Try minimum repeats
    if b in a * min_repeats:
        return min_repeats
    
    # Try one more repeat (in case b spans boundary)
    if b in a * (min_repeats + 1):
        return min_repeats + 1
    
    # Impossible
    return -1


# Test cases
print("\n" + "=" * 70)
print("Problem 15: LeetCode 686 - Repeated String Match")
print("=" * 70)

test_cases_686 = [
    ("abcd", "cdabcdab", 3),
    ("a", "aa", 2),
    ("a", "a", 1),
    ("abc", "cabcabca", 4)
]

for a, b, expected in test_cases_686:
    result = repeatedStringMatch(a, b)
    status = "✅" if result == expected else "❌"
    print(f"a='{a}', b='{b}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 22: LeetCode 718 - Maximum Length of Repeated Subarray (MEDIUM) ⭐
# ============================================================================

"""
Problem:
--------
Given a string s and an array of strings words, return the number of words[i] 
that is a subsequence of s.

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace"

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2

Constraints:
- 1 <= s.length <= 5 * 10^4
- 1 <= words.length <= 5000
- 1 <= words[i].length <= 50
- s and words[i] consist of only lowercase English letters
"""

def numMatchingSubseq(s, words):
    """
    Approach: Bucket + Iterator
    
    Key Insight:
    - Naive: Check each word individually O(n * m * k)
    - Optimize: Group words by their first character
    - Process s once, advance all words simultaneously
    - Use iterators to track position in each word
    
    Why This Works:
    - Instead of checking each word separately
    - Group words by next character they're waiting for
    - When we see a character in s, advance all words waiting for it
    - More efficient than checking each word independently
    
    Algorithm:
    1. Create buckets for each character a-z
    2. Put iterator for each word in bucket of its first character
    3. For each character in s:
       a. Get all words waiting for this character
       b. Advance their iterators
       c. If word complete, increment count
       d. Otherwise, put in bucket of next character
    
    Pattern Recognition:
    - "number of subsequences" → optimize with grouping
    - "multiple words" → process simultaneously
    
    Time: O(n + sum of word lengths)
    Space: O(total characters in words)
    """
    from collections import defaultdict
    
    # Create buckets for each character
    waiting = defaultdict(list)
    
    # Put each word's iterator in bucket of its first character
    for word in words:
        it = iter(word)
        waiting[next(it)].append(it)
    
    count = 0
    
    # Process each character in s
    for char in s:
        # Get all words waiting for this character
        current_waiting = waiting[char]
        waiting[char] = []
        
        for it in current_waiting:
            # Try to get next character in word
            next_char = next(it, None)
            if next_char is None:
                # Word complete
                count += 1
            else:
                # Put in bucket of next character
                waiting[next_char].append(it)
    
    return count


# Test cases
print("\n" + "=" * 70)
print("Problem 16: LeetCode 792 - Number of Matching Subsequences")
print("=" * 70)

test_cases_792 = [
    ("abcde", ["a","bb","acd","ace"], 3),
    ("dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"], 2)
]

for s, words, expected in test_cases_792:
    result = numMatchingSubseq(s, words)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', words={words} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 23: LeetCode 76 - Minimum Window Substring (HARD) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given two strings s and t, return the number of distinct subsequences of s which equals t.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation: There are 3 ways you can generate "rabbit" from s.

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of English letters
"""

def numDistinct(s, t):
    """
    Approach: Dynamic Programming (2D DP)
    
    Key Insight:
    - dp[i][j] = number of ways to form t[0...j-1] from s[0...i-1]
    - If s[i-1] == t[j-1], we can use or skip this character
    - If s[i-1] != t[j-1], we must skip this character
    
    DP Recurrence:
    - If s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
      (use this char + skip this char)
    - If s[i-1] != t[j-1]: dp[i][j] = dp[i-1][j]
      (skip this char)
    
    Base Cases:
    - dp[i][0] = 1 (empty t can be formed in 1 way)
    - dp[0][j] = 0 for j > 0 (can't form non-empty t from empty s)
    
    Pattern Recognition:
    - "count distinct subsequences" → DP
    - "number of ways" → counting DP
    
    Time: O(m * n)
    Space: O(m * n)
    """
    m, n = len(s), len(t)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty t
    for i in range(m + 1):
        dp[i][0] = 1
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 17: LeetCode 115 - Distinct Subsequences (HARD)")
print("=" * 70)

test_cases_115 = [
    ("rabbbit", "rabbit", 3),
    ("babgbag", "bag", 5)
]

for s, t, expected in test_cases_115:
    result = numDistinct(s, t)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', t='{t}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 24: LeetCode 72 - Edit Distance (HARD) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an input string s and a pattern p, implement regular expression matching 
with support for '.' and '*' where:
- '.' Matches any single character
- '*' Matches zero or more of the preceding element

Example 1:
Input: s = "aa", p = "a"
Output: false

Example 2:
Input: s = "aa", p = "a*"
Output: true

Example 3:
Input: s = "ab", p = ".*"
Output: true

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 30
- s contains only lowercase English letters
- p contains only lowercase English letters, '.', and '*'
"""

def isMatch(s, p):
    """
    Approach: Dynamic Programming (2D DP)
    
    Key Insight:
    - dp[i][j] = True if s[0...i-1] matches p[0...j-1]
    - Handle '.' and '*' specially
    - '*' can match zero or more of preceding character
    
    DP Recurrence:
    - If p[j-1] == '*':
        - Zero match: dp[i][j] = dp[i][j-2]
        - One or more match: if s[i-1] matches p[j-2], dp[i][j] = dp[i-1][j]
    - Else if s[i-1] == p[j-1] or p[j-1] == '.':
        - dp[i][j] = dp[i-1][j-1]
    
    Base Cases:
    - dp[0][0] = True (empty matches empty)
    - dp[0][j] = handle patterns like a*, a*b*, etc.
    
    Pattern Recognition:
    - "regular expression" → DP
    - "wildcards" → handle special cases
    - Classic hard DP problem
    
    Time: O(m * n)
    Space: O(m * n)
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc.
    for j in range(2, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # Zero match
                dp[i][j] = dp[i][j-2]
                # One or more match
                if s[i-1] == p[j-2] or p[j-2] == '.':
                    dp[i][j] = dp[i][j] or dp[i-1][j]
            elif s[i-1] == p[j-1] or p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 18: LeetCode 10 - Regular Expression Matching (HARD)")
print("=" * 70)

test_cases_10 = [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("mississippi", "mis*is*p*.", False)
]

for s, p, expected in test_cases_10:
    result = isMatch(s, p)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', p='{p}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 25: LeetCode 115 - Distinct Subsequences (HARD) ⭐
# ============================================================================

"""
Problem:
--------
Given an input string s and a pattern p, implement wildcard pattern matching 
with support for '?' and '*' where:
- '?' Matches any single character
- '*' Matches any sequence of characters (including the empty sequence)

Example 1:
Input: s = "aa", p = "a"
Output: false

Example 2:
Input: s = "aa", p = "*"
Output: true

Example 3:
Input: s = "cb", p = "?a"
Output: false

Constraints:
- 0 <= s.length, p.length <= 2000
- s contains only lowercase English letters
- p contains only lowercase English letters, '?' or '*'
"""

def isMatchWildcard(s, p):
    """
    Approach: Dynamic Programming (2D DP)
    
    Key Insight:
    - Similar to regex matching but simpler
    - '?' matches exactly one character
    - '*' matches zero or more characters
    - dp[i][j] = True if s[0...i-1] matches p[0...j-1]
    
    DP Recurrence:
    - If p[j-1] == '*':
        - Zero match: dp[i][j] = dp[i][j-1]
        - One or more match: dp[i][j] = dp[i-1][j]
    - Else if s[i-1] == p[j-1] or p[j-1] == '?':
        - dp[i][j] = dp[i-1][j-1]
    
    Base Cases:
    - dp[0][0] = True
    - dp[0][j] = True if p[0...j-1] is all '*'
    
    Pattern Recognition:
    - "wildcard matching" → DP
    - Simpler than regex (no preceding element for *)
    
    Time: O(m * n)
    Space: O(m * n)
    """
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case
    dp[0][0] = True
    
    # Handle leading '*'
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif s[i-1] == p[j-1] or p[j-1] == '?':
                dp[i][j] = dp[i-1][j-1]
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 19: LeetCode 44 - Wildcard Matching (HARD)")
print("=" * 70)

test_cases_44 = [
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False)
]

for s, p, expected in test_cases_44:
    result = isMatchWildcard(s, p)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', p='{p}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 26: LeetCode 10 - Regular Expression Matching (HARD) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given two strings word1 and word2, return the minimum number of steps required 
to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Example 1:
Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea"

Example 2:
Input: word1 = "leetcode", word2 = "etco"
Output: 4

Constraints:
- 1 <= word1.length, word2.length <= 500
- word1 and word2 consist of only lowercase English letters
"""

def minDeleteDistance(word1, word2):
    """
    Approach: LCS + Calculate Deletions
    
    Key Insight:
    - Find longest common subsequence (LCS)
    - Deletions needed = (len(word1) - LCS) + (len(word2) - LCS)
    - Keep LCS, delete everything else
    
    Why This Works:
    - LCS is the longest part they have in common
    - Delete characters not in LCS from both strings
    - Result: both strings become the LCS
    
    Pattern Recognition:
    - "make strings same" → find LCS
    - "delete operations" → variation of edit distance
    
    Time: O(m * n)
    Space: O(m * n)
    """
    m, n = len(word1), len(word2)
    
    # Find LCS length
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    lcs_length = dp[m][n]
    
    # Calculate deletions
    return (m - lcs_length) + (n - lcs_length)


# Test cases
print("\n" + "=" * 70)
print("Problem 20: LeetCode 583 - Delete Operation for Two Strings")
print("=" * 70)

test_cases_583 = [
    ("sea", "eat", 2),
    ("leetcode", "etco", 4)
]

for word1, word2, expected in test_cases_583:
    result = minDeleteDistance(word1, word2)
    status = "✅" if result == expected else "❌"
    print(f"word1='{word1}', word2='{word2}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 27: LeetCode 44 - Wildcard Matching (HARD) ⭐⭐
# ============================================================================

"""
Problem:
--------
Given two integer arrays nums1 and nums2, return the maximum length of a subarray 
that appears in both arrays.

Example 1:
Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
Output: 3
Explanation: The repeated subarray with maximum length is [3,2,1]

Example 2:
Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
Output: 5

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 100
"""

def findLength(nums1, nums2):
    """
    Approach: Dynamic Programming (2D DP)
    
    Key Insight:
    - dp[i][j] = length of longest common subarray ending at nums1[i-1] and nums2[j-1]
    - Different from LCS: must be contiguous (subarray not subsequence)
    - If elements match, extend previous length
    - If elements don't match, reset to 0
    
    DP Recurrence:
    - If nums1[i-1] == nums2[j-1]: dp[i][j] = 1 + dp[i-1][j-1]
    - Else: dp[i][j] = 0
    
    Track maximum value seen in entire table
    
    Pattern Recognition:
    - "longest common subarray" → DP with contiguous constraint
    - Different from LCS (subsequence)
    
    Time: O(m * n)
    Space: O(m * n)
    """
    m, n = len(nums1), len(nums2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                max_length = max(max_length, dp[i][j])
    
    return max_length


# Test cases
print("\n" + "=" * 70)
print("Problem 21: LeetCode 718 - Maximum Length of Repeated Subarray")
print("=" * 70)

test_cases_718 = [
    ([1,2,3,2,1], [3,2,1,4,7], 3),
    ([0,0,0,0,0], [0,0,0,0,0], 5)
]

for nums1, nums2, expected in test_cases_718:
    result = findLength(nums1, nums2)
    status = "✅" if result == expected else "❌"
    print(f"nums1={nums1}, nums2={nums2} → {result} (expected: {expected}) {status}")


# ============================================================================
# SUMMARY & KEY TAKEAWAYS
# ============================================================================

print("\n" + "=" * 70)
print("SUMMARY: STRING MANIPULATION & PATTERN MATCHING")
print("=" * 70)

print("""
KEY PATTERNS:
=============

1. CHARACTER FREQUENCY (Hash Map) - Problems 1, 2, 6
   - Use hash map to count character occurrences
   - Compare frequency maps for anagrams
   - Two-pass: build map, then query
   - Time: O(n), Space: O(1) for fixed charset

2. SLIDING WINDOW - Problems 3, 8, 10
   - Maintain window with specific property
   - Expand window by moving right
   - Shrink window when constraint violated
   - Track optimal window (min/max length)
   - Time: O(n), Space: O(k) for charset

3. TWO POINTERS FOR PALINDROME - Problems 3, 7, 9
   - Expand around center for palindromes
   - Check both odd and even length
   - Two pointers from opposite ends
   - Time: O(n²) for expand, O(n) for check

4. PATTERN MATCHING - Problems 4, 5
   - Subsequence: two pointers, greedy matching
   - Substring: sliding window or KMP
   - Two pointers move at different speeds
   - Time: O(n+m)

5. STRING DP - Problems 11, 12
   - Edit distance: insert/delete/replace
   - LCS: match or skip characters
   - 2D DP table for two strings
   - Time: O(m*n), Space: O(m*n) or O(n) optimized

PROBLEM IDENTIFICATION:
=======================
- "anagram" → character frequency hash map
- "palindrome" → two pointers or expand around center
- "longest substring" → sliding window
- "minimum window" → sliding window with shrinking
- "subsequence" → two pointers or DP
- "edit distance" / "LCS" → 2D DP
- "pattern matching" → KMP or two pointers

COMMON MISTAKES TO AVOID:
=========================
1. Confusing substring (contiguous) vs subsequence (order preserved)
2. Not handling empty strings in edge cases
3. Off-by-one errors in string slicing
4. Forgetting to check both odd/even palindromes
5. Not optimizing space in DP (can often use 1D)
6. Using wrong data structure (set vs map for frequencies)
7. Not considering Unicode in follow-up questions

INTERVIEW TIPS:
===============
1. Clarify: substring vs subsequence
2. Ask about character set (ASCII, Unicode, etc.)
3. Discuss trade-offs: time vs space
4. Start with brute force, then optimize
5. For DP: draw the table, identify recurrence
6. For sliding window: identify expand/shrink conditions
7. Test edge cases: empty, single char, all same

COMPLEXITY PATTERNS:
====================
- Hash map frequency: O(n) time, O(1) space (fixed charset)
- Sliding window: O(n) time, O(k) space
- Expand around center: O(n²) time, O(1) space
- Two pointers: O(n) time, O(1) space
- 2D DP: O(m*n) time, O(m*n) or O(n) space

MUST-KNOW PROBLEMS FOR FAANG:
==============================
⭐⭐⭐ LeetCode 76: Minimum Window Substring (HARDEST!)
⭐⭐⭐ LeetCode 3: Longest Substring Without Repeating
⭐⭐⭐ LeetCode 5: Longest Palindromic Substring
⭐⭐⭐ LeetCode 49: Group Anagrams
⭐⭐⭐ LeetCode 72: Edit Distance
⭐⭐ LeetCode 1143: Longest Common Subsequence
⭐⭐ LeetCode 647: Palindromic Substrings

PRACTICE PROGRESSION:
=====================
Week 1: Problems 1-5 (Easy - fundamentals)
Week 2: Problems 6-9 (Medium - core patterns)
Week 3: Problems 10-12 (Hard - advanced DP)
Week 4: Variations and company-specific problems

BY COMPANY FOCUS:
=================
Google: LC 76, LC 3, LC 5, LC 72
Meta: LC 49, LC 76, LC 3, LC 1143
Amazon: LC 3, LC 5, LC 242, LC 125
Apple: LC 242, LC 5, LC 125
Microsoft: LC 3, LC 125, LC 28

All solutions use optimal time and space complexity!
Master these patterns and you'll ace string problems in interviews! 🚀
""")

print("=" * 70)
print("END OF STRING MANIPULATION & PATTERN MATCHING SOLUTIONS")
print("=" * 70)
