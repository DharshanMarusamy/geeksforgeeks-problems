class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counts = 0
        max_count = [0]
        for i in nums:
            if i==1:
                counts +=1
                max_count.append(counts)
            else:
                counts =0  
        return max(max_count)



"""
You are given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]

Output: 3

Example 2:

Input: nums = [1,0,1,1,0,1]

Output: 2
"""
