a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
n= None
m=a
if m<b :
  m=b 
elif m<c:
  m=c
if a == b == c:
    m = n
elif (a == b and a == m) or (a == c and a == m) or (b == c and b == m):
    m = n
if m==a :  
  print("le vainqueur est:a")
elif m==b:
  print("le vainqueur est :b",)
elif m==c :
  print("le vainqueur est c")
elif m== n :
  print("match null")
   