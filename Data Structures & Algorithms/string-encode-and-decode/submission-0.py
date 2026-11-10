class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        # print(result)
        return result

    def decode(self, s: str) -> List[str]:
        
        result = []
        start = end = 0
        while end < len(s):
            if s[end] == "#":
                count = int(s[start:end])
                count_len = len(s[start:end])
                result.append(s[start+count_len+1:end + count + 1])
                end += count
                start = end + 1
            end += 1

        return result



