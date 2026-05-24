# Create a class to replicate the structure
class Solution:
    # Function to print the element in rth row and cth column 
    def pascalTriangleI(self, r, c):
        return self.nCr(r - 1, c - 1)
    
    # Function to calculate nCr
    def nCr(self, n, r):
        # Choose the smaller value for lesser iterations
        if r > n - r:
            r = n - r
        
        # base case
        if r == 1:
            return n
        
        res = 1  # to store the result 
        
        # Calculate nCr using iterative method avoiding overflow 
        for i in range(r):
            res = res * (n - i)
            res = res // (i + 1)
        
        return res  # return the result 
