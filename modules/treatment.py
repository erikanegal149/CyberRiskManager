# pages/treatment.py
"""Страница плана обработки рисков"""

import streamlit as st
import pandas as pd
from config import TREATMENT_OPTIONS, TREATMENT_STATUSES
from data_manager import save_data


def render():
    """Отрисовка страницы плана обработки"""
    st.title("🛠️ План обработки рисков")
    st.markdown("---")
    
    if not st.session_state.risks:
        st.warning("Сначала добавьте риски в разделе 'Оценка рисков'")
        return
    
    with st.expander("➕ Добавить план обработки", expanded=False):
        with st.form("add_treatment"):
            selected_risk = st.selectbox(
                "Выберите риск",
                options=[r['name'] for r in st.session_state.risks]
            )
            treatment_option = st.selectbox("Вариант обработки", TREATMENT_OPTIONS)
            measures = st.text_area("Меры по обработке")
            responsible = st.text_input("Ответственный")
            deadline = st.date_input("Срок выполнения")
            status = st.selectbox("Статус", TREATMENT_STATUSES)
            
            if st.form_submit_button("Добавить план"):
                new_plan = {
                    "id": max([p['id'] for p in st.session_state.treatment_plans], default=0) + 1,
                    "risk": selected_risk,
                    "option": treatment_option,
                    "measures": measures,
                    "responsible": responsible,
                    "deadline": deadline.strftime("%Y-%m-%d"),
                    "status": status
                }
                st.session_state.treatment_plans.append(new_plan)
                save_data()
                st.success("План обработки добавлен!")
                st.rerun()
    
    # Таблица планов
    if st.session_state.treatment_plans:
        st.subheader("Планы обработки")
        df_plans = pd.DataFrame(st.session_state.treatment_plans)
        st.dataframe(df_plans, use_container_width=True, hide_index=True)