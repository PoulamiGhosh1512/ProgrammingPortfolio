import math

#Calculates and returns euclidean distance between points p and q 
def distance(p, q):
  return math.sqrt(math.pow(p[0] - q[0],2) + math.pow(p[1] - q[1],2))

def minDistance(Px,Py):
  '''Px and Py contain the same set of points sorted by x and y coordinates respectively'''
  s = len(Px)
  #Base case is when Px has 2 or 3 points.
  if (s == 2):
    return distance(Px[0],Px[1])
  elif (s == 3):
    return min(distance(Px[0],Px[1]), distance(Px[1],Px[2]), distance(Px[2],Px[0]))

  #When there are more than 3 points
  m = s//2 #Median
  Qx,Rx = Px[:m],Px[m:] #Dividing Px into Qx and Rx with respect to the x-coordinate of median
  xR = Rx[0][0]#minimum value of s in Rx
  
  Qy,Ry=[],[]
  #Divide Py into Qy and Ry with respect to xR. Resulting Py and Qy will be automatically sorted with respect to y value.
  for p in Py:
    if(p[0] < xR):
      Qy.append(p)
    else:
      Ry.append(p)

  delta = min(minDistance(Qx, Qy), minDistance(Rx, Ry))

  #Constructing Sy with all points within the delta band lying on either sides of the separator
  Sy = []
  for p in Py:
    if abs(p[0]-xR) <= delta:
      Sy.append(p)
    
  sizeS = len(Sy)
  if sizeS > 1:
      minS = distance(Sy[0], Sy[1])
      for i in range(1, sizeS-1):
          for j in range(i, min(i+15, sizeS)-1):
              minS = min(minS, distance(Sy[i], Sy[j+1]))
      return min(delta, minS)
  else:
      return delta

def minimumDistance(Points):
  Px = sorted(Points) #Points sorted by x
  Py = Points
  Py.sort(key=lambda x: x[-1]) #Points sorted by y
  return minDistance(Px, Py)

