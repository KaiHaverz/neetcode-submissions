class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort() #先排序

        for i,a in enumerate(nums):
            # 如果最小的数都大于零，直接退出
            if a>0:
                break
            # 对第一个数字去重
            if i>0 and a==nums[i-1]:
                continue
        
        # 转化为twosum，定义左右指针
            l,r=i+1,len(nums)-1
            while l<r:
                threeSum=a+nums[l]+nums[r]
                if threeSum>0:
                    r-=1
                elif threeSum<0:
                    l+=1
                else:
                    # 有效三元组
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1

                    # 对左指针指向的数字去重
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    # 对右指针指向的数字去重
                    while l<r and nums[r]==nums[r+1]:
                        r-=1

        return res