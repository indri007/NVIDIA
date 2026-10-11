# Unified Specifications: Data Schemas & Methodological Rules (Q1 Standard)

> **Repositori Riset Empiris:** *Silent Authority dan Paradigma Branding Iceberg*  
> **Penulis:** Indri Anjar Kartika Sari, Agung Budi Prasetio, Waspodo Tjipto Subroto (2026)  
> **Standar:** Scopus / WoS Q1 Peer-Review, FAIR Principles, Gebru et al. (2021) Datasheet Standard.

---

# BAGIAN I: DATA SCHEMAS (SPESIFIKASI SKEMA DATA)

## 1. Arsitektur Relasional (3NF Overview)

Dataset diorganisasikan ke dalam skema relasional terstandarisasi bentuk normal ketiga (3NF) guna menjamin integritas referensial dan menghilangkan anomali redundansi:

```text
[COMPANY] 1 ──── N [CORPORATE_ACCOUNT] 1 ──── N [ACCOUNT_SNAPSHOT] N ──── 1 [AUDIT_EVIDENCE]
    │                     │                                                     │
    │ 1                   │ 1                                                   │ N
    │                     │                                                     │
    ▼ N                   ▼ 1                                                   ▼ 1
[LOOKALIKE_ACCOUNT]  [PRESENCE_BENCHMARK_CODING]                       [RESEARCH_TOOLING]
    │
[THIRD_PARTY_METRICS] (N:1 to COMPANY)
[CODED_DOCUMENT] (N:1 to COMPANY) 1 ──── N [THEMATIC_SEGMENT_CODING] N ──── 1 [THEMATIC_CODE_RUBRIC]
[FINANCIAL_MACRO_METRICS] (N:1 to COMPANY)
```

---

## 2. Definisi Skema Tabel (Data Dictionary)

### 2.1. `COMPANY` (Entitas Korporat)
- **Deskripsi:** Entitas induk korporasi teknologi global dalam korpus studi komparatif (N=20).
- **Primary Key:** `company_id` (VARCHAR(16))
- **Kolom:**
  - `company_id`: string (PK) — Simbol unik (e.g. `NVDA`, `AMD`, `INTC`, `MSFT`, `AAPL`)
  - `company_name`: string — Nama legal entitas (e.g. `NVIDIA Corporation`)
  - `sector`: string — Kluster industri (`Semiconductors (AI / GPU)`, `Big Tech Platform`, `Enterprise SaaS`)
  - `business_model`: string — Orientasi pasar (`B2B & Consumer`, `Pure B2B`, `Consumer Tech`)
  - `market_cap_tier`: string — Klasifikasi valuasi (`Mega-Cap (>$1T)`, `Large-Cap`)
  - `headquarters_country`: string — Yurisdiksi hukum korporasi (e.g. `United States`)

### 2.2. `CORPORATE_ACCOUNT` (Akun Resmi Multi-Platform)
- **Deskripsi:** Titik kehadiran resmi entitas korporat lintas platform media sosial.
- **Primary Key:** `account_id` (VARCHAR(32))
- **Foreign Key:** `company_id` $\to$ `COMPANY(company_id)`
- **Kolom:**
  - `account_id`: string (PK) — ID unik (e.g. `ACC_NV_CORP`, `ACC_NV_GEFORCE`, `ACC_AMD_CORP`)
  - `company_id`: string (FK) — Referensi perusahaan
  - `platform`: string — Nama platform (`TikTok`, `X`, `LinkedIn`, `YouTube`, `Instagram`)
  - `handle`: string — Identifier publik (e.g. `@nvidia`, `@nvidiageforce`)
  - `account_type`: string — Fungsi akun (`Corporate Official`, `Consumer Sub-brand`, `Enterprise/Recruitment`)
  - `verified`: boolean — Keberadaan lencana otentikasi resmi platform (`TRUE` / `FALSE`)

### 2.3. `ACCOUNT_SNAPSHOT` (Dataset D1: Observasi Longitudinal)
- **Deskripsi:** Rekaman metrik observasional berkala berstempel waktu UTC (14 pekan pengamatan).
- **Primary Key:** `snapshot_id` (VARCHAR(64))
- **Foreign Keys:**
  - `account_id` $\to$ `CORPORATE_ACCOUNT(account_id)`
  - `sha256` $\to$ `AUDIT_EVIDENCE(sha256)`
