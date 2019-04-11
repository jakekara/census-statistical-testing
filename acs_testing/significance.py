import numpy as np

class Estimate:
    
    def __init__(self, value, moe, Z=1.645):
        self.value = float(value)
        self.moe = float(moe)
        self.se = float(self.moe) / Z
        self.max = self.value + abs(self.moe)
        self.min = self.value - abs(self.moe)
        self.ci = (self.min, self.max)
        
        """ Standard Error = Margin of Error / Z

        where Z = 1.645 for 2006 and later years as well as all multiyear 
        estimates and Z = 1.65 for 2005 and earlier years."""
        
class Difference:
    
    def get_Z(self):
        num = (self.A.value - self.B.value) 
        denom = np.sqrt(
            np.power(self.A.se, 2) +\
            np.power(self.B.se, 2)
        )
        
        return num / denom
    
    def is_significant(self, thresh=1.645):
        return abs(self.Z) > 1.645
    
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.Z = self.get_Z()
