#integer division
res=27//5
print(res)
myvar =10
print(myvar)

myvar="5"
print(myvar)

#string
my_name= "Nwawel"
print(my_name)
first_letter=my_name[0]
print(first_letter)
#another way to get letters from a string with negative index

last_letter=my_name[-1]
print(last_letter)
secondLast_letter=my_name[-2]
print(secondLast_letter)
print(secondLast_letter=='e')

my_substr= my_name[0:3]
print(my_substr)
my_substr = my_name[-4:-1]
print(my_substr)

#getting a substrig with every 2 letters (the empty space is considered as a character
my_name = "Nwawel Sylvestre "
my_substr = my_name[::2]
print(my_substr)
#substring with every 3 letters
my_substr = my_name[::3]
print(my_substr)
#substring with every second value up index 7
my_substr = my_name[0:7:2]
print(my_substr)

#substring with every second value up index 9
my_substr = my_name[0:9:2]
print(my_substr)

#length of a string
print(len(my_name))
print(len(my_name[2:9]))

#concatenation
complete_name = my_name+ " Mireille "
print(complete_name)

#replication

#2 times a string
complete_name_3=3*complete_name
print(complete_name_3)
#5 times a same string
my_name_5 = 5*my_name
print(my_name_5)

#escape sequences
#new line \n

two_line_string = "go\nline"
print(two_line_string)

#tabulation \t

two_line_string = "go\tline"
print(two_line_string)

#Methods 
print(my_name.upper())
print(my_name.replace("Nwawel", "Moulong"))

print(my_name.find("waw"))#display the first index of the substring, here 1
print(my_name.find("wal")) #display -1 because not found









