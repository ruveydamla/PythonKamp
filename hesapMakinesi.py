print("1-Toplama  2-Çıkarma 3-Çarpma 4-Bölme Q veya q-Çıkış")
while True:
    islem = input("işlem seçiniz : ")
     
    if islem == "1":
     sayi1 = int(input("Sayı giriniz: "))
     sayi2 = int(input("Sayı giriniz: "))
     print("Sonuç: ", sayi1 + sayi2)
    
    elif islem == "2":
     sayi1 = int(input("Sayı giriniz: "))
     sayi2 = int(input("Sayı giriniz: "))
     print("Sonuç: ", sayi1 - sayi2)
    
    elif islem == "3":
     sayi1 = int(input("Sayı giriniz: "))
     sayi2 = int(input("Sayı giriniz: "))
     print("Sonuç: ", sayi1 * sayi2) 
    
    elif islem == "4":
     sayi1 = int(input("Sayı giriniz: "))
     sayi2 = int(input("Sayı giriniz: "))
     print("Sonuç: ", sayi1 / sayi2)
    
    elif islem == "Q" or "q":
        break

    else:
        print("YANLIŞ SEÇİM")
