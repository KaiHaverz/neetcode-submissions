class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 滑动窗口
        count={} # 记录当前窗口内每个字符出现的频次
        res=0 #记录最长有效窗口的长度
        l=0
        max_freq=0 #窗口内最频繁字符的出现次数

        for r in range(len(s)):
            # 将新加入的字符计入hash table
            count[s[r]]=1+count.get(s[r],0)
            max_freq=max(max_freq,count[s[r]])

            while(r-l+1)-max_freq>k:
                count[s[l]]-=1
                l+=1
            
            res=max(res,r-l+1)
        return res