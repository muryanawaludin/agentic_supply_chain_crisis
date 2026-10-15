"""
Orkestrator Supervisor: Supply Chain Crisis Commander.
Mengatur sintesis multi-kriteria berbasis SMDP dan Options Framework.
© 2026 Muryan Awaludin.
"""
from typing import Dict
from agent.schema import CargoOrderRecord, HierarchicalMitigationDecision
from agent.workers import (
    GeopoliticalRiskSpecialist, MeteorologyPortSpecialist, FreightEconomicsSpecialist
)

class SupplyChainCrisisSupervisor:

    @staticmethod
    def _get_sensitivity_weights(category: str) -> Dict[str, float]:
        """Menentukan profil bobot [w_Time, w_Cost, w_Risk] berdasarkan kategori produk."""
        cat_lower = category.lower()
        if "semiconductor" in cat_lower or "pharmaceutical" in cat_lower or "perishable" in cat_lower:
            return {"w_time": 0.65, "w_cost": 0.15, "w_risk": 0.20}
        elif "consumer electronics" in cat_lower or "auto parts" in cat_lower:
            return {"w_time": 0.45, "w_cost": 0.35, "w_risk": 0.20}
        else:
            return {"w_time": 0.20, "w_cost": 0.60, "w_risk": 0.20}

    @classmethod
    def resolve_supply_chain_crisis(cls, order: CargoOrderRecord) -> HierarchicalMitigationDecision:
        weights = cls._get_sensitivity_weights(order.product_category)
        
        # 1. Pendelegasian Analisis ke Tiga Worker
        geo_rep = GeopoliticalRiskSpecialist.evaluate_corridor(order)
        met_rep = MeteorologyPortSpecialist.evaluate_environment(order)
        econ_rep = FreightEconomicsSpecialist.evaluate_economics(order)
        
        event_str = str(order.disruption_event)
        decision: str = "Standard Shipping"
        delay_saved = 0
        financial_delta = 0.0
        rationale = ""
        
        # 2. Logika Optimasi Multi-Atribut Supervisor (SMDP Option Selection)
        if geo_rep.corridor_status == "BLOCKED_HAZARDOUS":
            if weights["w_time"] >= 0.50 and econ_rep.air_freight_feasibility:
                decision = "Expedited Air Freight"
                delay_saved = max(5, int(order.delay_days * 0.8))
                financial_delta = econ_rep.estimated_air_cost_usd - order.shipping_cost_usd
                rationale = (
                    f"Supervisor mengesahkan opsi EXPEDITED AIR FREIGHT: Kargo {order.product_category} memiliki sensitivitas "
                    f"waktu kritis ({weights['w_time']*100:.0f}%). Koridor Suez/Pacific terblokir konflik; pengalihan "
                    f"ke moda udara menyelamatkan estimasi {delay_saved} hari keterlambatan."
                )
            else:
                decision = "Re-routing"
                delay_saved = max(2, int(order.delay_days * 0.4))
                financial_delta = econ_rep.estimated_reroute_cost_usd - order.shipping_cost_usd
                rationale = (
                    f"Supervisor mengesahkan opsi RE-ROUTING: Jalur maritim dialihkan memutari koridor aman alternatif. "
                    f"Meskipun menambah biaya bahan bakar bunker, opsi ini melindungi integritas fisik kargo tanpa lonjakan tarif udara."
                )
        elif met_rep.atmospheric_condition == "SEVERE_STORM_ALERT" or met_rep.projected_port_dwell_days >= 4:
            if weights["w_time"] >= 0.50 and econ_rep.air_freight_feasibility:
                decision = "Expedited Air Freight"
                delay_saved = max(3, int(order.delay_days * 0.7))
                financial_delta = econ_rep.estimated_air_cost_usd - order.shipping_cost_usd
                rationale = (
                    f"Supervisor mengesahkan opsi EXPEDITED AIR FREIGHT: Kemacetan pelabuhan/badai laut parah dihindari "
                    f"dengan mentransfer muatan ke terminal kargo udara demi memenuhi Service Level Agreement produk bernilai tinggi."
                )
            else:
                decision = "Standard Shipping"
                delay_saved = 0
                financial_delta = 0.0
                rationale = (
                    f"Supervisor mempertahankan opsi STANDARD SHIPPING: Kategori {order.product_category} "
                    f"memiliki toleransi biaya tinggi ({weights['w_cost']*100:.0f}%). Penambahan biaya transfer udara tidak proporsional "
                    f"terhadap nilai barang; keterlambatan {order.delay_days} hari diserap melalui penyangga stok lokal."
                )
        else:
            decision = "Standard Shipping"
            delay_saved = 0
            financial_delta = 0.0
            rationale = "Operasi pengiriman kargo berada pada ambang batas koridor normal. Tidak diperlukan intervensi mitigasi darurat."

        return HierarchicalMitigationDecision(
            order_id=order.order_id,
            product_category=order.product_category,
            disruption_type=event_str if event_str != "nan" else "Tidak Ada Disrupsi",
            sensitivity_weights=weights,
            geopolitical_report=geo_rep,
            meteorology_report=met_rep,
            economics_report=econ_rep,
            recommended_mitigation=decision,
            projected_delay_mitigated_days=delay_saved,
            projected_financial_impact_usd=round(financial_delta, 2),
            executive_rationalization=rationale
        )