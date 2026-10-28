class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        data = defaultdict(list)
        for word in strs:
            a = [0]*26
            for chr in word:
                index = ord(chr) - ord('a')
                a[index] += 1
            data[tuple(a)].append(word)

        return list(data.values())


        