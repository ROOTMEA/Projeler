import random


def toplama():
    puan=0 #her doğru cevapta + 10 puan  eklenir, her yanlışta -5 puan azalır 
    while True:    
        sayi1=random.randint(1,999)
        sayi2=random.randint(1,999)
        soru=int(input("{}+{} sonucu kaçtır: ".format(sayi1,sayi2)))
        cevap=sayi1+sayi2

        if soru == cevap:
            print("Tebrikler Doğru Cevap!")
            puan+=10
            print("Puan:",puan)
        else:
            print("Yanlış Cevap! Doğru Cevap:{}".format(cevap))
            puan-=5
            print("Puan:",puan)
            cikis=input("Devam etmek istermisin?(E-H): ")
            if cikis=="E" or cikis=="e":
                continue
            elif cikis=="H" or cikis=="h":
                print("Görüşmek Üzere...")
                exit()
            else:
                print("Yanlış Girdi!!")
                continue 

def cikartma():
    puan=0 #her doğru cevapta + 10 puan  eklenir, her yanlışta -5 puan azalır
    while True:        
        sayi1=random.randint(1,500)
        sayi2=random.randint(1,250) 
        soru=int(input("{}-{} sonucu kaçtır: ".format(sayi1,sayi2)))
        cevap=sayi1-sayi2

        if soru == cevap:
            print("Tebrikler Doğru Cevap!")
            puan+=10
            print("Puan:",puan)
        else:
            print("Yanlış Cevap! Doğru Cevap:{}".format(cevap))
            puan-=5
            print("Puan:",puan)
            cikis=input("Devam etmek istermisin?(E-H): ")
            if cikis=="E" or cikis=="e":
                continue
            elif cikis=="H" or cikis=="h":
                print("Görüşmek Üzere...")
                exit()
            else:
                print("Yanlış Girdi!!")
                continue 

def carpma():
    puan=0 #her doğru cevapta + 10 puan  eklenir, her yanlışta -5 puan azalır
    while True:
        sayi1=random.randint(1,100)
        sayi2=random.randint(1,100)
        soru=int(input("{}*{} sonucu kaçtır: ".format(sayi1,sayi2)))
        cevap=sayi1*sayi2
        
        if soru == cevap:
            print("Tebrikler Doğru Cevap!")
            puan+=10
            print("Puan:",puan)
        else:
            print("Yanlış Cevap! Doğru Cevap:{}".format(cevap))
            puan-=5
            print("Puan:",puan)
            cikis=input("Devam etmek istermisin?(E-H): ")
            if cikis=="E" or cikis=="e":
                continue
            elif cikis=="H" or cikis=="h":
                print("Görüşmek Üzere...")
                exit()
            else:
                print("Yanlış Girdi!!")
                continue

def bolme():
    puan=0 #her doğru cevapta + 10 puan  eklenir, her yanlışta -5 puan azalır
    while True:
        sayi1=random.randint(1,1000)
        sayi2=random.randint(1,1000)
        soru=int(input("{}/{} sonucu kaçtır: ".format(sayi1,sayi2)))
        cevap=sayi1//sayi2

        if soru == cevap:
            print("Tebrikler Doğru Cevap!")
            puan+=10
            print("Puan:",puan)
        else:
            print("Yanlış Cevap! Doğru Cevap:{}".format(cevap))
            puan-=5
            print("Puan:",puan)
            cikis=input("Devam etmek istermisin?(E-H): ")
            if cikis=="E" or cikis=="e":
                continue
            elif cikis=="H" or cikis=="h":
                print("Görüşmek Üzere...")
                exit()
            else:
                print("Yanlış Girdi!!")
                continue


while True:
        print("""
        ******************************
        DÖRT İŞLEM OYUNUNA HOŞGELDİN
        ******************************
        
        1-TOPLAMA
        2-ÇIKARTMA
        3-ÇARPMA
        4-BÖLME

        ---> Eğer 'q' tuşuna basarsan oyundan çıkarsın
        --->Puanın her soru cevapladığında sana gösterilir
        --->Hangi işlemde oynamak istiyorsan numarasını girerek bunu sağlayabilirsin

        İYİ OYUNLAR...:)
        """)


        tercih=input("Neyi tercih etmek istersin: ")

        if tercih == "q":
            print("Görüşmek üzere...")
            exit()
        if tercih == "1":
            toplama()
        elif tercih == "2":
            cikartma()
        elif tercih == "3":
            carpma()
        elif tercih == "4":
            bolme()
        else:
            print("Geçersiz Tercih!!!")
            exit()

    
