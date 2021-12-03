import sys
parola, numef, numeg = sys.argv[1:]
f = open(numef, "r")
g = open(numeg, "wb")

text = f.readline()

for i in range(len(text)):
    text = text[:i] + chr(ord(text[i]) ^ ord(parola[i % len(parola)])) + text[(i + 1):]

g.write(bytes(text, "utf-8"))
g.close()