- **Kolom:**
  - `snapshot_id`: string (PK) — e.g. `SNAP_NV_CORP_20261011`
  - `account_id`: string (FK)
  - `captured_at_utc`: timestamp (ISO 8601 UTC)
  - `followers`: integer ($\ge 0$)
  - `following`: integer ($\ge 0$)
  - `likes`: bigint ($\ge 0$)
  - `video_count`: integer ($\ge 0$)
  - `verified`: boolean
  - `bio`: text — Teks deskripsi profil
  - `evidence_file`: string — Jalur relatif berkas bukti (e.g. `screenshots/nvidia_tiktok_20261011.png`)
  - `sha256`: char(64) (FK) — Digest SHA-256 verifikasi berkas bukti fisik

### 2.4. `AUDIT_EVIDENCE` (Rantai Integritas Kriptografis)
- **Deskripsi:** Registry bukti visual screenshot arsip yang dilindungi hash kriptografis tak terubahkan.
- **Primary Key:** `sha256` (CHAR(64))
- **Foreign Key:** `captured_by_tool` $\to$ `RESEARCH_TOOLING(tool_name)`
- **Kolom:**
  - `sha256`: char(64) (PK) — 256-bit hexadecimal string
  - `file_path`: string (UNIQUE) — Relatif path berkas
  - `file_type`: string (`PNG`, `PDF`, `WARC`)
  - `captured_by_tool`: string (FK) — Nama alat yang digunakan (e.g. `ArchiveBox`, `zeeschuimer`)
  - `file_size_bytes`: bigint (> 0)
  - `captured_timestamp`: timestamp

### 2.5. `PRESENCE_BENCHMARK_CODING` (Dataset D2: Pengodean Tipologi Kehadiran)
- **Deskripsi:** Hasil pengodean ganda independen tipologi kehadiran digital korporat 20 perusahaan.
- **Primary Key:** `coding_id` (VARCHAR(32))
- **Foreign Key:** `account_id` $\to$ `CORPORATE_ACCOUNT(account_id)`
- **Kolom:**
  - `coding_id`: string (PK)
  - `account_id`: string (FK)
  - `presence_type`: string — Nilai konsensus: `['active', 'defensive', 'dormant', 'placeholder']`
  - `coder_1`: string — Penetapan Koder 1
  - `coder_2`: string — Penetapan Koder 2
  - `adjudicated_type`: string — Ground truth hasil adjudikasi arbiter
  - `notes`: text — Dokumentasi catatan empiris kualitatif

### 2.6. `LOOKALIKE_ACCOUNT` (Dataset D3: Sensus Cybersquatting & Phishing)
- **Deskripsi:** Registri akun tidak resmi, peniruan identitas merek, dan eksploitasi domain/handle.
- **Primary Key:** `lookalike_id` (VARCHAR(32))
- **Foreign Key:** `brand_target` $\to$ `COMPANY(company_id)`
- **Kolom:**
  - `lookalike_id`: string (PK)
  - `brand_target`: string (FK)
  - `platform`: string (e.g. `TikTok`)
  - `handle`: string (e.g. `@nvidia_drivers_official`)
  - `found_at`: date (YYYY-MM-DD)
  - `reason`: text — Modus operandi (`Typosquatting`, `Phishing driver downloads`, `Fan meme page`)
  - `status`: string (`phishing_flagged`, `unverified_fan`, `unverified_creator`, `community_unofficial`)
  - `risk_level`: string (`High`, `Medium`, `Low`)

### 2.7. `THIRD_PARTY_METRICS` (Dataset D4: Kompensasi Wacana Pihak Ketiga)
- **Deskripsi:** Data longitudinal wacana publik pihak ketiga pengimbang keheningan akun resmi.
- **Primary Key:** `metric_id` (VARCHAR(32))
- **Foreign Key:** `company_id` $\to$ `COMPANY(company_id)`
- **Kolom:**
  - `metric_id`: string (PK)
  - `company_id`: string (FK)
  - `source`: string (`TikTok Hashtag`, `Google Trends`, `Global Tech Media`)
  - `query`: string (`#nvidia`, `#nvidiageforce`, `NVIDIA AI Blackwell`)
  - `week_start`: date (YYYY-MM-DD)
  - `volume`: bigint ($\ge 0$) — Tayangan video tagar, indeks Google Trends (0–100), atau jumlah artikel
  - `sentiment_score`: float (0.000 hingga 1.000)

### 2.8. `CODED_DOCUMENT` & `THEMATIC_SEGMENT_CODING` (Dataset D5: Dokumen Korporat)
- **Deskripsi:** Segmen teks korporat resmi (SEC 10-K, GTC Keynote Jensen Huang, Earnings Call) yang dikodekan ganda.
- **Primary Key Document:** `doc_id` (VARCHAR(32))
- **Primary Key Segment:** `segment_id` (VARCHAR(32))
- **Kolom Dokumen:**
  - `doc_id`: string (PK) (e.g. `DOC_10K_FY26_01`)
  - `company_id`: string (FK)
  - `document_type`: string (`SEC 10-K Filing`, `GTC Keynote Transcript`, `Earnings Call`)
  - `filing_date`: date
  - `primary_source_url`: string
