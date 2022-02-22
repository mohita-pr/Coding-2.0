#Majority Element
#The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.\


#Approach 1 - Dictionary/Hash map. O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        for k,v in d.items():
            if v> floor(len(nums)/2):
                return k
            

#Approach 2 - Sort the list - O(nlogn)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        length = len(nums)
        return nums[length/2]
            

#Approach 3 - Moore's Voting Algorithm O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        majorityElement = 0
        for i in range(0,length):
            if count == 0:
                majorityElement = nums[i]
            if majorityElement == nums[i]:
                count+=1
            else:
                count-=1
        return majorityElement
