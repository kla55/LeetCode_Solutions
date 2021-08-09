class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # list = []
        # for i in nums:
        #     counter = 0 
        #     copy = nums.copy()
        #     copy.remove(i)
        #     for j in copy:
        #         if i > j:
        #             counter = counter + 1
        #     list.append(counter)
        # return list
        
    # If sorted
        list = []
        num_sort = sorted(nums)
        for i in range(0,len(num_sort)):
            list.append(num_sort.index(nums[i]))
        return list