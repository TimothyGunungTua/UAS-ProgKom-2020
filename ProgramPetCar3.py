iterasi = True
aa = True
bb = True
list = ["[No] - [Jenis Hewan] - [Fasilitas] - [Keterangan] - [Biaya]"]
set = []
biaya = []

set.append(list)

class time1(object):
    def __init__(self,datein, dateout, jamin, jamout, menitin, menitout, detikin, detikout, selisihtgl, selisihjam) : #, datein, dateout, jamin, jamout, menitin, menitout, jamin, jamout, menitin, menitout, detikin, detikout ): 
        from datetime import date
        import datetime
        tanggal = int(input("Silahkan Input Tanggal dan Waktu Masuk \nTanggal (1-31)     : "))
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
            
        self.datein = tgl_in
        self.dateout = tgl_out
        self.jamin = jam
        self.jamout = jam_out
        self.menitin = menit
        self.menitout = menit_out
        self.detikin = detik
        self.detikout = detik_out
        self.selisihtgl = int(selisih_tgl.days)
        self.selisihjam = durasijam
        
    def displayTime(self) :
        print("Masuk  ", "\n  ",self.datein, "\n   pukul", self.jamin,":", self.menitin,":", self.detikin)
        print("Keluar \n  ", self.dateout, "\n   pukul",self.jamout,":",self.menitout,":",self.detikout)
        print("Peliharaan anda telah menginap selama :")
        print("  ",self.selisihtgl, 'hari ', self.selisihjam,"jam")
    
def anjing() :
    ii= time1(0,0,0,0,0,0,0,0,0,0)
    print("Jenis hewan : Anjing")
    jumlaha =int(input("Jumlah hewan:"))
    if selisih_tgl.days >= 0 :
        if 24 > round(durasijam) > 0 : 
            bayar = (25000)*jumlaha
            ii.displayTime()
            print("Tarif inap per hewan : Rp.", (selisih_tgl.days*25000))
            print("Tarif total : Rp.", bayar)
            biaya.append(bayar)
        else :
            bayar = ((selisih_tgl.days * 25000))*jumlaha
            print("Tarif per hewan : Rp.", selisih_tgl.days*25000)
            print("Tarif total : Rp ", bayar)
            biaya.append(bayar)
    else :
        print ("Sistem Error")
    list5 = [j],['Anjing'],['Penitipan'],['Penitipan',jumlaha,'ekor','selama',selisih_tgl.days,'hari',durasijam,'jam'],['Rp.', bayar]
    set.append(list5)
               
def kucingnginep():
    ii= time1(0,0,0,0,0,0,0,0,0,0)
    print("Jenis hewan : Kucing")
    jumlahk = int(input("Jumlah hewan:"))
    if selisih_tgl.days >= 0 :
        if 24 > round(durasijam) > 0 :
            bayar = (20000)*jumlahk
            ii.displayTime()
            print("Tarif inap per hewan : Rp.", (selisih_tgl.days*20000))
            print("Tarif total : Rp.", bayar)
            biaya.append(bayar)
        else :
            bayar = ((selisih_tgl.days * 20000))*jumlahk
            print("Tarif per hewan : Rp.", selisih_tgl.days*20000)
            print("Tarif total : Rp ", bayar)
            biaya.append(bayar)
    else :
        print ("Sistem Error")
    list10 = [j], ['Kucing'],['Penitipan'],['Penitipan',jumlahk,'ekor','selama',selisih_tgl.days,'hari',durasijam,'jam'],['Rp.', bayar]
    set.append(list10)
        
            
