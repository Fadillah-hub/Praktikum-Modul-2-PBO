# ==================================================
# A. MEMBUAT CLASS BUKU
# ==================================================

class Buku:
    def __init__(self, judul, penulis, kode_buku, stok, lokasi_rak):
        # Public
        self.judul = judul
        self.penulis = penulis
        self.kode_buku = kode_buku

        # Protected
        self._stok = stok

        # Private
        self.__lokasi_rak = lokasi_rak

    # Getter lokasi rak
    def get_lokasi_rak(self):
        return self.__lokasi_rak

    # Setter lokasi rak
    def set_lokasi_rak(self, lokasi):
        self.__lokasi_rak = lokasi

    # Menambah stok buku
    def tambah_stok(self, jumlah):
        self._stok += jumlah

    # Mengurangi stok buku
    def kurangi_stok(self, jumlah):
        if self._stok >= jumlah:
            self._stok -= jumlah
            return True
        return False

    def info_buku(self):
        print("Kode Buku  :", self.kode_buku)
        print("Judul      :", self.judul)
        print("Penulis    :", self.penulis)
        print("Stok       :", self._stok)
        print("Lokasi Rak :", self.__lokasi_rak)


# ==================================================
# B. MEMBUAT CLASS ANGGOTA
# ==================================================

class Anggota:
    def __init__(self, id_anggota, nama):
        # Public
        self.id_anggota = id_anggota
        self.nama = nama

        # Protected
        self._maks_pinjam = 2

        # Private
        self.__status_aktif = True

        # Aggregation: daftar peminjaman
        self.daftar_peminjaman = []

    # Getter status
    def get_status(self):
        return self.__status_aktif

    # Setter status
    def set_status(self, status):
        self.__status_aktif = status

    # Meminjam buku
    def pinjam_buku(self, buku, tanggal_pinjam, tanggal_kembali):
        if not self.__status_aktif:
            print("Anggota tidak aktif!")
            return

        if len(self.daftar_peminjaman) >= self._maks_pinjam:
            print("Maksimal peminjaman adalah 2 buku!")
            return

        if buku._stok <= 0:
            print("Stok buku habis!")
            return

        peminjaman = Peminjaman(
            buku,
            self,
            tanggal_pinjam,
            tanggal_kembali
        )

        buku.kurangi_stok(1)
        self.daftar_peminjaman.append(peminjaman)

        print(self.nama, "berhasil meminjam buku:", buku.judul)

    # Mengembalikan buku
    def kembalikan_buku(self, kode_buku):
        for peminjaman in self.daftar_peminjaman:
            if (peminjaman.buku.kode_buku == kode_buku
                    and peminjaman.status == "Dipinjam"):

                peminjaman.status = "Dikembalikan"
                peminjaman.buku.tambah_stok(1)

                print("Buku", peminjaman.buku.judul,
                      "berhasil dikembalikan.")
                return

        print("Data peminjaman tidak ditemukan!")

    def info_anggota(self):
        print("ID Anggota :", self.id_anggota)
        print("Nama       :", self.nama)
        print("Status     :", "Aktif" if self.__status_aktif else "Tidak Aktif")
        print("Maksimal Pinjam :", self._maks_pinjam)


# ==================================================
# C. MEMBUAT CLASS PEMINJAMAN
# ==================================================

class Peminjaman:
    def __init__(self, buku, anggota, tanggal_pinjam, tanggal_kembali):
        # Association: Peminjaman berhubungan dengan Buku
        self.buku = buku

        # Hubungan dengan Anggota
        self.anggota = anggota

        self.kode_buku = buku.kode_buku
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali
        self.status = "Dipinjam"

    # Menampilkan informasi peminjaman
    def info_peminjaman(self):
        print("Kode Buku      :", self.kode_buku)
        print("Judul Buku     :", self.buku.judul)
        print("Nama Anggota   :", self.anggota.nama)
        print("Tanggal Pinjam :", self.tanggal_pinjam)
        print("Tanggal Kembali:", self.tanggal_kembali)
        print("Status         :", self.status)


# ==================================================
# D. INSTANSIASI / MEMBUAT OBJEK
# ==================================================

# Composition: Perpustakaan memiliki daftar buku
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, judul, penulis, kode_buku, stok, lokasi_rak):
        buku = Buku(judul, penulis, kode_buku, stok, lokasi_rak)
        self.daftar_buku.append(buku)
        return buku


# Membuat objek perpustakaan
perpustakaan = Perpustakaan("Perpustakaan STITEK")

# Membuat 3 buku
buku1 = perpustakaan.tambah_buku(
    "Pemrograman Python", "Budi Santoso", "B001", 5, "A1"
)

buku2 = perpustakaan.tambah_buku(
    "Belajar OOP", "Andi Wijaya", "B002", 3, "A2"
)

buku3 = perpustakaan.tambah_buku(
    "Dasar Basis Data", "Siti Aminah", "B003", 4, "B1"
)

# Membuat 2 anggota
anggota1 = Anggota("A001", "Fadillah")
anggota2 = Anggota("A002", "Uppa")

# Anggota 1 meminjam 2 buku
anggota1.pinjam_buku(buku1, "25-11-2026", "02-12-2026")
anggota1.pinjam_buku(buku2, "25-11-2026", "02-12-2026")

# Anggota 2 meminjam 1 buku
anggota2.pinjam_buku(buku3, "25-11-2026", "02-12-2026")

# Pengembalian buku
anggota1.kembalikan_buku("B001")


# ==================================================
# E. DEMONSTRASI PROGRAM MENGGUNAKAN PRINT()
# ==================================================

print("\n======================================")
print(" INFORMASI PERPUSTAKAAN")
print("======================================")
print("Nama Perpustakaan:", perpustakaan.nama)


# 1. Informasi buku dan stoknya
print("\n======================================")
print(" INFORMASI BUKU DAN STOK")
print("======================================")

for buku in perpustakaan.daftar_buku:
    buku.info_buku()
    print("------------------------------")


# 2. Informasi anggota
print("\n======================================")
print(" INFORMASI ANGGOTA")
print("======================================")

anggota1.info_anggota()
print("------------------------------")
anggota2.info_anggota()


# 3. Daftar peminjaman masing-masing anggota
print("\n======================================")
print(" DAFTAR PEMINJAMAN ANGGOTA 1")
print("======================================")

for peminjaman in anggota1.daftar_peminjaman:
    peminjaman.info_peminjaman()
    print("------------------------------")


print("\n======================================")
print(" DAFTAR PEMINJAMAN ANGGOTA 2")
print("======================================")

for peminjaman in anggota2.daftar_peminjaman:
    peminjaman.info_peminjaman()
    print("------------------------------")
