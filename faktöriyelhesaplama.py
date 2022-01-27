sayi = int(input("Kaçın faktöriyelini hesaplayayım : "))

faktoriyel = 1

if sayi<0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
elif sayi==0:
    print("sonuç : 1")
else:
    for i in range(sayi):
        faktoriyel = faktoriyel * (i+1)
        print("sonuç : ", faktoriyel)
