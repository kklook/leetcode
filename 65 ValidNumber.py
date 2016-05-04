

# TELL ALOUND ME WHY PYTHON?
class Solution(object):
    
    def isNumber(self, s):
        try:
            float(s)
        except Exception:
            return False
        return True