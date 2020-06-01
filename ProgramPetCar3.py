iterasi = True
def klinik () : 
    jumlah = int(input("Input Jumlah Hewan : "))
    print ("Poliklinik Hewan '8Care' ")
    print ("[1] : Konsultasi Dokter")
    print ("[2] : Vaksinasi")
    print ("[3] : lain-lain")
    klk=input("Input jasa poliklinik : ")
    if klk == "1" :
        hargakonsul = 200000*jumlah
        print("Harga konsultasi dokter per hewan : Rp.200000")
        print("Total harga konsultasi : Rp.", hargakonsul)
    elif klk == "2" :
        harga_vaksin = 100000*jumlah
        print("Harga vaksinasi : Rp.100000 per hewan" )
        print("Total harga vaksinasi : Rp.", harga_vaksin)
    elif klk == "3" :
        lain = 150000*jumlah
        print("Total biaya perawatan lain-lain : Rp.150000 per hewan")
        print("Total harga perawatan lain-lain : Rp.", lain)

       
def kucing () :
    print ("Poliklinik Hewan '8Care' ")
    print ("[1] : Konsultasi Dokter")
    print ("[2] : Vaksinasi")
    print ("[3] : lain-lain")
    klk = input("Input jasa poliklinik :")
    if klk == "1" :
        hargakonsul = 150000*jumlah
        print ("Harga konsultasi dokter per hewan : Rp.150000")
        print ("Total harga konsultasi : Rp.", hargakonsul)
    elif klk == "2" :
        harga_vaksin = 80000*jumlah
        print ("Harga vaksinasi : Rp.80000 per hewan")
        print ("Total harga vaksinasi : Rp.", harga_vaksin)
    elif klk == "3" :
        lain = 120000*jumlah
        print ("Total biaya perawatan lain-lain : Rp.120000 per hewan")
        print ("Total harga perawatan lain-lain : Rp.", lain)
