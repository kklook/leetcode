



class Solution(object):


    
    def reverseBits(self, n):

        """
        
	:type n: int
        
	:rtype: int
        
	"""


        ret = 0

        for i in range(32):

            ret = (ret << 1) ^ (n & 1)

            n = n >> 1

        return ret