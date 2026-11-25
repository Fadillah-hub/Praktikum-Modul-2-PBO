class Mahasiswa:
    def __init__(self, nim, nama, semester, ipk):
        self.nim = nim
        self.nama = nama
        self._semester = semester
        self.__ipk = ipk

    # Getter semester
    def get_semester(self):
        return self._semester

    # Setter semester
    def set_semester(self, semester):
        if semester < 1:
            raise ValueError("Semester tidak valid.")
        self._semester = semester

    # Getter IPK
    def get_ipk(self):
        return self.__ipk

    # Setter IPK
    def set_ipk(self, ipk):
        if not (0.0 <= ipk <= 4.0):
            raise ValueError("IPK harus antara 0.0 dan 4.0.")
        self.__ipk = round(ipk, 2)


# Contoh penggunaan
if __name__ == "__main__":

    # Membuat 2 objek mahasiswa
    mhs1 = Mahasiswa("23001", "Fadillah", 3, 3.75)
    mhs2 = Mahasiswa("23002", "Uppa", 5, 3.90)

    # Mengubah semester dan IPK
    mhs1.set_semester(4)
    mhs1.set_ipk(3.85)

    mhs2.set_semester(6)
    mhs2.set_ipk(3.95)

    # Menampilkan data mahasiswa pertama
    print("=== Data Mahasiswa 1 ===")
    print("NIM:", mhs1.nim)
    print("Nama:", mhs1.nama)
    print("Semester:", mhs1.get_semester())
    print("IPK:", mhs1.get_ipk())

    print()

    # Menampilkan data mahasiswa kedua
    print("=== Data Mahasiswa 2 ===")
    print("NIM:", mhs2.nim)
    print("Nama:", mhs2.nama)
    print("Semester:", mhs2.get_semester())
    print("IPK:", mhs2.get_ipk())