def klinikA () : 
    print ("Poliklinik Hewan 'PetCare' ")
    print ("[1] : Konsultasi Dokter")
    print ("[2] : Vaksinasi")
    print ("[3] : Obat Bius")
    klk=input("Input jasa poliklinik : ")
    if klk == "1" :
        jumlah1 = int(input("Jumlah hewan:"))
        hargakonsul = 200000*jumlah1
        print("Harga konsultasi dokter per hewan : Rp.200000")
        print("Total harga konsultasi : Rp.", hargakonsul)
        list1 = [j],['Anjing'],['Klinik'],['Konsultasi Dokter untuk', jumlah1, 'ekor'],['Rp.', hargakonsul]
        set.append(list1)
        biaya.append(hargakonsul)
    elif klk == "2" :
        jumlah2 = int(input("Jumlah hewan:"))
        harga_vaksin = 100000*(jumlah2)
        print("Harga vaksinasi : Rp.100000 per hewan" )
        print("Total harga vaksinasi : Rp.", harga_vaksin)
        list2 = [j],['Anjing'],['Klinik'],['Vaksinasi untuk', jumlah2,'ekor'],['Rp.', harga_vaksin]
        set.append(list2)
        biaya.append(harga_vaksin)
    elif klk == "3" :
        print("Biaya obat bius per anjing : Rp.50000")
        jumlah3 = int(input("Jumlah hewan:"))
        lain = 50000
        print("Total harga obat bius : Rp.", lain*jumlah3)
        list3 = [j],['Anjing'],['Klinik'],['Obat bius untuk', jumlah3, 'ekor'],['Rp.', lain]
        set.append(list3)
        biaya.append(lain)
    else :
        print ("Tidak Tersedia")

       
def klinikK () :
    print ("Poliklinik Hewan 'PetCare' ")
    print ("[1] : Konsultasi Dokter")
    print ("[2] : Vaksinasi")
    print ("[3] : Obat Bius")
    klk = input("Input jasa poliklinik :")
    if klk == "1" :
        jumlah4 = int(input("Jumlah hewan:"))
        hargakonsul = 150000*(jumlah4)
        print ("Harga konsultasi dokter per hewan : Rp.150000")
        print ("Total harga konsultasi : Rp.", hargakonsul)
        list6 = [j],['Kucing'],['Klinik'],['Konsultasi Dokter untuk', jumlah4, 'ekor'],['Rp.', hargakonsul]
        set.append(list6)
        biaya.append(hargakonsul)
    elif klk == "2" :
        jumlah5 = int(input("Jumlah hewan:"))
        harga_vaksin = 80000*(jumlah5)
        print ("Harga vaksinasi : Rp.80000 per hewan")
        print ("Total harga vaksinasi : Rp.", harga_vaksin)
        list7 = j,['Kucing'],['Klinik'],['Vaksinasi untuk', jumlah5, 'ekor'],['Rp.', harga_vaksin]
        set.append(list7)
        biaya.append(harga_vaksin)
    elif klk == "3" :
        print("Biaya obat bius per kucing : Rp.45000")
        lain = 45000
        jumlah11 = int(input("Jumlah hewan : "))
        print ("Total harga obat bius : Rp.", lain*jumlah11)
        list8 = j, ['Kucing'],['Klinik'],['Obat bius untuk', jumlah11, 'ekor'],['Rp.', lain]
        set.append(list8)
        biaya.append(lain)
    else :
        print ("Tidak Tersedia")

def fasilitasA () :
    print ("List fasilitas yang tersedia:")
    print ("[1] : Klinik")
    print ("[2] : Grooming")
    print ("[3] : Penitipan")
    fsl = input("Input fasilitas yang digunakan :")
    if fsl == "1" :
        klinikA()   
    elif fsl == "2" :
        jumlah7=int(input("Jumlah hewan:"))
        harga = 65000*jumlah7
        print("Harga Grooming Rp.65000 per hewan")
        print("Total harga Grooming : Rp.", harga)
        list4 = [j],['Anjing'],['Grooming'],['Grooming untuk', jumlah7, 'ekor'],['Rp.', harga]
        set.append(list4)
        biaya.append(harga)
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
         klinikK ()
    elif fsl == "2" :
        jumlah8 = int(input("Jumlah hewan:"))
        harga = 50000*(jumlah8)
        print("Biaya Grooming untuk kucing sebesar Rp.50000/kucing.")
        print("Total biaya Grooming : Rp.", harga)
        list9 = [j], ['Kucing'],['Grooming'],['Grooming untuk', jumlah8, 'ekor'],['Rp.', harga]
        set.append(list9)
        biaya.append(harga)
    elif fsl == "3" :
        kucingnginep ()
    else :
        print ("Tidak Tersedia")

