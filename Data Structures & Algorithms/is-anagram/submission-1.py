class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        

        if len(s) != len(t):
            return False

        freqS = {}
        freqT = {}

        for word in s:
            freqS[word] = freqS.get(word, 0)+1 
        for words in t:
            freqT[words] = freqT.get(words, 0)+ 1
        if freqS == freqT:
            return True
        return False 


        # return sorted(s) == sorted(t);
        # or 
        # return Counter(s) == Counter(t);  



























