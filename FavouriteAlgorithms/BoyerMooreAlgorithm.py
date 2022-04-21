'''
Boyer-Moore Algorithm:
t:Text,p:pattern
'''
def boyermoore(t,p):
    #Preprocess:For each character in pattern p,we record its rightmost position/index in dictionary last.
    last = {}
    for i in range(len(p)):
        last[p[i]] = i
    poslist=[]
    i = 0
    while i <= (len(t)-len(p)):
        matched,j = True,len(p)-1
        while j >= 0 and matched:
            if t[i+j] != p[j]:
                matched = False
            j = j - 1
        if matched:#A match is found for pattern p, record the position and start scanning from the next index.
            poslist.append(i)
            i = i + 1
        else:
            j = j + 1
            if t[i+j] in last.keys():
                i = i + max(j-last[t[i+j]],1)
            else:
                i = i + j + 1
    return(poslist)
print(boyermoore('abcaaacabcaaadcabcdddababc','abc'))
