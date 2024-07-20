# You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

# i < j < k,
# nums[j] - nums[i] == diff, and
# nums[k] - nums[j] == diff.
# Return the number of unique arithmetic triplets.

class Solution:
    def arithmeticTriplets(self, nums, diff):
        triplets = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if [i] < [j] < [k]:
                        if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                            triplets.append((i, j, k))
        return len(triplets)


solution = Solution()

nums = [0, 1, 4, 6, 7, 10]
diff = 3

output = solution.arithmeticTriplets(nums, diff)

print(output)
