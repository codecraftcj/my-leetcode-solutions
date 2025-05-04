class Solution(object):
    def twoSum(self, nums, target):
        
        output = []
        for index,number in enumerate(nums):
            current_num = number
            current_index = index
            if output != []:
                continue
            for inner_index,other_number in enumerate(nums):

                if inner_index == current_index:
                    continue
                current_sum = current_num + other_number
                if current_sum == target:
                    output = [current_index,inner_index]
        return output
                

        