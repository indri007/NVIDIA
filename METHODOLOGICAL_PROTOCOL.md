# Standard Operating Procedure (SOP) & Methodological Protocol

> **Panduan Operasional Pengumpulan & Pengolahan Data untuk Peneliti (Q1 Research Standards)**  
> Disusun oleh: Indri Anjar Kartika Sari, Agung Budi Prasetio, Waspodo Tjipto Subroto (2026)  
> Repository: `silent-authority-tiktok-dataset`

Dokumen ini menetapkan alur kerja metodologis baku (*Standard Operating Procedure*) untuk menjamin bahwa seluruh data yang dikumpulkan memenuhi kriteria transparansi, legalitas, etika, dan keterulangan (*reproducibility*) yang dituntut oleh reviewer jurnal internasional bereputasi tinggi (Scopus Q1).

---

## 🗺️ Matriks Alur Kerja & Pemilihan Instrumen Riset

| Tahap Riset | Instrumen Utama yang Dipakai | Alasan Pemilihan & Rasionalisasi Metodologis | Batasan / Catatan Kritis untuk Naskah |
| :--- | :--- | :--- | :--- |
| **1. Pengambilan Data TikTok** | **4CAT + Zeeschuimer** | Dirancang khusus untuk riset ilmu sosial digital oleh *Digital Methods Initiative*. Data ditangkap melalui browser peneliti sendiri tanpa memerlukan izin API khusus atau scraping agresif. | Hindari scraping anonim tanpa kendali; simpan data mentah JSON/CSV hasil ekspor Zeeschuimer tanpa modifikasi. |
| **2. Jalur Akses Peneliti (Alternatif Resmi)** | **TikTok Research API Wrapper** | Jalur paling kredibel dan kuat di mata reviewer karena disetujui resmi oleh platform TikTok untuk kalangan akademisi. | Memerlukan persetujuan proposal riset dari TikTok. Jika belum disetujui, nyatakan secara eksplisit bahwa pengumpulan memakai metode observasi browser (4CAT). |
| **3. Bukti Arsip & Audit Snapshot** | **ArchiveBox + Tangkapan Layar Manual + Hash SHA-256** | Menyediakan bukti visual dan arsip statis (*snapshot*) bertanggal yang tidak dapat disangkal (*tamper-proof audit trail*). | Setiap tangkapan layar wajib diverifikasi *checksum* SHA-256-nya dan dicatat dalam `evidence/hashes.sha256`. |
| **4. Pencacahan Akun Tiruan & Squatting** | **Pencarian Manual Terstruktur di TikTok** (Spreadsheet) | Menghindari halusinasi data. `dnstwist` diposisikan sebagai pembanding metode permutasi nama domain, sedangkan identifikasi *handle* TikTok dilakukan via penelusuran kata kunci manual. | Kriteria penandaan (nama mirip, bio klaim resmi, tautan driver mencurigakan) harus dicatat secara eksplisit di [codebook.md](codebook.md). |
| **5. Pelacakan Tren Minat (Google Trends)** | **Ekspor CSV Manual dari Situs Resmi Google Trends** | Jauh lebih stabil, terverifikasi, dan aman dari pemblokiran dibandingkan pseudo-API tidak resmi (`pytrends`). `pytrends` hanya dipakai jika diperlukan data frekuensi tinggi dalam jumlah masif. | Simpan parameter kueri: Wilayah (Worldwide), Kategori (All), Rentang Waktu (Juli–Oktober 2026). Simpan file CSV mentah asli. |
| **6. Pengodean Akun & Dokumen** | **Spreadsheet / CSV Terstruktur Berbasis Codebook** | Sangat andal dan transparan untuk sampel 15–30 perusahaan dan segmen dokumen korporat kunci. | Wajib menggunakan dua koder independen (`coder_1` dan `coder_2`) pada minimal 20% sampel (diimplementasikan 100% pada korpus ini). |
| **7. Uji Reliabilitas Antar-Koder** | **fast-krippendorff (Python)** | Menghitung koefisien *Krippendorff’s Alpha* ($\alpha$) untuk data nominal/kategorikal. | Standar jurnal Q1: $\alpha \ge 0.70$ (dapat diterima) dan $\alpha \ge 0.80$ (sangat kokoh). Hasil riset ini mencapai $\alpha = 0.925$ dan $\alpha = 1.000$. |
| **8. Analisis Teks Korpus Besar** | **BERTopic** | Pemodelan topik (*topic modeling*) berbasis transformer untuk mengekstraksi klaster narasi dari tagar komunitas, komentar, dan transkrip panjang. | Gunakan representasi topik ter-reduksi (c-TF-IDF) untuk memetakan diskursus hegemoni versus viralitas. |
| **9. Rilis Data Publik & DOI** | **GitHub + Zenodo + Datasheet for Datasets** | Memenuhi kewajiban *Data Availability Statement* jurnal Q1 dengan menghasilkan *Digital Object Identifier* (DOI) permanen. | Seluruh kode di bawah lisensi MIT dan dataset di bawah lisensi CC-BY 4.0. |

---

## 🛠️ Langkah-Langkah Operasional Harian Peneliti

### Langkah 1: Pengambilan Snapshot Mingguan
1. Buka akun target (`@nvidia`, `@nvidiageforce`, `@amd`, `@intel`) pada browser dengan ekstensi **Zeeschuimer** aktif.
2. Ambil tangkapan layar penuh jendela profil (*full-page screenshot*).
3. Simpan berkas gambar ke `evidence/screenshots/<handle>_tiktok_<YYYYMMDD>.png`.
4. Hitung hash SHA-256 berkas tersebut di terminal:
   ```bash
   shasum -a 256 evidence/screenshots/<nama_file>.png
   ```
5. Tambahkan baris baru pada `data/raw/snapshots_account_raw.csv` dengan stempel waktu UTC presisi dan hash yang diperoleh.

### Langkah 2: Pengodean Ganda (Double-Coding Protocol)
1. Koder 1 dan Koder 2 membuka `data/raw/comparison_accounts_raw.csv` secara terpisah.
2. Berikan label kehadiran (`active`, `dormant`, `placeholder`, `defensive`) berdasarkan definisi operasional di [codebook.md](codebook.md).
3. Jalankan skrip audit reliabilitas untuk memverifikasi konsistensi:
   ```bash
   python scripts/compute_krippendorff.py
   ```
4. Jika terdapat perbedaan label, selesaikan melalui diskusi penentuan konsensus (*adjudication*).

### Langkah 3: Eksekusi Analisis & Pembaruan Naskah
Jalankan analisis end-to-end dengan satu perintah:
```bash
python scripts/run_analysis.py
```
Semua tabel di `paper/tables/` dan gambar di `paper/figures/` akan diperbarui secara otomatis dan langsung dirujuk dalam naskah ilmiah [paper/manuscript_draft_en.md](paper/manuscript_draft_en.md).
