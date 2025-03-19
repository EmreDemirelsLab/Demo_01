sayi = int(input('Sayı Giriniz:'))
sayac = 2
if sayi < 2:
    print(sayi, 'Asal Değildir.')
if sayi == 2:
    print(sayi, 'Asaldır')

if sayi % 2 == 0:
    print(sayi, 'Asal Değildir.')
    exit()
    while sayi >= sayac:

        if sayac % sayi == 0:
            print(sayi, 'Asaldır')
            break

        sayac += 1

# if sayi % 2 == 0:
#     print(sayi, 'Asal Değildir')
