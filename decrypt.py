import sys
numef, parola, numeg = sys.argv[1:]
f = open(numef, "rb")
g = open(numeg, "w")

cheie_criptare = parola
text = f.read()

for i in range(len(text)):
    text = text[:i] + chr(ord(text[i]) ^ ord(cheie_criptare[i % len(cheie_criptare)])) + text[(i + 1):]

g.write(text)
g.close()
