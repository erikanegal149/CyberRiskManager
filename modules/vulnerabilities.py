# pages/vulnerabilities.py
"""Страница каталога уязвимостей"""

import streamlit as st
import pandas as pd
from config import VULNERABILITY_CATEGORIES
from data_manager import save_data


def render():
    """Отрисовка страницы уязвимостей"""
    st.title("🔓 Каталог уязвимостей")
    st.markdown("---")
    
    # Форма добавления уязвимости
    with st.expander("➕ Добавить новую уязвимость", expanded=False):
        with st.form("add_vulnerability"):
            vuln_name = st.text_input("Название уязвимости")
            vuln_category = st.selectbox("Категория", VULNERABILITY_CATEGORIES)
            
            if st.form_submit_button("Добавить уязвимость"):
                if vuln_name:
                    new_vuln = {
                        "id": max([v['id'] for v in st.session_state.vulnerabilities], default=0) + 1,
                        "name": vuln_name,
                        "category": vuln_category
                    }
                    st.session_state.vulnerabilities.append(new_vuln)
                    save_data()
                    st.success(f"Уязвимость '{vuln_name}' добавлена!")
                    st.rerun()
                else:
                    st.error("Введите название уязвимости")
    
    # Таблица уязвимостей
    st.subheader("Список уязвимостей")
    df_vulns = pd.DataFrame(st.session_state.vulnerabilities)
    
    # Фильтр по категории
    categories = df_vulns['category'].unique()
    selected_category = st.selectbox("Фильтр по категории", ["Все"] + list(categories))
    
    if selected_category != "Все":
        df_vulns = df_vulns[df_vulns['category'] == selected_category]
    
    st.dataframe(df_vulns, use_container_width=True, hide_index=True)