class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t = [-float('inf'), -float('inf'), -float('inf')]
        
        for triplet in triplets:
            if (triplet[0] > target[0]) or (triplet[1] > target[1]) or (triplet[2] > target[2]):
                continue
            t = [max(t[0], triplet[0]), max(t[1], triplet[1]), max(t[2], triplet[2])]

        if t == target:
            return True
        return False