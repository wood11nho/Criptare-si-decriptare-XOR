import sys
parola, numef, numeg = sys.argv[1:]
f = open(numef, "r")
g = open(numeg, "wb")

cheie_criptare = parola
text = f.read()

for i in range(len(text)):
    text = text[:i] + chr(ord(text[i]) ^ ord(cheie_criptare[i % len(cheie_criptare)])) + text[(i + 1):]

g.write(text)
g.close()
