# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/?envType=daily-question&envId=2023-12-12
# Maximum Product of Two Elements in an Array

# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         nums.sort(reverse=True)

#         return (nums[0]-1) * (nums[1]-1)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        
        return (max1 - 1) * (max2 - 1)