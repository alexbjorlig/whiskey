from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, inconsistent
import numpy as np



########
# Guide: https://joernhees.de/blog/2015/08/26/scipy-hierarchical-clustering-and-dendrogram-tutorial/
######
np.set_printoptions(precision=5, suppress=True)  # suppress scientific

np.random.seed(4711)  # for repeatability of this tutorial
a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])
# print(a)
a1 = np.array([[11,23],[15,52]])
a2 = np.array([[12,29],[91,95]])
print(a1)
print(a2)

print(np.concatenate((a1,a2),))

X = np.concatenate((a, b),)
# print(X)

Z = linkage(X, 'ward')

def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)

    if (max_d) and ('color_threshold' not in kwargs):
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

fancy_dendrogram(
    Z,
    truncate_mode='lastp',
    p=12,
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,
    annotate_above=10,# useful in small plots so annotations don't overlap
    max_d=16,
)
plt.show()