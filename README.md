# Criptare-si-decriptare-XOR

TO ENCRYPT:

python encrypt.py "parola" "input file" "output file"

TO DECRYPT:

python decrypt.py "output file" "parola" "input_recuperat file"
  
  
# Echipa noastra: Girafele
# Echipa adversa: MontBlanc
# Parola echipei adverse: S12permut0SSSS

PARTEA 1:

Pentru a afla parola adversarilor, am folosit urmatoarea gandire:

input ^ parola = output
input ^ output = input ^ ( input ^ parola ) = input ^ input ^ parola = 0 ^ parola = PAROLA

Astfel, am folosit un program in python, in care xoram fiecare caracter din input cu fiecare 
caracter din output, astfel parola va aparea in mod repetat. Stiind ca parola are intre 10 si 15 
caractere, am luat in considerare doar primele astfel de caractere, si ne-am folosit de programul
de criptare pentru a verifica daca output-ul generat este identic cu cel dat de adversari. In 
momentul in care cele 2 fisiere output erau identice, ne-am asigurat ca aceasta este parola.
