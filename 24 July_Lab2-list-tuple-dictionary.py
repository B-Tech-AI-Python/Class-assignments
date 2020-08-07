#Create a list
my_list = [1, 2, 3]
print(my_list)

#%%
#Create a tuple
my_tuple=(12, 13, 14)
print(my_tuple)

#%%
#Create a dictionary
my_dictionary={"Name":"Ishani", "Age":19, "Height":160}
print(my_dictionary)

#%%
#Addition with list and tuple
l1=[1, 2, 3]
l2=[4, 5, 6]

print(l1+l2)

t1=(12, 13, 14)
t2=("Name", "Age")

print(t1+t2)

#%%
#Multiplication with list and tuple -not possible-
l1=[1, 2, 3]
l2=[4, 5, 6]

print(l1*l2)

t1=(12, 13, 14)
t2=("Name", "Age")

print(t1*t2)

#%%
#Slicing list and tuple
l1=[1, 2, 3, 4, 5, 6]
print(l1[:3])

t1=("First_Name", "Last_Name", "Age", "Height", "Gender")
print(t1[:5:2])