- **Kolom Segmen:**
  - `segment_id`: string (PK)
  - `doc_id`: string (FK)
  - `code_id`: string (FK $\to$ `THEMATIC_CODE_RUBRIC`)
  - `coder_id`: string (`coder_1`, `coder_2`)
  - `excerpt_ref`: text — Kutipan teks dan referensi bab/menit

### 2.9. `FINANCIAL_MACRO_METRICS` (Disparitas Finansial vs Metrik Sosial)
- **Deskripsi:** Indikator fundamental korporat tahunan FY21–FY26 yang membuktikan independensi otoritas struktural.
- **Primary Key:** `financial_id` (VARCHAR(16))
- **Foreign Key:** `company_id` $\to$ `COMPANY(company_id)`
- **Kolom:**
  - `fiscal_year`: string (`FY21`–`FY26`)
  - `revenue_usd_billion`: numeric(10,2)
  - `datacenter_rev_percent`: numeric(5,2)
  - `cuda_developers_million`: numeric(5,2)
  - `tiktok_corp_uploads`: int (= 0)
  - `tiktok_corp_followers`: int (= 0)
  - `market_cap_trillion_usd`: numeric(6,3)

---

# BAGIAN II: METHODOLOGICAL & OPERATIONAL RULES (ATURAN RISET)

## RULE 1: Pohon Keputusan Tipologi Kehadiran Digital (Presence Typology)

Setiap akun media sosial dalam korpus pembanding wajib diklasifikasikan ke dalam salah satu dari empat kategori saling eksklusif (*mutually exclusive*) berdasarkan algoritma berikut:

```text
                                [Apakah Akun Terverifikasi Resmi?]
                                       │                   │
                                      YA                 TIDAK
                                       │                   │
                       [Apakah Unggahan Publik > 0?]   [Apakah Unggahan > 0?]
                                │           │              │           │
                               YA         TIDAK           YA         TIDAK
                                │           │              │           │
            [Unggahan dalam 60 hari?]   [DEFENSIVE]    [DORMANT /  [PLACEHOLDER]
                    │           │                       ACTIVE     (Unverified,
                   YA         TIDAK                   UNOFFICIAL]   abandoned)
                    │           │
                [ACTIVE]    [DORMANT]
```

1. **Aturan `defensive` (Jangkar Otoritas Hening):**
   - Syarat 1: `verified == True` (centang biru/emas resmi platform).
   - Syarat 2: `video_count == 0` (tidak ada video publik yang diterbitkan).
   - Syarat 3: `followers == 0` (atau diminimalkan tanpa kampanye akuisisi follower).
   - Syarat 4: Bio profil menetapkan kepemilikan merek resmi secara statis.
2. **Aturan `active`:**
   - Syarat 1: `verified == True`.
   - Syarat 2: Mengunggah $\ge 1$ video dalam 60 hari terakhir.
   - Syarat 3: `followers > 1,000` dan mengaktifkan fitur keterlibatan publik.
3. **Aturan `dormant`:**
   - Riwayat unggahan ada di masa lalu, namun tidak ada aktivitas baru selama $> 180$ hari berturut-turut.
4. **Aturan `placeholder`:**
   - Akun tidak bercentang verifikasi (`verified == False`), bio kosong/tidak terawat, dibuat tanpa konfirmasi legal institusional.

---

## RULE 2: Protokol Reliabilitas Antar-Koder (Inter-Coder Agreement)

1. **Prinsip Double-Blind:**
   - Pengodean dilakukan secara independen oleh dua koder (`coder_1` dan `coder_2`) tanpa komunikasi silang selama proses pelabelan.
2. **Metrik Evaluasi:**
   - Koefisien **Krippendorff’s Alpha ($\alpha$)** dihitung menggunakan pustaka resmi `fast-krippendorff` pada skala data nominal:
     $$\alpha = 1 - \frac{D_o}{D_e}$$
     di mana $D_o$ adalah ketidaksepakatan yang teramati (*observed disagreement*) dan $D_e$ adalah ketidaksepakatan yang diharapkan secara acak (*expected disagreement*).
