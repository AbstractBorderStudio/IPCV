# IPCV

A repository created to store "Image processing and Computer Vision" course's projects.

<logo>

# Learining python and OpenCV

## First step

Python borns as a programming language that aim to be clear to read. If we take a look a comparison between c and pyhton we can understand why.

``` c
include <stdio.h>

int main() {
    // this is a comment
    printf("Hello!"\n);
    return 0;
}
```

``` python
# this is a comment
print("Hello!")
```

>As we can see we are explicitly typing only what we want and nothing more.

``` python
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


# if statement
is_on = True

if (is_on):
    print("yes")
else:
    print("no")

# while cycle
doctor = 1

while doctor <= 13:
    print(doctor)
    doctor += 1


# for cycle
iterator = ["aaaaah", 1, True]   # list

for element in iterator:    # cycles from 0 to 9
    print(str(type(element)) + "\t" + str(element))

# whit range
for element in range(0,5):    # cycles from 0 to 4
    print(element)

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

# ---
# dictionaries (key, value)
games = {"WoW": "MMORPG", "lol": "MOBA"}
print(games.keys())     # dict_keys(['WoW', 'lol'])
print(games.values())   # dict_values(['MMORPG', 'MOBA'])
print(games["WoW"])     # MMORPG
```

---