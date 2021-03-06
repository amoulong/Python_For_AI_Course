#branching
#age=int(input("Enter your age: "))
age=25
if(age>18):
    print("you can enter")
elif(age==18):
    print("go see pink floyd")
else:
    print("go see Meat Loaf")

print("move on")

#logic operators

#loops
range_data = range(5)
print(list(range_data))
range_data=range(9,41,4)
print(set(range_data))
range_data= range(8,19)
print(tuple(range_data))
print(range_data[2])

for i in range(0,len(range_data)):
    print(range_data[i],"",'\n')

for data in range_data:
    print(data, end=" ")

print('\n')
for i,x in enumerate(["A","D","F"]):
    print(i,x,sep='#', end=" ")

print('\n')

i=0
while (i<len(range_data)):
    print("(",range_data[i],")")
    i=i+1



#functions
album_rating = [12,13,11,100]
llen= len(album_rating)
print("length = ",llen)
ssum= sum(album_rating)
print("sum = ",ssum)
ssorted= sorted(album_rating)
print("sorted list ",ssorted)

def multList(l,multiplier):
    
    """
    function documentation
    multiply all the elements of the list l by the multiplier
    """
    reslist= [mult * multiplier for mult in l]
    return reslist

print(multList(album_rating,10))
print (multList(album_rating, 100))
print(5*album_rating)

#function with variable number of objects in parameter
def namesInList(*names):
    """
    put all the names in a list

    """
    retList=[]
    for name in names:
        retList.append(name)
    return retList

print(namesInList("ado","toto","fifi"))


#exception handling
def divideSmth(a,b):
    """
    the function divide b per a
    """
    c=None
    try:
        c=a/b
    except :
        print(" a could not be divided by b, check both types")
    finally:
        return c


print(divideSmth(78,"smoth"))
print(divideSmth(complex(2,10),2))
print(divideSmth(98,25))

#objects and classes
class Circle (object):
    #object is the parent class of circle
    def __init__(self, radius, color):
        #this is one of the special methods of a class
        #self refers to the newly created instance of a class
        self.radius=radius
        self.color=color

    def add_radius(self, r):
        self.radius=self.radius+r

class Rectangle(object):

    def __init__(self, color, height, width):
        self.color= color
        self.height = height
        self.width=width

redCircle= Circle(10,"red")
print (redCircle.color )
print (redCircle.radius)

#dir to get all the attributes of an object
print (dir(redCircle))