def hesapla():
    name=input("Name: ")
    surname=input("Surname: ")
    firstNote=int(input("FirstNote: "))
    secondNote=int(input("SecondNote: "))
    endNote=(firstNote+secondNote)//2
    
    if endNote < 50:
        print(name,surname,"\nKaldınız!=",endNote)
        kalanlar=open("kalanlar.txt","a")
        kalanlar.writelines(name)
        kalanlar.writelines(surname)
        kalanlar.writelines(str(endNote))
        kalanlar.close()
    else:
        print(name,surname,"\nGeçtiniz!=",endNote)
        gecenler=open("geçenler.txt","a")
        gecenler.writelines(name)
        gecenler.writelines(surname)
        gecenler.writelines(str(endNote))
        gecenler.close()

def oku():
    fileRead=input("Dosya Okumak İstiyormusun(Evet-Hayır): ")
    if fileRead == "Evet" or fileRead=="evet":
        enterFile=input("Dosya ismini girin: ")
        file=open(enterFile,"r")
        print(file.read())
        file.close()
    else:
        pass

hesapla()

oku()

