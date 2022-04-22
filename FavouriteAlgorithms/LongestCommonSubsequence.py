#Importing Packages
import numpy as np

def LCS(s1,s2):
    (m,n) = (len(s1),len(s2))#Storing the length of strings s1 and s2 in variables m and n
    lcs = np.zeros((m+1,n+1))#Initialising the DP table
    for c in range(n-1,-1,-1):
        for r in range(m-1,-1,-1):
            if s1[r] == s2[c]:
                lcs[r,c] = 1 + lcs[r+1,c+1]
            else:
                lcs[r,c] = max(lcs[r+1,c], lcs[r,c+1])                
    return lcs[0,0]
