class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = ""
        for s in strs:
            n = len(s)
            result += str(n) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        
        result = []
        i = 0
        while i < len(s):
            
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            word = s[j+1:j+1+length]

            result.append(word)

            i = j + length +1

        return result


