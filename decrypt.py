import sys
numef, parola, numeg = sys.argv[1:]
f = open(numef, "rb")
g = open(numeg, "w")

text = f.readline()

for i in range(len(text)):
    text = text[:i] + chr(ord(text[i]) ^ ord(parola[i % len(parola)])) + text[(i + 1):]
text = text.decode("utf-8")
g.write(text)
g.close()