class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str_list = list(s)
        substring_list = []
        last_character = ""
        current_string = ""
        longest_string = 1
        if s == "":
            longest_string = 0
        for index,current_character in enumerate(str_list):
            if current_character not in current_string:
                current_string+=current_character
                last_character = current_character
                if index is len(str_list)-1:
                    if current_string not in substring_list:
                        substring_list.append(current_string)
                    if len(current_string) > longest_string:
                        longest_string = len(current_string)
                    if current_string[-1] is not current_character:
                        current_string = current_string[-1] + current_character
                    else:
                        current_string = current_character
            else:
                
                occurence = current_string.index(current_character)
                if current_string != "":
                    if current_string not in substring_list:
                        substring_list.append(current_string)
                    if len(current_string) > longest_string:
                        longest_string = len(current_string)
                    if current_string[-1] is not current_character:
                        current_string = current_string[occurence+1:] + current_character
                    else:
                        current_string = current_character
        return longest_string
        
