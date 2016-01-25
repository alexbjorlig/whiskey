import numpy, json, operator, collections
from scipy.spatial import distance

with open('whiskey_dict.txt') as data_file:
    whiskey_dict = json.load(data_file)


def calculate_euclidean_distance(a, b):
    """
    The purpose of this definition is to calculate the euclidean distance from two points.
    Please refer to Provost and Fawcett 146
    :param a:
    :param b:
    :return:
    """
    a_2 = numpy.array(a)
    b_2 = numpy.array(b)

    return distance.jaccard(a_2,b_2)

whiskey_bunnahabhain_tuple = tuple(whiskey_dict['20']['tuple'])  # In the book they wan't to calculate distance from bunnahabhain.

result_dict = {}
for number, whiskey in whiskey_dict.items():
    result_dict[whiskey['1. name']] = calculate_euclidean_distance(whiskey_bunnahabhain_tuple, tuple(whiskey['tuple']))
    print(whiskey['1. name'] + " : ", end="")
    print(calculate_euclidean_distance(whiskey_bunnahabhain_tuple, tuple(whiskey['tuple'])))

sorted_dict = sorted(result_dict.items(), key=operator.itemgetter(1))
print(sorted_dict)

# for key, whiskey in result_dict.items():
#     # if whiskey != 0.0 and key == 'Glenglassaugh':
#     if whiskey != 0.0:
#         print((whiskey))

# for key, whiskey in whiskey_dict.items():
#     if whiskey['1. name'] == 'Glenglassaugh':
#         print(whiskey['1. name'])
#         print(whiskey['tuple'])

