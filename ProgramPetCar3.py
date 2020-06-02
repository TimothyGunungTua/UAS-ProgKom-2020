iterasi = True

def time1(): 
    from datetime import date
    import datetime
    tanggal = int(input("Silahkan Input Tanggal dan Waktu Masuk\nTanggal (1-31)     : "))
    bulan = int(input("Bulan (1-12)       : "))
    tahun = 2020
    jam   = int(input("Jam (format 24 jam): "))
    menit = int(input("Menit (0-60)       : "))
    detik = int(input("Detik (0-60)       : "))
    
    global selisih_tgl
    global durasijam
    
    tgl_in = date(tahun, bulan, tanggal)
    tgl_out = date.today()
    selisih_tgl= tgl_out - tgl_in
    
    #waktu masuk
    wkt_in = (jam*3600 + menit*60 + detik)

    #waktu keluar
    x = datetime.datetime.now()
    jam_out = x.hour
    menit_out= x.minute
    detik_out = x.second
    wkt_out = (jam_out*3600)+(menit_out*60)+(detik_out)

    import math
    selisih_wkt = wkt_out - wkt_in
    durasijam= math.ceil(selisih_wkt/3600)

    print()
    print("----------------------------------")
    print("       Billing PetCare 2020 ")
    print("----------------------------------")
    print("Masuk ", "\n  ",tgl_in, "\n   pukul", jam,":", menit,":", detik)
    print("Keluar \n  ", tgl_out, "\n   pukul",jam_out,":",menit_out,":",detik_out )
    print('Peliharaan anda menginap selama :')
    print("  ",selisih_tgl.days, 'hari ', durasijam,"jam")
    
def anjing():
    time1()
    print("Jenis hewan : anjing")
    if selisih_tgl.days > 0 :
            bayar = ((selisih_tgl.days * 25000) + 3000)*jumlah
            print("Tarif inap per hewan : Rp.",(selisih_tgl.days*25000) + 3000)
            #print("Tarif           : Rp ", bayar)
            print("Tarif inap total : Rp ", bayar)
                
    else:
        bayar =  20000*jumlah
        print("Tarif per hewan : Rp.", 2000)
        print("Tarif total : Rp ", bayar)
        
        
def kucingnginep():
    time1()
    print("Jenis hewan : kucing")
    if selisih_tgl.days > 0 :
        if round(durasijam) > 0 :
            bayar = ((selisih_tgl.days * 25000) + 3000)*jumlah
            print("Tarif inap per hewan : Rp.", (selisih_tgl.days*25000) + 3000)
            print("Tarif total : Rp.", bayar)
        else :
            bayar = ((selisih_tgl.days * 25000))*jumlah
            print("Tarif per hewan : Rp.", selisih_tgl.days*25000)
            print("Tarif total : Rp ", bayar)
    else:
        bayar =  (3000)*jumlah
        print("Tarif per hewan : Rp.", 3000)
        print("Tarif total : Rp ", bayar)
def klinik () : 
    jumlah = int(input("Input Jumlah Hewan : "))
    print ("Poliklinik Hewan 'PetCare' ")
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
    print ("Poliklinik Hewan 'PetCare' ")
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
            kucingnginep ()
    else :
        print ("Tidak Tersedia")
        
       
print ("===============================================================")
print ("                           PET CARE                                  ")
print ("===============================================================")
print ()
print (input("Input Nama Petugas : "))
print (input("Input Nama Pemilik : "))
print ("[1] : Anjing")
print ("[2]: Kucing")
jenis = int(input("Input Jenis Hewan : "))

if jenis == 1:
    jumlah = int(input("Input Jumlah Hewan : "))
    fasilitasA ()
    while iterasi:
        next = input("Tambah operasi lainnya untuk jenis hewan yang sama? (y/n) : ")
        if next == "y":
           jumlah = int(input("Input Jumlah Hewan : "))
           fasilitasA ()
        elif next == "n":
           print("Terima kasih telah berkunjung")
           iterasi = False
        else:
            print("Sistem error silahkan ulangi")
            iterasi = False
            
      
elif jenis == 2:
    jumlah = int(input("Input Jumlah Hewan : "))
    fasilitasK ()
    while iterasi:
        next = input("Tambah operasi lainnya untuk jenis hewan yang sama? (y/n) : ")
        if next == "y":
           jumlah = int(input("Input Jumlah Hewan : "))
           fasilitasK ()
        elif next == "n" :
           print("Terima kasih telah berkunjung")
           iterasi = False
        else:
            print("Sistem error silahkan ulangi")
            iterasi = False
else:
    print("Error, silahkan ulangi")
