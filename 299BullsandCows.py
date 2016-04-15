

class Solution(object):
    
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        
        count = [0 for i in range(10)]
        bull = 0
        cows = 0
        for i in range(len(secret)):
            if guess[i] == secret[i]:
                bull += 1
            else:
                count[int(secret[i])] += 1
                if count[int(secret[i])] <= 0:
                    cows += 1
                count[int(guess[i])] -= 1
                if count[int(guess[i])] >= 0:
                    cows += 1
        return "%sA%sB" %(bull, cows)
            