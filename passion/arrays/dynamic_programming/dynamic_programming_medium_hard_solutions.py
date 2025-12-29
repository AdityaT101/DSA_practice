"""
Dynamic Programming Solutions - Medium & Hard Problems
=====================================================
This file contains medium and hard difficulty dynamic programming problems
commonly asked in FAANG and high-frequency interview questions, supplementing
the problems in the main dynamic_programming_solutions.py file.

Each problem includes:
1. Problem statement and examples
2. Key insights for solving
3. Pattern template/approach
4. Solution with detailed explanations
5. Time and space complexity
6. Test cases with expected outputs

Note: Problems that already exist in dynamic_programming_solutions.py
(LC 5, LC 322, LC 300, LC 62) have been excluded from this file.
"""

# ============================================================================
# MEDIUM PROBLEMS - INTERMEDIATE DP CONCEPTS
# ============================================================================


# ============================================================================
# PROBLEM 1: LeetCode 139 - Word Break (MEDIUM) ⭐⭐⭐
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
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique
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
    
    Time: O(n²) - where n is length of string s
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
print("Problem 1: LeetCode 139 - Word Break")
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
# PROBLEM 2: LeetCode 152 - Maximum Product Subarray (MEDIUM) ⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an integer array nums, find a contiguous non-empty subarray within the array 
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -10 <= nums[i] <= 10
- The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

def maxProduct(nums):
    """
    Approach: Dynamic Programming with Two States
    
    Key Insight:
    - Unlike maximum sum subarray, the maximum product can be affected by negative numbers
    - A negative number can make the maximum product become the minimum and vice versa
    - Need to track both the maximum and minimum product ending at each position
    - When encountering a negative number, swap max and min products
    - Update global maximum at each step
    
    DP States:
    - max_so_far[i] = maximum product of any subarray ending at position i
    - min_so_far[i] = minimum product of any subarray ending at position i
    
    DP Recurrence:
    - If nums[i] >= 0:
      max_so_far[i] = max(nums[i], max_so_far[i-1] * nums[i])
      min_so_far[i] = min(nums[i], min_so_far[i-1] * nums[i])
    - If nums[i] < 0:
      max_so_far[i] = max(nums[i], min_so_far[i-1] * nums[i])
      min_so_far[i] = min(nums[i], max_so_far[i-1] * nums[i])
    
    Pattern Recognition:
    - Two-state DP (tracking both maximum and minimum)
    - Handling negative numbers
    - Similar to Kadane's algorithm but with product instead of sum
    
    Time: O(n) - one pass through the array
    Space: O(1) - using constant extra space with optimized implementation
    """
    if not nums:
        return 0
    
    n = len(nums)
    max_so_far = min_so_far = result = nums[0]
    
    for i in range(1, n):
        # If current number is negative, swap max and min
        # (because multiplying by negative makes max become min and vice versa)
        if nums[i] < 0:
            max_so_far, min_so_far = min_so_far, max_so_far
        
        # Update max and min product ending at current position
        max_so_far = max(nums[i], max_so_far * nums[i])
        min_so_far = min(nums[i], min_so_far * nums[i])
        
        # Update global result
        result = max(result, max_so_far)
    
    return result


# Test cases
print("\n" + "=" * 70)
print("Problem 2: LeetCode 152 - Maximum Product Subarray")
print("=" * 70)

test_cases_152 = [
    ([2, 3, -2, 4], 6),
    ([-2, 0, -1], 0),
    ([-2, 3, -4], 24),
    ([0, 2], 2),
    ([-2, -3, -1], 6)
]

for nums, expected in test_cases_152:
    result = maxProduct(nums)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums} → {result} (expected: {expected}) {status}")


# ============================================================================
# HARD PROBLEMS - ADVANCED DP CONCEPTS
# ============================================================================


