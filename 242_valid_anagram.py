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


#Approach 2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        countS, countT = {}, {}    

        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)

        for c in countS:
            if countS[c]!=countT.get(c,0):
                return False
        return True 
        
