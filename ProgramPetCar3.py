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


def fasilitasA () :
    print ("List fasilitas yang tersedia:")
    print ("[1] : Klinik")
    print ("[2] : Grooming")
    print ("[3] : Penitipan")
    fsl = input("Input fasilitas yang digunakan :")
    if fsl == "1" :
        klinik()
        
    elif fsl == "2" :
            harga = 65000*jumlah
            print("Harga Grooming Rp.65000 per hewan")
            print("Total harga Grooming : Rp.", harga)
    elif fsl == "3" :
            anjing ()
    else :
        print ("Tidak Tersedia")
def fasilitasK () :
    print ("List fasilitas yang tersedia:")
    print ("[1] : Klinik")
    print ("[2] : Grooming")
    print ("[3] : Penitipan")
    fsl = input("Input fasilitas yang digunakan :")
    if fsl == "1" :
         kucing ()
    elif fsl == "2" :
            harga = 50000*jumlah
            print("Biaya Grooming untuk kucing sebesar Rp.50000/kucing.")
            print("Total biaya Grooming : Rp.", harga)
    elif fsl == "3" :
            inapkucing ()
    else :
        print ("Tidak Tersedia")
