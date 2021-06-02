class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set=set(nums)
        nums_list=list(nums_set)
        nums_list.sort(reverse=True)
        print(nums_list)
        if len(nums_list) > 2:
            nums_list3 = nums_list[2]
            return nums_list3
        else:
            nums_list2 = nums_list[0]
            return nums_list2
            