# ============================================================================
# PROBLEM 3: LeetCode 10 - Regular Expression Matching (HARD) ⭐⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an input string s and a pattern p, implement regular expression matching with 
support for '.' and '*' where:
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Constraints:
- 1 <= s.length <= 20
- 1 <= p.length <= 30
- s contains only lowercase English letters.
- p contains only lowercase English letters, '.', and '*'.
- It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
"""

def isMatch(s, p):
    """
    Approach: Dynamic Programming (2D)
    
    Key Insight:
    - Define dp[i][j] = whether s[0...i-1] matches pattern p[0...j-1]
    - Base case: dp[0][0] = True (empty string matches empty pattern)
    - Handle pattern with '*' by considering cases where it matches zero times or multiple times
    - For a star pattern like 'a*', we can:
      1. Ignore it (match zero times) - check if s[0...i-1] matches p[0...j-3]
      2. Match it multiple times - check if current char in s matches pattern char and
         if previous chars match: s[0...i-2] matches p[0...j-1]
    
    DP State:
    - dp[i][j] = whether s[0...i-1] matches p[0...j-1]
    
    DP Recurrence:
    - If p[j-1] is not '*':
      dp[i][j] = dp[i-1][j-1] if s[i-1] matches p[j-1] else False
    - If p[j-1] is '*':
      dp[i][j] = dp[i][j-2] (zero occurrences) OR 
                (dp[i-1][j] if s[i-1] matches p[j-2]) (multiple occurrences)
    
    Pattern Recognition:
    - String matching with complex patterns
    - 2D DP with base cases
    - Multiple matching scenarios for special characters
    - Careful boundary conditions
    
    Time: O(m*n) where m is length of s, n is length of p
    Space: O(m*n) for the 2D DP table
    """
    m, n = len(s), len(p)
    
    # Initialize DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc. that can match empty string
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]  # '*' can match zero characters
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # '*' can match zero times or multiple times
                dp[i][j] = dp[i][j-2]  # Match zero occurrences
                
                # Check if current char in s matches the pattern char before '*'
                if p[j-2] == '.' or p[j-2] == s[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]  # Match multiple occurrences
            
            elif p[j-1] == '.' or p[j-1] == s[i-1]:
                # Current characters match
                dp[i][j] = dp[i-1][j-1]
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 3: LeetCode 10 - Regular Expression Matching")
print("=" * 70)

test_cases_10 = [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("aab", "c*a*b", True),
    ("mississippi", "mis*is*p*.", False),
    ("ab", ".*c", False),
    ("", "c*", True)
]

for s, p, expected in test_cases_10:
    result = isMatch(s, p)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', p='{p}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 4: LeetCode 72 - Edit Distance (HARD) ⭐⭐⭐⭐
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
    Approach: Dynamic Programming (2D)
    
    Key Insight:
    - Define dp[i][j] = minimum operations to convert word1[0...i-1] to word2[0...j-1]
    - For each pair of positions (i,j), we have multiple choices:
      1. If characters match, no operation needed
      2. If they don't match, we can:
         a. Replace: 1 + dp[i-1][j-1]
         b. Delete from word1: 1 + dp[i-1][j]
         c. Insert into word1: 1 + dp[i][j-1]
    - Take the minimum of these operations
    
    DP State:
    - dp[i][j] = min operations to convert word1[0...i-1] to word2[0...j-1]
    
    DP Recurrence:
    - If word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
    - Else: dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    
    Pattern Recognition:
    - String transformation problems
    - Multiple operation choices at each step
    - 2D table with base cases
    - Alignment problems (e.g., DNA sequence alignment)
    
    Time: O(m*n) where m is length of word1, n is length of word2
    Space: O(m*n) for the 2D DP table
    """
    m, n = len(word1), len(word2)
    
    # Edge cases: if one string is empty, the distance is the length of the other
    if m == 0:
        return n
    if n == 0:
        return m
    
    # Initialize DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: converting empty string to word2[0...j]
    for j in range(n + 1):
        dp[0][j] = j
    
    # Base cases: converting word1[0...i] to empty string
    for i in range(m + 1):
        dp[i][0] = i
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i-1][j-1]
            else:
                # Take minimum of three operations
                dp[i][j] = 1 + min(
                    dp[i-1][j-1],  # Replace
                    dp[i-1][j],     # Delete
                    dp[i][j-1]      # Insert
                )
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 4: LeetCode 72 - Edit Distance")
print("=" * 70)

