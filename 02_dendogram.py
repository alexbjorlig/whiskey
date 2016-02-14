import json
import numpy as np
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

# suppress scientific float notation
np.set_printoptions(precision=5, suppress=True)

# We load the whiskey data file
with open('whiskey_dict.txt') as data_file:
    whiskey_dict = json.load(data_file)


def fancy_dendrogram(*args, **kwargs):  # This method is for future improvement.
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        plt.title('Hierarchical Clustering Dendrogram (truncated)')
        plt.xlabel('sample index or (cluster size)')
        plt.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                plt.plot(x, y, 'o', c=c)
                plt.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                             textcoords='offset points',
                             va='top', ha='center')
        if max_d:
            plt.axhline(y=max_d, c='k')
    return ddata

# Book they wan't to calculate distance, bunnahabhain.
whiskey_bunnahabhain_tuple = tuple(whiskey_dict['20']['attribute_value_list'])
whiskey_caol_tuple = tuple(whiskey_dict['21']['attribute_value_list'])


whiskey_names_list = []  # This list is to display legend data
placeholder_list = []
for key, whiskey in whiskey_dict.items():  # The following loop builds a simple list of all whiskyes
    placeholder_list.append(whiskey['attribute_value_list'])
    whiskey_names_list.append(key + ' ' + whiskey['1. name'])

#  Convert the list to a numpy matrix
#  Example... [[0 0 0 ..., 0 0 1][0 0 0 ..., 1 0 0]]
X = np.matrix(placeholder_list)

#  Convert the distance based on the Jaccard distance
#  Example... [[27.  90.  2.23607   2.]
#              [15.  74.  2.44949   2.]]
Z = linkage(X, 'ward')

plt.figure(figsize=(25, 10))  # Intiate the mat plot figure size
plt.title('Hierarchical Clustering Dendrogram')  # Set title
plt.xlabel('sample index')  # Set the x axis label
plt.ylabel('distance')  # Set the y axis label
dendrogram(  # From scipy we now use the dendrogram
    Z,
    # truncate_mode='lastp',
    leaf_rotation=90.,  # Set the rotation of the legends
    leaf_font_size=9.,  # Set the font size
    show_contracted=True,  # Display all labels
    # p=12,
    labels=tuple(whiskey_names_list),  # Set the labels to the name list.
)

#  Finally display the plot
plt.show()
