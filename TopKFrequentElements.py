class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict = {}
        for num in nums:
            if num_dict.get(num) is not None:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        processed_values = sorted(num_dict, key=num_dict.get, reverse=True)
        return processed_values[0:k]
        