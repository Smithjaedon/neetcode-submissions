class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bank = {}
        arr = []
        for v in nums:
            if v in bank:
                bank[v]+=1
            else:
                bank[v] = 1
        newarr = dict(sorted(bank.items(), key=lambda x: x[1], reverse=True))
        for i, v in enumerate(newarr):
            if i < k:
                arr.append(v)
        return arr
