class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_string = strs[0]
        list_of_chars_of_first_string = list(first_string)
        character_dict = {}
        for character in list_of_chars_of_first_string:
            for string in strs:
                for string_character in list(string):
                    if character == string_character:
                        if character not in character_dict:
                            character_dict[character] = 1
                        else:
                            character_dict[character] += 1
                        print(character_dict)

        
        prefix = ""
        for matched_character in character_dict:
            if character_dict[matched_character] == len(strs):
                prefix += matched_character
            else:
                break
        return prefix
        
        