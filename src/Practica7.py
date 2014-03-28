#!/usr/bin/python
import sys
Pi=3.1415926535897931159979634685441852
def aproximacion(n):
   suma=0.0
   for i in range(1,n+1):
      x_i=float(i-1.0/2)/(n)
      fx_i=4.0/(1+x_i**2)
      suma=suma + fx_i
   pi=(1.0/float(n))*suma
   return pi
if __name__ == "__main__":     
   print'Intervalo n>0:'
   n=int(sys.argv[1])
   veces = int(sys.argv[2])
   a=[]
   print'i                 PI35DT                         lista i                                 PI35DT - lista i'
   for repetir in range(1,veces+1):
     api=aproximacion(n)
     a=a+[api]
     resta=aproximacion(n) - Pi
     print'%d %1.35f | %1.35f | %1.35f' % (repetir, Pi, aproximacion(n), resta)
     n=n*2
   print a