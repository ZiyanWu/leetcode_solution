'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashtable={}
        for i in nums:
            if hashtable.get(i)==None:
                hashtable[i]=0
            hashtable[i]=hashtable[i]+1
            if(hashtable[i]>(len(nums)/2)):
                return i