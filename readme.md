# 🚢 Supply Chain Crisis Command Center: Hierarchical Multi-Agent Architecture

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agentic-supply-chain-crisis.streamlit.app)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/muryanawaludin/agentic_supply_chain_crisis.git)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Platform **Sistem Multi-Agen Hierarkis (Hierarchical Multi-Agent System / HMAS)** untuk automasi komando krisis logistik dan ketahanan rantai pasok global. Sistem menerapkan pola **Supervisor-Worker**, formalisasi **Semi-Markov Decision Process (SMDP)**, serta **Options Framework** untuk memitigasi disrupsi pengiriman kargo lintas benua secara otonom dan terukur.

---

## 🌐 Demo Aplikasi Langsung

Aplikasi dapat dijalankan langsung di peramban tanpa instalasi lokal:  
👉 **[Buka Demo Aplikasi Streamlit](https://agentic-supply-chain-crisis.streamlit.app)**  
*(Tautan alternatif: [agentic_supply_chain_crisis.streamlit.app](https://agentic_supply_chain_crisis.streamlit.app))*

---

## 🎯 Arsitektur Kognitif & Struktur Komando

Platform memisahkan secara tegas antara **penalaran strategis tingkat tinggi (*strategic reasoning*)** dan **eksekusi taktis tertutup (*domain-specific execution*)**:

| Komponen Agen | Peran & Tanggung Jawab | Output Analisis |
| :--- | :--- | :--- |
| **Supervisor Agent** *(Crisis Commander)* | Triage insiden kargo, ekstraksi profil sensitivitas produk, agregasi multi-kriteria SMDP, dan penetapan putusan mitigasi. | Putusan Mitigasi Final (*Standard / Re-route / Expedited Air*), Estimasi Delay Diselamatkan, & Penyesuaian Biaya. |
| **Geopolitical Risk Specialist** *(Worker 1)* | Monitoring stabilitas koridor maritim (*Suez, Pacific, Atlantic, dll.*) dan evaluasi titik sempit maritim (*chokepoints*). | Status Koridor (*Safe / Caution / Blocked*), Indeks Risiko Geopolitik, & Rekomendasi Rute Maritim. |
| **Meteorology & Port Specialist** *(Worker 2)* | Deteksi kegentingan cuaca oseanografi (*badai/siklon*) dan analisis kepadatan sandar terminal kargo. | Status Atmosferik, Indeks Keparahan Cuaca, & Proyeksi *Port Dwell Days*. |
| **Freight Economics Specialist** *(Worker 3)* | Analisis kelayakan kapasitas pesawat kargo terhadap berat pesanan dan kalkulasi lonjakan tarif moda kargo. | Kelayakan Fisik Udara (*Air Feasibility*), Multiplikasi Biaya, & Estimasi Biaya Alternatif. |

---

## 📊 Dataset Penelitian

Aplikasi menggunakan dataset logistik global publik dari Kaggle:  
**[Global Supply Chain Disruption and Resilience Dataset](https://www.kaggle.com/datasets/bertnardomariouskono/global-supply-chain-disruption-and-resilience)**  
- **Volume Data:** 10.000 transaksi pengiriman kargo internasional lintas benua.
- **Fitur Kunci:** `Order_ID`, `Route_Type`, `Product_Category`, `Transportation_Mode`, `Delay_Days`, `Disruption_Event`, `Geopolitical_Risk_Index`, `Weather_Severity_Index`, `Shipping_Cost_USD`, `Order_Weight_Kg`, dan `Mitigation_Action_Taken`.

---

## 🚀 Panduan Menjalankan Secara Lokal

1. **Clone Repositori:**
   ```bash
   git clone [https://github.com/muryanawaludin/agentic_supply_chain_crisis.git](https://github.com/muryanawaludin/agentic_supply_chain_crisis.git)
   cd agentic_supply_chain_crisis

   agentic_supply_chain_crisis/
├── data/
│   └── global_supply_chain_disruption_v1.csv   # Dataset 10.000 pesanan kargo
├── agent/
│   ├── __init__.py
│   ├── schema.py                                # Skema Pydantic status kargo & asesmen
│   ├── workers.py                               # 3 Worker: Geopolitik, Cuaca, & Ekonomi
│   └── supervisor.py                            # Supervisor: Sintesis multi-kriteria SMDP
├── config.py                                    # Ambang batas risiko & parameter sistem
├── requirements.txt                             # Dependensi pustaka Python
├── app.py                                       # Antarmuka web interaktif Streamlit
├── .gitignore                                   # Filter berkas lingkungan & cache
└── README.md                                    # Dokumentasi resmi proyek

👨‍💻 Penulis & Peneliti
Muryan Awaludin, S.Kom., M.Kom.

Dosen & Peneliti Kecerdasan Buatan / Rekayasa Perangkat Lunak

GitHub: @muryanawaludin

📄 Hak Cipta & Lisensi
Hak Cipta © 2026 Muryan Awaludin. Seluruh hak cipta dilindungi undang-undang.

Proyek ini didistribusikan di bawah lisensi MIT License.
