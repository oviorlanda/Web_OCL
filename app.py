import streamlit as st

# =====================
# PAGE CONFIG
# =====================
st.set_page_config(
    page_title="Optical Communication Laboratory",
    page_icon="🔬",
    layout="wide"
)

# =====================
# SIDEBAR MENU
# =====================
menu = st.sidebar.radio(
    "📌 MENU",
    [
        "HOME",
        "ABOUT US",
        "OUR TEAM",
        "OUR ACTIVITY",
        "INFORMATIONS",
        "RESEARCH & PUBLICATIONS",
        "LAB FACILITIES",
        "PRACTICUM MODULES",
        "AI: OPTICAL SIGNAL DETECTION"
    ]
)

# =====================
# HEADER
# =====================
st.title("🔬 Optical Communication Laboratory (OCL)")
st.caption("Education • Research • Innovation")
st.divider()

# =====================
# HOME
# =====================
if menu == "HOME":
    st.subheader("🏠 HOME")
    st.markdown("""
    **Optical Communication Laboratory (OCL)** merupakan laboratorium
    yang berfokus pada pengembangan ilmu dan praktikum di bidang
    komunikasi optik dan fotonika.

    **Fokus utama laboratorium:**
    - Sistem komunikasi serat optik
    - Analisis redaman dan dispersi
    - Jaringan optik dan fotonik
    """)

# =====================
# ABOUT US
# =====================
elif menu == "ABOUT US":
    st.subheader("📘 ABOUT US")
    st.markdown("""
    Optical Communication Laboratory berperan sebagai sarana pendukung
    kegiatan akademik, penelitian, dan pengembangan teknologi
    komunikasi berbasis cahaya.

    Laboratorium ini mendukung:
    - Praktikum mahasiswa
    - Penelitian dosen dan mahasiswa
    - Kegiatan akademik dan inovasi
    """)

# =====================
# OUR TEAM
# =====================
elif menu == "OUR TEAM":
    st.subheader("👥 OUR TEAM")
    st.markdown("""
    - Kepala Laboratorium  
    - Dosen Pembimbing  
    - Asisten Laboratorium  
    - Mahasiswa Peneliti
    """)

# =====================
# OUR ACTIVITY
# =====================
elif menu == "OUR ACTIVITY":
    st.subheader("🧪 OUR ACTIVITY")
    activities = [
        "Praktikum Komunikasi Optik",
        "Penelitian Serat Optik",
        "Seminar dan Workshop",
        "Pengabdian Masyarakat"
    ]
    for act in activities:
        st.markdown(f"- {act}")

# =====================
# INFORMATIONS
# =====================
elif menu == "INFORMATIONS":
    st.subheader("ℹ️ INFORMATIONS")
    st.info("📅 Jadwal praktikum akan diumumkan melalui website.")
    st.success("📢 Open recruitment asisten laboratorium.")
    st.warning("⏰ Deadline laporan praktikum: Jumat, 17.00 WIB.")

# =====================
# RESEARCH & PUBLICATIONS
# =====================
elif menu == "RESEARCH & PUBLICATIONS":
    st.subheader("🔬 RESEARCH & PUBLICATIONS")
    st.markdown("""
    **Topik Riset Unggulan:**
    - Optical Fiber Communication
    - Dispersion & Attenuation Analysis
    - Dense Wavelength Division Multiplexing (DWDM)
    - Photonic Devices

    **Publikasi:**
    - Jurnal ilmiah
    - Prosiding konferensi nasional & internasional
    """)

# =====================
# LAB FACILITIES
# =====================
elif menu == "LAB FACILITIES":
    st.subheader("🧰 LAB FACILITIES")
    st.markdown("""
    **Peralatan Laboratorium:**
    - Optical Time Domain Reflectometer (OTDR)
    - Optical Power Meter
    - Laser Source
    - Optical Spectrum Analyzer
    """)

# =====================
# PRACTICUM MODULES
# =====================
elif menu == "PRACTICUM MODULES":
    st.subheader("📘 PRACTICUM MODULES")
    modules = [
        "Modul 1: Pengenalan Serat Optik",
        "Modul 2: Pengukuran Redaman",
        "Modul 3: Analisis Dispersi",
        "Modul 4: Sistem Komunikasi Optik"
    ]
    for mod in modules:
        st.markdown(f"- {mod}")

# =====================
# AI FEATURE
# =====================
elif menu == "AI: OPTICAL SIGNAL DETECTION":
    st.subheader("🧠 Optical Signal Quality Detection")

    st.markdown("""
    Fitur ini digunakan untuk **mendeteksi kualitas sinyal optik**
    berdasarkan parameter transmisi.  
    Tujuannya adalah membantu mahasiswa memahami pengaruh jarak,
    redaman, dan daya terhadap performa sistem komunikasi optik.
    """)

    # Input
    input_power = st.number_input("Input Power (dBm)", -30.0, 10.0, -10.0)
    distance = st.slider("Distance (km)", 1, 100, 10)
    attenuation = st.number_input("Attenuation (dB/km)", 0.1, 1.0, 0.25)

    # Calculation
    total_loss = distance * attenuation
    received_power = input_power - total_loss

    st.divider()
    st.markdown("### 📊 Analysis Result")

    st.write(f"**Total Loss:** {total_loss:.2f} dB")
    st.write(f"**Received Power:** {received_power:.2f} dBm")

    # Decision
    if received_power > -20:
        st.success("🟢 Signal Quality: GOOD")
    elif received_power > -30:
        st.warning("🟡 Signal Quality: DEGRADED")
    else:
        st.error("🔴 Signal Quality: BAD")
