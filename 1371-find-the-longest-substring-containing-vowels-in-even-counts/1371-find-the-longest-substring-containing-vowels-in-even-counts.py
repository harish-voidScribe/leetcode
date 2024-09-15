class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = 'aeiou'
        state = 0
        first_occurrence = {0: -1}
        longest = 0

        for i, char in enumerate(s):
            if char in vowels:
                state ^= 1 << vowels.index(char)
            if state not in first_occurrence:
                first_occurrence[state] = i
            longest = max(longest, i - first_occurrence[state])

        return longest
