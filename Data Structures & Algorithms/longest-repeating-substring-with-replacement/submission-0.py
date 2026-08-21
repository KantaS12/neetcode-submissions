class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # Basically a sliding window that counts the counts of the different letters. Take a count in the window of the distinct letters and we look at the least amount count and we switch it to the one with the most count. We also take remove a k or two or more. We then keep on sliding until we end up at the end.


        left = 0
        longest_repeating = 0
        character_dict = {}

        # contraints 1 to 100,000

        if len(s) == 1:
            return 1

        for i in range(0, len(s)):

            # We're setting the character with a count of 1 to start
            if s[i] not in character_dict:
                character_dict[s[i]] = 1

            # Add the character into dictionary
            elif s[i] in character_dict:
                character_dict[s[i]] += 1

            # Let's calcualte the window length
            window_length = i - left + 1

            # Now let's find how much characters to replace
            character_replace = window_length - max(character_dict.values())

            # If this replace is greater than k, then there is too much distinct characters!

                
            # Static so we need to re calculate it.
            while ((i - left + 1) - max(character_dict.values())) > k:
                # Remove the left count since we're "leaving it"
                character_dict[s[left]] -= 1
                    
                # Move left pointer to 1 right
                left += 1

            longest_repeating = max(i - left + 1, longest_repeating)

        return longest_repeating

            

