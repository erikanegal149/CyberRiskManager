# app.py
"""Главный файл приложения Менеджмент киберрисков"""

import streamlit as st
from config import APP_TITLE, APP_ICON
from data_manager import init_session_state
from modules import dashboard, assets, threats, vulnerabilities, risks, matrix, treatment, reports, analytics

# Конфигурация страницы
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Инициализация данных
init_session_state()

# Боковое меню
page = st.sidebar.radio(
    "Навигация",
    ["📊 Дашборд", "💼 Активы", "⚠️ Угрозы", "🔓 Уязвимости", 
     "📋 Оценка рисков", "📈 Матрица рисков", "🛠️ План обработки", 
     "📉 Аналитика", "📄 Отчёты"]
)

# Роутинг страниц
match page:
    case "📊 Дашборд":
        dashboard.render()
    case "💼 Активы":
        assets.render()
    case "⚠️ Угрозы":
        threats.render()
    case "🔓 Уязвимости":
        vulnerabilities.render()
    case "📋 Оценка рисков":
        risks.render()
    case "📈 Матрица рисков":
        matrix.render()
    case "🛠️ План обработки":
        treatment.render()
    case "📉 Аналитика":
        analytics.render()
    case "📄 Отчёты":
        reports.render()

# Футер
st.sidebar.markdown("---")
st.sidebar.markdown(f"**{APP_TITLE}**")
st.sidebar.markdown("Согласно ISO/IEC 27005:2022")
st.sidebar.markdown("и ISO/IEC 27032")