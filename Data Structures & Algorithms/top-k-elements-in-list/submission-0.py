class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurrences = defaultdict(int)
        for num in nums:
            occurrences[num] += 1

        # sort (num, count) pairs by count descending, take first k
        sorted_items = sorted(occurrences.items(), key=lambda x: x[1], reverse=True)
        return [num for num, count in sorted_items[:k]]