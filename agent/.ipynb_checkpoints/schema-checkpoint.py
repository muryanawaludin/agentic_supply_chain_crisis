"""
Definisi Skema Pydantic untuk Pesanan Kargo, Laporan Spesialis Worker, dan Putusan Supervisor.
© 2026 Muryan Awaludin.
"""
from typing import List, Dict, Any, Optional, Literal
from pydantic import BaseModel, Field

class CargoOrderRecord(BaseModel):
    order_id: str
    order_date: str
    origin_city: str
    destination_city: str
    route_type: str
    transportation_mode: str
    product_category: str
    base_lead_time_days: int
    scheduled_lead_time_days: int
    actual_lead_time_days: int
    delay_days: int
    delivery_status: str
    disruption_event: Optional[str] = "None"
    geopolitical_risk_index: float
    weather_severity_index: float
    inflation_rate_pct: float
    shipping_cost_usd: float
    order_weight_kg: float
    historical_mitigation: str

class GeopoliticalAssessment(BaseModel):
    corridor_status: Literal["SAFE", "CAUTION", "BLOCKED_HAZARDOUS"]
    risk_level_score: float
    chokepoint_threat: str
    recommended_corridor: str

class MeteorologyAssessment(BaseModel):
    atmospheric_condition: Literal["CLEAR", "MODERATE_CHOP", "SEVERE_STORM_ALERT"]
    weather_severity_score: float
    projected_port_dwell_days: int
    berth_advisory: str

class FreightEconomicsAssessment(BaseModel):
    air_freight_feasibility: bool
    estimated_air_cost_usd: float
    estimated_reroute_cost_usd: float
    cost_surge_multiplier: float
    cargo_weight_status: str

class HierarchicalMitigationDecision(BaseModel):
    order_id: str
    product_category: str
    disruption_type: str
    sensitivity_weights: Dict[str, float]
    geopolitical_report: GeopoliticalAssessment
    meteorology_report: MeteorologyAssessment
    economics_report: FreightEconomicsAssessment
    recommended_mitigation: Literal["Standard Shipping", "Re-routing", "Expedited Air Freight"]
    projected_delay_mitigated_days: int
    projected_financial_impact_usd: float
    executive_rationalization: str