"""
Konfigurasi Global Sistem Hierarkis Krisis Rantai Pasok.
© 2026 Muryan Awaludin. Seluruh hak cipta dilindungi undang-undang.
"""
from dataclasses import dataclass
import os

@dataclass(frozen=True)
class SupplyChainConfig:
    APP_TITLE: str = "Supply Chain Crisis Command Center: Hierarchical Multi-Agent"
    AUTHOR_COPYRIGHT: str = "© 2026 Muryan Awaludin. Seluruh hak cipta dilindungi undang-undang."
    DATA_PATH: str = os.path.join(os.path.dirname(__file__), "data", "global_supply_chain_disruption_v1.csv")

    # Ambang Batas Evaluasi Krisis
    GEOPOLITICAL_CRITICAL_THRESHOLD: float = 0.60
    WEATHER_SEVERITY_CRITICAL_THRESHOLD: float = 7.0
    AIR_FREIGHT_MAX_WEIGHT_KG: float = 12000.0

CONFIG = SupplyChainConfig()