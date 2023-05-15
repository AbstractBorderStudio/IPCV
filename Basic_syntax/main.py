# data types
first = 10
flt = 10.1 
second = "Hello"
third = """
Hello, how are
you?
"""
f = ", how are you?"

# ---
# string manipulation
second_f = second + f
print(second_f)             # Hello, how are you?
more_second = second * 4     
print(more_second)          # HelloHelloHelloHello

# ---
# if statement
is_on = True

if (is_on):
    print("yes")
else:
    print("no")

# ---
# while cycle
doctor = 1

while doctor <= 13:
    print(doctor)
    doctor += 1

# ---
# for cycle
iterator = ["aaaaah", 1, True]   # list

for element in iterator:        # cycles from 0 to 9
    print(str(type(element)) + "\t" + str(element))

# whit range
for element in range(0,5):      # cycles from 0 to 4
    print(element)              # 0 1 2 3 4

# range and step
for element in range(0,11, 2):  # cycles form 0 to 10 with a step of 2
    print(element)              # 0 2 4 6 8 10

# ---
# string formatting
var1 = "yes"
var2 = 10

comb_vars = "this is a string -> %s, while this is an int %d" %(var1, var2)
print(comb_vars)

# alt
comb_vars_2 = "this is a string -> {}, while this is an int {}".format(var1, var2)
print(comb_vars_2)

# ---
# lists
cars = ["fiat", "maserati", "lamborghini"]
numbers = [10, 77, 55]

print(cars)         # ['fiat', 'maserati', 'lamborghini']
print(cars[0:2])    # ['fiat', 'maserati']

# append a single element at the end of the list
cars.append("Renault") # ['fiat', 'maserati', 'lamborghini', 'Renault']
# allow us to append another list
numbers.extend([7,7,11]) # [10, 77, 55, 7, 7, 11]
print(cars)
print(numbers)

# we can sum two list and get their concatenation
sum_lists = ["ciao"] + [1, 2]
print(sum_lists) #['ciao', 1, 2]

# slicing operator
sum_lists_sliced = sum_lists[0:2] # return a list with element form 0 to 1
print(sum_lists_sliced) # ['ciao', 1]

sum_lists.pop(2) # remove item at index i
print(sum_lists) # ['ciao', 1]
sum_lists.remove("ciao") # removes the element "ciao"
print(sum_lists) # [1]

# ---
# dictionaries (key, value)
games = {"WoW": "MMORPG", "lol": "MOBA"}
print(games.keys())     # dict_keys(['WoW', 'lol'])
print(games.values())   # dict_values(['MMORPG', 'MOBA'])
print(games["WoW"])     # MMORPG

#---
# functions
def function(var=1):
    print(var)

function() #1