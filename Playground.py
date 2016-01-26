import numpy
from scipy.spatial import distance

a = numpy.array((23,2,2))
b = numpy.array((40,10,1))


dist = numpy.linalg.norm(a-b)
print(dist)
print(distance.euclidean(a,b))
print(distance.jaccard(a,b))