class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = []
        count = 0
        for num in nums:
            if num in seen:
                return [seen.index(num),count]
            needed = target-num
            seen.append(needed)
            count +=1