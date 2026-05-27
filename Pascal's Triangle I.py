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

Format 2: Building a Pascal's triangle of given height N
# Class containing Pascal's Triangle generation logic
class Solution:
    # Function to generate Pascal's Triangle up to numRows
    def generate(self, numRows):
        # Result list to hold all rows
        triangle = []

        # Loop for each row
        for i in range(numRows):
            # Create a row with size (i+1) and initialize all elements to 1
            row = [1] * (i + 1)

            # Fill elements from index 1 to i-1 (middle values)
            for j in range(1, i):
                # Each element = sum of two elements above it
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            # Add current row to the triangle
            triangle.append(row)

        return triangle


if __name__ == "__main__":
    obj = Solution()
    n = 5

    # Generate and print Pascal's Triangle
    result = obj.generate(n)
    for row in result:
        print(" ".join(map(str, row)))
