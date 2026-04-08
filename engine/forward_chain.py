from knowledge_base import SYMPTOMS, FRAMES, RULES

def forward_chaining(gejala_user: list[str]):
    """
    Melakukan diagnosa menggunakan metode Forward Chaining.
    Sistem mengecek irisan antara fakta (gejala user) dengan aturan (RULES).
    """
    hasil_diagnosa = []

    # Iterasi melalui setiap rule di RULES
    for rule in RULES:
        kode_k = rule["konklusi"]
        syarat_gejala = rule["premis"]
        
        # Logika: Mencari irisan (intersection) antara gejala user dan syarat pada Rule
        gejala_cocok = [kode_g for kode_g in syarat_gejala if kode_g in gejala_user]
        
        # Hitung statistik kecocokan
        matched_count = len(gejala_cocok)
        total_syarat = len(syarat_gejala)
        
        # Jika minimal ada 1 gejala yang cocok (Sesuai logika Anda sebelumnya)
        if matched_count > 0:
            # Ambil data detail dari FRAMES
            info_kerusakan = FRAMES.get(kode_k, {})
            
            hasil_diagnosa.append({
                'kode': kode_k,
                'nama': info_kerusakan.get("nama", "Tidak diketahui"),
                'persentase_match': round((matched_count / total_syarat) * 100, 2),
                'jumlah_cocok': matched_count,
                'total_syarat': total_syarat,
                'gejala_cocok': [SYMPTOMS[g]["teks"] for g in gejala_cocok],
                'penyebab': info_kerusakan.get("penyebab", "-"),
                'solusi_detail': info_kerusakan.get("solusi_detail", "-")
            })
            
    # Urutkan berdasarkan persentase kecocokan tertinggi
    return sorted(hasil_diagnosa, key=lambda x: x['persentase_match'], reverse=True)