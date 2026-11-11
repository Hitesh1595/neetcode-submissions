class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(word.lower() for word in s if word.isalnum())
        print(s)
        r = "".join(list(reversed(s)))
        print(r)
        return s == r
        