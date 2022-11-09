def palindromo(a):
    if a == a[::-1]:
        return True
    else:
        return False;
entrada = input()
for i in range (0,len(entrada)//2):
    if palindromo(entrada) and len(entrada)%2==0:
        print("IMPOSSÍVEL")
        exit()
    temp = list(entrada)
    temp[i] = temp[len(entrada)-1-i]
    test = entrada[::-1][0:(len(entrada)//2)] == entrada[0:(len(entrada)//2)]
    if palindromo("".join(temp)) or entrada[::-1][0:(len(entrada)//2)] == entrada[0:(len(entrada)//2)]:
        print("POSSÍVEL")
        exit()
print("IMPOSSÍVEL")
