"""
Implementasi Agen Spesialis Bawah (Worker Agents):
1. Geopolitical Risk Specialist
2. Meteorology & Port Operations Specialist
3. Freight Economics Specialist
© 2026 Muryan Awaludin.
"""
from agent.schema import (
    CargoOrderRecord, GeopoliticalAssessment,
    MeteorologyAssessment, FreightEconomicsAssessment
)
from config import CONFIG

class GeopoliticalRiskSpecialist:
    @staticmethod
    def evaluate_corridor(order: CargoOrderRecord) -> GeopoliticalAssessment:
        risk = order.geopolitical_risk_index
        event = str(order.disruption_event).lower()
        
        if "geopolitical" in event or risk >= CONFIG.GEOPOLITICAL_CRITICAL_THRESHOLD:
            status = "BLOCKED_HAZARDOUS"
            threat = f"Eskalasi konflik militer pada koridor maritim {order.route_type}. Risiko penyitaan kargo tinggi."
            rec_corridor = "Alihkan rute memutari Tanjung Harapan (Cape Route) atau koridor laut aman alternatif."
        elif risk >= 0.40:
            status = "CAUTION"
            threat = f"Ketegangan diplomatik terpantau pada rute {order.route_type}. Prosedur inspeksi bea cukai diperketat."
            rec_corridor = "Pertahankan koridor pelayaran dengan peningkatan pengawasan telemetri."
        else:
            status = "SAFE"
            threat = "Koridor transit maritim terpantau stabil tanpa anomali keamanan regional."
            rec_corridor = "Jalur pelayaran reguler standar."

        return GeopoliticalAssessment(
            corridor_status=status,
            risk_level_score=risk,
            chokepoint_threat=threat,
            recommended_corridor=rec_corridor
        )

class MeteorologyPortSpecialist:
    @staticmethod
    def evaluate_environment(order: CargoOrderRecord) -> MeteorologyAssessment:
        weather = order.weather_severity_index
        event = str(order.disruption_event).lower()
        
        dwell_days = 0
        if "port congestion" in event:
            dwell_days = max(3, int(order.delay_days))
            condition = "MODERATE_CHOP"
            advisory = f"Kepadatan terminal tambat di {order.destination_city}. Waktu antre sandar kapal bertambah {dwell_days} hari."
        elif "weather" in event or weather >= CONFIG.WEATHER_SEVERITY_CRITICAL_THRESHOLD:
            dwell_days = max(4, int(weather / 2))
            condition = "SEVERE_STORM_ALERT"
            advisory = "Peringatan badai siklon tropis melintasi jalur laut. Kecepatan jelajah kapal dikurangi demi keselamatan kontainer."
        else:
            condition = "CLEAR"
            advisory = "Kondisi oseanografi dan kapasitas dermaga sandar pelabuhan beroperasi dalam batas normal."

        return MeteorologyAssessment(
            atmospheric_condition=condition,
            weather_severity_score=weather,
            projected_port_dwell_days=dwell_days,
            berth_advisory=advisory
        )

class FreightEconomicsSpecialist:
    @staticmethod
    def evaluate_economics(order: CargoOrderRecord) -> FreightEconomicsAssessment:
        weight = order.order_weight_kg
        base_cost = order.shipping_cost_usd
        inflation = order.inflation_rate_pct
        
        # Kelayakan Fisik Muatan Pesawat Kargo
        is_air_feasible = weight <= CONFIG.AIR_FREIGHT_MAX_WEIGHT_KG
        
        # Estimasi Lonjakan Tarif Moda Udara (Air Freight Premium)
        air_surge_rate = 3.2 * (1.0 + (inflation / 100.0))
        est_air_cost = round(base_cost * air_surge_rate, 2) if is_air_feasible else 0.0
        
        # Estimasi Biaya Perutean Ulang Maritim (Bahan Bakar & Hari Layar Tambahan)
        reroute_surge_rate = 1.35 * (1.0 + (inflation / 100.0))
        est_reroute_cost = round(base_cost * reroute_surge_rate, 2)
        
        weight_status = (
            f"Berat kargo {weight:,.0f} kg memenuhi batas muat pesawat kargo."
            if is_air_feasible
            else f"Berat kargo {weight:,.0f} kg melampaui kapasitas pesawat komersial reguler."
        )
        
        return FreightEconomicsAssessment(
            air_freight_feasibility=is_air_feasible,
            estimated_air_cost_usd=est_air_cost,
            estimated_reroute_cost_usd=est_reroute_cost,
            cost_surge_multiplier=round(air_surge_rate if is_air_feasible else reroute_surge_rate, 2),
            cargo_weight_status=weight_status
        )