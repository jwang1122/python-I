"""
calculate factorial
"""
n = 4
fact = 1
  
for i in range(1,n+1): 
    fact *= i 
      
print ("The factorial of %d is : %d." %(n, fact)) 

import math
print(math.factorial(n))