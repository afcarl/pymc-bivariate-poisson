from __future__ import division
import numpy as np

def bivariate_poisson_like(int a, int b, float l_1, float l_2, float l_3):
    eps = 1e-3
    l_1 = max(l_1,eps)
    l_2 = max(l_2,eps)
    l_3 = max(l_3,eps)
    x = min(a,b)
    y = max(a,b)
    t_0 = l_3
    if a < b:
        t_1 = l_1
        t_2 = l_2
    else:
        t_2 = l_1
        t_1 = l_2

    p_km_km = np.exp(-t_1-t_2-t_0)
    if y == 0:
        return np.log(p_km_km)
    for k in range(1,y-x+1):
        p_km_km *= t_2/k

    if x == 0:
        return np.log(p_km_km)

    p_km_k = p_km_km * t_2 / (y-x+1)

    for k in range(1,x):
        p_k_k = t_1/k*p_km_k +t_0/k*p_km_km 
        p_k_kp = t_2/(y-x+k+1)*p_k_k +t_0/(y-x+k+1)*p_km_k
        p_km_km = p_k_k
        p_km_k = p_k_kp

    return np.log(t_1/x*p_km_k+t_0/x*p_km_km)
