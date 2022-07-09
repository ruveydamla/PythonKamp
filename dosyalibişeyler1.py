with open("399393_gblık_dosya.txt", "r",encoding='utf8') as dosya:
    user=input("Kullanıcı adı: ")
    for satir in dosya.readlines():
        liste=satir.split(":")
        if liste[0]==user:
            password=int(input("Şifre: "))
            sifre=int(liste[1])
            if password==sifre:
                print("Giriş başarılıyla gerçekleşti.")
            else:
                print("Şifre yanlış. Lütfen tekrar deneyiniz.")
            break   
    else:
        print("Kullanıcı bulunamadı! Lütfen kaydolunuz.")