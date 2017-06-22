print("Telefon Rehberi v.1.1")
rehber ={"Ali":"12345","Veli":"23456","Ayşe":"34567"}
#rehber[isim] kullanarak rehber sözlüğünde isime karşılık gelen numarayı buluyorum.
def isimbul():
    isim = input("Mamarasını Aradığınız İsmi Giriniz :")
    print("{} numarası".format(isim),rehber[isim])
#rehber[ad] = numara diyerek yeni bir eleman ekliyorum.
def kayit():
    ad = input("Adı Giriniz :")
    numara = input("Numarayı Giriniz :")
    rehber[ad] = numara
    print("Kayıt Tamamlandı :)")
# i sözlükteki her elemanın ilk kısmınnı j ise ikinci kısmını alcak ve aradaki tırnak işareti ise stringe dönüştürecek.
def listele():
    for i,j in rehber.items():
        print(i,"",j)
print("Merhabalar :) Telefon Rehberine Hoş Geldiniz.")
#Yapılan her işlemden sonra programın bitmememsi için While True döngüsü kuruyorum.
while True:
    secim = input("Ne Yapmak İstiyorsunuz ? \n (1)Numara Aramak \n (2)Kayıt Yapmak \n (3)Listele")
    if secim == "1":
        isimbul()
        #Kullanıcıdan çıkış yapmak isteyip istemediğine dair bilgi alıyorum eğer olumlu sonuç verirse break ile döngüyü kırıyorum.
        cikis = input("Çıkmak İsiyor Musunuz ? \n (1)Evet \n (2)Hayır")
        if cikis == "1":
            break
    elif secim == "2":
        kayit()
        cikis = input("Çıkmak İsiyor Musunuz ? \n (1)Evet \n (2)Hayır")
        #Kullanıcıdan çıkış yapmak isteyip istemediğine dair bilgi alıyorum eğer olumlu sonuç verirse break ile döngüyü kırıyorum.
        if cikis == "1":
            break
    elif secim == "3":
        listele()
        cikis = input("Çıkmak İsiyor Musunuz ? \n (1)Evet \n (2)Hayır")
        #Kullanıcıdan çıkış yapmak isteyip istemediğine dair bilgi alıyorum eğer olumlu sonuç verirse break ile döngüyü kırıyorum.
        if cikis == "1":
            break
