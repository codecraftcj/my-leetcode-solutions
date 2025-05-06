class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_value = {
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
        }
        list_s = list(s)
        current_sum = 0
        skip = False
        for index,character in enumerate(list_s):
            if skip:
                skip = False
                continue
            if(index+1 != len(list_s)):
                if(roman_to_value[character] < roman_to_value[list_s[index+1]] ):
                    current_sum += roman_to_value[list_s[index+1]] - roman_to_value[character]
                    skip = True
                else:
                    current_sum += roman_to_value[character]
            elif(skip is False):
                current_sum += roman_to_value[character]
        return current_sum

        