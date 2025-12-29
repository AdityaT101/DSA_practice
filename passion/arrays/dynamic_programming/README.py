"""
Dynamic Programming Problems Categorized by Data Structure
=========================================================

This file organizes all dynamic programming problems by their primary data structure
to help you tackle similar problems together. Problems are ordered from easier to harder
within each category.
"""

# ============================================================================
# 1. ARRAY-BASED PROBLEMS (Start Here)
# ============================================================================

"""
Array-based DP problems typically involve:
- Finding optimal subsequences
- Computing maximum/minimum values across an array
- Making decisions at each array element
"""

array_problems = [
    # Easy
    {"id": "LC 53", "name": "Maximum Subarray", "difficulty": "Easy", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Find contiguous subarray with largest sum"},
    
    {"id": "LC 121", "name": "Best Time to Buy and Sell Stock", "difficulty": "Easy", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Maximum profit by buying and selling once"},
    
    {"id": "LC 122", "name": "Best Time to Buy and Sell Stock II", "difficulty": "Easy", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Maximum profit by buying and selling multiple times"},
    
    {"id": "LC 198", "name": "House Robber", "difficulty": "Easy/Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Maximum money that can be robbed without alerting adjacent houses"},
    
    {"id": "LC 213", "name": "House Robber II", "difficulty": "Medium", 
     "file": "dynamic_programming_final_problems.py", 
     "description": "House Robber with houses arranged in a circle"},
    
    {"id": "LC 300", "name": "Longest Increasing Subsequence", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Length of longest strictly increasing subsequence"},
    
    {"id": "LC 368", "name": "Largest Divisible Subset", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Find largest subset where elements are divisible by each other"},
    
    {"id": "LC 152", "name": "Maximum Product Subarray", "difficulty": "Medium", 
     "file": "dynamic_programming_medium_hard_solutions.py", 
     "description": "Find contiguous subarray with largest product"},
    
    {"id": "LC 413", "name": "Arithmetic Slices", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Count number of arithmetic subarrays"},
    
    {"id": "LC 740", "name": "Delete and Earn", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Maximum points earned by deleting numbers"},
    
    {"id": "LC 322", "name": "Coin Change", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Minimum number of coins to make up a given amount"},
    
    {"id": "LC 377", "name": "Combination Sum IV", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Number of combinations that sum to target"},
    
    {"id": "LC 416", "name": "Partition Equal Subset Sum", "difficulty": "Medium", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Whether array can be partitioned into two equal sum subsets"},
    
    {"id": "LC 494", "name": "Target Sum", "difficulty": "Medium", 
     "file": "dynamic_programming_final_problems.py", 
     "description": "Ways to assign + and - to reach a target sum"},
    
    {"id": "LC 1049", "name": "Last Stone Weight II", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Minimum possible weight after smashing stones"},
    
    {"id": "LC 309", "name": "Best Time to Buy and Sell Stock with Cooldown", "difficulty": "Medium", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Max profit from trading stocks with cooldown constraint"},
    
    {"id": "LC 718", "name": "Maximum Length of Repeated Subarray", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Find longest common subarray between two arrays"},
    
    {"id": "LC 123/188", "name": "Best Time to Buy and Sell Stock III/IV", "difficulty": "Hard", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Max profit with at most k transactions"},
    
    {"id": "LC 354", "name": "Russian Doll Envelopes", "difficulty": "Hard", 
     "file": "dynamic_programming_final_problems.py", 
     "description": "Max number of envelopes that can be nested (2D extension of LIS)"},
    
    {"id": "LC 312", "name": "Burst Balloons", "difficulty": "Hard", 
     "file": "dynamic_programming_medium_hard_solutions.py", 
     "description": "Maximum coins by bursting balloons"},
    
    {"id": "LC 1235", "name": "Maximum Profit in Job Scheduling", "difficulty": "Hard", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Maximum profit from non-overlapping jobs"},
    
    {"id": "LC 1425", "name": "Constrained Subsequence Sum", "difficulty": "Hard", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Maximum sum of subsequence with distance constraint"}
]

# ============================================================================
# 2. STRING-BASED PROBLEMS
# ============================================================================

"""
String-based DP problems typically involve:
- Substring/subsequence operations
- Pattern matching
- String transformations
"""

string_problems = [
    {"id": "LC 5", "name": "Longest Palindromic Substring", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Find the longest palindromic substring"},
    
    {"id": "LC 647", "name": "Palindromic Substrings", "difficulty": "Medium", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Count all palindromic substrings in a string"},
    
    {"id": "LC 516", "name": "Longest Palindromic Subsequence", "difficulty": "Medium", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Length of longest palindromic subsequence"},
    
    {"id": "LC 1143", "name": "Longest Common Subsequence", "difficulty": "Medium", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Length of longest common subsequence between two strings"},
    
    {"id": "LC 139", "name": "Word Break", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Determine if a string can be segmented into dictionary words"},
    
    {"id": "LC 91", "name": "Decode Ways", "difficulty": "Medium", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Count ways to decode a string of digits"},
    
    {"id": "LC 97", "name": "Interleaving String", "difficulty": "Medium", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Whether s3 is formed by interleaving s1 and s2"},
    
    {"id": "LC 583", "name": "Delete Operation for Two Strings", "difficulty": "Medium", 
     "file": "dynamic_programming_final_problems.py", 
     "description": "Min deletions to make two strings equal"},
    
    {"id": "LC 1048", "name": "Longest String Chain", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Longest chain where each word adds one letter"},
    
    {"id": "LC 72", "name": "Edit Distance", "difficulty": "Hard", 
     "file": "dynamic_programming_medium_hard_solutions.py", 
     "description": "Minimum operations to convert one string to another"},
    
    {"id": "LC 10", "name": "Regular Expression Matching", "difficulty": "Hard", 
     "file": "dynamic_programming_medium_hard_solutions.py", 
     "description": "Match string to pattern with '.' and '*' wildcards"},
    
    {"id": "LC 44", "name": "Wildcard Matching", "difficulty": "Hard", 
     "file": "dynamic_programming_medium_hard_solutions.py", 
     "description": "Match string to pattern with '?' and '*' wildcards"},
    
    {"id": "LC 115", "name": "Distinct Subsequences", "difficulty": "Hard", 
     "file": "dynamic_programming_medium_hard_solutions.py", 
     "description": "Count distinct subsequences of t in s"},
    
    {"id": "LC 32", "name": "Longest Valid Parentheses", "difficulty": "Hard", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Length of longest valid parentheses substring"}
]

# ============================================================================
# 3. MATRIX/GRID-BASED PROBLEMS
# ============================================================================

"""
Matrix/Grid-based DP problems typically involve:
- Path finding in a 2D grid
- Area/region calculation
- Cell-to-cell state transitions
"""

matrix_grid_problems = [
    {"id": "LC 62", "name": "Unique Paths", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Number of unique paths from top-left to bottom-right in a grid"},
    
    {"id": "LC 64", "name": "Minimum Path Sum", "difficulty": "Medium", 
     "file": "dynamic_programming_final_problems.py", 
     "description": "Find path with minimum sum in a grid"},
    
    {"id": "LC 120", "name": "Triangle", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Minimum path sum from top to bottom in a triangle"},
    
    {"id": "LC 221", "name": "Maximal Square", "difficulty": "Medium", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Find largest square containing only 1's in a binary matrix"},
    
    {"id": "LC 1105", "name": "Filling Bookcase Shelves", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Minimum height of bookshelf with width constraint"},
    
    {"id": "LC 85", "name": "Maximal Rectangle", "difficulty": "Hard", 
     "file": "dynamic_programming_medium_hard_solutions.py", 
     "description": "Find largest rectangle containing only 1's in a binary matrix"},
    
    {"id": "LC 174", "name": "Dungeon Game", "difficulty": "Hard", 
     "file": "dynamic_programming_final_problems.py", 
     "description": "Minimum initial health to rescue the princess"}
]

# ============================================================================
# 4. TREE/GRAPH-BASED PROBLEMS
# ============================================================================

"""
Tree/Graph-based DP problems typically involve:
- Path finding in a graph
- Tree traversal with memoization
- Substructure optimization
"""

tree_graph_problems = [
    {"id": "LC 329", "name": "Longest Increasing Path in a Matrix", "difficulty": "Hard", 
     "file": "dynamic_programming_additional_problems.py", 
     "description": "Length of longest increasing path in a matrix (treated as a graph)"},
     
    {"id": "LC 403", "name": "Frog Jump", "difficulty": "Hard", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Whether frog can cross river by jumping on stones"}
]

# ============================================================================
# 5. OTHER PROBLEMS (MATHEMATICAL/SEQUENTIAL)
# ============================================================================

"""
Other DP problems typically involve:
- Mathematical sequences
- Counting problems
- Problems not primarily based on a specific data structure
"""

other_problems = [
    {"id": "LC 70", "name": "Climbing Stairs", "difficulty": "Easy", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Count ways to climb n stairs taking 1 or 2 steps at a time"},
    
    {"id": "LC 746", "name": "Min Cost Climbing Stairs", "difficulty": "Easy", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Minimum cost to reach the top of the stairs"},
    
    {"id": "LC 279", "name": "Perfect Squares", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Least number of perfect squares that sum to n"},
    
    {"id": "LC 303", "name": "Range Sum Query - Immutable", "difficulty": "Easy", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Calculate the sum of elements between indices (prefix sum)"},
    
    {"id": "LC 338", "name": "Counting Bits", "difficulty": "Easy", 
     "file": "dynamic_programming_final_problems.py", 
     "description": "Count number of 1s in binary representation of integers"},
     
    {"id": "LC 887", "name": "Super Egg Drop", "difficulty": "Hard", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Minimum moves to find floor f with k eggs"},
     
    {"id": "LC 1359", "name": "Count All Valid Pickup and Delivery Options", "difficulty": "Hard", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Count valid pickup/delivery sequences"},
     
    {"id": "LC 983", "name": "Minimum Cost For Tickets", "difficulty": "Medium", 
     "file": "dynamic_programming_solutions.py", 
     "description": "Minimum cost of travel tickets for given days"}
]


# ============================================================================
# RECOMMENDED LEARNING PATH
# ============================================================================

"""
Recommended Learning Path:

1. Start with easy array problems:
   - LC 53 (Maximum Subarray)
   - LC 121 (Best Time to Buy and Sell Stock)
   - LC 198 (House Robber)

2. Move to medium array problems:
   - LC 300 (Longest Increasing Subsequence)
   - LC 322 (Coin Change)
   - LC 152 (Maximum Product Subarray)
   - LC 740 (Delete and Earn)
   - LC 416 (Partition Equal Subset Sum)
   - LC 413 (Arithmetic Slices)

3. Try string-based problems:
   - LC 5 (Longest Palindromic Substring)
   - LC 1143 (Longest Common Subsequence)
   - LC 91 (Decode Ways)
   - LC 647 (Palindromic Substrings)
   - LC 1048 (Longest String Chain)

4. Explore grid-based problems:
   - LC 62 (Unique Paths)
   - LC 64 (Minimum Path Sum)
   - LC 120 (Triangle)
   - LC 221 (Maximal Square)
   - LC 1105 (Filling Bookcase Shelves)

5. Tackle advanced array problems:
   - LC 309 (Buy/Sell Stock with Cooldown)
   - LC 494 (Target Sum)
   - LC 377 (Combination Sum IV)
   - LC 368 (Largest Divisible Subset)

6. Challenge yourself with hard problems:
   - LC 72 (Edit Distance)
   - LC 32 (Longest Valid Parentheses)
   - LC 85 (Maximal Rectangle)
   - LC 403 (Frog Jump)
   - LC 329 (Longest Increasing Path in a Matrix)
   - LC 887 (Super Egg Drop)
   - LC 1425 (Constrained Subsequence Sum)
   - LC 1359 (Count All Valid Pickup and Delivery Options)
"""


# Print summary statistics
def print_statistics():
    print(f"Total DP Problems: {len(array_problems) + len(string_problems) + len(matrix_grid_problems) + len(tree_graph_problems) + len(other_problems)}")
    print(f"Array-based Problems: {len(array_problems)}")
    print(f"String-based Problems: {len(string_problems)}")
    print(f"Matrix/Grid-based Problems: {len(matrix_grid_problems)}")
    print(f"Tree/Graph-based Problems: {len(tree_graph_problems)}")
    print(f"Other Problems: {len(other_problems)}")


if __name__ == "__main__":
    print_statistics()
