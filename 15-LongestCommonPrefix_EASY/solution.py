class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_string = max(strs, key=len)
        prefix = ""
        for index,character in enumerate(list(longest_string)):
            # if all strings have the same character at this index append the character to the prefix
            character_count = 0
            for string in strs:
                try:
                    if character != list(string)[index]:
                        break
                    else:
                        character_count+=1
                except:
                    break
            if character_count == len(strs):
                prefix += character
            else:
                break
            
        return prefix

        
        