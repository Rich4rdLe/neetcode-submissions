class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {} # Creating dictionaries to count each letter
        countT = {}

        for i in range(len(s)): # populating dictionary for each letter count in string s and t
            countS[s[i]] = 1 + countS.get(s[i], 0) # key s[i] contains value 1 + (1 if same key found, 0 otherwise)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT