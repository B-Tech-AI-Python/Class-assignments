# squared dictionary
squares = dict()

def add(dictionary):
    
    for i in range(1,16):
        dictionary.update({i:i**2})
    
    
add(squares)

print(squares)
print()

for key, value in squares.items():
    
    print(key, ':', value)

# %% print unique values

my_dict = {1:'hello', 2:'hello', 3:'i', 4:'am', 5:'hello', 6:'excited'}

unique = list()

for value in my_dict.values():
    
    if value not in unique:
        unique.append(value)

print()
print(unique)

# %% common keys

dictionary1 = {1:1, 2:4, 3:9, 4:16, 5:25}
dictionary2 = {1:1, 3:9, 5:25}

print()

for key in dictionary1.keys():
    
    if key in dictionary2.keys():
        print(key)

# %%

prices = {'Chips': {'stock':20, 'price':10}, 'Fruit': {'stock':15, 'price':30}, 'Vegetables': {'stock':10, 'price':50}}

total = 0

for key in prices:
    
    total += prices[key]['price']*prices[key]['stock']
    

print()
for key in prices:
  
    print(key, '-- Price:', prices[key]['price'], ', Stock:',
          prices[key]['stock'])
    

print('\nThe total profit is:',total) 

# %%

inventory = {'gold': [10, 20, 30, 40], 'pouch': [],
             'backpack': [5, 1, 7, 6, 3, 9, 0, 2, 8, 4]}

inventory.update({'pocket': ['seashell', 'strange berry', 'lint']})

print()
for key, value in inventory.items():
    
    print(key, ':', value)

print()
inventory['backpack'].sort()
print(inventory['backpack'])
inventory['backpack'].pop(0)
print(inventory['backpack'])

print()
inventory['gold'].append(50)
print(inventory['gold'])

print('\n\n')
for key, value in inventory.items():
    
    print(key, ':', value)

# %%
