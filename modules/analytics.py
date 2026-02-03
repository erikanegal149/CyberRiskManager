# modules/analytics.py
"""Страница аналитики"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils import get_risk_level


def render():
    """Отрисовка страницы аналитики"""
    st.title("📊 Аналитика киберрисков")
    st.markdown("---")
    
    if not st.session_state.risks:
        st.warning("Нет данных для анализа. Добавьте риски в разделе 'Оценка рисков'.")
        return
    
    # Преобразуем данные в DataFrame
    df_risks = pd.DataFrame(st.session_state.risks)
    df_risks['level'] = df_risks.apply(
        lambda x: get_risk_level(x['probability'], x['impact'])[0], axis=1
    )
    df_risks['date'] = pd.to_datetime(df_risks['date'])
    
    # Метрики в верхней части
    st.subheader("📈 Ключевые показатели")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    total_risks = len(df_risks)
    critical = len(df_risks[df_risks['level'] == 'Критический'])
    high = len(df_risks[df_risks['level'] == 'Высокий'])
    medium = len(df_risks[df_risks['level'] == 'Средний'])
    low = len(df_risks[df_risks['level'] == 'Низкий'])
    
    col1.metric("Всего рисков", total_risks)
    col2.metric("🔴 Критических", critical)
    col3.metric("🟠 Высоких", high)
    col4.metric("🟡 Средних", medium)
    col5.metric("🟢 Низких", low)
    
    st.markdown("---")
    
    # Графики в два столбца
    col1, col2 = st.columns(2)
    
    with col1:
        # График по категориям угроз
        st.subheader("Риски по категориям угроз")
        
        df_threats = pd.DataFrame(st.session_state.threats)
        risk_threats = df_risks.merge(
            df_threats[['name', 'category']], 
            left_on='threat', 
            right_on='name', 
            how='left',
            suffixes=('', '_threat')
        )
        
        threat_counts = risk_threats['category'].value_counts()
        
        fig_threats = px.bar(
            x=threat_counts.index,
            y=threat_counts.values,
            labels={'x': 'Категория угрозы', 'y': 'Количество рисков'},
            color=threat_counts.values,
            color_continuous_scale='Reds'
        )
        fig_threats.update_layout(showlegend=False)
        st.plotly_chart(fig_threats, use_container_width=True)
    
    with col2:
        # График по активам
        st.subheader("Риски по активам")
        
        asset_counts = df_risks['asset'].value_counts().head(10)
        
        fig_assets = px.bar(
            x=asset_counts.values,
            y=asset_counts.index,
            orientation='h',
            labels={'x': 'Количество рисков', 'y': 'Актив'},
            color=asset_counts.values,
            color_continuous_scale='Blues'
        )
        fig_assets.update_layout(showlegend=False, yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig_assets, use_container_width=True)
    
    st.markdown("---")
    
    # Вторая строка графиков
    col1, col2 = st.columns(2)
    
    with col1:
        # Динамика рисков по времени
        st.subheader("Динамика выявления рисков")
        
        df_risks_sorted = df_risks.sort_values('date')
        df_risks_sorted['cumulative'] = range(1, len(df_risks_sorted) + 1)
        
        fig_timeline = px.line(
            df_risks_sorted,
            x='date',
            y='cumulative',
            labels={'date': 'Дата', 'cumulative': 'Накопленное количество рисков'},
            markers=True
        )
        fig_timeline.update_traces(line_color='#ff6b6b')
        st.plotly_chart(fig_timeline, use_container_width=True)
    
    with col2:
        # Статус обработки рисков
        st.subheader("Статус обработки рисков")
        
        if st.session_state.treatment_plans:
            df_plans = pd.DataFrame(st.session_state.treatment_plans)
            status_counts = df_plans['status'].value_counts()
            
            colors_map = {
                'Выполнено': '#28a745',
                'В процессе': '#ffc107',
                'Запланировано': '#6c757d'
            }
            
            fig_status = px.pie(
                values=status_counts.values,
                names=status_counts.index,
                color=status_counts.index,
                color_discrete_map=colors_map
            )
            st.plotly_chart(fig_status, use_container_width=True)
        else:
            st.info("Нет планов обработки")
    
    st.markdown("---")
    
    # Третья строка
    col1, col2 = st.columns(2)
    
    with col1:
        # Средний балл риска по активам
        st.subheader("Средний уровень риска по активам")
        
        avg_risk = df_risks.groupby('asset')['score'].mean().sort_values(ascending=True)
        
        fig_avg = px.bar(
            x=avg_risk.values,
            y=avg_risk.index,
            orientation='h',
            labels={'x': 'Средний балл риска', 'y': 'Актив'},
            color=avg_risk.values,
            color_continuous_scale='RdYlGn_r'
        )
        fig_avg.update_layout(showlegend=False)
        st.plotly_chart(fig_avg, use_container_width=True)
    
    with col2:
        # Распределение по вероятности и воздействию
        st.subheader("Распределение рисков")
        
        fig_scatter = px.scatter(
            df_risks,
            x='probability',
            y='impact',
            size='score',
            color='level',
            hover_name='name',
            labels={
                'probability': 'Вероятность',
                'impact': 'Воздействие',
                'level': 'Уровень'
            },
            color_discrete_map={
                'Низкий': '#28a745',
                'Средний': '#ffc107',
                'Высокий': '#fd7e14',
                'Критический': '#dc3545'
            }
        )
        fig_scatter.update_layout(
            xaxis=dict(tickmode='linear', tick0=1, dtick=1),
            yaxis=dict(tickmode='linear', tick0=1, dtick=1)
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown("---")
    
    # Таблица сводки
    st.subheader("📋 Сводная таблица рисков по уровням")
    
    summary_data = []
    for level in ['Критический', 'Высокий', 'Средний', 'Низкий']:
        level_risks = df_risks[df_risks['level'] == level]
        if len(level_risks) > 0:
            summary_data.append({
                'Уровень': level,
                'Количество': len(level_risks),
                'Доля (%)': round(len(level_risks) / total_risks * 100, 1),
                'Средний балл': round(level_risks['score'].mean(), 1),
                'Макс. балл': level_risks['score'].max()
            })
    
    df_summary = pd.DataFrame(summary_data)
    st.dataframe(df_summary, use_container_width=True, hide_index=True)