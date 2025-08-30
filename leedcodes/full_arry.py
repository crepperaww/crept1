import numpy as np
class Solution():
    def permute(self,nums):
        list_used=np.zeros([len(nums)])
        nums=np.array(nums)
        list_small=[]
        list_big=[]
        self.cycle(list_used,nums,list_small,list_big)
        print(list_big)


    def cycle(self,list_used:np.ndarray,nums:np.ndarray,list_small,list_big,number=""):
        list_used_temp=list_used.copy()
        list_small_temp=list_small.copy()
        if number!="":
            list_small_temp.append(int(number))
            list_used_temp[nums == number] = 1
        if len(list_small_temp) == len(nums):
            list_big.append(list_small_temp)
        list_now=nums[list_used_temp==0]
        for number in list_now:
            self.cycle(list_used_temp,nums,list_small_temp,list_big,number)







nums=[1,2,3]
answer=Solution()
out=answer.permute(nums)



