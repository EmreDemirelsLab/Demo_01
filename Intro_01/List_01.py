# Kullanıcıdan 3 tane isim al ve listeye ekle yazdır
from soupsieve.util import lower

# isimler = [] # Boş bir liste oluşturduk
#
# sayac = 0 # Kaç isim aldığımızı takip etmek için sayaç
#
# while sayac < 3: # 3 Kez Dönecek
#     isim = input('Bir İsim Girin: ')
#     isimler.append(isim) # Listeye Ekle
#     sayac += 1 # Sayacı 1 artır
# print('Girilen İsimler: ', isimler)


cümle = input('Bİr Cümle Girin: ').lower()

sesli_harfler = []
sessiz_harfler = []
for harf in cümle:
    if harf.isalpha(): # Harf mi? (Yani sayılar ve özel karakterler dışarda)
        if harf in 'aeıioöuü': # Sesli harf mi?
            if harf not in sesli_harfler: # Eğer sesli harf zaten yoksa ekle
                sesli_harfler.append(harf)
        else: # Sessiz harf
            if harf not in sessiz_harfler: # Eğer sessiz harf zaten yoksa, ekle
                sessiz_harfler.append(harf)

print('Sesli Harfler:', sesli_harfler)
print('Sessiz Harfler:',sessiz_harfler)

