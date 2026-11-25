class Nilai:
    def __init__(self, kode_mk: str, skor: float):
        self.kode_mk = kode_mk
        self.skor = skor


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.daftar_nilai = []

    def tambah_nilai(self, nilai):
        self.daftar_nilai.append(nilai)

    def rata_rata(self):
        if not self.daftar_nilai:
            return 0

        total = sum(n.skor for n in self.daftar_nilai)
        return total / len(self.daftar_nilai)


class MataKuliah:
    def __init__(self, kode: str, nama: str):
        self.kode = kode
        self.nama = nama


class ProgramStudi:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_matakuliah = []

    def tambah_matakuliah(self, mk: MataKuliah):
        self.daftar_matakuliah.append(mk)


class Universitas:
    def __init__(self, nama):
        self.nama = nama
        self.programs = []

    def buat_program(self, nama_prodi):
        prodi = ProgramStudi(nama_prodi)
        self.programs.append(prodi)
        return prodi


if __name__ == "__main__":
    uni = Universitas("Universitas A")

    # Membuat 3 Program Studi
    prodi_ti = uni.buat_program("Teknik Informatika")
    prodi_si = uni.buat_program("Sistem Informasi")
    prodi_bd = uni.buat_program("Bisnis Digital")

    # Mata Kuliah Teknik Informatika
    mk1 = MataKuliah("TI101", "Pemrograman Dasar")
    mk2 = MataKuliah("TI102", "Struktur Data")

    prodi_ti.tambah_matakuliah(mk1)
    prodi_ti.tambah_matakuliah(mk2)

    # Mata Kuliah Sistem Informasi
    mk3 = MataKuliah("SI101", "Analisis Sistem")
    mk4 = MataKuliah("SI102", "Basis Data")

    prodi_si.tambah_matakuliah(mk3)
    prodi_si.tambah_matakuliah(mk4)

    # Mata Kuliah Bisnis Digital
    mk5 = MataKuliah("BD101", "Akuntansi Dasar")
    mk6 = MataKuliah("BD102", "Sistem Informasi Manajemen")

    prodi_bd.tambah_matakuliah(mk5)
    prodi_bd.tambah_matakuliah(mk6)

    # Membuat 3 mahasiswa
    m1 = Mahasiswa("23001", "Fadillah")
    m2 = Mahasiswa("23002", "Uppa")
    m3 = Mahasiswa("23003", "Illa")

    # Menambahkan nilai mahasiswa
    m1.tambah_nilai(Nilai("TI101", 85))
    m1.tambah_nilai(Nilai("TI102", 78))
    m1.tambah_nilai(Nilai("SI101", 88))

    m2.tambah_nilai(Nilai("TI101", 90))
    m2.tambah_nilai(Nilai("SI102", 85))
    m2.tambah_nilai(Nilai("BD101", 92))

    m3.tambah_nilai(Nilai("TI102", 80))
    m3.tambah_nilai(Nilai("SI101", 87))
    m3.tambah_nilai(Nilai("BD102", 89))

    semua_mahasiswa = [m1, m2, m3]

    # Menampilkan rata-rata setiap mahasiswa
    print("=== RATA-RATA NILAI MAHASISWA ===")

    for m in semua_mahasiswa:
        print(f"{m.nim} - {m.nama}: {m.rata_rata():.2f}")

    # Fungsi laporan Program Studi
    def report_program(prodi: ProgramStudi, semua_mahasiswa: list[Mahasiswa]):
        print(f"\nProgram Studi: {prodi.nama}")

        print(
            "Matakuliah:",
            ", ".join([mk.kode for mk in prodi.daftar_matakuliah]) or "-"
        )

        print("Mahasiswa dan rata-rata nilai:")

        for m in semua_mahasiswa:
            relevan = [
                n for n in m.daftar_nilai
                if any(
                    n.kode_mk == mk.kode
                    for mk in prodi.daftar_matakuliah
                )
            ]

            if relevan:
                avg = sum(n.skor for n in relevan) / len(relevan)
                print(f"- {m.nim} - {m.nama}: {round(avg, 2)}")
            else:
                print(f"- {m.nim} - {m.nama}: -")

    # Memanggil fungsi report_program untuk setiap Program Studi
    print("\n=== LAPORAN PROGRAM STUDI ===")

    report_program(prodi_ti, semua_mahasiswa)
    report_program(prodi_si, semua_mahasiswa)
    report_program(prodi_bd, semua_mahasiswa)

    # Menampilkan seluruh Program Studi dan Mata Kuliah
    print("\n=== DAFTAR PROGRAM STUDI UNIVERSITAS ===")

    for prodi in uni.programs:
        print(f"\nProgram Studi: {prodi.nama}")

        for mk in prodi.daftar_matakuliah:
            print(f"- {mk.kode}: {mk.nama}")