import streamlit as st

# ==================================================
# 1. CONFIG & INITIALIZATION (SESSION STATE)
# ==================================================
st.set_page_config(page_title="Sistem Antrian Bank", page_icon="🏦", layout="wide")

if "antrian_prioritas" not in st.session_state:
    st.session_state.antrian_prioritas = []
if "antrian_lansia" not in st.session_state:
    st.session_state.antrian_lansia = []
if "antrian_reguler" not in st.session_state:
    st.session_state.antrian_reguler = []

if "nomor_prioritas" not in st.session_state:
    st.session_state.nomor_prioritas = 1
if "nomor_lansia" not in st.session_state:
    st.session_state.nomor_lansia = 1
if "nomor_reguler" not in st.session_state:
    st.session_state.nomor_reguler = 1

if "nasabah_dipanggil" not in st.session_state:
    st.session_state.nasabah_dipanggil = None


# ==================================================
# 2. HEADER & INPUT UTAMA
# ==================================================
st.title("🏦 Aplikasi Antrian Bank Pertamaku!")
st.write("Selamat! Kamu berhasil menggabungkan logika **Sistem Antrian Bank** ke dalam *interface* **Streamlit** yang interaktif dan dinamis.")

st.divider() # Garis pembatas dari kode kedua

# Membagi halaman menjadi 2 kolom (Kiri: Operasional | Kanan: Live Monitor)
col1, col2 = st.columns([1, 1])

with col1:
    # ----------------------------------------------
    # FITUR: TAMBAH NASABAH
    # ----------------------------------------------
    st.header("➕ Registrasi Nasabah")
    
    # Input komponen interaktif
    nama = st.text_input("Siapa nama nasabah?")
    jenis = st.selectbox("Pilih Kategori Nasabah:", ["Prioritas", "Lansia", "Reguler"])

    if st.button("Ambil Nomor Antrian"):
        if nama: # Validasi jika nama sudah diisi (Logika dari kode kedua)
            if jenis == "Prioritas":
                nomor = f"P{st.session_state.nomor_prioritas:03d}"
                st.session_state.antrian_prioritas.append({"nomor": nomor, "nama": nama})
                st.session_state.nomor_prioritas += 1
            elif jenis == "Lansia":
                nomor = f"L{st.session_state.nomor_lansia:03d}"
                st.session_state.antrian_lansia.append({"nomor": nomor, "nama": nama})
                st.session_state.nomor_lansia += 1
            elif jenis == "Reguler":
                nomor = f"R{st.session_state.nomor_reguler:03d}"
                st.session_state.antrian_reguler.append({"nomor": nomor, "nama": nama})
                st.session_state.nomor_reguler += 1
            
            # Memunculkan alert sukses dan animasi balon (Dari kode kedua)
            st.success(f"Sukses! Nomor Antrian **{nomor}** dibuat untuk **{nama}** ({jenis})")
            st.balloons() 
            
        else:
            # Memunculkan alert peringatan jika teks input kosong (Dari kode kedua)
            st.warning("Isi nama nasabah terlebih dahulu di kotak atas!")

    st.divider()

    # ----------------------------------------------
    # FITUR: PANGGIL NASABAH (LOGIKA HIERARKI)
    # ----------------------------------------------
    st.header("📢 Loket Panggilan")
    if st.button("Panggil Antrian Berikutnya", type="primary", use_container_width=True):
        # Menyaring urutan prioritas: Prioritas -> Lansia -> Reguler
        if st.session_state.antrian_prioritas:
            st.session_state.nasabah_dipanggil = st.session_state.antrian_prioritas.pop(0)
            st.session_state.nasabah_dipanggil["jenis"] = "PRIORITAS"
        elif st.session_state.antrian_lansia:
            st.session_state.nasabah_dipanggil = st.session_state.antrian_lansia.pop(0)
            st.session_state.nasabah_dipanggil["jenis"] = "LANSIA"
        elif st.session_state.antrian_reguler:
            st.session_state.nasabah_dipanggil = st.session_state.antrian_reguler.pop(0)
            st.session_state.nasabah_dipanggil["jenis"] = "REGULER"
        else:
            st.session_state.nasabah_dipanggil = None

    # Menampilkan papan info panggilan saat ini
    if st.session_state.nasabah_dipanggil:
        nsb = st.session_state.nasabah_dipanggil
        st.info(f"### Menuju Loket: **{nsb['nomor']}** - {nsb['nama']} [{nsb['jenis']}]")
    else:
        st.caption("Belum ada panggilan aktif atau antrian kosong.")


with col2:
    # ==================================================
    # 3. LIVE MONITOR & STATISTIK
    # ==================================================
    st.header("📊 Monitor Antrian")
    
    # Membaca panjang list antrian saat ini
    len_p = len(st.session_state.antrian_prioritas)
    len_l = len(st.session_state.antrian_lansia)
    len_r = len(st.session_state.antrian_reguler)
    total_sisa = len_p + len_l + len_r

    # Menampilkan visual data statistik ringkas
    st.subheader(f"Total Sisa Antrian: {total_sisa} Orang")
    
    # Menampilkan list isi antrian menggunakan komponen Expander
    with st.expander(f"🔴 Antrian Prioritas ({len_p})", expanded=True):
        if len_p == 0: st.text("Kosong")
        for data in st.session_state.antrian_prioritas:
            st.text(f"• {data['nomor']} - {data['nama']}")

    with st.expander(f"🟡 Antrian Lansia ({len_l})", expanded=True):
        if len_l == 0: st.text("Kosong")
        for data in st.session_state.antrian_lansia:
            st.text(f"• {data['nomor']} - {data['nama']}")

    with st.expander(f"🟢 Antrian Reguler ({len_r})", expanded=True):
        if len_r == 0: st.text("Kosong")
        for data in st.session_state.antrian_reguler:
            st.text(f"• {data['nomor']} - {data['nama']}")

    st.divider()
    
    # ----------------------------------------------
    # FITUR: RESET ALL
    # ----------------------------------------------
    if st.button("Hapus Semua Antrian", use_container_width=True):
        st.session_state.antrian_prioritas.clear()
        st.session_state.antrian_lansia.clear()
        st.session_state.antrian_reguler.clear()
        st.session_state.nasabah_dipanggil = None
        st.rerun() # Memaksa halaman refresh seketika
