# Gereksinimler:
# Giriş Sistemi:
#
# Kullanıcıdan bir şifre al ve doğrula. (Örneğin: Şifre 1234 olsun.)
# Yanlış girerse tekrar denemesini iste, üç hatalı girişte programı kapat.
# İşlem Menüsü:
#
# Kullanıcı giriş yaptıktan sonra şu seçenekleri görecek:
# 1️⃣ Bakiye Görüntüleme
# 2️⃣ Para Yatırma
# 3️⃣ Para Çekme
# 4️⃣ Çıkış
# Bakiye Yönetimi:
#
# Kullanıcının başlangıçta 1000 TL bakiyesi olsun.
# Kullanıcı para yatırabilir ve çekebilir.
# Eğer çekmek istediği miktar bakiyesinden fazlaysa işlem reddedilmeli.
# Döngü Sistemi:
#
# Kullanıcı çıkış yapana kadar menü tekrar gösterilmeli.



hata_sayisi = 0
hesap_bakiyesi = 1000
while hata_sayisi < 3:
    sifre = (input('Lütfen Şifrenizi Giriniz:'))
    print()
    if sifre == '1234':
        print('Hoşgeldiniz', end="\n\n")
        break
    else:
        hata_sayisi += 1
        if hata_sayisi < 3:
            print(f'Hatalı Şifre! Kalan hakkınız: { 3 - hata_sayisi}', end='\n\n')
        else:
            print('Çok Fazla Hatalı Giriş Yaptınız! Program kapatılıyor')
        if hata_sayisi == 3:
            exit()
while True:
    print('Lütfen Bir Seçenek Giriniz', end='\n\n')
    print('1: Bakiye Görüntüleme')
    print('2: Para Yatırma')
    print('3: Para Çekme')
    print('4: Çıkış')
    secim = int(input(':'))

    if secim == 1:
        print(f'Hesap Bakiyesi: {hesap_bakiyesi}', end='\n\n')
        print('Başka Bir işlem Yapmak İsterseniz Lütfen Seçiniz, Çıkış için 4 e basınız')
    if secim == 2:
        yatirilan = int(input('Lütfen Yatırmak İstediğiniz Tutarı Giriniz: '))
        hesap_bakiyesi += yatirilan
        print(f'Yeni Hesap Bakiyeniz: {hesap_bakiyesi}')

    if secim == 3:
        cekilen = int(input('Lütfen Çekmek İstediğiniz Tutarı Giriniz: '))
        if cekilen < hesap_bakiyesi:
            hesap_bakiyesi -= cekilen
            print(f'Yeni Hesap Bakiyeniz: {hesap_bakiyesi}')
        else:
            print('Yetersiz Bakiye')
    if secim == 4:
        exit()









