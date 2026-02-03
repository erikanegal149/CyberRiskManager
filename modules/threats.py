# pages/threats.py
"""Страница каталога угроз"""

import streamlit as st
import pandas as pd
from config import THREAT_CATEGORIES
from data_manager import save_data


def render():
    """Отрисовка страницы угроз"""
    st.title("⚠️ Каталог киберугроз")
    st.markdown("---")
    
    # Форма добавления угрозы
    with st.expander("➕ Добавить новую угрозу", expanded=False):
        with st.form("add_threat"):
            threat_name = st.text_input("Название угрозы")
            threat_category = st.selectbox("Категория", THREAT_CATEGORIES)
            
            if st.form_submit_button("Добавить угрозу"):
                if threat_name:
                    new_threat = {
                        "id": max([t['id'] for t in st.session_state.threats], default=0) + 1,
                        "name": threat_name,
                        "category": threat_category
                    }
                    st.session_state.threats.append(new_threat)
                    save_data()
                    st.success(f"Угроза '{threat_name}' добавлена!")
                    st.rerun()
                else:
                    st.error("Введите название угрозы")
    
    # Таблица угроз
    st.subheader("Список угроз")
    df_threats = pd.DataFrame(st.session_state.threats)
    
    # Фильтр по категории
    categories = df_threats['category'].unique()
    selected_category = st.selectbox("Фильтр по категории", ["Все"] + list(categories))
    
    if selected_category != "Все":
        df_threats = df_threats[df_threats['category'] == selected_category]
    
    st.dataframe(df_threats, use_container_width=True, hide_index=True)