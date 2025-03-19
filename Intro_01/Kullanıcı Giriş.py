import string

# Kullanıcı listesi
users = [
    ('beast', '123'),
    ('savage', '987'),
    ('bear', '567')
]


def is_pwd_valid(password: str) -> bool:
    """Şifrenin güvenli olup olmadığını kontrol eder."""
    char_set = set(password)

    is_result = (
            len(password) >= 8  # 16 yerine daha makul bir uzunluk belirledim (8)
            and any(c in string.ascii_uppercase for c in char_set)  # Büyük harf kontrolü
            and any(c in string.ascii_lowercase for c in char_set)  # Küçük harf kontrolü
            and any(c in string.digits for c in char_set)  # Rakam kontrolü
            and any(c in string.punctuation for c in char_set)  # Özel karakter kontrolü
    )

    return is_result


def sign_in(username: str, password: str) -> str:
    """ Kullanıcının giriş yapmasını sağlar. """
    for userName, pwd in users:
        if userName == username and pwd == password:
            return f'{username} Hoş Geldiniz.'
    return 'Bilgiler Hatalı..!'


def sign_up(username: str, password: str) -> str:
    """ Yeni kullanıcı ekler. """
    global users  # Kullanıcı listesini değiştirebilmek için global olarak tanımlandı.

    for userName, pwd in users:
        if userName == username:  # Kullanıcı adı kontrolü
            return 'Bu Kullanıcı Zaten Alındı..!'

    if is_pwd_valid(password):  # Şifre geçerliyse kullanıcıyı ekleyelim
        users.append((username, password))
        return 'Üyelik İşlemi Tamamlandı.'
    return 'Geçersiz şifre! Şifreniz en az 8 karakter, bir büyük harf, bir küçük harf, bir rakam ve bir özel karakter içermelidir.'


# Kullanıcı giriş yapmaya çalışıyor
print('Giriş Yapmak İçin Bilgilerinizi Giriniz..!')
while True:
    username = input('Username: ')
    password = input('Password: ')

    result = sign_in(username, password)
    print(result)

    if result != 'Bilgiler Hatalı..!':
        break  # Başarılı giriş yaptıysa döngüden çık

# Yeni kullanıcı kaydı
print('Lütfen Yeni Kullanıcı Bilgilerinizi Giriniz..!')
while True:
    username = input('Username: ')
    password = input('Password: ')

    result = sign_up(username, password)
    print(result)

    if result == 'Üyelik İşlemi Tamamlandı.':
        break  # Kayıt başarılıysa döngüden çık

# Kullanıcı listesini yazdırarak yeni kullanıcı eklendi mi kontrol edelim
print("Güncellenmiş Kullanıcı Listesi:", users)

# Yeni kullanıcı giriş yapmayı deniyor
print('Şimdi giriş yapalıyor..!')
login_result = sign_in(username, password)
print(login_result)