def fasilitasC () :
    print ("List fasilitas yang tersedia:")
    print ("[1] : Klinik")
    print ("[2] : Grooming")
    print ("[3] : Penitipan")
    fsl = input("Input fasilitas yang digunakan :")
    if fsl == "1" :
        print ("Input Jenis Hewan \n[1] : Anjing \n[2] : Kucing")
        jns = input ("Input Jenis Hewan :")
        if jns == "1" :
            klinikA ()
        elif jns == "2" :
            klinikK ()
        else :
            print("Sistem error")
    elif fsl == "2" :
        print ("Input Jenis Hewan \n[1] : Anjing \n[2] : Kucing")
        jns = input ("Input Jenis Hewan :")
        if jns == "1" :
            jumlah22 = int(input("Jumlah hewan:"))
            harga = 65000*(jumlah22)
            print("Biaya Grooming untuk anjing sebesar Rp.65000/ekor.")
            print("Total biaya Grooming : Rp.", harga)
            list17 = [j],['Anjing'],['Grooming'],['Grooming untuk', jumlah22, 'ekor'],['Rp.',harga]
            set.append(list17)
            biaya.append(harga)
        elif jns == "2" :
            jumlah23 = int(input("Jumlah hewan:"))
            harga = 50000*(jumlah23)
            print("Biaya Grooming untuk kucing sebesar Rp.50000/ekor.")
            print("Total biaya Grooming : Rp.", harga)
            list18 = [j],['Kucing'],['Grooming'],['Grooming untuk', jumlah23, 'ekor'],['Rp.',harga]
            set.append(list18)
            biaya.append(harga)
        else :
            print("Sistem error")            
    elif fsl == "3" :
        print ("Input Jenis Hewan \n[1] : Anjing \n[2] : Kucing")
        jns = input ("Input Jenis Hewan :")
        if jns == "1" :
            anjing ()
        elif jns == "2" :
            kucingnginep ()
        else :
            print("Tidak Tersedia")            
    else :
        print ("Tidak Tersedia")

def struk ():
    print ("----------------------------------------")
    print ("            Billing Pet Care            ")
    print ("----------------------------------------")
    print ('Nama petugas : ', petugas)
    print ('Nama pemilik : ', pemilik)
    print('\n')
    
    i = 0
    while i < len(set):
        print(set[i])
        i = i + 1

    print('\n')
    total = sum(biaya)
    print('Total biaya Rp.', total)
    print ("----------------------------------------")
    print ("   Terima Kasih Atas Kepercayaan Anda   ")
    print ("----------------------------------------")
    
print ("===============================================================")
print ("                           PET CARE                            ")
print ("===============================================================")
print ()
while bb:
    try:
        petugas = input("Input Nama Petugas : ")
        if petugas=='':
            raise ValueError
        else:
            bb =False
    except Exception:
        print ('Wajib diisi')
        petugas = input("Input Nama Petugas : ")
        if petugas=='':
            bb = True
        else:
            bb = False            
while aa:
    try:
        pemilik = input("Input Nama Pemilik : ")
        if pemilik == '':
            raise ValueError
        else:
            aa=False
    except Exception:
        print ('Wajib diisi')
        pemilik = input("Input Nama Pemilik : ")
        if pemilik== '':
            aa=True
        else:
            aa=False
print ("[1]: Anjing")
print ("[2]: Kucing")
print ("[3]: Campur")
jenis = int(input("Input Jenis Hewan : "))

j = 1

if jenis == 1:
    fasilitasA ()
    while iterasi:
        next = input("Tambah operasi lainnya untuk jenis hewan yang sama? (y/n) : ")
        if next == "y":
            j = j+1
            fasilitasA ()
        elif next == "n":
           print("Terima kasih telah berkunjung")
           iterasi = False
        else:
            print("Sistem error silahkan ulangi")
            iterasi = False
            
      
elif jenis == 2:
    fasilitasK ()
    while iterasi:
        next = input("Tambah operasi lainnya untuk jenis hewan yang sama? (y/n) : ")
        if next == "y":
            j = j+1
            fasilitasK ()
        elif next == "n" :
           print("Terima kasih telah berkunjung")
           iterasi = False
        else:
            print("Sistem error silahkan ulangi")
            iterasi = False

elif jenis == 3 :
    fasilitasC ()
    while iterasi:
        next = input("Tambah operasi lainnya ? (y/n) : ")
        if next == "y":
            j = j+1
            fasilitasC ()
        elif next == "n" :
           print("Terima kasih telah berkunjung")
           iterasi = False
        else:
            print("Sistem error silahkan ulangi")
            iterasi = False
            
else:
    print("Error, silahkan ulangi")


struk ()
