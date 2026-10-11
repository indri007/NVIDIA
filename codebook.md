# Codebook: Operasionalisasi "Silent Authority" & Kehadiran Digital Korporat

> **Protokol Standar Pengodean Riset Empiris Multi-Kasus**  
> Penulis: Indri Kartikasari et al. (2026)  
> Target Jurnal: Jurnal Internasional Bereputasi Tinggi (Scopus / WoS Q1)

---

## 1. Landasan Teoretis Konstruk "Silent Authority"

Konstruk **Silent Authority** dioperasionalisasikan dengan menjembatani tiga kerangka literatur utama:
1. **Signaling Theory (Spence, 1973; Connelly et al., 2011):** Sinyal yang kredibel harus memiliki *costly signal* atau *unassailable backing*. Bagi korporasi bernilai triliunan dolar, memilih untuk tidak bersuara di platform video pendek dopamin (*System 1 Thinking*) merupakan sinyal sengaja bahwa otoritas legitimasi mereka tidak bergantung pada *vanity metrics* platform tersebut.
2. **Strategic / Communicative Silence (Murayama, 1995; Wang, 2019):** Keheningan bukan ketiadaan komunikasi, melainkan bentuk komunikasi tingkat tinggi (*non-action as strategic action*). Dalam konteks B2B dan deep-tech, keheningan pada kanal konsumen retail merefleksikan eksklusivitas korporat dan perlindungan wibawa institusional.
3. **Institutional Legitimacy & Economic Moat (Suchman, 1995; Buffett, 2007):** Legitimasi didasarkan pada monopoli fondasi infrastruktur (seperti ekosistem CUDA dan dominasi pusat data komputasi AI), sehingga keberadaan akun di platform sosial cukup berstatus defensif legal.

---

## 2. Tipologi Kehadiran Akun Digital Korporat (Presence Types)

Setiap akun media sosial korporat dalam korpus pembanding diklasifikasikan ke dalam 4 kategori eksklusif:

| Kode Kehadiran | Definisi Operasional | Kriteria Ambang (Threshold) | Bukti Platform |
| :--- | :--- | :--- | :--- |
| **`active`** | Korporasi aktif mengelola akun untuk interaksi publik atau pemasaran ritel. | Mengunggah $\ge 1$ video dalam 60 hari terakhir; memiliki bio dinamis, metrik followers bertumbuh, dan menggunakan fitur interaksi (komentar/sound). | Status verifikasi centang biru/emas, jumlah video $>0$, followers $>1.000$. |
| **`dormant`** | Akun pernah aktif di masa lalu, namun ditinggalkan atau dihentikan aktivitasnya. | Tidak ada unggahan baru selama $>180$ hari berturut-turut, meskipun terdapat arsip video lama. | Riwayat posting terakhir $>6$ bulan lalu; tidak ada interaksi terkini. |
| **`placeholder`** | Akun terdaftar tanpa bukti verifikasi merek resmi, atau dibuat seadanya tanpa tujuan strategis terbukti. | Akun tidak memiliki tanda verifikasi resmi (*unverified*); bio kosong atau generik; tidak ada klaim perlindungan hak cipta resmi. | Tidak bercentang biru/emas; status kepemilikan oleh korporasi diragukan atau belum diotentikasi. |
| **`defensive`** | **Jangkar Perlindungan Merek / Silent Authority.** Korporasi mengamankan *handle* resmi dan memverifikasi identitas legal untuk mencegah *cybersquatting*, namun secara sadar tidak menerbitkan konten publik. | Akun **terverifikasi resmi** (centang biru/emas); jumlah unggahan publik $=0$; jumlah followers $=0$ (atau diminimalkan); bio menetapkan identitas resmi. | Verifikasi centang biru/emas aktif; video count $=0$; identitas legal terlindungi. |

---

## 3. Rubrik Pengodean Dokumen Korporat (D5)

Pengodean tematik pada dokumen korporat (Laporan Tahunan 10-K SEC, Transkrip Keynote GTC Jensen Huang, Transkrip Earnings Call, dan Siaran Pers):

| Kode Tematik | Nama Kategori | Definisi & Contoh Potongan Teks |
| :--- | :--- | :--- |
| `CODE_CUDA_MOAT` | Arsitektur & Ekosistem Pengembang | Penyebutan *switching costs*, lock-in 6.2M+ developer CUDA, pustaka cuDNN, infrastruktur software de facto. |
| `CODE_DEFENSIVE_IDENTITY` | Proteksi Merek & Registrasi Defensif | Kebijakan perlindungan kekayaan intelektual, paten merek dagang, pencegahan penipuan siber pada aset digital. |
| `CODE_GEO_TECH_WAR` | Geopolitik & Kedaulatan AI | Pembatasan kontrol ekspor, kedaulatan AI nasional, kompetisi blok dagang AS vs China (sanksi chip dan ekosistem CANN). |
| `CODE_SILENT_AUTHORITY` | Otoritas Tanpa Algoritma Dopamin | Pernyataan kepemimpinan bahwa bisnis inti ditentukan oleh lab litbang & pusat data, bukan oleh viralitas video pendek. |
| `CODE_MISSION_IS_BOSS` | Budaya Organisasi Flat Adaptif | Kecepatan inovasi tanpa silo birokrasi, filosofi kepemimpinan Jensen Huang menghadapi tekanan pasar ekstrem. |
| `CODE_RHWR_FILTER` | Protokol Komunikasi Krisis | Penerapan filter *Rational, Healthy, Wise, Right* dalam mitigasi rumor produk atau dinamika rantai pasok. |

---

## 4. Protokol Uji Reliabilitas Antar-Koder (Inter-Coder Agreement)

1. **Jumlah Koder:** Minimal dua koder independen (`coder_1` dan `coder_2`) yang telah dilatih secara terpisah menggunakan rubrik di atas.
2. **Ukuran Sampel Uji:** Minimal 20% dari total unit analisis (pada korpus ini diuji pada 100% sampel akun pembanding dan potongan dokumen).
3. **Statistik Pengujian:** **Krippendorff’s Alpha ($\alpha$)** untuk skala pengukuran nominal (tipe kehadiran) dan kategorikal (kode dokumen).
4. **Kriteria Keberterimaan (Acceptance Threshold):**
   - $\alpha \ge 0.800$: Reliabilitas sangat tinggi (*robust agreement*).
   - $0.700 \le \alpha < 0.800$: Reliabilitas dapat diterima untuk eksplorasi tentatif (*acceptable tentative agreement*).
   - $\alpha < 0.700$: Reliabilitas tidak memadai; koder harus dire-training dan codebook direvisi.
5. **Adjudikasi Perselisihan:** Jika terjadi perbedaan penentuan kategori antara `coder_1` dan `coder_2`, kasus tersebut diserahkan ke *Third-Party Arbiter* (Peneliti Senior) untuk penetapan *ground truth* final.
