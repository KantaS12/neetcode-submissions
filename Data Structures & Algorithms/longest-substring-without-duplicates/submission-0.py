class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        word_dict = {}
        longest_sequence = 1
        left = 0
        
        if len(s) == 0:
            return 0

        for i in range(0, len(s)):

            if s[i] not in word_dict:
                word_dict[s[i]] = 1

            elif s[i] in word_dict:
                word_dict[s[i]] += 1

            while word_dict[s[i]] > 1:
                word_dict[s[left]] -= 1
                left += 1

            size_of_window = i - left + 1
            
            if size_of_window > longest_sequence:
                longest_sequence = size_of_window

        return longest_sequence