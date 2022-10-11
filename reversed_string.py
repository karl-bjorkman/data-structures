import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
print(string)
reversed_string = ""
s = stack.Stack()

# Solution here:
for char in string:
    s.push(char)

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)

string2 = "!yug looc a si lraK"
print(string2)
reversed_string2 = ""
k = stack.Stack()

# Solution #2:
for char in string2:
    k.push(char)

while not k.is_empty():
    reversed_string2 += k.pop()

print(reversed_string2)