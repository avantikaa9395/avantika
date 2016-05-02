
from pylab import *
from scipy.integrate import odeint
import pylab
import numpy
from scipy.optimize import fsolve
T=298.0 #Room Temperature in K
P=101325 #in Pascals
Hco2=1635/55.342  #Henrys constant for CO2 in atm/(mol/dm3) 
Hch4=39200/55.342 #Henrys constant for Methane in atm/(mol/dm3) 
kla_co2=0.002 # in 1/s
kla_ch4=0.0001 # typical values from Perrys Handbook Edition 7 pg 2113 table 23-9 in 1/s
kga_wh20=0.0005 #assumed typical values in 1/s 
A=10.0 # cross sectional area in m2
L=10.0 # height of column in m
psat_H20=3290.0 # in Pa;source given below
G_ini=100.0 #initial flow rate in moles/sec  on gas side
L_ini=100.0 #initial flowrate of liquid in moles/sec
xco2i= 0.5 #mole fraction of CO2 in inlet gas
xch4i= 0.0 #mole fraction of Ch4 in inlet gas
xh20i= 0.5 #mf of h20 in inlet gas
"For the above values references are as follows:"
#http://www.engineeringtoolbox.com/water-vapor-saturation-pressure-d_599.html"
#Henry's constant and Masst transfer coeeficients are taken from Perry's Hanbook Edition 7 and 8.
#http://www.unhas.ac.id/rhiza/arsip/kuliah/Sistem-dan-Tekn-Kendali-Proses/PDF_Collections/REFERENSI/Perrys_Chemical_Engineering_Handbook.pdf
"Let us assume 100 stages between the inlet and outlet"
n=100
class column(self):
      
      P=self.P ; T=self.T ; xco2i=self.xco2i ; xch4i=self.xch4i ; xh20i=self.xh20i
      L= self.L ; A=self.A ; n=self.n ; Hco2=self.Hco2 ; Hch4= self.Hch4
      Klaco2=self.Klaco2 ; Klach4=self.Klach4 ; Kgh20=self.Kgh20
      Pco2= Hco2*xco2
      Pch4= Hch4*xch4
      Pco2g=Hco2*xco2g
      Pch4g=xch4g*Hch4
      
      
      

def absorber(c,z):
    P= 101325 
    Hco2=1635.0/55.32 
    Hch4=39200.0/55.32
    kla_co2=0.15*0.0001 
    kla_ch4=0.15*0.0001 
    kga_h20=0.00003#assumed values in 1/s that is typically observed
    A=1 
    
    psat_h20=3290# in Pa;source given below
   
    R1=kla_co2*A*((1000000.0*c[3])/(c[5]*18)-(c[0]/(c[0]+c[1]+c[2]))*P/Hco2)#CO2 
    R2=kla_ch4*A*((1000000.0*c[4])/(c[5]*18)-(c[1]/(c[0]+c[1]+c[2]))*P/Hch4)#Methane    
    R3=kga_w*A*(pwsat-(c[1]/(c[0]+c[1]+c[2]))*P)  #Water  
    
    R4=kla_co2*A*((1000000.0*c[3])/(18*c[5])-(c[0]/(c[0]+c[1]+c[2]))*P/Hco2)#CO2
    R5=kla_ch4*A*(1000000.0*c[4]/(18*c[5])-(c[1]/(c[0]+c[1]+c[2]))*P/Hch4)#Methane
    R6=kga_w*A*(pwsat-(c[1]/(c[0]+c[1]+c[2]))*P)#Water
    dcdt=[R1 R2,R3,R4,R5,R6]    
    return dcdt


def err(y):
    
    z=numpy.linspace(0,1,101)
    c=odeint(absorber,([50.0,50.0,0,y[0],y[1],y[2]]),z)
    error=[(c[100])[3],(c[100])[4],((c[100])[5]-100.0)]
    return error

y = fsolve(err,[1.0,1.0,99.0])


'Solution of ode with correct guess value'
z=numpy.linspace(0,1,101)
dcdt0=[50,50,0,y[0],y[1],y[2]]
c=odeint(varad,dcdt0,z)


pylab.figure(1)
plt.plot(z,c[:,0])
pylab.show()
plt.plot(z,c[:,1])
pylab.show()
plt.plot(z,c[:,2])
pylab.show()

pylab.figure(2)
plt.plot(z,c[:,3])
pylab.show()
plt.plot(z,c[:,4])
pylab.show()
plt.plot(z,c[:,5])
pylab.show()



   


    


       
        