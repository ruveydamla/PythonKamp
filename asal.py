n = int(input("sayı gir: "))
for i in range(0 , n+1):
    if i>1:
        for x in range(2,i):
            if i%x == 0:
             break
        else:
            print(i)

