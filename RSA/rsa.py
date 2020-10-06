P = 3
Q = 7
F = (P - 1 ) * (Q - 1)
Public = P * Q
print("Вычислитьфункцию Эйлера F(n) = (P - 1)*(Q - 1)")
print("F = ", F)




#k = 0
#i = 2

def Euclid(F):
    for k in range(1, F+1):
        a = F % k
        if a != 0:
            #print(k)
            break
    return k

G = Euclid(F)
print("Public key:=",G,Public)

 
for key in range(1,F + 1):
    kol = F % key
    print(key)
    print(kol)
    if kol != 0:
        #print(key)
        break

print("Найдем d - число обратное e по модулю F")
d = G + F
PrivateKey = (d * G) % F
print("d:=",PrivateKey)
print("Private key:=",d,Public)

slovo = input("Введите слово: ")
razbi = list(slovo)
slovarik = {i: j for i, j in enumerate(razbi)}
print(slovarik)
for ke in slovarik:
    de = 9
    vo = 8
    if ke == 0:
        slovarik[0] = slovarik[de]
    elif ke == 1:
        slovarik[1] = slovarik[vo]
        print(slovarik)
print(slovarik)
#seq = 2
#a = []
#for value in len(slovo):

    #spis = a.append(value)

    #val = int(value)
    #slo = dict.fromkeys(seq,[val])
    #seq += 1
    #print(spis)



#while i < F:
#    e = Euclid(F, i)
#    if e == 1:
#        k = i
#        break
#    i+=1



#print("Выбираем значение открытого ключа К с соблюдением условий")
#print("1 < K < F(n), Ko и F(n) - взаимно простые числа (их НОД = 1)")
#print("Ko = ", Ko)


#i = 2
#while i < n:
#    if (i * k) % Fn == 1:
#        Kc = i
#        break
#    i += 1


##print("Находим Кс =", Kc)

#C = M ** k % n
#print("Шифрование: С=", C)

#Md = C** Kc % n
#print("Расшифрование: М=", Md)



