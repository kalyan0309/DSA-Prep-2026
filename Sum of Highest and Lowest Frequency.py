class Solution:
    def sumHighestAndLowestFrequency(self, nums):

        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        
        highest_freq = max(freq.values())

        lowest_freq = min(freq.values())

        return highest_freq + lowest_freq
