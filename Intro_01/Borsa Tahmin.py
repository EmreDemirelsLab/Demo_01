#ChatGPT
import yfinance as yf

print("Hisse senedi tahmin programına hoş geldiniz!")

while True:
    try:
        # Kullanıcıdan hangi hisseyi takip etmek istediğini soruyoruz
        hisse_ticker = input("Hangi hisseyi takip etmek istersiniz? (Örnek: AAPL, TSLA, etc.): ")

        # Hisse senedi verilerini çekmek için yfinance kütüphanesini kullanıyoruz
        hisse = yf.Ticker(hisse_ticker)

        # Son 5 günün kapanış fiyatlarını alıyoruz
        fiyatlar = hisse.history(period="5d")['Close']

        print(f"{hisse_ticker} hissesi için geçmiş 5 günün kapanış fiyatları: \n{fiyatlar}")

        # Geçmiş fiyatların ortalamasını hesaplıyoruz
        ortalama_fiyat = fiyatlar.mean()

        # Bugünkü fiyatı alıyoruz
        bugunku_fiyat = fiyatlar.iloc[-1]

        print(f"Bugünkü fiyat: {bugunku_fiyat}")

        # Fiyat karşılaştırmasını yapıyoruz
        if bugunku_fiyat > ortalama_fiyat:
            print("Fiyatın artmaya devam etmesini tahmin ediyorum.")
        elif bugunku_fiyat < ortalama_fiyat:
            print("Fiyatın düşmeye devam etmesini tahmin ediyorum.")
        else:
            print("Fiyat sabit kalacak gibi görünüyor.")

        # Kullanıcıya başka bir işlem yapmak isteyip istemediğini soruyoruz
        devam = input("Başka bir tahmin yapmak ister misiniz? (Evet/Hayır): ").lower()
        if devam != "evet":
            print("Program sonlandırılıyor...")
            break  # Eğer kullanıcı "Evet" demediyse döngü sonlanır

    except ValueError:
        print("Geçersiz giriş! Lütfen geçerli bir hisse sembolü girin.")
        continue  # Eğer geçersiz giriş yapılırsa, tekrar işlem yapılır
    except Exception as e:
        print(f"Hata oluştu: {e}")
        continue  # Diğer hata durumlarında da tekrar işlem yapılır


