
## Example 1
def reassign(list):
    list = [0, 1]

def append(list):
    list.append(1)


list = [0]
print(list)  # Prints [0]

reassign(list)
print(list)  # Prints [0]

append(list)
print(list)  # Prints [0, 1]

## Example 2
def increment(a):
    a+=1
    return a


a = 3
print(a) #prints 3

print(increment(a)) #prints 4

print(a) #prints 3