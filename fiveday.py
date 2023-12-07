import terminaltables

#Fungsi Menu Utama
def menu():
    print("-----------TOKO FIVE DAY----------------")
    kolom = ("No","JENIS BAJU","Harga")
    daftar = [(listNo[i],listjenisBaju[i],format(listharga[i],",.2f"))for i in range(len(listNo))]

    data_tabel = [kolom]
    data_tabel.extend(daftar)
    tabel = terminaltables.AsciiTable(data_tabel)
    print(tabel.table)

#fungsi validasi input hanya meneriama angka
def angka(pesan):
    while True:
        try:
            ipt = int(input(pesan))
            return ipt
        except ValueError:
            print("\nMAAF INPUT HANYA MENERIMA ANGKA")

#fungsi validasi input hanya menerima y/t
def tambah(pesan):
    ipt = input(pesan).lower()
    while ipt != "y" and ipt != "t":
        print("PERINTAH TIDAK DIKETAHUI")
        ipt = input(pesan).lower()
    return ipt

#fungsi menampilkan pesanan pertama
def output_pilihan():
    print("\n----PILIHAN ANDA----")
    print(">> Baju         : ",baju)
    print(">> Jumlah       : ",iptjumalahbaju)
    print(">> Ukuran       : ",iptukuran)
    print(">> Harga Satuan : ",format(hrg,",.2f"))
    print(">> Total Harga  : ",format(tothrg,",.2f"))

def output_beli():
    kolom = ["NO","JENIS BAJU","UKURAN","HARGA","TOTAL HARGA"]
    daftar = [(i+1,listbaju[i],listsemuaUkuran[i],format(listhrgsat[i],",.2f"),format(listtothrg[i],",.2f")) for i in range(len(listbaju))]

    Daftar_menu = [kolom]
    Daftar_menu.extend (daftar)
    tabel = terminaltables.AsciiTable (Daftar_menu)
    print(tabel.table)

#list
listNo = [1,2,3,4,5,6,7,8,9,10]
listjenisBaju = ["Kemeja Pendek","Kemeja Panjang","Kaos Pendek","Kaos Panjang","Hoodie","Sweater","Tunik","Jaket","Daster","Blouse"]
listharga = [100_000,120_000,50_000,55_000,95_000,75_000,150_000,200_000,60_000,120_000]
listukuran = ["S","M","L","XL"]
listbaju = []
listsemuaUkuran = []
listjumlah = []
listhrgsat = []
listtothrg = []

iptTambah = "y"
while iptTambah =="y":
    menu()
    #input kode/no jenis baju
    #jika input tidak ada di dalam list maka akan di ulang
    iptkodebaju = angka(">> Masukan No Baju         : ")
    while iptkodebaju not in listNo:
        print("NOMOR BAJU YANG KAMU PILIH TIDAK TERSEDIA")
        iptkodebaju = angka(">> Masukan No Baju     : ")
    #inputan jumlah baju
    iptjumalahbaju = angka(">> Masukan Jumlah beli     : ")

    #inputan ukuran baju
    iptukuran = input(">> Pilih Ukuran (S/M/L/XL) : ").upper()
    while iptukuran not in listukuran:
        print("UKURAN YANG KAMU PILIH TIDAK TERSEDIA")
        iptukuran = input(">> Pilih Ukuran (S/M/L/XL) : ").upper()

    for i in range(len(listNo)):
        if iptkodebaju == listNo[i]:
            kodebaju = listNo[i]
            baju = listjenisBaju[i]
            hrg = listharga[i]
            tothrg = hrg * iptjumalahbaju
    output_pilihan()

    listbaju.append (baju)
    listjumlah.append (iptjumalahbaju)
    listsemuaUkuran.append (iptukuran)
    listtothrg.append (tothrg)
    listhrgsat.append (hrg)

    iptTambah = tambah("\n>> Tambah Lagi y/t : ")
    hrgsemuaitem = sum(listtothrg)

output_beli()
print("\n>> Total Bayar :",format(hrgsemuaitem,",.2f"))
bayar = int(input(">> Bayar       : "))
kembalian = bayar - hrgsemuaitem
print(">> Kembalian   :", format(kembalian,",.2f"))

iptkeluar = input("\nKetik Apa Saja Untuk Keluar : ")