test_cases_72 = [
    ("horse", "ros", 3),
    ("intention", "execution", 5),
    ("", "a", 1),
    ("a", "", 1),
    ("zoologicoarchaeologist", "zoogeologist", 10)
]

for word1, word2, expected in test_cases_72:
    result = minDistance(word1, word2)
    status = "✅" if result == expected else "❌"
    print(f"word1='{word1}', word2='{word2}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 5: LeetCode 44 - Wildcard Matching (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given an input string (s) and a pattern (p), implement wildcard pattern matching 
with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence of characters.

Example 3:
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Constraints:
- 0 <= s.length, p.length <= 2000
- s contains only lowercase English letters.
- p contains only lowercase English letters, '?' or '*'.
"""

def isWildcardMatch(s, p):
    """
    Approach: Dynamic Programming (2D)
    
    Key Insight:
    - Define dp[i][j] = whether s[0...i-1] matches pattern p[0...j-1]
    - For '?' in pattern, it matches exactly one character in s
    - For '*' in pattern, it can match empty sequence or any number of characters
    - When encountering '*', we have two choices:
      1. Match zero characters (ignore '*')
      2. Match current character in s, then consider '*' again for next characters
    
    DP State:
    - dp[i][j] = whether s[0...i-1] matches p[0...j-1]
    
    DP Recurrence:
    - If p[j-1] is '?': dp[i][j] = dp[i-1][j-1]
    - If p[j-1] is '*': dp[i][j] = dp[i][j-1] (match empty) OR dp[i-1][j] (match multiple)
    - If p[j-1] is a character: dp[i][j] = dp[i-1][j-1] if s[i-1] == p[j-1] else False
    
    Pattern Recognition:
    - String pattern matching
    - Handling wildcard patterns
    - 2D DP with base cases
    - Similar to regular expression matching but with simpler rules
    
    Time: O(m*n) where m is length of s, n is length of p
    Space: O(m*n) for the 2D DP table
    """
    m, n = len(s), len(p)
    
    # Optimize: remove consecutive '*' in pattern
    new_pattern = []
    for char in p:
        if not new_pattern or char != '*' or new_pattern[-1] != '*':
            new_pattern.append(char)
    p = ''.join(new_pattern)
    n = len(p)
    
    # Edge case: empty pattern matches only empty string
    if n == 0:
        return m == 0
    
    # Initialize DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns like '*', '**', etc. that can match empty string
    for j in range(1, n + 1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-1]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j-1] == '*':
                # '*' can match empty sequence or one or more characters
                dp[i][j] = dp[i][j-1] or dp[i-1][j]
            elif p[j-1] == '?' or p[j-1] == s[i-1]:
                # '?' matches any character, or characters match exactly
                dp[i][j] = dp[i-1][j-1]
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 5: LeetCode 44 - Wildcard Matching")
print("=" * 70)

test_cases_44 = [
    ("aa", "a", False),
    ("aa", "*", True),
    ("cb", "?a", False),
    ("adceb", "*a*b", True),
    ("acdcb", "a*c?b", False),
    ("", "*", True),
    ("abcdefg", "a*e?g", True)
]

for s, p, expected in test_cases_44:
    result = isWildcardMatch(s, p)
    status = "✅" if result == expected else "❌"
    print(f"s='{s}', p='{p}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 6: LeetCode 115 - Distinct Subsequences (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting 
some (can be none) of the characters without disturbing the remaining characters' 
relative positions.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation: There are 3 ways to get "rabbit" from s:
"rabbbit" -> "rabbit" (remove the first 'b')
"rabbbit" -> "rabbit" (remove the second 'b')
"rabbbit" -> "rabbit" (remove the third 'b')

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation: There are 5 ways to get "bag" from s.

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of lowercase English letters.
"""

def numDistinct(s, t):
    """
    Approach: Dynamic Programming (2D)
    
    Key Insight:
    - Define dp[i][j] = number of distinct subsequences of s[0...i-1] that equal t[0...j-1]
    - If current characters match (s[i-1] == t[j-1]), we have two choices:
      1. Include s[i-1] in the match: dp[i-1][j-1]
      2. Skip s[i-1] and look for matches earlier: dp[i-1][j]
    - If characters don't match, we can only skip s[i-1]: dp[i-1][j]
    
    DP State:
    - dp[i][j] = number of distinct subsequences of s[0...i-1] that equal t[0...j-1]
    
    DP Recurrence:
    - If s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    - Else: dp[i][j] = dp[i-1][j]
    
    Pattern Recognition:
    - Subsequence counting
    - Character matching with skipping
    - 2D DP with base cases
    - Similar pattern to sequence alignment problems
    
    Time: O(m*n) where m is length of s, n is length of t
    Space: O(m*n) for the 2D DP table
    """
    m, n = len(s), len(t)
    
    # Initialize DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base case: empty t is a subsequence of any s exactly once
    for i in range(m + 1):
        dp[i][0] = 1
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                # Current characters match, we can either:
                # 1. Include s[i-1] in match: dp[i-1][j-1]
                # 2. Skip s[i-1] and look for matches earlier: dp[i-1][j]
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                # Characters don't match, can only skip s[i-1]
                dp[i][j] = dp[i-1][j]
    
    return dp[m][n]


# Test cases
print("\n" + "=" * 70)
print("Problem 6: LeetCode 115 - Distinct Subsequences")
print("=" * 70)

test_cases_115 = [
    ("rabbbit", "rabbit", 3),
    ("babgbag", "bag", 5),
    ("abc", "abc", 1),
    ("aaaaa", "aa", 10),
    ("xslledayhxhadmctrliaxqpokyezcfhzaskeykchkmhpyjipxtsuljkwkovmvelvwxzwieeuqnjozrfwmzsylcwvsthnxujvrkszqwtglewkycikdaiocglwzukwovsghkhyidevhbgffoqkpabthmqihcfxxzdejletqjoxmwftlxfcxgxgvpperwbqvhxgsbbkmphyomtbjzdjhcrcsggleiczpbfjcgtpycpmrjnckslrwduqlccqmgrdhxolfjafmsrfdghnatexyanldrdpxvvgujsztuffoymrfteholgonuaqndinadtumnuhkboyzaqguwqijwxxszngextfcozpetyownmyneehdwqmtpjloztswmzzdzqhuoxrblppqvyvsqhnhryvqsqogpnlqfulurexdtovqpqkfxxnqykgscxaskmksivoazlducanrqxynxlgolnknnwhqevlljwwwhhryxdginbshcnkqkyxpnqswqwpfjqoxvaezlrhdgwvrlrglqwmhbpjygmitscjeltnqimgapvaahmmiasthqmnrmfnjrxrhgkorrwponopfhvgyjxyvushimizjzzwvpfwhgdlmyxyxgcvdgpdzpjhjvajekhajbhlpothcbnadkecipvlbyjmkxljjplkzwuclmgngictgkfgjtjyjnhyomtlizryxrvkghrxahoaacvpwqmkcbsozlqvljoukplazpvfrjnlmkhrgeixmapyzdqmkiumucunqqvapbjvepkoudifmekdxbmchldkstypwfgcncdycmfkjlpagjnpvmfaiyxmdcyncxaxriyzldcpgnbqbnumlvtfxhehdgsaigvkgubvxivlirgzdoxrjwgzcmcnpkluxrgbqecdvnnzbbspthuaognbmipvehoqoihyrojcksxnfwxyuaeyetbzpfbhrspibnfnkhhyozzpjiudAAiiqsuoazfenmcizizexqdptlgvuyqrmhetvpiljspnbvvmrdltcdziulsgnddsmxkldozkpahvihzdozigbcvtdhedobntksrvmvoejgzikgabrjtiymxxxmueonovhjwafgxhcibnatkyvqdilsphpmdlcurzhwhkujxxbsyraymxbiqwupxpjshwropkvrgjcenkyentykajjdzocngvqvgturxoxpmxjuoisyyvzrqbcxkpuihjdnmqmshrjxxvzhdprogoyrgkdtttsvnbixkwwxrkjawznpuupmkltoufpeurgatipxgrjyvnnwwgksutzgbdkcmfsibcxwuoluyrmveqajrxkuggerdzgclbqkdtfaegpqkdjtgtzrlaeirpsefhqepfusgltwukvlclvcvlaapbzqmsemztfvfzngyld", "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 0)
]

for s, t, expected in test_cases_115:
    result = numDistinct(s, t)
    status = "✅" if result == expected else "❌"
    print(f"s='{s[:20]}{'...' if len(s) > 20 else ''}', t='{t[:20]}{'...' if len(t) > 20 else ''}' → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 7: LeetCode 312 - Burst Balloons (HARD) ⭐⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
You are given n balloons, indexed from 0 to n-1. Each balloon is painted with a 
number on it represented by array nums. You are asked to burst all the balloons.

If you burst balloon i you will get nums[i-1] * nums[i] * nums[i+1] coins. 
If i-1 or i+1 goes out of bounds of the array, then treat it as if there is a 
balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:
Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +  3*5*8   +  1*3*8  + 1*8*1 = 167

Example 2:
Input: nums = [1,5]
Output: 10

Constraints:
- n == nums.length
- 1 <= n <= 500
- 0 <= nums[i] <= 100
"""

def maxCoins(nums):
    """
    Approach: Dynamic Programming (2D)
    
    Key Insight:
    - The order of popping balloons matters, and it's hard to decide which one to pop first
    - Instead, think in reverse: which balloon to pop LAST
    - Define dp[i][j] = maximum coins obtainable by bursting all balloons between i and j
    - For each (i,j) range, try each balloon k as the last one to burst
    - When k is the last balloon in (i,j), its neighbors are i-1 and j+1
    
    DP State:
    - dp[i][j] = maximum coins by bursting all balloons in the range [i,j]
    
    DP Recurrence:
    - dp[i][j] = max(dp[i][k-1] + dp[k+1][j] + nums[i-1]*nums[k]*nums[j+1]) for all k in [i,j]
    
    Pattern Recognition:
    - Interval DP pattern
    - Decision sequence optimization
    - Building from smaller intervals to larger ones
    - Careful boundary handling
    
    Time: O(n³) where n is the number of balloons
    Space: O(n²) for the 2D DP table
    """
    # Add virtual balloons with value 1 at the beginning and end
    nums = [1] + nums + [1]
    n = len(nums)
    
    # Initialize DP table
    dp = [[0] * n for _ in range(n)]
    
    # Fill DP table
    # len is the length of the current subarray
    for length in range(1, n - 1):
        for i in range(1, n - length):
            j = i + length - 1
            for k in range(i, j + 1):
                # Try each balloon k as the last one to burst
                dp[i][j] = max(dp[i][j], 
                              dp[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + dp[k+1][j])
    
    return dp[1][n-2]  # The answer is the max coins for the entire original array


# Test cases
print("\n" + "=" * 70)
print("Problem 7: LeetCode 312 - Burst Balloons")
print("=" * 70)

test_cases_312 = [
    ([3, 1, 5, 8], 167),
    ([1, 5], 10),
    ([3, 1, 5], 35),
    ([1], 1),
    ([9, 76, 64, 21], 116718)
]

for nums, expected in test_cases_312:
    result = maxCoins(nums)
    status = "✅" if result == expected else "❌"
    print(f"nums={nums} → {result} (expected: {expected}) {status}")


# ============================================================================
# PROBLEM 8: LeetCode 85 - Maximal Rectangle (HARD) ⭐⭐⭐⭐
# ============================================================================

"""
Problem:
--------
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle 
containing only 1's and return its area.

Example 1:
Input: matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.

Example 2:
Input: matrix = [["0"]]
Output: 0

Example 3:
Input: matrix = [["1"]]
Output: 1

Constraints:
- rows == matrix.length
- cols == matrix[i].length
- 1 <= row, cols <= 200
- matrix[i][j] is '0' or '1'.
"""

def maximalRectangle(matrix):
    """
    Approach: Dynamic Programming with Histogram
    
    Key Insight:
    - For each row, build a histogram representing the number of consecutive 1's above
    - Apply "largest rectangle in histogram" algorithm on each row
    - The largest rectangle across all rows is the answer
    - This transforms a 2D problem into multiple 1D problems
    
    DP State:
    - heights[j] = number of consecutive 1's in the current column j up to the current row
    
    Pattern Recognition:
    - Building histograms from matrix
    - Stack-based calculation for largest rectangle
    - Row-by-row processing with state carrying forward
    
    Time: O(rows * cols) - linear time for each cell
    Space: O(cols) - for the heights array and stack
    """
    if not matrix or not matrix[0]:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0
    
    for row in range(rows):
        # Update heights for current row
        for col in range(cols):
            if matrix[row][col] == '1':
                heights[col] += 1
            else:
                heights[col] = 0
        
        # Find largest rectangle in current histogram
        max_area = max(max_area, largestRectangleArea(heights))
    
    return max_area


def largestRectangleArea(heights):
    """
    Helper function: Finds largest rectangle in a histogram
    Uses stack-based approach to track potential rectangle boundaries
    
    Time: O(n) where n is the length of heights
    Space: O(n) for the stack
    """
    stack = []  # (index, height)
    max_area = 0
    
    for i, height in enumerate(heights):
        start = i
        
        # Pop higher heights and calculate area
        while stack and stack[-1][1] > height:
            index, h = stack.pop()
            max_area = max(max_area, h * (i - index))
            start = index
        
        # Push current height with earliest possible start index
        stack.append((start, height))
    
    # Process remaining heights in stack
    for i, height in stack:
        max_area = max(max_area, height * (len(heights) - i))
    
    return max_area


# Test cases
print("\n" + "=" * 70)
print("Problem 8: LeetCode 85 - Maximal Rectangle")
print("=" * 70)

test_cases_85 = [
    ([
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ], 6),
    ([["0"]], 0),
    ([["1"]], 1),
    ([
        ["1","1","1","1","1"],
        ["1","1","1","1","1"],
        ["1","1","1","1","1"]
    ], 15)
]

for matrix, expected in test_cases_85:
    result = maximalRectangle(matrix)
    status = "✅" if result == expected else "❌"
    print(f"matrix={matrix[:2]}{'...' if len(matrix) > 2 else ''} → {result} (expected: {expected}) {status}")


# ============================================================================
# CONCLUSION AND SUMMARY
# ============================================================================

"""
Dynamic Programming Pattern Summary:

1. Basic DP Patterns:
   - Linear DP (1D): Maximum Product Subarray
   - Interval DP: Burst Balloons
   - Grid DP: Maximal Rectangle
   - State-based DP: Maximum Product Subarray (two states)
   - Optimization DP: Burst Balloons (maximization)

2. Common DP Approaches:
   - Bottom-up (Tabulation): Build solutions from smaller to larger problems
   - Top-down (Memoization): Recursive with caching to avoid redundant calculations
   - Space optimization: Reduce 2D DP to 1D when only dependent on previous states

3. Problem-Solving Tips:
   - Define states clearly: What does dp[i] or dp[i][j] represent?
   - Identify recurrence relation: How to build current state from previous states?
   - Handle base cases properly: What are the smallest subproblems?
   - Consider optimizations: Can space complexity be reduced?
   - Validate with examples: Test solution against edge cases

4. Advanced DP Techniques:
   - String DP: Edit Distance, Regular Expression Matching, Wildcard Matching
   - Subsequence problems: Distinct Subsequences
   - Interval problems: Burst Balloons
   - Grid transformations: Maximal Rectangle

These patterns and techniques form the foundation for solving a wide range of 
dynamic programming problems in interviews and beyond.
"""
