"""
Aplikasi Antarmuka Pengguna Streamlit:
Dasbor Pusat Komando Krisis Rantai Pasok Berbasis Arsitektur Agen Hierarkis.
© 2026 Muryan Awaludin. Seluruh hak cipta dilindungi undang-undang.
"""
import streamlit as st
import pandas as pd
import json
import os
from config import CONFIG
from agent.schema import CargoOrderRecord
from agent.supervisor import SupplyChainCrisisSupervisor

st.set_page_config(
    page_title=CONFIG.APP_TITLE,
    page_icon="🚢",
    layout="wide"
)

st.title("🚢 Supply Chain Crisis Command Center: Hierarchical Multi-Agent Architecture")
st.caption("Penerapan Pola Supervisor-Worker: Komando Kognitif, Delegasi Spesialis, dan Resolusi Mitigasi SMDP Berbasis Dataset Kaggle")

# Pemuatan Dataset Kaggle Secara Defensif
@st.cache_data
def load_supply_chain_dataset(path: str) -> pd.DataFrame:
    if os.path.exists(path):
        try:
            return pd.read_csv(path, sep=None, engine="python", encoding="utf-8-sig")
        except Exception:
            try:
                return pd.read_csv(path, encoding="latin-1")
            except Exception:
                return pd.DataFrame()
    return pd.DataFrame()

df_sc = load_supply_chain_dataset(CONFIG.DATA_PATH)

# Sidebar: Filter dan Pemilihan Tiket Kargo
with st.sidebar:
    st.header("📋 Pemilihan Tiket Pengiriman Kargo")
    st.markdown("Sumber: *Kaggle Global Supply Chain Disruption Dataset (10.000 Baris)*")

    if not df_sc.empty:
        filter_mode = st.radio(
            "Filter Skenario Pesanan:",
            ["Seluruh Data", "Disrupsi Geopolitik", "Kongesti Pelabuhan", "Cuaca Ekstrem (Badai/Topan)"]
        )

        if filter_mode == "Disrupsi Geopolitik":
            filtered_df = df_sc[df_sc["Disruption_Event"].astype(str).str.contains("Geopolitical", na=False)]
        elif filter_mode == "Kongesti Pelabuhan":
            filtered_df = df_sc[df_sc["Disruption_Event"].astype(str).str.contains("Port Congestion", na=False)]
        elif filter_mode == "Cuaca Ekstrem (Badai/Topan)":
            filtered_df = df_sc[df_sc["Disruption_Event"].astype(str).str.contains("Weather", na=False)]
        else:
            filtered_df = df_sc

        selected_idx = st.selectbox(
            "Pilih ID Pesanan:",
            range(min(50, len(filtered_df))),
            format_func=lambda i: f"[{filtered_df.iloc[i]['Order_ID']}] {filtered_df.iloc[i]['Product_Category']} ({filtered_df.iloc[i]['Route_Type']})"
        )

        row = filtered_df.iloc[selected_idx]
        active_order = CargoOrderRecord(
            order_id=str(row["Order_ID"]),
            order_date=str(row["Order_Date"]),
            origin_city=str(row["Origin_City"]),
            destination_city=str(row["Destination_City"]),
            route_type=str(row["Route_Type"]),
            transportation_mode=str(row["Transportation_Mode"]),
            product_category=str(row["Product_Category"]),
            base_lead_time_days=int(row["Base_Lead_Time_Days"]),
            scheduled_lead_time_days=int(row["Scheduled_Lead_Time_Days"]),
            actual_lead_time_days=int(row["Actual_Lead_Time_Days"]),
            delay_days=int(row["Delay_Days"]),
            delivery_status=str(row["Delivery_Status"]),
            disruption_event=str(row["Disruption_Event"]) if pd.notna(row["Disruption_Event"]) else "None",
            geopolitical_risk_index=float(row["Geopolitical_Risk_Index"]),
            weather_severity_index=float(row["Weather_Severity_Index"]),
            inflation_rate_pct=float(row["Inflation_Rate_Pct"]),
            shipping_cost_usd=float(row["Shipping_Cost_USD"]),
            order_weight_kg=float(row["Order_Weight_Kg"]),
            historical_mitigation=str(row["Mitigation_Action_Taken"])
        )
    else:
        st.error("Dataset 'global_supply_chain_disruption_v1.csv' tidak ditemukan.")
        active_order = None

    btn_trigger_crisis = st.button("🚀 Aktifkan Komando Krisis Hierarkis", type="primary", use_container_width=True, disabled=(active_order is None))

    if active_order:
        st.divider()
        st.markdown(f"**Order ID:** `{active_order.order_id}`")
        st.markdown(f"**Kategori Produk:** `{active_order.product_category}`")
        st.markdown(f"**Rute:** {active_order.origin_city} ➔ {active_order.destination_city} (`{active_order.route_type}`)")
        st.markdown(f"**Event Disrupsi:** `{active_order.disruption_event}`")
        st.markdown(f"**Keterlambatan Tercatat:** `{active_order.delay_days} Hari`")
        st.markdown(f"**Biaya Pengiriman Dasar:** `USD {active_order.shipping_cost_usd:,.2f}`")

    st.divider()
    st.markdown("© 2026 **Muryan Awaludin**  \nHak Cipta Dilindungi.")

# Area Kerja Utama
if btn_trigger_crisis and active_order:
    with st.spinner("Supervisor sedang mengorkestrasi analisis spesialis geopolitik, cuaca, dan ekonomi kargo..."):
        decision_report = SupplyChainCrisisSupervisor.resolve_supply_chain_crisis(active_order)
        st.session_state.crisis_decision = decision_report
        st.session_state.active_order_stored = active_order

