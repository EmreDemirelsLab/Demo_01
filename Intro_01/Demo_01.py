# import requests
# response = requests.get("http://www.google.com")
# print(response.text)

# import webbrowser
# url = 'http://google.com'
# webbrowser.get('safari').open_new(url)


sayi = int(input('Sayı:'))
sonuc = 1

while sayi > 0:
    sonuc *= sayi
    sayi -= 1
print(f'{sonuc} Faktöriyel')
