## 3.soru ##

import random

## Bilgisayar 1-100 arasında rastgele sayı ##
sayi = int(random.random() * 100) + 1

print("Bilgisayar 1-100 arasinda bir sayi tuttu.Tahmin etmeye çalişin!")
deneme_hakki = 10

for deneme in range(1,deneme_hakki + 1):
    tahmin = int(input(f"{deneme}.tahmininiz:"))

    if tahmin == sayi:
        print("Tebrikler! Doğru tahmin!")
        break
    elif tahmin < sayi:
        print("Daha buyuk sayi söyleyin.")
    else:
        print("Daha küçük bir sayi söyleyin.")

        kalan= deneme_hakki - deneme
        if kalan>0:
            print(f"kalan deneme hakkiniz: {kalan}\n")
        else:
           print ("\nDeneme hakkinizz bitti!")
    print(f"Tutulan sayi: {sayi}")                                    