if "crisis_decision" in st.session_state and st.session_state.crisis_decision is not None:
    res = st.session_state.crisis_decision
    ord_ctx = st.session_state.active_order_stored

    # 1. Lapisan Atas: Putusan Strategis Supervisor
    st.subheader(f"🎯 Putusan Strategis Supervisor: Pesanan #{res.order_id}")
    
    col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
    col_stat1.metric("Rekomendasi Mitigasi", res.recommended_mitigation)
    col_stat2.metric("Mitigasi Historis Industri", ord_ctx.historical_mitigation)
    col_stat3.metric("Hari Delay Dihemat", f"{res.projected_delay_mitigated_days} Hari")
    col_stat4.metric("Dampak Biaya Tambahan", f"USD {res.projected_financial_impact_usd:,.2f}")

    if res.recommended_mitigation == "Expedited Air Freight":
        st.success("⚡ **PUTUSAN SUPERVISOR: TRANSFER KARGO UDARA EKSPRES DISETUJUI**")
    elif res.recommended_mitigation == "Re-routing":
        st.warning("🔄 **PUTUSAN SUPERVISOR: PERUTEAN ULANG MARITIM AMAN DISETUJUI**")
    else:
        st.info("📦 **PUTUSAN SUPERVISOR: PENYERAPAN STOK STANDAR DIPERTAHANKAN**")

    st.markdown("#### Rasionalisasi Komando Eksekutif")
    st.info(res.executive_rationalization)

    st.divider()

    # 2. Lapisan Bawah: Laporan 3 Agen Spesialis Worker
    st.subheader("🕵️ Laporan Evaluasi Tiga Agen Spesialis (Worker Level)")
    col_geo, col_met, col_econ = st.columns(3)

    with col_geo:
        st.markdown("### 🌐 Geopolitical Risk Specialist")
        st.caption("Pilar Stabilitas Koridor & Chokepoints")
        with st.container(border=True):
            st.markdown(f"**Indeks Risiko Geopolitik:** `{res.geopolitical_report.risk_level_score}`")
            status_badge = "🔴" if res.geopolitical_report.corridor_status == "BLOCKED_HAZARDOUS" else ("🟡" if res.geopolitical_report.corridor_status == "CAUTION" else "🟢")
            st.markdown(f"{status_badge} **Status Koridor:** `{res.geopolitical_report.corridor_status}`")
            st.markdown(f"**Ancaman Wilayah:**\n{res.geopolitical_report.chokepoint_threat}")
            st.markdown(f"**Rekomendasi Rute:**\n*{res.geopolitical_report.recommended_corridor}*")

    with col_met:
        st.markdown("### ⛈️ Meteorology & Port Agent")
        st.caption("Pilar Cuaca Ekstrem & Kongesti Sandar")
        with st.container(border=True):
            st.markdown(f"**Indeks Keparahan Cuaca:** `{res.meteorology_report.weather_severity_score} / 10.0`")
            met_badge = "🔴" if res.meteorology_report.atmospheric_condition == "SEVERE_STORM_ALERT" else ("🟡" if res.meteorology_report.atmospheric_condition == "MODERATE_CHOP" else "🟢")
            st.markdown(f"{met_badge} **Kondisi:** `{res.meteorology_report.atmospheric_condition}`")
            st.markdown(f"**Proyeksi Delay Pelabuhan:** `{res.meteorology_report.projected_port_dwell_days} Hari`")
            st.markdown(f"**Advis Sandar:**\n{res.meteorology_report.berth_advisory}")

    with col_econ:
        st.markdown("### 💰 Freight Economics Specialist")
        st.caption("Pilar Analisis Tarif Kargo & Batas Bobot")
        with st.container(border=True):
            st.markdown(f"**Kelayakan Moda Udara:** `{'LAYAK' if res.economics_report.air_freight_feasibility else 'TIDAK LAYAK (OVERWEIGHT)'}`")
            st.markdown(f"**Multiplikasi Lonjakan Biaya:** `{res.economics_report.cost_surge_multiplier}x`")
            st.markdown(f"**Estimasi Biaya Udara:** `USD {res.economics_report.estimated_air_cost_usd:,.2f}`")
            st.markdown(f"**Estimasi Biaya Reroute:** `USD {res.economics_report.estimated_reroute_cost_usd:,.2f}`")
            st.caption(f"Status: {res.economics_report.cargo_weight_status}")

    # Profil Bobot Sensitivitas Produk
    st.divider()
    st.markdown("#### Matriks Pembobotan Multi-Atribut SMDP Berdasarkan Kategori Produk")
    w = res.sensitivity_weights
    w_df = pd.DataFrame([{
        "Kategori Produk": res.product_category,
        "Bobot Sensitivitas Waktu (w_Time)": f"{w['w_time']*100:.0f}%",
        "Bobot Sensitivitas Biaya (w_Cost)": f"{w['w_cost']*100:.0f}%",
        "Bobot Sensitivitas Risiko (w_Risk)": f"{w['w_risk']*100:.0f}%"
    }])
    st.dataframe(w_df, use_container_width=True, hide_index=True)
else:
    st.info("Pilih tiket pesanan kargo pada bilah samping lalu tekan **'Aktifkan Komando Krisis Hierarkis'** untuk memulai analisis.")

st.divider()
st.caption(CONFIG.AUTHOR_COPYRIGHT)