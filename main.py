"""
jb -> Judul buku
jbb -> jumlah buku
np -> nama peminjam
jp -> Jumlah peminjam
tb -> Total biaya
bl -> Buku list

"""
BiayaPerHari = 3000

# INPUT
print("="*50)
print("SISTEM MANAJEMEN PERPUSTAKAAN (SIMPUS)".center(50))
print("="*50)

# Masukan nama peminjaman
np = input("Nama peminjaman: ")
# Masukan jumlah buku
jbb = int(input("Masukan jumlah buku yang ingin dipinjam: "))

# Array untuk menyimpan data buku dan hari
bl = []
# deklarasi total biaya
tb = 0

# Perulangan untuk input data buku
for i in range(jbb):
    print(f"buku {i+1}:")
    jb = input("Judul buku : ")

    # Perulangan jika jumlah hari <= 0 dan > 30
    while(True):
        try:
            jp = int(input("Masukan jumlah hari peminjaman: "))
            if jp <= 0:
                print("Jumlah hari harus lebih dari 0!")
                continue
            if jp > 30:
                print("PERINGATAN! MAXIMAL PEMINJAMAN 30 HARI")
                continue
            break
        # Output jika masukan bukan angka
        except ValueError:
            print("Masukan hanya angka!")
    
    # untuk menyimpan data buku ke array
    bl.append({
        'nama': jb, #'nama' untuk menyimpan data nama buku
        'hari': jp #'hari' untuk menyimpan data hari  peminjaman buku
    })
    # menghitung biaya buku
    bb = jp*BiayaPerHari
    # menambahkan biaya buku ke total biaya
    tb += bb

# OUTPUT
print("\n" + "="*50)
# menggunakan fungsi capitalize() untuk mengkapitalkan huruf pertama
print(f"Nama peminjam: {np.capitalize()}")
# Perulangan untuk print data nama buku, jumlah hari, dan biaya buku 
for i, buku in enumerate (bl, 1):
    print(f"Buku {i}:")
    print(f"nama buku: {buku['nama'].capitalize()}")
    print(f"Jumlah Hari peminjaman: {buku['hari']} hari")
    # biaya = jumlah hari x biaya per hari
    print(f"Biaya: Rp.{buku['hari']*BiayaPerHari}" + "\n")
print(f"TOTAL BIAYA: Rp.{tb}")

print("="*50)
print("Terima kasih sudah memakai layanan kami!".center(50))

"""
Made by Kelompok 10 TI-B
- Immanuel Rey Usmin Sinaga
- Muhammad Ilham Jamaluddin
- Maulana Ibrahim
"""
