from ssl import VERIFY_X509_STRICT


username = "Sude Rüveyda Damla"
liste1 = username.split()
password = "123 456 890"
liste2 = password.split()
username = input("Kullanıcı Adı: ")
password = input("Şifre: ")
if username == liste1[0] and password == liste2[0]:
    print("Giriş başarıyla gerçekleşti.")
elif username == liste1[1] and password == liste2[1]:
    print("Giriş başarıyla gerçekleşti.")
elif username == liste1[2] and password == liste2[2]:
    print("Giriş başarıyla gerçekleşti.")
else:
    print("Kullanıcı adı veya şifreniz yanlış. Lütfen tekrar deneyiniz.")