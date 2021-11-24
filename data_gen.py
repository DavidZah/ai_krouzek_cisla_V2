import itertools

import numpy as np
import random as rdn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib._cm_listed import cmaps
from numpy import ndarray


def gen_rnd_lst(num_grups,bounds):
    oper_lst = []
    for i in range(0,num_grups):
        oper_lst.append([rdn.randrange(bounds[0],bounds[1]),rdn.randrange(bounds[0],bounds[1])])
    return oper_lst

def plt_centriods(lst):

    colors = itertools.cycle(['bo','go','ro','co','mo','yo','ko','wo'])
    lst = gen_rnd_lst(num_grups, bounds)
    for i in lst:
        plt.plot(i[0], i[1], next(colors), markersize=12, alpha = 0.4)


def gen_clusters(lst,sigma):
    data_lst = []
    for i in lst:
        data_x = ndarray.tolist(np.random.normal(i[0], sigma, 20))
        data_y = ndarray.tolist(np.random.normal(i[1], sigma, 20))
        data_lst.append([data_x,data_y])
    return data_lst

def plt_clusters(cluster_lst):
    colors = itertools.cycle(['bo', 'go', 'ro', 'co', 'mo', 'yo', 'ko', 'wo'])
    for i in cluster_lst:
        color = next(colors)
        for j in range(0,len(i)):
            plt.plot(i[0][j],i[1][j],color)



if __name__ == "__main__":
    num_grups = 5
    bounds = [0,10]
    sigma = 0.5
    print(f"Number of groups{num_grups}, size of plane is {bounds} sigma is {sigma}")

    lst = gen_rnd_lst(num_grups, bounds)
    plt_centriods(lst)

    y = gen_clusters(lst,sigma)
    plt_clusters(y)
    plt.show()
    print("to je ale kód")
