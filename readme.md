# 👥 Autonomous Software Engineering Squad: Multi-Agent System (MAS) Platform

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://agentic-software-squad.streamlit.app)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/muryanawaludin/agentic_software_squad.git)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Implementasi platform **Sistem Multi-Agen (MAS)** otonom untuk simulasi dan automasi rekayasa perangkat lunak perusahaan. Memadukan pembagian peran fungsional terdistribusi, protokol komunikasi terstruktur berbasis **FIPA-ACL**, arsitektur memori bersama (*Blackboard System*), serta **Protokol Konsensus Semantik** dengan hak veto pengujian.

---

## 🌐 Demo Aplikasi Langsung

Aplikasi ini dapat diuji secara interaktif tanpa instalasi lokal melalui peramban:  
👉 **[Buka Demo Aplikasi Streamlit](https://agentic-software-squad.streamlit.app)**  
*(Alternatif: [agentic_software_squad.streamlit.app](https://agentic_software_squad.streamlit.app))*

---

## 🎯 Peran Skuad & Arsitektur Kognitif

Sistem mengorkestrasi 4 agen spesialis yang berkolaborasi menyelesaikan tiket pengembangan dari dataset Kaggle:

| Peran Agen | Tanggung Jawab Operasional | Artefak Keluaran |
| :--- | :--- | :--- |
| **Analyst Agent** | Dekomposisi tugas & analisis kebutuhan | *User Story* & *Acceptance Criteria* formal |
| **Programmer Agent** | Perancangan arsitektur & sintesis logika | Kode modul Python deterministik |
| **Reviewer Agent** | Audit keamanan kode & pemeriksaan *code smell* | Skor audit keamanan & catatan kelemahan |
| **Tester Agent** | Eksekusi unit test sintetis & kasus batas | Matriks uji kasus batas (*Passed/Failed*) |

---

## 📊 Sumber Data Penelitian

Dataset yang digunakan bersumber dari repositori publik Kaggle:  
**[Software Development Employee Project Dataset](https://www.kaggle.com/datasets/firozfau/software-development-employee-project-dataset)**  
- `employees.csv`: 2.500 profil karyawan dengan matriks keahlian, beban kerja, dan skor kinerja historis.
- `tasks.csv`: 15.000 catatan tugas perangkat lunak lintas kompleksitas (*Low, Medium, High*).
- `projects.csv`: 900 proyek enterprise dengan dependensi tumpukan teknologi modern.

---

## 🚀 Panduan Menjalankan Secara Lokal

1. **Kloning Repositori:**
   ```bash
   git clone [https://github.com/muryanawaludin/agentic_software_squad.git](https://github.com/muryanawaludin/agentic_software_squad.git)
   cd agentic_software_squad

👨‍💻 Penulis & Peneliti
Muryan Awaludin, S.Kom., M.Kom.

Dosen & Peneliti Kecerdasan Buatan / Rekayasa Perangkat Lunak

GitHub: @muryanawaludin

Hak Cipta © 2026 Muryan Awaludin. Seluruh hak cipta dilindungi undang-undang.