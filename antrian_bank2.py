import streamlit as st
import time
from collections import deque

# Queue
antrian_prioritas = deque()
antrian_lansia = deque()
antrian_reguler = deque()

# Counter nomor antrian
nomor_prioritas = 1
nomor_lansia = 1
nomor_reguler = 1

while True:

    print("\n" + "=" * 55)
    print("      SISTEM ANTRIAN BANK PRIORITAS")
    print("=" * 55)

    print("1. Tambah Nasabah")
    print("2. Lihat Antrian")
    print("3. Panggil Nasabah")
    print("4. Statistik Antrian")
    print("5. Hapus Semua Antrian")
    print("6. Keluar")

    print("=" * 55)

    pilihan = input("Pilih menu (1-6): ")

    # ==================================================
    # TAMBAH NASABAH
    # ==================================================
    if pilihan == "1":

        nama = input("Masukkan Nama Nasabah : ")

        print("\nJenis Nasabah")
        print("1. Prioritas")
        print("2. Lansia")
        print("3. Reguler")

        jenis = input("Pilih Jenis (1/2/3) : ")

        if jenis == "1":

            nomor = f"P{nomor_prioritas:03d}"

            antrian_prioritas.append({
                "nomor": nomor,
                "nama": nama
            })

            nomor_prioritas += 1

            print(f"\nBerhasil ditambahkan!")
            print(f"Nomor Antrian : {nomor}")

        elif jenis == "2":

            nomor = f"L{nomor_lansia:03d}"

            antrian_lansia.append({
                "nomor": nomor,
                "nama": nama
            })

            nomor_lansia += 1

            print(f"\nBerhasil ditambahkan!")
            print(f"Nomor Antrian : {nomor}")

        elif jenis == "3":

            nomor = f"R{nomor_reguler:03d}"

            antrian_reguler.append({
                "nomor": nomor,
                "nama": nama
            })

            nomor_reguler += 1

            print(f"\nBerhasil ditambahkan!")
            print(f"Nomor Antrian : {nomor}")

        else:
            print("Pilihan tidak valid!")

    # ==================================================
    # LIHAT ANTRIAN
    # ==================================================
    elif pilihan == "2":

        print("\n===== ANTRIAN PRIORITAS =====")

        if not antrian_prioritas:
            print("Kosong")
        else:
            for data in antrian_prioritas:
                print(f"{data['nomor']} - {data['nama']}")

        print("\n===== ANTRIAN LANSIA =====")

        if not antrian_lansia:
            print("Kosong")
        else:
            for data in antrian_lansia:
                print(f"{data['nomor']} - {data['nama']}")

        print("\n===== ANTRIAN REGULER =====")

        if not antrian_reguler:
            print("Kosong")
        else:
            for data in antrian_reguler:
                print(f"{data['nomor']} - {data['nama']}")

    # ==================================================
    # PANGGIL NASABAH
    # ==================================================
    elif pilihan == "3":

        if antrian_prioritas:

            nasabah = antrian_prioritas.popleft()

            print("\n===== NASABAH DIPANGGIL =====")
            print(f"Nomor : {nasabah['nomor']}")
            print(f"Nama  : {nasabah['nama']}")
            print("Jenis : PRIORITAS")

        elif antrian_lansia:

            nasabah = antrian_lansia.popleft()

            print("\n===== NASABAH DIPANGGIL =====")
            print(f"Nomor : {nasabah['nomor']}")
            print(f"Nama  : {nasabah['nama']}")
            print("Jenis : LANSIA")

        elif antrian_reguler:

            nasabah = antrian_reguler.popleft()

            print("\n===== NASABAH DIPANGGIL =====")
            print(f"Nomor : {nasabah['nomor']}")
            print(f"Nama  : {nasabah['nama']}")
            print("Jenis : REGULER")

        else:
            print("\nTidak ada antrian.")

    # ==================================================
    # STATISTIK
    # ==================================================
    elif pilihan == "4":

        jumlah_prioritas = len(antrian_prioritas)
        jumlah_lansia = len(antrian_lansia)
        jumlah_reguler = len(antrian_reguler)

        total = (
            jumlah_prioritas +
            jumlah_lansia +
            jumlah_reguler
        )

        print("\n===== STATISTIK ANTRIAN =====")
        print(f"Prioritas : {jumlah_prioritas}")
        print(f"Lansia    : {jumlah_lansia}")
        print(f"Reguler   : {jumlah_reguler}")
        print("-" * 30)
        print(f"Total     : {total}")

    # ==================================================
    # HAPUS SEMUA
    # ==================================================
    elif pilihan == "5":

        antrian_prioritas.clear()
        antrian_lansia.clear()
        antrian_reguler.clear()

        print("\nSemua antrian berhasil dihapus.")

    # ==================================================
    # KELUAR
    # ==================================================
    elif pilihan == "6":

        print("\nTerima kasih telah menggunakan sistem.")
        break

    else:
        print("\nMenu tidak tersedia!")
