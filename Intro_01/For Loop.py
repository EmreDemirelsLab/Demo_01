cumle = 'pyhton is good'

for harf in cumle:
    print(harf)
print('\n')

for sayi in range(1, 6):
    print(f'{sayi}^2 = {sayi ** 2}')
print('\n\n\n')

sayilar = [2,10, 33, 21, 48, 95]
for sayi in sayilar:
    if sayi % 2 == 0:
        print(f'{sayi} Çift Sayıdır.')
    else:
        print(f'{sayi} Tek Sayıdır')
print('\n')

isimler = []

for i in range(3): #kullanıcıdan 3 tane isim alacağız.
    isim = input('Bir İsim Girin:')
    isimler.append(isim)
print('Girilen İsimler: ', isimler)

for i in range(1,6):
    for j in range(1,6):
        print(f'{i} * {j}')
