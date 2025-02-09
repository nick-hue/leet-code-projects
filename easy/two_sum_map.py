from typing import List 

class Solution:        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(f"{nums=}")
        print(f"{target=}")

        dic = {}
        for i, curr in enumerate(nums):
            needed = target - curr

            try:
                return i, dic[needed]
            except KeyError:
                dic.update({curr: i})


print(Solution().twoSum([2,7,11,15], 9))