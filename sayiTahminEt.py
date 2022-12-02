"Python sayı tahmin oyunu"

"Seviye 1 2 3"
"1.Seviye 1-10"
"2.Seviye 1-50"
"3.Seviye 1-100"


import random
import sys

def seviyeBir():
    global Asayi
    Asayi=random.randint(1,10)
    while True:
        global Atahminet
        Atahminet=int(input("Tahmin Et: "))
        if Atahminet > Asayi:
            print("Lütfen daha küçük bir değer girin!")
        elif Atahminet < Asayi:
            print("Lütfen daha büyük bir değer girin!")
        else:
            print("Tebrikler doğru tahmin!\n{}".format(Asayi))
            sys.exit()
    
def seviyeIki():
    global Bsayi
    Bsayi=random.randint(1,50)
    while True:
        global Btahminet
        Btahminet=int(input("Tahmit Et: "))
        if Btahminet > Bsayi:
            print("Lütfen daha küçük bir değer girin!")
        elif Btahminet > Bsayi:
            print("Lütfen daha büyük bir değer girin!")
        else:
            print("Tebrikler doğru tahmin!\n{}".format(Bsayi))
            sys.exit()
    
def seviyeUc():
    global Csayi
    Csayi=random.randint(1,100)
    while True:
        global Ctahminet
        Ctahminet=int(input("Tahmin Et: "))
        if Ctahminet > Csayi:
            print("Lütfen daha küçük değer girin!")
        elif Ctahminet < Csayi:
            print("Lütfen daha büyük değer girin!")
        else:
            print("Tebrikler doğru tahmint!\n{}".format(Csayi))
            sys.exit()
    
     
        
while True:
    print("""
          Sayı tahmin oyununa hoş geldin
          
          A=1.Seviye 1-10
          B=2.Seviye 1-50
          C=3.Seviye 1-100
          
          Oyundan çıkmak için 'q' komutunu girin.
          """)
    
    seviyeSec=input("Bir Seviye Giriniz (A-B-C): ")

    if seviyeSec == "q":
        print("Oyundan çıkılıyor...")
        sys.exit()
    elif seviyeSec == "A" or "a":
        seviyeBir()
    elif seviyeSec == "B" or "b":
        seviyeIki()
    elif seviyeSec == "C" or "c":
        seviyeUc()
    else:
        print("Üzgünüm geçersiz değer")



