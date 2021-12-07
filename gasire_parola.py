f = open("input.txt", "r")
g = open("output", "rb")
x = f.read(1)
y = g.read(1)
text = ""
while x != "":
    text = text + chr(ord(x) ^ ord(y))
    x = f.read(1)
    y = g.read(1)
print(text)