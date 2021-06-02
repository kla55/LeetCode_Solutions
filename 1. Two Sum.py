class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lista = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                print(nums[i])
                print(nums[j])
                if nums[i]+nums[j] == target:
                #     lista.append[nums[i],nums[j]]
                    return i,j