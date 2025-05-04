class Solution:
    def isPalindrome(self, x: int) -> bool:

        string_x = str(x)
        if(len(string_x)) == 1:
            return True
        
        list_of_chars = list(string_x)
        length_of_chars = len(string_x)
        middle = floor(length_of_chars/2)
        first_half = list_of_chars[:middle]
        second_half = list_of_chars[middle:]
        
        if(length_of_chars % 2 == 0):
            #even
            second_half = list_of_chars[middle:]
        else:
            second_half = list_of_chars[middle+1:]
            #odd
        second_half.reverse()

        if first_half == second_half:
            return True
        else:
            return False
        