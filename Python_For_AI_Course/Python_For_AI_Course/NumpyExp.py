
myArr=[0,1,6]
print(myArr)
print(myArr[-1])
print(myArr[-2])
print(myArr[-3:-1])
print(myArr[0])

import numpy as np

a= np.array([4,6,6,8,12])
print(a)
print(type(a))
print(a.size) #size =5
print(a.ndim) #dimension =1
print(a.shape) #the shape = (5,) a tuple

b=np.array([4.,8.2,9,7.,9])
print(b)
print(b.dtype)#the type of data inside the array here it is float 64

#operations on numpy array

#addition and substraction
u=np.array([1,0])
v=np.array([0,1])

z=u+v #vector addition
print(z)

z=u-v #vector substraction
print(z)

z=5*u 
print(z)

u=np.array([5,4])
v=np.array([10,3])

z=u*v #vector product (elt by elt)
print(z)

z=  np.dot(u,v)  #dot product (produit scalaire)
print(z)

z=u+1 #array translation
print(z)

a=np.array([2,-4,5,9])
m=a.mean() #mean
print(m)
print(a.max())
print(a.std())

x=np.array([0.0,np.pi/2., np.pi])
print(np.sin(x))

#generate a sequence
l=np.linspace(-2,7,10)
print(l)

#plot maths functions

x=np.linspace(0,2*np.pi,1000)
y=np.sin(x)


import matplotlib.pyplot as plt
#%matplotlib inline
plt.plot(x,y)
plt.show()


#two dimensional numpy
a=[[1,2,3.0],[8,2,3.0],[10,2,0.5]]
a=np.array(a) #matrice 3x3
print(a)
print(a.ndim)
print(a.size)
print(a.shape)
print(a[0][2])
print(a[0,2])
#matrice addition
b=[[10,10,12.0],[1,1,1.0],[200,200,200]]
print(a+b)
#matrice multiplication
print(np.dot(a,b))
#multiplication elt par elt
print(a*b)
print(np.multiply(a,b))

print("----")

a=[[[1,2,3.0],[8,2,3.0],[10,2,0.5]],[[2,2,3.0],[6,2,3.0],[100,2,0.5]]]
a=np.array(a) #2 matrices 3x3
print(a)
print(a.ndim)
print(a.size)
print(a.shape)
print(a[0][1][2])
print(a[0,1,2])
