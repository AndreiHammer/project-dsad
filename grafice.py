import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.colors import rgb2hex
from scikitplot.metrics import plot_silhouette
from scipy.cluster.hierarchy import dendrogram
from seaborn import scatterplot


def generare_rampa(denumire, nr_clusteri):
    cmap = cm.get_cmap(denumire, nr_clusteri)
    culori = [rgb2hex(cmap(i)) for i in range(nr_clusteri)]
    return culori


def plot_ierarhie(h, threshold, titlu, etichete):
    fig = plt.figure("Dendrograma:" + titlu, figsize=(9, 7))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    dendrogram(h, ax=ax, color_threshold=threshold,
               labels=etichete)


def histograme(t, variabila, partitie, titlu, culori):
    fig = plt.figure("Histograma. " + variabila, figsize=(9, 7))
    fig.suptitle(titlu + ". Histograma pentru nivelul de educatie " + variabila)
    clase = np.unique(partitie)
    q = len(clase)
    min_max = (t[variabila].min(), t[variabila].max())
    ax = fig.subplots(1, q, sharey=True)
    for i in range(q):
        axe = ax[i]
        axe.set_xlabel(str(clase[i]))
        axe.hist(t[partitie == clase[i]][variabila], range=min_max, rwidth=0.9, color=culori[i])


def plot_indecsi_silhouette(x, partitia, titlu, culori):
    fig = plt.figure("Silhouette:" + titlu, figsize=(10, 7))
    ax = fig.add_subplot(1, 1, 1)
    cmap = LinearSegmentedColormap.from_list("cmap", culori, len(culori))
    plot_silhouette(x, partitia, titlu, ax=ax, cmap=cmap)


def show():
    plt.show()


def plot_partitie(z, p, titlu, culori, etichete=None):
    fig = plt.figure("Scatter." + titlu, figsize=(8, 7))
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    ax.set_xlabel("Z1")
    ax.set_ylabel("Z2")
    scatterplot(x=z[:, 0], y=z[:, 1], hue=p, hue_order=np.unique(p), ax=ax, legend=True, palette=culori)
    if etichete is not None:
        for i in range(len(etichete)):
            ax.text(x=z[i, 0], y=z[i, 1], s=etichete[i])


def harta(shp, camp_legatura, t, camp_harta, titlu, culori):
    shp1 = pd.merge(shp, t, left_on=camp_legatura, right_index=True)
    f = plt.figure(titlu + "-" + camp_harta, figsize=(9, 7))
    ax = f.add_subplot(1, 1, 1)
    ax.set_title(titlu, fontdict={"fontsize": 16, "color": "b"})
    cmap = LinearSegmentedColormap.from_list("cmap", culori, len(culori))
    shp1.plot(camp_harta, cmap=cmap, ax=ax, legend=True, edgecolor='black')
