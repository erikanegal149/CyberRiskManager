# pages/dashboard.py
"""Страница дашборда"""

import streamlit as st
import pandas as pd
import plotly.express as px
from utils import get_risk_level


def render():
    """Отрисовка страницы дашборда"""
    st.title("📊 Дашборд менеджмента киберрисков")
    st.markdown("---")
    
    # Метрики
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Всего активов", len(st.session_state.assets))
    
    with col2:
        st.metric("Всего рисков", len(st.session_state.risks))
    
    with col3:
        critical_risks = len([r for r in st.session_state.risks 
                            if get_risk_level(r['probability'], r['impact'])[0] == "Критический"])
        st.metric("Критических рисков", critical_risks)
    
    with col4:
        treated = len([t for t in st.session_state.treatment_plans if t.get('status') == 'Выполнено'])
        st.metric("Обработано рисков", treated)
    
    st.markdown("---")
    
    if st.session_state.risks:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Распределение рисков по уровням")
            risk_levels = [get_risk_level(r['probability'], r['impact'])[0] 
                          for r in st.session_state.risks]
            df_levels = pd.DataFrame({"Уровень": risk_levels})
            level_counts = df_levels['Уровень'].value_counts()
            
            fig = px.pie(
                values=level_counts.values, 
                names=level_counts.index,
                color=level_counts.index,
                color_discrete_map={
                    "Низкий": "#28a745",
                    "Средний": "#ffc107",
                    "Высокий": "#fd7e14",
                    "Критический": "#dc3545"
                }
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("Топ-5 критических рисков")
            sorted_risks = sorted(st.session_state.risks, 
                                 key=lambda x: x['probability'] * x['impact'], 
                                 reverse=True)[:5]
            for risk in sorted_risks:
                level, icon = get_risk_level(risk['probability'], risk['impact'])
                st.write(f"{icon} **{risk['name']}** — {level} ({risk['probability'] * risk['impact']})")
    else:
        st.info("Пока нет оценённых рисков. Перейдите в раздел 'Оценка рисков' для добавления.")