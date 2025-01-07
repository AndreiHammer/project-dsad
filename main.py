import numpy as np
import pandas as pd

from functii import nan_replace_t
from scipy.cluster.hierarchy import linkage
from geopandas import GeoDataFrame
from grafice import plot_ierarhie, show, plot_indecsi_silhouette, plot_partitie, histograme, generare_rampa, harta
from sklearn.metrics import silhouette_samples
from sklearn.decomposition import PCA
from functii import elbow
from sklearn.cluster import AgglomerativeClustering


set_date = pd.read_csv("data_in/personal_didactic_2023.csv", index_col=0, encoding='ISO-8859-1')
variabile_observate = list(set_date)[3:]

fisier_harta = "RO_NUTS2/Ro.shp"
camp_legatura = "sj"

if fisier_harta is not None:
    harta_shp = GeoDataFrame.from_file(fisier_harta)

nan_replace_t(set_date)
x = set_date[variabile_observate].values
model_pca = PCA()
z = model_pca.fit_transform(x)

metoda="ward"
h = linkage(x,metoda)
t_h = pd.DataFrame(h,columns=["Cluster 1","Cluster 2","Distanta","Frecventa"])
t_h.index.name="Numar Jonctiune"
t_h.to_csv("data_out/Ierarhie.csv")

partitii = elbow(h, 2)
tabel_partitii = pd.DataFrame(index=set_date.index)
for i in range(len(partitii)):
    k = partitii[i][0]
    threshold = partitii[i][1]
    model_hclust = AgglomerativeClustering(k,linkage=metoda)
    model_hclust.fit(x)
    p = np.array(["C"+str(v+1) for v in model_hclust.labels_])
    if i == 0:
        titlu = "Partitie optimala"
        tabel_partitii["P_Opt"] = p
        tabel_partitii["P_Opt_Silh"] = silhouette_samples(x, p)
    else:
        titlu = "Partitia din "+str(k)+" clusteri"
        tabel_partitii["P_" + str(k)] = p
        tabel_partitii["P_" + str(k) + "_Silh"] = silhouette_samples(x, p)
    culori = generare_rampa("rainbow",k)
    plot_ierarhie(h,threshold,titlu,set_date.index)
    sil_hi = silhouette_samples(x,p)
    plot_indecsi_silhouette(x,p,titlu,culori)
    plot_partitie(z,p,titlu,culori)
    for variabila in variabile_observate:
        histograme(set_date,variabila,p,titlu,culori)
        if fisier_harta is not None:
            if i == 0:
                harta(harta_shp, camp_legatura, tabel_partitii,
                      "P_Opt", "Partitia optimala", culori)
            else:
                harta(harta_shp, camp_legatura, tabel_partitii,
                      "P_" + str(k), "Partitia din " + str(k) + " clusteri", culori)
    show()
tabel_partitii.to_csv("data_out/Partitii.csv")