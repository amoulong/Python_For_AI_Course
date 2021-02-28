#tuples
rating= (12,3,.6)
print(rating)
tuple1= ('disco', 48,25.3)
print(type(tuple1))
print(tuple1)
#accessing elts

print( tuple1[0])
print(tuple1[2])
print(tuple1[-3])
print(tuple1[-1])

#adding tuples
tuple2= tuple1+("toto",15)
print(tuple2)
#slicing
print(tuple2[0:3])#elts from index 0 to 2 (3-1)
print(len(tuple1))
print(len(tuple2))
#sorting a tuple return a list
rating =(5,2,4,9,8,4,4,6,3,5,2)
sortedRatings= sorted(rating)
print(type(sortedRatings))
print(sortedRatings)

#nesting (tuple inside a tuple ) ou imbrication
nt = (1,2,("pop","rock"),4,(4.5,9),("disco",(4,8)))
print(nt)
print(nt[2])
print(nt[1:len(nt)-2])
print(nt[2][1])


#lists (very similar to tuples)

llist= ["Midd",4,89.5, "dd",7,5]
print(llist)
listh=llist+[14,25,[5,"fr"],"fff",6]
print(listh)
print(listh[8][0])
print(listh[8][-1])
print(listh[-3][-1])
print(listh[4:10])

#list are mutable unlike tuples
listh[3]=7899999
print(listh)
listh.extend(["pop",12])
print(listh)

listh.append("grosso")
print(listh)
listh.append([45,"bob"])
print(listh)

#deleting elts
del(listh[1])
print(listh)

#convert a string to a list
print("hard rock star".split() )
print("A,B ,C,D".split(",") )

#cloning the list a to have different references
listA=["bad",1,987]
listB=listA[:]
print(listA)
print(listB)

listB[1]=0
print(listA)
print(listB)

#not cloned, same reference
listB=listA
print(listA)
print(listB)
listB[1]=0
print(listA)
print(listB)
#print(help(list))


#dictionary

dict1={"armel":32, "lui":58, 54:98,(4,"toto"):987,"reco":[4,5,5]}

print(dict1)
print(dict1[(4,"toto")])
dict1[54]="human"
print(dict1)

#adding value 
dict1[78988]=["jhdf",87,'j',48]
print(dict1)

#deleting value
del(dict1["lui"])
print(dict1)

#checking key
print("armel"in dict1)
print(dict1.keys())
print(dict1.values())

#set (no duplicated items )

set1={"bob","lee", "moul",1,8,8,"lee"}
print(set1)

#convert a list to a set
album_list=["bob","thriller","thriller",189]
print(album_list)

list_set=set(album_list)
print(list_set)

#Operations in sets
set1.add("Ebwa")
print(set1)

set1.remove('lee')
print(set1)

print("bob" in set1)
print("lee" in set1)

#maths operations
#intersection

set_intersect= set1&list_set
print(set_intersect)

#union

#subset
print(set1.issubset(list_set))



















