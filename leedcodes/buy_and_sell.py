class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        up_down=[]
        #
        for P_now_index in range(len(prices)-1):
            price_now=prices[P_now_index]
            if prices[P_now_index+1]>price_now:
                up_down.append(True)
            else:
                up_down.append(False)
        counts=0
        for up_trends in range(len(up_down)):
            if up_down[up_trends]==True:
                counts+=prices[up_trends+1]-prices[up_trends]

        print(counts)
        return counts


Item=Solution()
answer=Item.maxProfit([7,1,5,3,6,4])



