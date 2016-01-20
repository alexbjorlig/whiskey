import numpy

a = numpy.array((1, 2, 3))
b = numpy.array((4, 5, 6))

dist = numpy.linalg.norm(a-b)
print(dist)
