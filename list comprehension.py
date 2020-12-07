'''word='string'
my_list=[]

for letter in word:
    my_list.append(letter)
print(my_list)'''

list=[1,2,3,4,5,6,7,8,9]
print('x'*50)
list_com=[((letter**2)) for letter in list if letter in [11,18,25,36,7,8]]   # list comprehension
print(list_com)

# nested list comprehension

list_com=[((letter**2)) for letter in list if letter in [11,18,25,36,7,8]]
nested_list_com=[[((letter**2)) for letter in list if letter in [11,18,25,36,7,8]] for x in range(20)]
print(nested_list_com)

print('x'*25)

my_list_one=[]
for x in (1,2,3,4):
    for y in (5,6,7):
        my_list_one.append(x+y)
print(my_list_one)