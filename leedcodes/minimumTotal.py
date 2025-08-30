import math
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        list_empty=[]
        layer_num=0
        count=math.inf
        count=self.cycle(layer_num,list_empty,count,triangle,0)
        print(count)

    def cycle(self,layer_num,list_empty,counts,triangle,index):
        count=counts
        number_this_layer=triangle[layer_num]
        length=len(triangle)
        for index_tempt,nums in enumerate(number_this_layer[index:(index+2)]):
            list_empty.append(nums)
            count_tempt = sum(list_empty)
            if len(list_empty)==length:
                if count_tempt<=count:
                    count=count_tempt
            if layer_num + 1 <length:
                index_now=index+index_tempt
                count=self.cycle(layer_num + 1, list_empty, count, triangle,index_now)
            list_empty.pop()
        return count



triangle=[[-1],[2,3],[1,-1,-3],[5,6,7,3,2]]

A=Solution()
answer=A.minimumTotal(triangle)


