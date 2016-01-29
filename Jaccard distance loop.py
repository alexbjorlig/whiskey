import numpy, json, operator
from scipy.spatial import distance
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
np.set_printoptions(precision=5, suppress=True)

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
whiskey_caol_tuple = tuple(whiskey_dict['21']['tuple'])

#  X = np.matrix([[1, 2, 3], [3, 5, 2], [2, 4, 2]])

placeholder_list = []
for key, whiskey in whiskey_dict.items():
    placeholder_list.append(whiskey['tuple'])

X = np.matrix(placeholder_list)

Z = linkage(X, 'ward')

plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
    show_contracted=True,
)

plt.show()


'''
for number, whiskey in whiskey_dict.items():
    result_dict[whiskey['1. name']] = calculate_euclidean_distance(whiskey_bunnahabhain_tuple, tuple(whiskey['tuple']))
    print(whiskey['1. name'] + " : ", end="")
    print(calculate_euclidean_distance(whiskey_bunnahabhain_tuple, tuple(whiskey['tuple'])))




# for key, whiskey in result_dict.items():
#     # if whiskey != 0.0 and key == 'Glenglassaugh':
#     if whiskey != 0.0:
#         print((whiskey))

# for key, whiskey in whiskey_dict.items():
#     if whiskey['1. name'] == 'Glenglassaugh':
#         print(whiskey['1. name'])
#         print(whiskey['tuple'])
'''
