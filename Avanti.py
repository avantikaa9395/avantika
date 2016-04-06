# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 21:40:57 2016

@author: Yash
"""
import scipy
from scipy.optimize import fmin
from scipy.integrate import quad
R=8.314
T=298.0

Pa=scipy.array([1,2,4,2,2])
Pa=Pa/R/T
Ph2=scipy.array([4,4,4,2,6])
Ph2=Ph2/R/T
rate=scipy.array([0.0121,0.0123,0.0119,0.006,0.018])
def datafit(n):
    e=(rate-n[0]*Pa**n[1]*Ph2**n[2])**2
    e=sum(e)
    return e
    
[k,a,b]=fmin(datafit,[4.5,0,1])
print [k,a,b]


Xdesired=0.7
Pa0=1.0
Pb0=1.0
Q=0.02
def integral(X):
    ra=k*(Pa0/R/T*(1-X))**a*(Pb0/R/T*(1-X))**b    
    return 1/ra

W=quad(integral,0,Xdesired)
Weight=W[0]*Q*Pa0/R/T
print Weight
Dp=0.001*0.01
e=0.5
myu=0.009
p=990
d=0.229
u=Q/3.14/d/d*4.0
L=Weight/3.14/d/d*4/e/p
DP=((150*myu*(1-e)**2*u/e**3/Dp**2)+(1.75*(1-e)*p*u**2/e**3/Dp))*L
print DP





