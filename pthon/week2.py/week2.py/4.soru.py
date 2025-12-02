def tek_sayilari_topla():
    toplam = 0 #tek sayilarin toplamı

    for i in range(10): # 10 defa kullanıcıdan sayı al
        sayi = int(input("bir sayi gir:"))

        if sayi %2 == 0:  # eğer çift ise
            continue #atla

        toplam += sayi
        print(f"{sayi}) tek bir sayi,toplama eklendi.")
        
    print("\nTek sayilarin toplami:", toplam)

tek_sayilari_topla()     #fonksiyonu çaliştir