3. **Ambang Batas Keberterimaan (Acceptance Thresholds):**
   - **$\alpha \ge 0.800$:** *Robust Agreement* $\to$ Data diterima mutlak untuk analisis inferensial jurnal Q1.
   - **$0.700 \le \alpha < 0.800$:** *Tentative Agreement* $\to$ Kesimpulan tentatif diperbolehkan dengan catatan eksplisit dalam naskah.
   - **$\alpha < 0.700$:** *Reject & Retrain* $\to$ Pengodean gugur; koder wajib dire-training dan codebook direvisi.
4. **Aturan Adjudikasi Arbiter:**
   - Apabila terjadi diskrepansi kategori antara Koder 1 dan Koder 2, kasus diserahkan kepada Peneliti Senior (*Adjudicator*) untuk menetapkan nilai `adjudicated_type` final berdasarkan rekaman audit screenshot bertanggal.

---

## RULE 3: Protokol Kriptografis & Integritas Bukti Visual (Cryptographic SOP)

1. **Pre-Commit Hash Integrity Check:**
   - Setiap berkas gambar bukti visual (`.png`) yang disimpan di `evidence/screenshots/` wajib memiliki intisari hash SHA-256 yang dihitung saat perekaman dan dicatat pada `evidence/hashes.sha256`.
2. **Kaidah Otentikasi Deterministik:**
   - Skrip validasi `scripts/validate_schemas.py` dijalankan secara otomatis pada CI/CD test suite. Jika nilai SHA-256 dari berkas fisik tidak identik dengan nilai pada database `snapshots_account.csv`, build dinyatakan **GAGAL (Exit Code 1)**.
3. **Perekaman Stempel Waktu (UTC Timestamp):**
   - Waktu observasi wajib menggunakan format ISO 8601 dengan offset zona waktu UTC (`YYYY-MM-DDTHH:MM:SSZ`) guna menghindari ambiguitas lintas yurisdiksi.

---

## RULE 4: Protokol Komunikasi Krisis Korporat (Filter RHWR)

Dalam mengevaluasi interaksi komunikasi digital dan mitigasi rumor publik (e.g. insiden konektor daya leleh GPU atau isu penundaan arsitektur Blackwell), setiap respons komunikasi wajib lolos uji 4 pilar RHWR sebelum dirilis ke publik:

1. **Rational (R):** Apakah respons didasarkan pada data laboratorium ilmiah, fakta teknik terverifikasi, dan analisis akar masalah kausal (bukan reaksi emosional atau opini persepsual)?
2. **Healthy (H):** Apakah pesan melindungi stabilitas ekosistem mitra industri secara berkelanjutan tanpa menciptakan kepanikan pasar modal atau rantai pasok?
3. **Wise (W):** Apakah pemilihan kanal komunikasi mencerminkan kedewasaan korporat (memilih rilis teknis terstruktur di situs resmi dibanding berdebat di utas komentar media sosial)?
4. **Right (R):** Apakah tindakan tersebut mematuhi seluruh koridor hukum pasar modal, kepatuhan SEC Regulation FD, dan etika tanggung jawab produk?

**Aturan Keputusan Simulator RHWR:**
- **4/4 Lolos:** `APPROVED_ROBUST` $\to$ Respons teknis disetujui untuk rilis publik.
- **3/4 Lolos:** `CONDITIONAL_APPROVAL` $\to$ Revisi draf komunikasi; wajib tinjauan legal tambahan.
- **$\le 2/4$ Lolos:** `HIGH_RISK_REJECTED` $\to$ Tahan komunikasi (*Strategic Silence diterapkan*).

---

## RULE 5: Batasan Etika Penelitian & Kepatuhan Legal (Scopus Q1 Standards)

1. **Proteksi Privasi Individu (Strict Non-PII):**
   - Tidak ada data pribadi pengguna perorangan (nama akun komentator biasa, nomor telepon, alamat surel individu, atau foto profil personal) yang dikumpulkan, diproses, atau disimpan dalam repositori.
   - Ruang lingkup analisis dibatasi secara ketat pada **entitas akun korporasi resmi, entitas merek publik, dan metrik agregat makro**.
2. **Kepatuhan Terms of Service (ToS) & Fair Use:**
   - Pengumpulan data dilakukan melalui observasi digital non-partisipatif dari antarmuka web publik dan keterbukaan dokumen emiten bursa (SEC EDGAR).
   - Pemanfaatan tangkapan layar dilakukan di bawah doktrin *Fair Use* untuk kepentingan analisis kritik ilmiah dan riset akademik nirlaba.
3. **Pemisahan Afiliasi Hukum:**
   - Riset beroperasi di bawah disclaimer hukum tegas bahwa penulis dan institusi terafiliasi **tidak memiliki hubungan komersial, endorsement, maupun sponsor dari NVIDIA Corporation atau ByteDance Ltd.**
