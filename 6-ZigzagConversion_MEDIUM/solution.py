class Solution:
    def convert(self, s: str, numRows: int) -> str:
        SKIPS = numRows*2-2
        holder_matrix = [[] for _ in range(numRows)]
        bridge_count = 2*(numRows-2)
        diagonal_step_list = list(range(2,bridge_count+1,2))
        if len(diagonal_step_list) > 1:
            diagonal_step_list.reverse()
        print(bridge_count)
        print(diagonal_step_list)
        if(len(s) == 1):
            return s
        for index_order,holder_list in enumerate(holder_matrix):
            if holder_list != holder_matrix[0] or holder_list != holder_matrix[-1]:
                target_index_list = range(index_order,len(s),SKIPS)
                for target_index in target_index_list:
                    holder_list.append(list(s)[target_index])
                    print("--------")
                    print(target_index)
                    print(index_order)
                    try:
                        print(target_index+diagonal_step_list[index_order-1])
                        holder_list.append(list(s)[target_index+diagonal_step_list[index_order-1]])
                    except Exception as e:
                        print("out of bound")
                    print(target_index+2*(numRows-index_order))
                    print(holder_matrix)
            else:
                target_index_list = range(index_order,len(s),SKIPS)
                for target_index in target_index_list:
                    holder_list.append(list(s)[target_index])
        print("OUTPUT")
        print(holder_matrix)
        output_str = ""
        for holder_list in holder_matrix:
            output_str += "".join(holder_list)
        return output_str
        

            

        


            
