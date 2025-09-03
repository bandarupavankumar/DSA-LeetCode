from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:  # put 0 at the front
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:  # leave 1 in the middle
                mid += 1
            else:  # nums[mid] == 2 → put 2 at the end
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
