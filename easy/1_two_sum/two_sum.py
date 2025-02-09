from typing import List 

class Solution:        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(f"{nums=}")
        print(f"{target=}")

        for i, num in enumerate(nums):
            for j, number in enumerate(nums[i+1:]):
                if num + number == target:
                    return nums.index(num), nums.index(number, nums.index(num)+1)
