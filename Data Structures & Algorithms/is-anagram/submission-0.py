import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1_dict = collections.defaultdict(int)
        str2_dict = collections.defaultdict(int)

        for c in s:
            str1_dict[c] +=1

        for c in t:
            str2_dict[c] +=1 
            
        if str1_dict == str2_dict:
            return True

        return False