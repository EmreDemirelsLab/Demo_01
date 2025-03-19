import random

# Major scale içindeki notalar
NOTALAR = ["C", "D", "E", "F", "G", "A", "B"]

def rastgele_melodi(uzunluk=8):
    melodi = [random.choice(NOTALAR) for _ in range(uzunluk)]
    return " - ".join(melodi)

# 8 notalık bir melodi üret
print("🎵 Rastgele Melodi:", rastgele_melodi())
