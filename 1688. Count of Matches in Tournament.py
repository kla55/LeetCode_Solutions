class Solution:
    def numberOfMatches(self, n: int) -> int:
            list1 = 0
            while n>1:  
                if (n%2) == 0:
                    n = (n/2)
                    list1 = list1 + n
                    print(list1)
                elif (n%2) == 1:
                    n = floor(n/2)
                    list1 = list1 + n
                    n = n +1
                    print(list1)
            xd = int(list1)
            return xd