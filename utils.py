# utils.py
"""Вспомогательные функции"""

from config import RISK_COLORS


def get_risk_level(probability: int, impact: int) -> tuple:
    """Расчёт уровня риска"""
    score = probability * impact
    if score <= 4:
        return "Низкий", "🟢"
    elif score <= 9:
        return "Средний", "🟡"
    elif score <= 16:
        return "Высокий", "🟠"
    else:
        return "Критический", "🔴"


def get_risk_color(level: str) -> str:
    """Цвет для уровня риска"""
    return RISK_COLORS.get(level, "#6c757d")