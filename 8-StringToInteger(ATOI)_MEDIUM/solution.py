class Solution:

    
    def myAtoi(self, s: str) -> int:
        clean_s = s.strip()
        signage = 1
        new_int_str = ""
        
        def isNumerical(character: str) -> bool:
            try:
                numerical_char = int(character)
                if(numerical_char or character is "0"):
                    return True
            except:
                return False

        for index,character in enumerate(list(clean_s)):
            if character == "-" and new_int_str == "":
                try:
                    if(isNumerical(list(clean_s)[index+1])):
                        signage = -1
                    else:
                        break
                except:
                    continue
            elif character == "+" and new_int_str == "":
                try:
                    if(isNumerical(list(clean_s)[index+1])):
                        signage = 1
                    else:
                        break
                except:
                    continue
            elif(isNumerical(character)):
                new_int_str+=character
            else:
                break

        if new_int_str:
            new_int =  int(new_int_str)*signage 
            if new_int > 2**31 -1:
                new_int = 2**31 -1
            elif new_int < -2**31:
                new_int = -2**31
            return new_int
        else:
            return 0



