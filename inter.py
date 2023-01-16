import numpy as np
import warnings

warnings.filterwarnings("ignore")

def inter1d(inp):
    arr = inp
    for i in range(len(arr)):
        step = 1
        while np.isnan(arr[i]):
            i_min = i - step
            i_max = i + step
            if i_min < 0:
                i_min = 0
            arr[i] = np.nanmean(arr[i_min:i_max])
            step += 1
    return arr

def inter2d(inp):
    arr = inp
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            step = 1
            while np.isnan(arr[i][j]):
                i_min = i - step
                i_max = i + step
                j_min = j - step
                j_max = j + step
                if i_min < 0:
                    i_min = 0
                if j_min < 0:
                    j_min = 0
                arr[i][j] = np.nanmean(arr[i_min:i_max,j_min:j_max])
                step += 1
    return arr

def inter3d(inp):
    arr = inp
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            for k in range(arr.shape[2]):
                step = 1
                while np.isnan(arr[i][j][k]):
                    i_min = i - step
                    i_max = i + step
                    j_min = j - step
                    j_max = j + step
                    k_min = k - step
                    k_max = k + step
                    if i_min < 0:
                        i_min = 0
                    if j_min < 0:
                        j_min = 0
                    if k_min < 0:
                        k_min = 0
                    arr[i][j][k] = np.nanmean(arr[i_min:i_max,j_min:j_max,k_min:k_max])
                    step += 1
    return arr
