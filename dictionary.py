users = {"Ali":"123","Rüveyda":"456","Damla":"890"}
username = input("Kullanıcı Adı:")
password = input("Şifre: ")
if(users[username] == password):
    print("Giriş başarıyla gerçekleşti.")
else:
    print("Hatalı giriş denemesi. Lütfen tekrar deneyiniz.")
