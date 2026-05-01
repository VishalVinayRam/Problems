class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        max_occurent = counter.most_common(k)
        result = []
        for item, val in max_occurent:
            result.append(item)
        return result
