import math
a=int(input("escriba el primer numero"))
b=int(input("escriba el segundo numero"))
c=int(input("escriba el tercer numero"))

d=(((b**2)-(4*a*c))**1/2)
if d>0:
 print("la primera solución es ", ((d)/2*a)**1/2)
 print("la segunda solución es ", (-b -(((d)/2*a)**1/2)))

else:
  if d==0:
   print("la solución es ", (-b)/2*a)
   
  else:
   if d<0:
    print("no tiene solución en numero reales")

