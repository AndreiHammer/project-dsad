import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype


def nan_replace_t(t: pd.DataFrame):
    for coloana in t.columns:
        if t[coloana].isna().any():
            if is_numeric_dtype(t[coloana]):
                t.fillna({coloana: t[coloana].mean()}, inplace=True)
            else:
                t.fillna({coloana: t[coloana].mode()[0]}, inplace=True)


def elbow(h: np.ndarray, nr_partitii):
    n = h.shape[0] + 1
    d = h[1:, 2] - h[:n - 2, 2]
    jonctiuni = np.flip(np.argsort(d)) + 1
    partitii = []
    for i in range(nr_partitii):
        jonctiune = jonctiuni[i]
        k = n - jonctiune
        threshold = (h[jonctiune, 2] + h[jonctiune - 1, 2]) / 2
        partitii.append((k, threshold))
    return partitii
