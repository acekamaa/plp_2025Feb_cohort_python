#creating an empty list
my_list = []

#append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#print list
print(my_list)

#insert at index(1)
my_list.insert(1, 15)
print("added value 15 at second position: " , my_list)

#list 2
other_list = [50, 60, 70]
print("My second list:" , other_list)

#extend list
my_list.extend(other_list)
print("Extended list: " , my_list)

#remove element at last index
my_list.pop()
print("Removed last element: " , my_list)

#sort in asc
my_list.sort()
print("Sorted list: " , my_list)

#find index of element 30
index = my_list.index(30)
print("Index of 30: " , index)