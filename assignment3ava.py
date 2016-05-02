# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 22:26:41 2016

@author: Dell_owner_Avantikaa
"""

#mass transfer in a packed column with Water and CO2, CH4,H20
#references : http://www.mpch-mainz.mpg.de/~sander/res/henry.html
import scipy
import numpy
import scipy.optimize
import matplotlib.pyplot as plt
class absorber:
    
     #input parameters
     T=298.0 #in Kelvin
     P=101325 #in Pascal
     xco2i= 0.5 #mole fraction of CO2 in inlet gas
     xch4i= 0.0
     xh20i= 0.5 #mf of h20 in inlet gas
     n= 10 #stages considered
     #Mass transfer coefficient and Hnery's constant
     Klaco2= (10**-2.6)/17.226 #Kla for co2 in s-1
     Klach4= (0.2/3600) #kla for methane in s-1
     Kgh20=2.452*(10**-6) #kga for vapourization of h20 in (mol/m3*s*Pa)
     Hco2= (1/0.00014)#henry's constant for methane in (Pa*m3/mol)
     Hch4= (1/0.00034) #henry's constant for co2 in same units as above
     xco2l= 0.0 #co2 mole fraction in liquid
     xch4l= 0.0
     xh20l= 1.0
     A= 10 #m**2
     L= 2 #height of column in meters
     #assigning class for non varying parameters
     def column(self):
          
          P=self.P ; T=self.T ; xco2i=self.xco2i ; xch4i=self.xch4i ; xh20i=self.xh20i
          H=L= self.L ; A=self.A ; n=self.n ; Hco2=self.Hco2 ; Hch4= self.Hch4
          Klaco2=self.Klaco2 ; Klach4=self.Klach4 ; Kgh20=self.Kgh20
          xco2l=self.xco2l ; xch4l= self.xch4l ; xh20ol= self.xh2ol
          Pco2= Hco2*xco2
          Pch4= Hch4*xch4
          Pco2g=Hco2*xco2g
          Pch4g=xch4g*Hch4
    #unknowns are xco2, xch4, xco2g, xch4g
          #defining Gi and Li
          def Liqfluxco2(Klaco2,Pco2,xco2 ):
              Liqfluxco2= Klaco2*((Pco2/Hco2)-xco2l)
              return Liqfluxco2
        
          def Liqfluxch4(Klach4, Pch4, xch4l):
              Liqfluxch4= Klach4*((Pch4/Hch4)-xch4l)
              return Liqfluxch4
          
          #assume Kgaco2 and Kgach4 are very high around 10,000 s-1
     Kgaco2= 10000.0 ; Kgach4= 10000.0 #s-1
     #Finding dGi/dn and dLi/dn
     
          def Gasfluxco2(Kgaco2,Pco2g):
              Gasfluxco2= Kgaco2*((Pco2g/Hco2)-xco2l)
              return Gasfluxco2
          
          def Gasfluxch4(Kgach4, Pch4g,):
              
              Gasfluxch4= kgach4*((Pch4g/Hch4)-xch4l)
              return gasfluxch4
         
         #derivatives of gas and liquid fluxes
         def derivLiqfluxco2(Liqfluxco2, n, dn=1):
             df = func((Liqfluxco2+Liqfluxco2)/2)-func(Liqfluxco2-Liqfluxco2/2)
             return dLiqfluxco2/dn
             
         def derivLiqfluxch4(Liqfluxch4, n, dn=1):
             df = func((Liqfluxch4+Liqfluxch4)/2)-func(Liqfluxch4-Liqfluxch4/2)
             return dLiqfluxch4/dn
         
         def derivGasfluxc02(Gasfluxco2, n, dn=1):
             df = func((Gasfluxco2+Gasfluxco2)/2)-func(Gasfluxco2-Gasfluxco2/2)
             return dGasfluxco2/dn
             
         def derivGasfluxch4(Gasfluxch4, n, dn=1):
             df = func((Gasfluxch4+Gasfluxch4)/2)-func(Gasfluxch4-Gasfluxch4/2)
             return dGasfluxch4/dn
          
         #forming residuals
          def F1(Gasfluxco2, xco2g,Pco2g):
              F1= Gasfluxco2n + dGasfluxco2/dn
              return F1
              
          def F2(Gasfluxch4, xch4g, Pch4g):
              F2= Gasfluxch4 + dGasfluxch4/dn
              return F2
             
          def F3(Liqfluxco2, xco2, Pco2):
              F3= Liqfluxco2 + dLiqfluxco2/dn
              return F3
              
          def F4(Liqfluxch4, xch4, Pch4):
              F4= Liqfluxch4+ dLiqfluxch4/dn
              return F4
        
        
          def P(F1, F2,F3,F4):
              P= F1 + F2 + F3 + F4                
              return P
          
          import fsolve
               
               def equations(Z):
                   xco2,xch4,xco2g,xch4g= Z
                   return(F1,F2,F3,F4)
              xco2,xch4,xco2g,xch4g= fsolve(equations, (0.1,0.1,0.1,0.0))
              print equations(xco2,xch4,xco2g,xch4g)
      

   