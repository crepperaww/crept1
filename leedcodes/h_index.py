


#new change in local

def hIndex(citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        record=[]
        for nums in citations:
            counts=0
            for compares in citations:
                if nums <= compares:
                    counts+=1
            if counts >=nums:
                record.append(nums)
            if len(citations)==counts:
                record.append(counts)


        maxnum=max(record)
        print(maxnum)

hIndex([100])

