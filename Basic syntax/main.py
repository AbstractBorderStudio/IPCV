first = 10
second = "Hello"
third = """
Hello, how are
you?
"""
f = ", how are you?"

second_f = second + f

print(second_f)             # Hello, how are you?

more_second = second * 4     

print(more_second)          # HelloHelloHelloHello

is_on = True

if (is_on):
    print("yes")
else:
    print("no")

iterator = ["aaaaah", 1, True]   # list

for element in iterator:    # cycles from 0 to 9
    print(str(type(element)) + "\t" + str(element))

var1 = "yes"
var2 = 10

comb_vars = "this is a string -> %s, while this is an int %d" %(var1, var2)

print(comb_vars)

# alt

comb_vars_2 = "this is a string -> {}, while this is an int {}".format(var1, var2)

print(comb_vars_2)

# lists
cars = ["fiat", "maserati", "lamborghini"]
numbers = [10, 77, 55]

print(cars)         # ['fiat', 'maserati', 'lamborghini']
print(cars[0:2])    # ['fiat', 'maserati']

# dictionaries (key, value)

games = {"WoW": "MMORPG", "lol": "MOBA"}
print(games.keys())     # dict_keys(['WoW', 'lol'])
print(games.values())   # dict_values(['MMORPG', 'MOBA'])
print(games["WoW"])     # MMORPG