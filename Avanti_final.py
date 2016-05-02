# -*- coding: utf-8 -*-
"""
Created on Mon May 02 12:07:00 2016

@author: Dell_owner
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 04 21:40:57 2016

@author: Avanti
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

"HEAT TRANSFER IN OPACKED BED" 
#assumptions made to reach the following correlation:
#The solid particles are so small or have such a high thermal conductivity that no temperature gradients exist within the solid particles. This means that the solids offer a negligible resistance to heat transfer
#The resistance to heat transfer by conduction in the fluid is also negligible
#The rate of heat transfer from fluid to solid or vise versa at any point in the bed is directly proportional to the average temperature differential between them at that point
#The densities of solid and fluid and other transport properties are independent of temperature
#Furnas (1930) postulated an empirical relation for the evaluation of the heat transfer coefficient thus:
"hv = AG**0.7*T**0.3*10**(1.68ε - 3.56 ε**2)/dp**0.9"
 #DATA
"A isconstant related to bed material)"
A=0.4733
#G isgas flow rate
G= 0.1/3600
e=0.5, 
#T is avg.Temperature of air
#http://lib.dr.iastate.edu/cgi/viewcontent.cgi?article=3554&context=rtd
T= 420.15 K
e=0.5
dp=0.00001
#hv isvolumetric heat transfer coefficient on film side
hv= (A*(G**0.7)*(T**0.3)*(10**(1.68*e-(3.56*e**2))))/dp**0.9
# heat transfer within packed beds has shown that the resistance to heat flow is a property that is distributed throughout the bed rather than being concentrated at the container wall
"he is very high"
print hv