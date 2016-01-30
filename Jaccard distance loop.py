import numpy as np, json, operator
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage






np.set_printoptions(precision=5, suppress=True)

with open('whiskey_dict.txt') as data_file:
    whiskey_dict = json.load(data_file)


def fancy_dendrogram(*args, **kwargs):
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

whiskey_bunnahabhain_tuple = tuple(whiskey_dict['20']['tuple'])  # In the book they wan't to calculate distance from bunnahabhain.
whiskey_caol_tuple = tuple(whiskey_dict['21']['tuple'])


whiskey_names_list = []
placeholder_list = []
for key, whiskey in whiskey_dict.items():
    placeholder_list.append(whiskey['tuple'])
    whiskey_names_list.append(key + ' ' + whiskey['1. name'])

X = np.matrix(placeholder_list)
Z = linkage(X, 'ward')



plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    # truncate_mode='lastp',
    leaf_rotation=90.,
    leaf_font_size=9.,
    show_contracted=True,
    # p=12,
    labels=tuple(whiskey_names_list),
)

plt.show()