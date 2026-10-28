class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = [0] * 26

        for ch in s:
            index = ord(ch) - ord('a')
            seen[index] += 1

        for ch in t:
            index = ord(ch) - ord('a')
            if seen[index] == 0:
                return False
            seen[index] -= 1

        return True
        