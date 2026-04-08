# 1. DATA GEJALA (SYMPTOMS)
SYMPTOMS: dict[str, dict] = {
    "G01": {"teks": "Laptop tidak menyala saat tombol power ditekan"},
    "G02": {"teks": "Lampu indikator charger tidak menyala"},
    "G03": {"teks": "Laptop hanya menyala saat charger terpasang"},
    "G04": {"teks": "Baterai tidak mengisi (charging) meskipun charger terpasang"},
    "G05": {"teks": "Baterai cepat habis meskipun baru diisi penuh"},
    "G06": {"teks": "Terdengar bunyi beep berulang saat startup"},
    "G07": {"teks": "Layar blank/hitam tetapi lampu power menyala"},
    "G08": {"teks": "Laptop terasa sangat panas saat digunakan"},
    "G09": {"teks": "Laptop mati sendiri setelah beberapa menit penggunaan"},
    "G10": {"teks": "Kipas laptop sangat bising atau ventilasi terasa sangat panas"},
    "G11": {"teks": "Muncul pesan 'No bootable device' atau gagal boot"},
    "G12": {"teks": "Laptop sangat lambat dan sering hang/freeze"},
    "G13": {"teks": "Bisa masuk BIOS tetapi gagal masuk sistem operasi"},
    "G14": {"teks": "Beberapa tombol keyboard tidak berfungsi"},
    "G15": {"teks": "Keyboard mengetik sendiri atau menghasilkan input ganda"},
    "G16": {"teks": "Layar bergaris, berkedip-kedip, atau ada artefak visual"},
    "G17": {"teks": "Tampilan pada monitor eksternal normal"},
    "G18": {"teks": "Adaptor atau kabel charger longgar, terkelupas, atau tidak stabil"},
    "G19": {"teks": "LED power berkedip tetapi laptop tidak start normal"},
    "G20": {"teks": "Laptop hidup sebentar (1-3 detik) lalu mati lagi"},
    "G21": {"teks": "Tidak ada tampilan di layar dan tidak ada bunyi beep"},
    "G22": {"teks": "Touchpad tidak merespons atau pointer meloncat-loncat"},
    "G23": {"teks": "WiFi sering putus atau tidak mendeteksi jaringan apapun"},
    "G24": {"teks": "Suara speaker pecah, terdistorsi, atau tidak keluar suara sama sekali"},
    "G25": {"teks": "Port USB tidak mendeteksi perangkat yang dihubungkan"}
}

