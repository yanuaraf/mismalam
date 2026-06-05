import streamlit as st

st.set_page_config(page_title="Sistem Antrian Bank", page_icon="🏦", layout="wide")

# Inisialisasi data antrian
if "antrian_prioritas" not in st.session_state:
    st.session_state.antrian_prioritas = []
if "antrian_lansia" not in st.session_state:
    st.session_state.antrian_lansia = []
if "antrian_reguler" not in st.session_state:
    st.session_state.antrian_reguler = []

# Inisialisasi nomor urut
if "nomor_prioritas" not in st.session_state:
    st.session_state.nomor_prioritas = 1
if "nomor_lansia" not in st.session_state:
    st.session_state.nomor_lansia = 1
if "nomor_reguler" not in st.session_state:
    st.session_state.nomor_reguler = 1

# Data nasabah yang sedang dipanggil
if "panggilan_sekarang" not in st.session_state:
    st.session_state.panggilan_sekarang = None

# Tampilan Utama
st.title("🏦 Sistem Antrian Bank Prioritas")
st.write("Aplikasi manajemen antrian nasabah berbasis web.")
st.divider()

# Membagi halaman menjadi dua kolom
kolom_kiri, kolom_kanan = st.columns([1, 1])

with kolom_kiri:
    st.header("Pendaftaran Nasabah")
    
    nama = st.text_input("Nama Nasabah:")
    kategori = st.selectbox("Pilih Kategori:", ["Prioritas", "Lansia", "Reguler"])

    if st.button("Ambil Antrian"):
        if nama:
            if kategori == "Prioritas":
                kode = f"P{st.session_state.nomor_prioritas:03d}"
                st.session_state.antrian_prioritas.append({"nomor": kode, "nama": nama})
                st.session_state.nomor_prioritas += 1
            elif kategori == "Lansia":
                kode = f"L{st.session_state.nomor_lansia:03d}"
                st.session_state.antrian_lansia.append({"nomor": kode, "nama": nama})
                st.session_state.nomor_lansia += 1
            elif kategori == "Reguler":
                kode = f"R{st.session_state.nomor_reguler:03d}"
                st.session_state.antrian_reguler.append({"nomor": kode, "nama": nama})
                st.session_state.nomor_reguler += 1
            
            st.success(f"Nomor antrian {kode} berhasil dibuat untuk {nama}")
            st.balloons()
        else:
            st.warning("Silakan isi nama nasabah terlebih dahulu!")

    st.divider()

    st.header("Panggil Antrian")
    if st.button("Panggil Berikutnya", type="primary", use_container_width=True):
        if st.session_state.antrian_prioritas:
            st.session_state.panggilan_sekarang = st.session_state.antrian_prioritas.pop(0)
            st.session_state.panggilan_sekarang["jenis"] = "Prioritas"
        elif st.session_state.antrian_lansia:
            st.session_state.panggilan_sekarang = st.session_state.antrian_lansia.pop(0)
            st.session_state.panggilan_sekarang["jenis"] = "Lansia"
        elif st.session_state.antrian_reguler:
            st.session_state.panggilan_sekarang = st.session_state.antrian_reguler.pop(0)
            st.session_state.panggilan_sekarang["jenis"] = "Reguler"
        else:
            st.session_state.panggilan_sekarang = None
            st.warning("Semua antrian sudah kosong.")

    # Menampilkan data yang dipanggil
    if st.session_state.panggilan_sekarang:
        nsb = st.session_state.panggilan_sekarang
        st.info(f"### Nomor: {nsb['nomor']} \n### Nama: {nsb['nama']} \nKategori: {nsb['jenis']}")

with kolom_kanan:
    st.header("Status Antrian")
    
    total_prioritas = len(st.session_state.antrian_prioritas)
    total_lansia = len(st.session_state.antrian_lansia)
    total_reguler = len(st.session_state.antrian_reguler)
    total_semua = total_prioritas + total_lansia + total_reguler

    st.write(f"**Total sisa antrian:** {total_semua} orang")
    
    with st.expander(f"Antrian Prioritas ({total_prioritas})", expanded=True):
        if total_prioritas == 0:
            st.text("Kosong")
        for orang in st.session_state.antrian_prioritas:
            st.text(f"- {orang['nomor']} : {orang['nama']}")

    with st.expander(f"Antrian Lansia ({total_lansia})", expanded=True):
        if total_lansia == 0:
            st.text("Kosong")
        for orang in st.session_state.antrian_lansia:
            st.text(f"- {orang['nomor']} : {orang['nama']}")

    with st.expander(f"Antrian Reguler ({total_reguler})", expanded=True):
        if total_reguler == 0:
            st.text("Kosong")
        for orang in st.session_state.antrian_reguler:
            st.text(f"- {orang['nomor']} : {orang['nama']}")

    st.divider()
    
    if st.button("Reset Semua Antrian", use_container_width=True):
        st.session_state.antrian_prioritas.clear()
        st.session_state.antrian_lansia.clear()
        st.session_state.antrian_reguler.clear()
        st.session_state.panggilan_sekarang = None
        st.rerun()
