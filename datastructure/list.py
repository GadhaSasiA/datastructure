my_list=["apple","orange",1,3.4]
a=len(my_list)
print(a)

my_list=["apple","orange",1,3.4]
my_list.insert(1,"cherry")
print(my_list)
#add elements in specified possitions

my_list=["apple","orange",1,3.4]
my_list.append(23)
print(my_list)

new_list=[1,2,3,4,5]
new_list.extend(my_list)
print(new_list) 
#compain two lists 

new_list=[1, 2, 3, 4, 5, 'apple', 'orange', 1, 3.4, 23]
new_list.pop()
print(new_list)

new_list=[1, 2, 3, 4, 5, 'apple', 'orange', 1, 3.4, 23]
new_list.remove(2)
print(new_list)

new_list=[1, 2, 3, 4, 5, 'apple', 'orange', 1, 3.4, 23]
new_list.pop(6)
print(new_list)

new_list=[1, 2, 3, 4, 5, 'apple', 'orange', 1, 3.4, 23]
del new_list[7]
print(new_list)