# 2. DATA KERUSAKAN & SOLUSI DETAIL (FRAMES)
FRAMES: dict[str, dict] = {
    "K01": {
        "nama": "Adaptor/Charger Rusak",
        "penyebab": "Suplai daya adaptor tidak stabil atau kabel rusak",
        "solusi_detail": (
            "1. Periksa lampu indikator adaptor.\n"
            "2. Coba gunakan adaptor/charger lain yang kompatibel.\n"
            "3. Periksa kabel apakah ada kerusakan fisik (terkelupas, patah).\n"
            "4. Ukur output tegangan adaptor dengan multimeter jika memungkinkan."
        )
    },
    "K02": {
        "nama": "Baterai Rusak/Drop",
        "penyebab": "Sel baterai melemah atau charging circuit error",
        "solusi_detail": (
            "1. Cek battery health melalui software diagnostik bawaan.\n"
            "2. Lakukan kalibrasi: charge 100% -> discharge hingga mati -> charge lagi.\n"
            "3. Jika health < 40%, pertimbangkan ganti baterai.\n"
            "4. Pastikan charger yang digunakan kompatibel dan berfungsi."
        )
    },
    "K03": {
        "nama": "RAM Bermasalah",
        "penyebab": "RAM longgar, pin kotor, atau modul rusak",
        "solusi_detail": (
            "1. Matikan laptop dan lepas baterai.\n"
            "2. Buka slot RAM, lepas modul RAM.\n"
            "3. Bersihkan pin kontak dengan penghapus pensil putih.\n"
            "4. Pasang kembali RAM hingga terdengar 'klik'."
        )
    },
    "K04": {
        "nama": "Overheating Sistem Pendingin",
        "penyebab": "Kipas kotor, heatsink tersumbat, atau thermal paste mengering",
        "solusi_detail": (
            "1. Bersihkan ventilasi dan kipas dari debu.\n"
            "2. Ganti thermal paste pada prosesor dan GPU.\n"
            "3. Gunakan cooling pad sebagai solusi sementara."
        )
    },
    "K05": {
        "nama": "LCD/Fleksibel Display Bermasalah",
        "penyebab": "Panel LCD rusak atau kabel fleksibel display putus/longgar",
        "solusi_detail": (
            "1. Hubungkan laptop ke monitor eksternal.\n"
            "2. Jika eksternal normal, masalah ada di LCD/kabel fleksibel internal.\n"
            "3. Bawa ke teknisi untuk penggantian panel LCD."
        )
    },
    "K06": {
        "nama": "HDD/SSD atau Boot System Bermasalah",
        "penyebab": "Storage rusak, bad sector, atau boot record corrupt",
        "solusi_detail": (
            "1. Masuk BIOS -> cek apakah HDD/SSD terdeteksi.\n"
            "2. Jalankan CHKDSK (Windows) untuk cek bad sector.\n"
            "3. Coba repair boot menggunakan USB instalasi OS."
        )
    },
    "K07": {
        "nama": "Keyboard Rusak",
        "penyebab": "Matriks keyboard rusak atau kabel fleksibel keyboard putus",
        "solusi_detail": (
            "1. Bersihkan keyboard dari debu.\n"
            "2. Uji dengan keyboard USB eksternal.\n"
            "3. Ganti keyboard internal jika masalah tetap ada."
        )
    },
    "K08": {
        "nama": "Motherboard/Power IC Bermasalah",
        "penyebab": "Komponen board-level rusak (power IC, audio IC, USB controller)",
        "solusi_detail": (
            "1. Kerusakan level board memerlukan skill teknis tinggi.\n"
            "2. Bawa ke teknisi spesialis reparasi motherboard.\n"
            "3. Jangan mencoba memperbaiki sendiri tanpa peralatan SMD."
        )
    },
    "K09": {
        "nama": "Touchpad Bermasalah",
        "penyebab": "Driver corrupt, kabel fleksibel longgar, atau modul touchpad rusak",
        "solusi_detail": (
            "1. Cek tombol Fn untuk mengaktifkan touchpad.\n"
            "2. Instal ulang driver touchpad dari situs resmi vendor.\n"
            "3. Cek koneksi kabel fleksibel touchpad di dalam laptop."
        )
    },
    "K10": {
        "nama": "Modul WiFi Bermasalah",
        "penyebab": "Driver corrupt, modul WiFi longgar, atau antena putus",
        "solusi_detail": (
            "1. Reset network settings pada sistem operasi.\n"
            "2. Re-seat (lepas pasang) modul WiFi card pada slotnya.\n"
            "3. Pastikan antena WiFi terpasang dengan benar pada modul."
        )
    }
}

# 3. ATURAN (RULES)
RULES: list[dict] = [
    {"rule_id": "R1", "premis": ["G01", "G02", "G18"], "konklusi": "K01"},
    {"rule_id": "R2", "premis": ["G03", "G04", "G05"], "konklusi": "K02"},
    {"rule_id": "R3", "premis": ["G06", "G07"], "konklusi": "K03"},
    {"rule_id": "R4", "premis": ["G08", "G09", "G10"], "konklusi": "K04"},
    {"rule_id": "R5", "premis": ["G07", "G16", "G17"], "konklusi": "K05"},
    {"rule_id": "R6", "premis": ["G11", "G12", "G13"], "konklusi": "K06"},
    {"rule_id": "R7", "premis": ["G14", "G15"], "konklusi": "K07"},
    {"rule_id": "R8", "premis": ["G19", "G20", "G21"], "konklusi": "K08"},
    {"rule_id": "R9", "premis": ["G22"], "konklusi": "K09"},
    {"rule_id": "R10", "premis": ["G23"], "konklusi": "K10"},
    {"rule_id": "R11", "premis": ["G24"], "konklusi": "K08"},
    {"rule_id": "R12", "premis": ["G25"], "konklusi": "K08"}
]