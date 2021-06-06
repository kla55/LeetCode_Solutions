class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        counter = 0
        lista= []
        for i in nums:
            counter = i + counter
            lista.append(counter)
        return lista