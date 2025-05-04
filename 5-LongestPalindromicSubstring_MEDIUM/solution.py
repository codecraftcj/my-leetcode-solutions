class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_list = list(s)
        current_palindrome = ""
        for current_index,current_character in enumerate(string_list):
            first_half_list = string_list[:current_index]
            first_half_list.reverse()
            second_half_list = string_list[current_index:]
            current_palindrome_half = ""
            for index in range(len(first_half_list)+1):
                try:
                    if first_half_list[index] == second_half_list[index]:
                        current_palindrome_half+=first_half_list[index]
                    else:
                        break
                except Exception as e:

                    break

            if current_palindrome_half is not "":
                found_palindrome = current_palindrome_half[::-1] + current_palindrome_half
                if len(found_palindrome) > len(current_palindrome):
                    current_palindrome = found_palindrome

        for current_index,current_character in enumerate(string_list):
            
            first_half_list = string_list[:current_index]
            first_half_list.reverse()

            second_half_list = string_list[current_index+1:]

            current_palindrome_half = ""
            for index in range(len(first_half_list)+1):
                try:
                    if first_half_list[index] == second_half_list[index]:
                        current_palindrome_half+=first_half_list[index]
                    else:
                        break
                except Exception as e:

                    break

            if current_palindrome_half is not "":
                found_palindrome = current_palindrome_half[::-1] + current_character + current_palindrome_half
                if len(found_palindrome) > len(current_palindrome):
                    current_palindrome = found_palindrome

        if len(string_list) == 2:
            if string_list[0] != string_list[1]:
                current_palindrome = s[0]
            else:
                current_palindrome = s
        elif len(string_list) == 1:
            current_palindrome = s
        if current_palindrome == "" and len(string_list) > 0:
            current_palindrome = string_list[0]
        return current_palindrome


    