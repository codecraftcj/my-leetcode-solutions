class Solution:
    def reverse(self, x: int) -> int:
        add_negative = False
        if(x<0):
            x=abs(x)
            add_negative = True
        new_x_list = list(str(x))
        new_x_list.reverse()
        new_x = int("".join(new_x_list))
        if add_negative:
            new_x = int("-"+str(new_x))
        if new_x <= 2**31 -1 and new_x >= -2**31:
            print(2**31 -1)
            print(new_x)
            print("---------------------")
            print(new_x <= 2**31 -1)
            print(-2**31)
            return new_x
        else:
            return 0
        