                                     # Data Structure
# List 
# order , changeable , dublicates
l = ["data"]

# Tuple
# order , unchangeable , dublicates
t = ("data")

# Set
# unorder , addable/removeable , no dublicates
s = {"data"}

# Dictionaries
# unorder , changeable , no dublicates
d = {"key1":2}



                                         #list
ll = [1,2,'a']
#Access
print(ll[1])
print(ll[::-1])


my_list = [1, 2, 3]

# Add
my_list.append(4)          # Add at end
my_list.insert(1, 10)      # Add at index 1
my_list.extend([5, 6])     # Add multiple values

# Remove
my_list.remove(2)          # Remove first occurrence of 2
my_list.pop()              # Remove last item
my_list.pop(1)             # Remove item at index 1
del my_list[0]             # Delete item at index 0
my_list.clear()            # Remove all items


                                         #tuple
tt = (1,2,'a')
#Access
print(tt[1])
print(tt[:2])

# Tuples themselves can't be modified directly — must convert to list first.
my_tuple = (1, 2, 3)

# Convert to list to modify
temp = list(my_tuple)
temp.append(4)
temp.remove(2)
my_tuple = tuple(temp)     # Convert back to tuple


                                             #set
ss = {1,2,'a'}
#Access
print(2 in ss)


my_set = {1, 2, 3}

# Add
my_set.add(4)              # Add single element
my_set.update([5, 6])      # Add multiple elements

# Remove
my_set.remove(2)           # Remove item (Error if not found)
my_set.discard(10)         # Remove item (No error if not found)
my_set.pop()               # Remove random item
my_set.clear()             # Remove all


                                         #dictionarie
dd = {"1":'a',"2":'b'}
#Access
print(dd["1"])

first_item = list(dd.items())[0]
print(first_item)  # Output: ('1', 'a')
first_key = list(dd)[0]
print(first_key)  # Output: '1'
first_value = list(dd.values())[0]
print(first_value)  # Output: 'a'


my_dict = {"a": 1, "b": 2}

# Add or update
my_dict["c"] = 3           # Add new key-value
my_dict["a"] = 100         # Update existing

# Remove
my_dict.pop("b")           # Remove key 'b'
del my_dict["a"]           # Delete key 'a'
my_dict.clear()            # Remove all items

#copy
my_dict1 = my_dict.copy()