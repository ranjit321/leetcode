#approach 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq=defaultdict(int)
        for c in s:
            freq[c]+=1
        for c in t:
            freq[c]-=1
        if all(value == 0 for value in freq.values()):
            return True
        return False
