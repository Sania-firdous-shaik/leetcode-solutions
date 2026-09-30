class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
                 n=len(nums)
                 l=set()
                 for i in range(n):
                         t1=nums[i]
                         for j in range(i+1,n):
                               d=set()
                               t2=nums[j]
                               for k in range(j+1,n):
                                     if target-t1-t2-nums[k] in d:
                                           l.add(tuple(sorted([t1,t2,nums[k],target-t1-t2-nums[k]])))
                                     d.add(nums[k])
                 return [list(i) for i in l]                  