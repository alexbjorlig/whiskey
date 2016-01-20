import numpy

a = numpy.array((0, 1, 0, 0, 1, 0))
b = numpy.array((1, 0, 0, 1, 0, 1))

dist = numpy.linalg.norm(a-b)
print(dist)
