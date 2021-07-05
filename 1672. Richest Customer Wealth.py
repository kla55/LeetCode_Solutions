class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0 
        for i in accounts:
            test =[]
            for j in i:
                test.append(j)
                a = sum(test)
                if a > richest:
                    richest = a
                else:
                    pass
        return richest