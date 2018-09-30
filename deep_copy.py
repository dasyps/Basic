from copy import deepcopy

x = [ "a" , ["b", "c"]]
y = [ "c" , "d"]
z = x
y = deepcopy(x)
x[1][1] = "bla"

print(y)
print(z)
print(x)