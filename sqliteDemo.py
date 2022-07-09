import sqlite3

def listele():
    baglanti = sqlite3.connect("degiskenlerr.py/first.py")
    cursor = baglanti.execute("select FirstName,LastName from customers")

    for satir in cursor:
        print(satir[1])

    baglanti.close

listele()