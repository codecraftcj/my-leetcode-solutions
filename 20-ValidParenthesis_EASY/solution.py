class Solution:
    def isValid(self, s: str) -> bool:
        validation_dict = {
            "(":["open",")"],
            ")":["close","("],
            "{":["open","}"],
            "}":["close","{"],
            "[":["open","]"],
            "]":["close","["],
        }
        valid = True
        found_chars = []
        for index,character in enumerate(list(s)):
            if validation_dict[character][0] is "open":
                found_chars.append(character)
                continue
            elif validation_dict[character][0] is "close":
                if len(found_chars) > 0:
                    if validation_dict[character][1] != found_chars[-1]:
                        valid=False
                        break
                    else:
                        found_chars.pop()
                else:
                    valid=False
                    break
            else:
                valid = False
                break
        if len(found_chars) > 0:
            valid = False
        return valid
            