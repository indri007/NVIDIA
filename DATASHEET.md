# Datasheet for Dataset: Silent Authority NVIDIA & Multi-Case Corporate Digital Presence

> **Format Standar:** Gebru et al. (2021) *Datasheets for Datasets* (Communications of the ACM) & LinkML Schema compliant.  
> **Repository:** `silent-authority-tiktok-dataset`  
> **Persistent Identifier:** Zenodo DOI reserved (e.g. `10.5281/zenodo.10260000`)

---

## 1. Motivation

### For what purpose was the dataset created?
Dataset ini dibuat untuk mengatasi keterbatasan studi kasus tunggal mengenai kehadiran digital akun TikTok resmi NVIDIA (`@nvidia`, 0 followers) dengan menyediakan korpus multi-kasus longitudinal dan data pembanding 20 korporasi teknologi global. Tujuannya adalah membuktikan secara empiris apakah keheningan akun terverifikasi merefleksikan **registrasi defensif dan otoritas struktural (*Silent Authority*)** atau sekadar akun yang terbengkalai.

### Who created the dataset?
Indri Anjar Kartika Sari (Magister Ilmu Komunikasi, Universitas Pembangunan Nasional "Veteran" Jawa Timur), Agung Budi Prasetio (Institut Teknologi Tangerang Selatan), dan Waspodo Tjipto Subroto (Universitas Negeri Surabaya).

### Who funded the creation of the dataset?
Riset akademik mandiri tanpa keterikatan komersial atau sponsor korporat dari pihak mana pun.

---

## 2. Composition

### What do the instances that comprise the dataset represent?
Unit analisis mencakup:
1. **Snapshots Akun Longitudinal (`snapshots_account.csv`):** 56 catatan observasi mingguan akun resmi TikTok (`@nvidia`, `@nvidiageforce`, `@amd`, `@intel`) disertai hash SHA-256 bukti visual tangkapan layar.
2. **Korpus Pembanding (`comparison_accounts.csv`):** 20 korporasi semikonduktor, big tech, dan enterprise SaaS lintas 5 platform media sosial (TikTok, X, LinkedIn, YouTube, Instagram).
3. **Akun Tiruan & Squatting (`lookalike_accounts.csv`):** 9 entitas akun tiruan, *phishing*, dan *fan community* yang mengklaim identitas merek.
4. **Seri Konten Pihak Ketiga (`third_party_series.csv`):** 56 catatan mingguan metrik penayangan tagar `#nvidia`, tren pencarian Google Trends, dan liputan berita global.
5. **Dokumen Terkode (`documents_coded.csv`):** 10 segmen teks dari dokumen korporat resmi (SEC 10-K, GTC Keynote, Earnings Call, Siaran Pers) yang dikodekan ganda (*double-coded*).

### Does the dataset contain all possible instances or is it a sample?
Merupakan sampel purposif yang representatif dari industri semikonduktor, perangkat keras komputasi, dan ekosistem kecerdasan buatan global.

### Does the dataset contain data that might be considered confidential or sensitive?
**Tidak.** Seluruh data dikumpulkan dari domain publik, antarmuka profil korporat resmi, dan keterbukaan dokumen pasar modal (SEC).

### Does the dataset contain personally identifiable information (PII)?
**Tidak.** Tidak ada data pribadi pengguna individu, foto profil pengguna perorangan, komentar personal, atau nama pengguna komentar yang dikumpulkan atau dirilis.

---

## 3. Collection Process

### How was the data associated with each instance acquired?
- Snapshot profil dicatat secara berkala dengan stempel waktu UTC presisi dan disimpan dalam arsip bukti gambar PNG berstempel hash SHA-256.
- Data pembanding diverifikasi langsung pada platform resmi masing-masing korporasi.
- Seluruh pengodean dilakukan oleh dua peneliti independen mengikuti [codebook.md](codebook.md).

### What mechanisms or procedures were used to collect the data?
Kombinasi observasi digital nonpartisipatif terstruktur dan skrip otomasi Python (`collect_snapshots.py`, `enumerate_lookalikes.py`).

---

## 4. Preprocessing, Cleaning, and Labeling

### Was any preprocessing/cleaning/labeling done?
Ya. Seluruh data mentah disimpan tanpa modifikasi di `data/raw/` dan diproses secara deterministik ke `data/processed/` melalui skrip validasi skema otomatis `scripts/validate_schemas.py`.

### Were inter-coder reliability checks performed?
Ya. Reliabilitas antar-koder diuji menggunakan koefisien **Krippendorff’s Alpha ($\alpha$)** dengan pustaka terverifikasi `fast-krippendorff`. Skor yang dicapai melampaui ambang batas standar ($\alpha \ge 0.76 - 0.85$).

---

## 5. Uses

### What (other) tasks could the dataset be used for?
- Studi komunikasi korporat B2B dan *signaling theory* di media sosial.
- Riset *cyber threat intelligence* mengenai *brand impersonation* dan *cybersquatting*.
- Analisis komparasi efektivitas *vanity metrics* versus performa fundamental korporat.

---

## 6. Distribution & Licensing

- **Dataset License:** [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- **Code License:** [MIT License](LICENSE)
- **Data Availability Statement:** Seluruh baris data, skrip transformasi, dan pengujian dapat diakses publik di repositori GitHub dan diarsipkan secara permanen dengan DOI di Zenodo.
