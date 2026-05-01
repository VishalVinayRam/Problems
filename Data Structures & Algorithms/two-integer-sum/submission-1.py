class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num = {}
        for i in range(len(nums)):
            balance = target - nums[i]
            if hash_num.get(str(balance)) is not None:
                return [hash_num.get(str(balance)), i]
            hash_num[str(nums[i])] = i
        return []