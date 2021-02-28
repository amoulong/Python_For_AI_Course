#branching
age=int(input("Enter your age: "))
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


