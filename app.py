"""
NVIDIA Silent Authority & Branding Iceberg Analytics Hub
Interactive Research Dashboard accompanying the paper:
'Silent Authority dan Paradigma Branding Iceberg: Analisis Strategi Komunikasi Digital NVIDIA di Platform TikTok dalam Era Marketing 5.0'
Published in Integrative Perspectives of Social and Science Journal (IPSSJ) Vol. 3 No. 9 2026.
Authors: Indri Anjar Kartika Sari, Agung Budi Prasetio, Waspodo Tjipto Subroto
"""

import os
import sys
import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Ensure scripts package is discoverable
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from scripts.digital_observation import (
    load_tiktok_observation,
    load_financial_social_df,
    load_gap_analysis,
    load_iceberg_dimensions,
    load_rhwr_framework,
    compute_silent_authority_index,
    evaluate_rhwr_filter
)

# Page configuration
st.set_page_config(
    page_title="NVIDIA Silent Authority | IPSSJ Research Hub",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS with NVIDIA Green (#76B900) & Modern Dark Theme
st.markdown("""
<style>
    /* Global & Typography */
    .nvidia-green { color: #76B900 !important; font-weight: bold; }
    .metric-card {
        background-color: #1a1f29;
        border-left: 4px solid #76B900;
        border-radius: 8px;
        padding: 18px 20px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .metric-value {
        font-size: 2.1rem;
        font-weight: 800;
        color: #76B900;
        margin-bottom: 4px;
    }
    .metric-label {
        font-size: 0.88rem;
        color: #9ca3af;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .badge-surface {
        background-color: #3b82f6;
        color: white;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .badge-foundation {
        background-color: #76B900;
        color: black;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 700;
    }
    .badge-system2 {
        background-color: #8b5cf6;
        color: white;
        padding: 3px 8px;
        border-radius: 4px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    .callout-box {
        background-color: #111827;
        border: 1px solid #374151;
        border-radius: 8px;
        padding: 16px;
        margin: 12px 0;
    }
    .footer-text {
        text-align: center;
        color: #6b7280;
        font-size: 0.85rem;
        padding-top: 30px;
        border-top: 1px solid #2d3748;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)


# Load Data Assets
@st.cache_data
def get_all_data():
    obs = load_tiktok_observation()
    fin_df = load_financial_social_df()
    gap_data = load_gap_analysis()
    iceberg = load_iceberg_dimensions()
    rhwr = load_rhwr_framework()
    tooling_path = os.path.join(BASE_DIR, "data", "research_tooling_versions.json")
    tooling_data = {}
    if os.path.exists(tooling_path):
        import json
        with open(tooling_path, "r", encoding="utf-8") as f:
            tooling_data = json.load(f)
    return obs, fin_df, gap_data, iceberg, rhwr, tooling_data

try:
    obs_data, fin_df, gap_data, iceberg_data, rhwr_data, tooling_data = get_all_data()
except Exception as e:
    st.error(f"Gagal memuat dataset: {e}")
    st.stop()


# Sidebar Configuration
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/21/Nvidia_logo.svg", width=190)
    st.markdown("### **Silent Authority & Branding Iceberg**")
    st.caption("Analisis Komunikasi Digital NVIDIA di TikTok (Marketing 5.0)")
    
    st.divider()
    
    selected_tab = st.radio(
        "Navigasi Analisis:",
        [
            "🧊 1. Branding Iceberg Matrix",
            "🤫 2. Silent Authority Index",
            "📱 3. Observasi Digital TikTok",
            "📈 4. Finansial vs Vanity Metrics",
            "⚖️ 5. Gap Analysis (Tabel 2)",
            "🛡️ 6. Simulator Protokol RHWR",
            "📄 7. Makalah Akademik & Sitasi",
            "🔬 8. Katalog Alat Riset (Q1)",
            "📊 9. Dataset Multi-Kasus & Naskah Q1"
        ]
    )
    
    st.divider()
    st.markdown("**Publikasi Rujukan:**")
    st.caption("Integrative Perspectives of Social and Science Journal (IPSSJ)")
    st.caption("Vol. 3 No. 9 2026 | E-ISSN: 3064-4011")
    st.markdown("---")
    st.caption(f"© {datetime.datetime.now().year} Indri Anjar Kartika Sari et al.")


# Header Banner
st.markdown("""
# <span class="nvidia-green">NVIDIA</span> Silent Authority & Branding Iceberg Hub
**Laboratorium Analisis Strategi Komunikasi Digital & Hegemoni Industri Semikonduktor di Era Marketing 5.0**
""", unsafe_allow_html=True)

st.markdown("""
> *“Otoritas sejati tidak selalu bersuara paling keras. Dalam ekosistem digital yang bising, keheningan strategis NVIDIA adalah sinyal dominasi struktural yang ditopang oleh 90% fondasi tak terlihat.”*  
> — **Indri Anjar Kartika Sari, Agung Budi Prasetio, & Waspodo Tjipto Subroto (2026)**
""")

# ==============================================================================
# TAB 1: BRANDING ICEBERG MATRIX
# ==============================================================================
if selected_tab == "🧊 1. Branding Iceberg Matrix":
    st.subheader("🧊 Paradigma Branding Iceberg: 10% Permukaan vs 90% Fondasi Bawah Air")
    st.write(
        "Teori Branding Iceberg membagi kehadiran korporat menjadi dua domain: puncak gunung es yang "
        "dapat disaksikan publik secara visual (10%) dan fondasi bawah laut yang menopang seluruh bobot industri (90%)."
    )

    col_top1, col_top2 = st.columns([1, 1])

    with col_top1:
        st.markdown("#### 🌊 Puncak Gunung Es (10% Visible Surface)")
        for elem in iceberg_data["visible_layer"]["elements"]:
            st.markdown(f"""
            <div class="metric-card" style="border-left-color: #3b82f6;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <strong style="color:#e5e7eb; font-size:1.05rem;">{elem['name']}</strong>
                    <span class="badge-surface">{elem['share_percent']}% Bobot</span>
                </div>
                <div style="color:#9ca3af; font-size:0.88rem; margin:6px 0;"><strong>Status:</strong> {elem['status']}</div>
                <div style="color:#d1d5db; font-size:0.85rem;"><strong>Fungsi:</strong> {elem['role']}</div>
                <div style="margin-top:6px;"><span class="badge-system2">{elem['system_type']}</span></div>
            </div>
            """, unsafe_allow_html=True)

    with col_top2:
        st.markdown("#### ⚓ Fondasi Bawah Air (90% Invisible Foundation)")
        for elem in iceberg_data["invisible_layer"]["elements"]:
            st.markdown(f"""
            <div class="metric-card" style="border-left-color: #76B900;">
                <div style="display:flex; justify-content:space-between; align-items:center;">
                    <strong style="color:#e5e7eb; font-size:1.05rem;">{elem['name']}</strong>
                    <span class="badge-foundation">{elem['share_percent']}% Bobot</span>
                </div>
                <div style="color:#9ca3af; font-size:0.88rem; margin:6px 0;"><strong>Kekuatan:</strong> {elem['status']}</div>
                <div style="color:#d1d5db; font-size:0.85rem;"><strong>Dampak:</strong> {elem['role']}</div>
                <div style="margin-top:6px;"><span class="badge-foundation" style="background:#1f2937; color:#76B900; border:1px solid #76B900;">{elem['system_type']}</span></div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### 📊 Proporsi Distribusi Gravitasi Brand NVIDIA")
    all_elements = []
    for el in iceberg_data["visible_layer"]["elements"]:
        all_elements.append({"Layer": "10% Visible Surface", "Elemen": el["name"], "Bobot (%)": el["share_percent"]})
    for el in iceberg_data["invisible_layer"]["elements"]:
        all_elements.append({"Layer": "90% Invisible Foundation", "Elemen": el["name"], "Bobot (%)": el["share_percent"]})
    
    df_sunburst = pd.DataFrame(all_elements)
    fig_sunburst = px.sunburst(
        df_sunburst,
        path=["Layer", "Elemen"],
        values="Bobot (%)",
        color="Layer",
        color_discrete_map={"10% Visible Surface": "#3b82f6", "90% Invisible Foundation": "#76B900"},
        title="Distribusi Struktur Identitas Korporat NVIDIA"
    )
    fig_sunburst.update_traces(textinfo="label+percent entry")
    fig_sunburst.update_layout(margin=dict(t=40, l=0, r=0, b=0))
    st.plotly_chart(fig_sunburst, use_container_width=True)

# ==============================================================================
# TAB 2: SILENT AUTHORITY INDEX
# ==============================================================================
elif selected_tab == "🤫 2. Silent Authority Index":
    st.subheader("🤫 Silent Authority Index (SAI) Calculator")
    st.write(
        "Kalkulator ini mensimulasikan rasio hegemoni industri terhadap ketergantungan metrik media sosial. "
        "Diadaptasi dari formulasi riset IPSSJ 2026, membuktikan bahwa perusahaan dengan fondasi ekosistem "
        "tak tergantikan tidak membutuhkan algoritma video pendek untuk mempertahankan valuasi pasarnya."
    )

    col_sim_left, col_sim_right = st.columns([1, 1])

    with col_sim_left:
        st.markdown("#### ⚙️ Parameter Korporat (Eksperimen Interaktif)")
        rev_in = st.slider("Revenue Tahunan (USD Miliar):", min_value=1.0, max_value=300.0, value=215.9, step=1.0)
        mcap_in = st.slider("Market Capitalization (USD Triliun):", min_value=0.01, max_value=5.0, value=3.45, step=0.05)
        cuda_in = st.slider("Jumlah Pengembang Ekosistem CUDA (Juta):", min_value=0.1, max_value=10.0, value=6.2, step=0.1)
        uploads_in = st.slider("Upload Konten TikTok Akun Korporat Utama:", min_value=0, max_value=1000, value=0, step=10)
        followers_in = st.number_input("Followers Akun Korporat Utama:", min_value=0, max_value=100000000, value=0, step=10000)

    # Calculate SAI
    sai_res = compute_silent_authority_index(
        revenue_billion=rev_in,
        market_cap_trillion=mcap_in,
        cuda_developers_million=cuda_in,
        corporate_tiktok_uploads=uploads_in,
        corporate_tiktok_followers=followers_in
    )

    with col_sim_right:
        st.markdown("#### 🎯 Hasil Analisis Silent Authority")
        score_val = sai_res["silent_authority_index"]
        
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Silent Authority Score</div>
            <div class="metric-value">{score_val} / 100</div>
            <div style="font-size:1.1rem; font-weight:700; color:#e5e7eb; margin:8px 0;">{sai_res['classification']}</div>
            <div style="color:#d1d5db; font-size:0.9rem; line-height:1.4;">{sai_res['interpretation']}</div>
        </div>
        """, unsafe_allow_html=True)

        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric("Skor Dominasi Substansi", f"{sai_res['substance_score']} / 100")
            st.metric("Skor Economic Moat CUDA", f"{sai_res['ecosystem_moat_score']} / 100")
        with col_m2:
            st.metric("Skor Kinerja Finansial", f"{sai_res['financial_dominance_score']} / 100")
            st.metric("Ketergantungan Dopamin/Sosmed", f"{sai_res['vanity_dependency_score']} / 100")

    # Gauge Chart
    fig_gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score_val,
        title={'text': "Silent Authority Quotient (SAI)"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#76B900"},
            'steps': [
                {'range': [0, 40], 'color': "#374151"},
                {'range': [40, 60], 'color': "#1e3a8a"},
                {'range': [60, 85], 'color': "#1e40af"},
                {'range': [85, 100], 'color': "#065f46"}
            ],
            'threshold': {
                'line': {'color': "white", 'width': 4},
                'thickness': 0.75,
                'value': score_val
            }
        }
    ))
    fig_gauge.update_layout(height=300, margin=dict(t=50, b=20, l=30, r=30))
    st.plotly_chart(fig_gauge, use_container_width=True)

# ==============================================================================
# TAB 3: OBSERVASI DIGITAL TIKTOK
# ==============================================================================
elif selected_tab == "📱 3. Observasi Digital TikTok":
    st.subheader("📱 Observasi Digital Nonpartisipatif Akun TikTok NVIDIA")
    st.write(
        "Hasil pemantauan langsung pada akun resmi NVIDIA mengungkap segmentasi arsitektur komunikasi "
        "yang sangat terencana antara entitas korporat, entitas produk gaming, dan saluran broadcast global."
    )

    accounts = obs_data["accounts"]
    cols = st.columns(len(accounts))

    for idx, acc in enumerate(accounts):
        with cols[idx]:
            is_corp = acc["handle"] == "@nvidia"
            border_c = "#76B900" if is_corp else "#3b82f6"
            
            st.markdown(f"""
            <div class="metric-card" style="border-left-color: {border_c}; min-height: 480px;">
                <div style="font-size: 1.25rem; font-weight: 800; color: #f3f4f6;">{acc['handle']}</div>
                <div style="color: #9ca3af; font-size: 0.85rem; margin-bottom: 8px;">{acc['platform']} • {acc['account_type']}</div>
                
                <div style="background:#111827; padding:8px 12px; border-radius:6px; margin: 10px 0;">
                    <div style="color:#76B900; font-size:1.1rem; font-weight:bold;">{acc['followers']:,} Followers</div>
                    <div style="color:#9ca3af; font-size:0.85rem;">{acc['uploads_count']} Postingan Video | {acc['likes']:,} Likes</div>
                    <div style="color:#60a5fa; font-size:0.8rem; margin-top:3px;">✔ {acc['badge_type']}</div>
                </div>

                <div style="margin-top: 12px;">
                    <div style="font-size: 0.85rem; font-weight: 700; color: #9ca3af;">Tujuan Strategis:</div>
                    <div style="font-size: 0.88rem; color: #e5e7eb; margin-bottom: 8px;">{acc['strategic_purpose']}</div>
                </div>

                <div style="margin-top: 8px;">
                    <div style="font-size: 0.85rem; font-weight: 700; color: #9ca3af;">Sistem Kognitif:</div>
                    <div style="font-size: 0.85rem; color: #c084fc;">{acc['cognitive_system']}</div>
                </div>

                <div style="margin-top: 8px;">
                    <div style="font-size: 0.85rem; font-weight: 700; color: #9ca3af;">Target Audiens:</div>
                    <div style="font-size: 0.85rem; color: #d1d5db;">{acc['target_audience']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("### 🔍 Mengapa Akun Korporat (@nvidia) Memilih Kosong?")
    st.markdown("""
    Dalam kacamata pemasaran konvensional, akun kosong bercentang biru mungkin dianggap sebagai "kelalaian admin". 
    Namun, melalui kerangka **Silent Authority** dan **System Thinking**:
    1. **Pencegahan Cyber Squatting (Defensive Registration):** NVIDIA mengamankan *handle* `@nvidia` dan hak verifikasi resmi untuk mencegah penipuan siber atau pihak lain yang ingin membajak identitas korporat.
    2. **Pemilahan Audiens yang Tegas:** Investor institusi, pengembang pusat data, dan pembuat kebijakan regulasi kecerdasan buatan tidak menggunakan TikTok sebagai dasar valuasi keputusan miliaran dolar.
    3. **Pembalikan Logika Engagement:** Keheningan tersebut justru menjadi pesan ancaman bagi kompetitor: *NVIDIA sudah sedemikian berkuasa di fondasi infrastruktur AI dunia, sehingga tidak perlu ikut berlomba tarian viral untuk membuktikan eksistensinya.*
    """)

# ==============================================================================
# TAB 4: FINANSIAL VS VANITY METRICS
# ==============================================================================
elif selected_tab == "📈 4. Finansial vs Vanity Metrics":
    st.subheader("📈 Kemenangan Substansi atas Viralitas (FY21 - FY26)")
    st.write(
        "Korelasi empiris membuktikan bahwa performa bisnis dan valuasi pasar NVIDIA melonjak "
        "secara eksponensial tanpa membutuhkan satupun unggahan video pada akun TikTok korporatnya."
    )

    # Top KPI Metrics FY26
    k1, k2, k3, k4 = st.columns(4)
    with k1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Revenue FY26</div>
            <div class="metric-value">$215.90 B</div>
            <div style="color:#10b981; font-size:0.85rem;">+1,194% vs FY21</div>
        </div>
        """, unsafe_allow_html=True)
    with k2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Data Center Share</div>
            <div class="metric-value">91.4%</div>
            <div style="color:#76B900; font-size:0.85rem;">AI Compute Monopoly</div>
        </div>
        """, unsafe_allow_html=True)
    with k3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Ekosistem Pengembang CUDA</div>
            <div class="metric-value">6.2 Juta</div>
            <div style="color:#3b82f6; font-size:0.85rem;">Structural Lock-in</div>
        </div>
        """, unsafe_allow_html=True)
    with k4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">TikTok Corp Uploads</div>
            <div class="metric-value">0</div>
            <div style="color:#a855f7; font-size:0.85rem;">Silent Authority</div>
        </div>
        """, unsafe_allow_html=True)

    # Interactive Chart
    fig_comp = go.Figure()
    fig_comp.add_trace(go.Bar(
        x=fin_df["fiscal_year"],
        y=fin_df["revenue_usd_billion"],
        name="Pendapatan (USD Miliar)",
        marker_color="#76B900",
        yaxis="y1"
    ))
    fig_comp.add_trace(go.Scatter(
        x=fin_df["fiscal_year"],
        y=fin_df["cuda_developers_million"],
        name="Pengembang CUDA (Juta)",
        mode="lines+markers",
        line=dict(color="#3b82f6", width=3),
        yaxis="y2"
    ))
    fig_comp.add_trace(go.Scatter(
        x=fin_df["fiscal_year"],
        y=fin_df["tiktok_corp_uploads"],
        name="Upload Video TikTok @nvidia",
        mode="lines+markers",
        line=dict(color="#ef4444", width=3, dash="dash"),
        yaxis="y1"
    ))

    fig_comp.update_layout(
        title="Pertumbuhan Pendapatan & Ekosistem CUDA vs Keheningan Konten TikTok Korporat",
        xaxis=dict(title="Tahun Fiskal"),
        yaxis=dict(title="Pendapatan USD (Miliar)", showgrid=True),
        yaxis2=dict(
            title="Pengembang CUDA (Juta)",
            overlaying="y",
            side="right",
            showgrid=False
        ),
        legend=dict(x=0.01, y=0.99),
        height=450
    )
    st.plotly_chart(fig_comp, use_container_width=True)

    st.dataframe(
        fin_df.rename(columns={
            "fiscal_year": "Tahun Fiskal",
            "revenue_usd_billion": "Pendapatan (USD B)",
            "datacenter_rev_percent": "Pusat Data (%)",
            "cuda_developers_million": "Dev CUDA (Juta)",
            "tiktok_corp_uploads": "Upload TikTok @nvidia",
            "tiktok_corp_followers": "Followers @nvidia",
            "tiktok_geforce_followers_million": "Followers @nvidiageforce (M)",
            "market_cap_trillion_usd": "Market Cap (USD T)"
        }),
        use_container_width=True
    )

# ==============================================================================
# TAB 5: GAP ANALYSIS (TABEL 2)
# ==============================================================================
elif selected_tab == "⚖️ 5. Gap Analysis (Tabel 2)":
    st.subheader("⚖️ Gap Analysis: Ekspektasi Publik vs Realitas Strategis NVIDIA")
    st.write(
        "Tabel 2 dalam artikel IPSSJ 2026 mengurai kesenjangan antara apa yang diharapkan masyarakat "
        "awam di media sosial dengan kalkulasi logis kepemimpinan NVIDIA."
    )

    filter_cat = st.multiselect(
        "Filter Dimensi Analisis:",
        options=[item["dimensi"] for item in gap_data],
        default=[item["dimensi"] for item in gap_data]
    )

    filtered_gaps = [item for item in gap_data if item["dimensi"] in filter_cat]

    for item in filtered_gaps:
        with st.expander(f"📌 {item['dimensi']} ({item['dimensi_en']}) — Status: {item['level_urgensi']}", expanded=True):
            col_a, col_b, col_c = st.columns([1, 1, 1])
            with col_a:
                st.markdown("**Ekspektasi Publik (10% Permukaan):**")
                st.info(item["ekspektasi_publik_10pct"])
            with col_b:
                st.markdown("**Realitas Strategis NVIDIA (90% Fondasi):**")
                st.success(item["realitas_strategis_90pct"])
            with col_c:
                st.markdown("**Dampak & Hegemoni Strategis:**")
                st.warning(item["dampak_strategis"])

# ==============================================================================
# TAB 6: SIMULATOR PROTOKOL RHWR
# ==============================================================================
elif selected_tab == "🛡️ 6. Simulator Protokol RHWR":
    st.subheader("🛡️ Simulator Protokol Krisis Komunikasi RHWR")
    st.write(
        "Protokol **RHWR** (*Rational, Healthy, Wise, Right*) dirumuskan pada Halaman 11 makalah "
        "sebagai filter wajib bagi komunikasi korporat teknologi untuk menutup *Interpretation Gap* "
        "dan meredam krisis reputasi tanpa mengorbankan wibawa industri."
    )

    st.markdown("#### 1. Uji Skenario Riil Industri")
    scenarios = rhwr_data["case_scenarios"]
    sc_titles = [f"{s['scenario_id']}: {s['title']}" for s in scenarios] + ["Kustom: Input Skenario Sendiri"]
    sel_sc = st.selectbox("Pilih Skenario Kasus:", sc_titles)

    if sel_sc.startswith("sc_"):
        sc_obj = next(s for s in scenarios if s["scenario_id"] == sel_sc.split(":")[0])
        st.markdown(f"**Konteks Krisis:** {sc_obj['context']}")
        st.markdown(f"**Tindakan Terverifikasi:** {sc_obj['recommended_action']}")
        st.caption(f"⚠️ Kesalahan Humas Tradisional yang Dihindari: {sc_obj['traditional_pr_error']}")
        
        # Pre-set flags for verified scenario
        r_val, h_val, w_val, rt_val = True, True, True, True
    else:
        st.write("Silakan atur pilar evaluasi untuk skenario kustom Anda:")
        r_val = st.checkbox("Rational: Apakah didukung data empiris & pengujian laboratorium?", value=True)
        h_val = st.checkbox("Healthy: Apakah menjaga mutualisme ekosistem developer & mitra?", value=True)
        w_val = st.checkbox("Wise: Apakah peka terhadap ketegangan geopolitik (Tech Cold War)?", value=False)
        rt_val = st.checkbox("Right: Apakah patuh etika AI dan kepatuhan hukum perdagangan?", value=True)

    st.markdown("#### 2. Evaluasi Protokol RHWR")
    eval_res = evaluate_rhwr_filter(r_val, h_val, w_val, rt_val)

    st.progress(eval_res["passed_pillars"] / 4.0)

    if eval_res["status"] == "APPROVED_ROBUST":
        st.success(f"✅ **{eval_res['verdict']}** ({eval_res['passed_pillars']}/4 Pilar)")
    elif eval_res["status"] == "CONDITIONAL_APPROVAL":
        st.warning(f"⚠️ **{eval_res['verdict']}** ({eval_res['passed_pillars']}/4 Pilar)")
    else:
        st.error(f"❌ **{eval_res['verdict']}** ({eval_res['passed_pillars']}/4 Pilar)")

    # Breakdown pillars
    st.markdown("##### Rincian 4 Pilar RHWR:")
    p_cols = st.columns(4)
    for idx, p in enumerate(rhwr_data["pillars"]):
        with p_cols[idx]:
            st.markdown(f"""
            <div class="callout-box">
                <div style="font-weight:700; color:#76B900;">[{p['code']}] {p['name']}</div>
                <div style="font-size:0.83rem; color:#d1d5db; margin:6px 0;">{p['question']}</div>
                <div style="font-size:0.75rem; color:#ef4444;"><strong>Risiko:</strong> {p['failure_mode']}</div>
            </div>
            """, unsafe_allow_html=True)

# ==============================================================================
# TAB 7: MAKALAH AKADEMIK & SITASI
# ==============================================================================
elif selected_tab == "📄 7. Makalah Akademik & Sitasi":
    st.subheader("📄 Informasi Publikasi Ilmiah & Sitasi Akademik")
    
    st.markdown("""
    ### *Silent Authority dan Paradigma Branding Iceberg: Analisis Strategi Komunikasi Digital NVIDIA di Platform TikTok dalam Era Marketing 5.0*
    """)
    st.markdown("""
    - **Penulis:** Indri Anjar Kartika Sari¹, Agung Budi Prasetio², Waspodo Tjipto Subroto³
    - **Afiliasi:**  
      ¹ Magister Ilmu Komunikasi, Universitas Pembangunan Nasional "Veteran" Jawa Timur, Surabaya  
      ² Institut Teknologi Tangerang Selatan, Tangerang Selatan  
      ³ Fakultas Ekonomika dan Bisnis, Universitas Negeri Surabaya, Surabaya  
    - **Jurnal:** *Integrative Perspectives of Social and Science Journal (IPSSJ)*
    - **Edisi:** Volume 3 No. 9, 2026 | E-ISSN: 3064-4011
    - **Korespondensi:** `indri.cs2026@ids.ac.id`, `agung@itts.ac.id`, `waspodosubroto@unesa.ac.id`
    """)

    st.markdown("#### Abstrak Makalah")
    st.markdown("""
    > Penelitian ini menganalisis kehadiran digital akun TikTok resmi NVIDIA (@nvidia) menggunakan kerangka
    > **Branding Iceberg** dan konsep **Silent Authority**. Penelitian menggunakan desain studi kasus kualitatif dengan
    > observasi digital nonpartisipatif dan analisis dokumen. Unit analisis meliputi status verifikasi akun, aktivitas
    > konten, indikator audiens yang terlihat, arsitektur akun, serta dokumen korporasi dan teknologi yang relevan.
    > Analisis dilakukan melalui pengodean tematik ke dalam dua lapisan: *visible elements* dan *invisible foundations*.
    > Triangulasi sumber digunakan dengan membandingkan observasi platform, dokumen resmi NVIDIA, dan literatur akademik.
    > Hasil menunjukkan bahwa minimnya aktivitas pada akun korporat dapat diinterpretasikan sebagai bentuk konfigurasi
    > identitas digital yang berbeda dari akun produk atau komunitas. Ekosistem CUDA, kinerja finansial masif (FY26 USD 215,9 Miliar),
    > dan arsitektur komunikasi korporat membuktikan kemenangan substansi industri atas perlombaan viralitas video pendek.
    """)

    st.markdown("#### Format Sitasi Ilmiah")
    col_c1, col_c2 = st.columns(2)

    with col_c1:
        st.markdown("**APA 7th Edition:**")
        apa_text = (
            "Sari, I. A. K., Prasetio, A. B., & Subroto, W. T. (2026). Silent Authority dan Paradigma "
            "Branding Iceberg: Analisis Strategi Komunikasi Digital NVIDIA di Platform TikTok dalam Era "
            "Marketing 5.0. Integrative Perspectives of Social and Science Journal (IPSSJ), 3(9), 1-12."
        )
        st.code(apa_text, language="text")

    with col_c2:
        st.markdown("**BibTeX Format:**")
        bibtex_text = """@article{sari2026silent,
  author    = {Sari, Indri Anjar Kartika and Prasetio, Agung Budi and Subroto, Waspodo Tjipto},
  title     = {Silent Authority dan Paradigma Branding Iceberg: Analisis Strategi Komunikasi Digital NVIDIA di Platform TikTok dalam Era Marketing 5.0},
  journal   = {Integrative Perspectives of Social and Science Journal (IPSSJ)},
  volume    = {3},
  number    = {9},
  pages     = {1--12},
  year      = {2026},
  issn      = {3064-4011}
}"""
        st.code(bibtex_text, language="bibtex")

    pdf_file_path = os.path.join(BASE_DIR, "View of Silent Authority dan Paradigma Branding Iceberg_ Analisis Strategi Komunikasi Digital NVIDIA di Platform TikTok dalam Era Marketing 5.0.pdf")
    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as f_pdf:
            st.download_button(
                label="📥 Unduh Naskah Lengkap PDF (IPSSJ Vol. 3 No. 9 2026)",
                data=f_pdf,
                file_name="NVIDIA_Silent_Authority_IPSSJ_2026.pdf",
                mime="application/pdf"
            )

# ==============================================================================
# TAB 8: KATALOG ALAT RISET & REPRODUKTIBILITAS (Q1)
# ==============================================================================
elif selected_tab == "🔬 8. Katalog Alat Riset (Q1)":
    st.subheader("🔬 Katalog Reproduktibilitas Alat & Pustaka Riset (Q1 Standards)")
    st.write(
        "Untuk menjamin keterulangan ilmiah (*reproducibility*) sesuai standar jurnal Q1, "
        "setiap instrumen perangkat lunak dan repositori pencarian data dicatat secara presisi "
        "beserta rilis resmi, commit hash Git, dan perannya dalam pengumpulan bukti."
    )

    if tooling_data and "catalog" in tooling_data:
        cat_list = tooling_data["catalog"]
        
        # Summary metrics
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric("Total Alat Tercatat", f"{len(cat_list)} Repositori")
        with m2:
            st.metric("Standar Format", "LinkML & Markdown Datasheets")
        with m3:
            st.metric("Metode Reliabilitas", "Krippendorff's Alpha >= 0.80")

        # Table display
        df_tools = pd.DataFrame([
            {
                "Alat / Repositori": item["name"],
                "Pengembang": item["developer"],
                "Versi": item["version"],
                "Git Commit Hash": item["commit_hash"][:10] + "...",
                "Fungsi Riset": item["purpose"],
                "Relevansi": ", ".join(item["research_points"])
            }
            for item in cat_list
        ])
        st.dataframe(df_tools, use_container_width=True)

        st.markdown("### 📋 Detail Instrumen per Kategori Riset")
        for item in cat_list:
            with st.expander(f"📦 {item['name']} ({item['version']}) — {item['developer']}", expanded=False):
                st.markdown(f"**Tautan Sumber:** [{item['repository']}]({item['repository']})")
                st.markdown(f"**Commit Hash Penuh:** `{item['commit_hash']}`")
                st.markdown(f"**Tanggal Commit:** `{item['commit_date']}`")
                st.markdown(f"**Tujuan Penggunaan:** {item['purpose']}")
                st.caption(f"Relevansi Poin: {', '.join(item['research_points'])}")

        st.markdown("### 🔬 Catatan Metodologis untuk Poin 6 (Wawancara & Eksperimen)")
        st.markdown("""
        Untuk instrumen **Poin 6** (wawancara mendalam kualitatif dan eksperimen survei) yang tidak memiliki repositori kode sumber langsung:
        1. **Penyimpanan Transkrip & Kode Etik:** Seluruh pedoman wawancara (*interview protocol*) dan kuesioner survei diarsipkan dalam format terstruktur dengan nomor registrasi etika riset.
        2. **Triangulasi Reliabilitas (Inter-coder Reliability):** Pengodean tematik transkrip wawancara diuji reliabilitas antar-peneliti menggunakan pustaka `fast-krippendorff` (Commit `2813eab7`) dengan ambang batas reliabilitas minimum $\\alpha \\ge 0.800$.
        3. **Audit Trail Data:** Setiap perubahan skema pengodean dicatat secara *versioned* (*audit trail*) bersamaan dengan metadata datasheet dataset (`bridge2ai/data-sheets-schema`).
        """)
    else:
        st.info("Katalog alat riset sedang dimuat atau belum tersedia.")

# ==============================================================================
# TAB 9: DATASET MULTI-KASUS & NASKAH Q1 (ALL-IN-ONE RESEARCH ENGINE)
# ==============================================================================
elif selected_tab == "📊 9. Dataset Multi-Kasus & Naskah Q1":
    st.subheader("📊 Dataset Empiris Multi-Kasus & Draf Naskah Ilmiah (Scopus Q1)")
    st.write(
        "Modul ini menyatukan dataset empiris multi-kasus 20 korporasi teknologi, bukti audit kriptografi SHA-256, "
        "hasil uji hipotesis (H1–H4), serta draf naskah ilmiah Bahasa Inggris yang siap diajukan ke jurnal bereputasi tinggi."
    )

    proc_path = os.path.join(BASE_DIR, "data", "processed")
    sub_tabs = st.tabs([
        "📈 D1: Snapshots Longitudinal",
        "🏢 D2: Korpus 20 Perusahaan",
        "🚨 D3: Akun Tiruan & Squatting",
        "🌐 D4: Kompensasi Pihak Ketiga",
        "📑 D5: Dokumen Terkode",
        "📐 Diagram Relasi Entitas (ERD)",
        "📝 Naskah Bahasa Inggris (Q1 Draft)"
    ])

    # Sub-tab D1
    with sub_tabs[0]:
        st.markdown("#### D1: Longitudinal Account Snapshots (14 Minggu Observasi)")
        f1_path = os.path.join(proc_path, "snapshots_account.csv")
        if os.path.exists(f1_path):
            df_s = pd.read_csv(f1_path)
            st.dataframe(df_s, use_container_width=True)
            
            fig1_img = os.path.join(BASE_DIR, "paper", "figures", "figure1_longitudinal_trajectory.png")
            if os.path.exists(fig1_img):
                st.image(fig1_img, caption="Gambar 1: Trajektori Longitudinal Kehadiran TikTok NVIDIA (Juli–Oktober 2026)")

    # Sub-tab D2
    with sub_tabs[1]:
        st.markdown("#### D2: Korpus 20 Perusahaan Pembanding Lintas 5 Platform")
        f2_path = os.path.join(proc_path, "comparison_accounts.csv")
        if os.path.exists(f2_path):
            df_c = pd.read_csv(f2_path)
            sec_filter = st.multiselect("Filter Sektor:", df_c["sector"].unique(), default=df_c["sector"].unique())
            st.dataframe(df_c[df_c["sector"].isin(sec_filter)], use_container_width=True)
            
            fig2_img = os.path.join(BASE_DIR, "paper", "figures", "figure2_presence_by_sector.png")
            if os.path.exists(fig2_img):
                st.image(fig2_img, caption="Gambar 2: Tipologi Kehadiran Media Sosial Korporat per Sektor Industri (N=20)")

    # Sub-tab D3
    with sub_tabs[2]:
        st.markdown("#### D3: Sensus Akun Tiruan, Cybersquatting, & Risiko Phishing")
        f3_path = os.path.join(proc_path, "lookalike_accounts.csv")
        if os.path.exists(f3_path):
            df_l = pd.read_csv(f3_path)
            st.dataframe(df_l, use_container_width=True)
            st.warning("⚠️ Akun @nvidia_drivers_official terdeteksi menyebarkan tautan phishing file driver VGA palsu, mengonfirmasi urgensi proteksi akun defensif resmi @nvidia.")

    # Sub-tab D4
    with sub_tabs[3]:
        st.markdown("#### D4: Seri Waktu Konten Pihak Ketiga & Google Trends")
        f4_path = os.path.join(proc_path, "third_party_series.csv")
        if os.path.exists(f4_path):
            df_t = pd.read_csv(f4_path)
            st.dataframe(df_t, use_container_width=True)
            
            fig3_img = os.path.join(BASE_DIR, "paper", "figures", "figure3_third_party_volume.png")
            if os.path.exists(fig3_img):
                st.image(fig3_img, caption="Gambar 3: Volume Penayangan Tagar Pihak Ketiga (#nvidia vs #nvidiageforce)")

    # Sub-tab D5
    with sub_tabs[4]:
        st.markdown("#### D5: Pengodean Tematik Dokumen Resmi (Laporan 10-K, GTC Keynote, Earnings Call)")
        f5_path = os.path.join(proc_path, "documents_coded.csv")
        if os.path.exists(f5_path):
            df_d = pd.read_csv(f5_path)
            st.dataframe(df_d, use_container_width=True)

    # Sub-tab ERD
    with sub_tabs[5]:
        st.markdown("#### 📐 Entity-Relationship Diagram (ERD) & Arsitektur Data Relasional")
        erd_path = os.path.join(BASE_DIR, "docs", "ERD.md")
        if os.path.exists(erd_path):
            with open(erd_path, "r", encoding="utf-8") as f_erd:
                erd_md = f_erd.read()
            st.download_button(
                label="📥 Unduh Dokumen ERD Lengkap (.md)",
                data=erd_md,
                file_name="NVIDIA_Silent_Authority_ERD.md",
                mime="text/markdown"
            )
            st.markdown(erd_md)

    # Sub-tab Naskah
    with sub_tabs[6]:
        st.markdown("#### 📄 Draf Lengkap Naskah Ilmiah (English Manuscript for Q1)")
        manuscript_path = os.path.join(BASE_DIR, "paper", "manuscript_draft_en.md")
        if os.path.exists(manuscript_path):
            with open(manuscript_path, "r", encoding="utf-8") as f_m:
                manuscript_content = f_m.read()
            st.download_button(
                label="📥 Unduh Naskah Lengkap Markdown (.md)",
                data=manuscript_content,
                file_name="Silent_Authority_MultiCase_Q1_Draft.md",
                mime="text/markdown"
            )
            st.markdown(manuscript_content)

# Footer
st.markdown(f"""
<div class="footer-text">
    Laboratorium Riset Komunikasi Digital NVIDIA • Didasarkan pada publikasi IPSSJ Vol. 3 No. 9 (2026)<br>
    © {datetime.datetime.now().year} Indri Anjar Kartika Sari, Agung Budi Prasetio, Waspodo Tjipto Subroto. All Rights Reserved.
</div>
""", unsafe_allow_html=True)
