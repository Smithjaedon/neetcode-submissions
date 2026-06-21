class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        res = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        bucket = [[] for _ in range(len(nums)+1)]
        for i, v in seen.items():
            bucket[v].append(i)
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

                

        
        
        