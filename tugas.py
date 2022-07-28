class pendaftaranqorik:
    def __init__(self,nama,tingkat,jenis_kelamin):
        self.nama = nama
        self.tingkat = tingkat
        self.jenis_kelamin = jenis_kelamin


    def keterangan(self):
        ket =""
        if jenis_kelamin == "L" or jenis_kelamin == "l":
            ket = "laki_laki"
        elif jenis_kelamin == "P" or jenis_kelamin == "p":
            ket = "perempuan"

        print("qorik dengan\n nama : {}\n tingkat : {}\n ".format(self.nama,self.tingkat,self.jenis_kelamin))
        
#program pendaftaran qorik
nama = input("masukkan nama :")
    
#jika menggunakan int maka 
#menetukan tingkat
tingkat = input("masukkan tingkat :")

# L = laki_laki
# P = perempuan


jenis_kelamin = input("pilih jenis_kelamin[L/P]: ")


pendaftaranqorik = pendaftaranqorik(nama, tingkat,jenis_kelamin)
pendaftaranqorik.keterangan()



            


        