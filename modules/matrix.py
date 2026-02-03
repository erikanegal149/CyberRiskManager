# pages/matrix.py
"""Страница матрицы рисков"""

import streamlit as st
import plotly.graph_objects as go


def render():
    """Отрисовка страницы матрицы рисков"""
    st.title("📈 Матрица киберрисков")
    st.markdown("---")
    
    # Создание матрицы 5x5
    matrix_data = [[0 for _ in range(5)] for _ in range(5)]
    risk_names_matrix = [[[] for _ in range(5)] for _ in range(5)]
    
    for risk in st.session_state.risks:
        p = risk['probability'] - 1
        i = risk['impact'] - 1
        matrix_data[4-i][p] += 1
        risk_names_matrix[4-i][p].append(risk['name'])
    
    # Цвета для матрицы
    colors = [
        ["#28a745", "#28a745", "#ffc107", "#ffc107", "#fd7e14"],
        ["#28a745", "#ffc107", "#ffc107", "#fd7e14", "#fd7e14"],
        ["#ffc107", "#ffc107", "#fd7e14", "#fd7e14", "#dc3545"],
        ["#ffc107", "#fd7e14", "#fd7e14", "#dc3545", "#dc3545"],
        ["#fd7e14", "#fd7e14", "#dc3545", "#dc3545", "#dc3545"],
    ]
    
    # Создание heatmap
    fig = go.Figure()
    
    for i in range(5):
        for j in range(5):
            risk_count = matrix_data[i][j]
            risk_list = risk_names_matrix[i][j]
            hover_text = f"Рисков: {risk_count}"
            if risk_list:
                hover_text += "<br>" + "<br>".join(risk_list[:5])
                if len(risk_list) > 5:
                    hover_text += f"<br>... и ещё {len(risk_list) - 5}"
            
            fig.add_trace(go.Scatter(
                x=[j + 0.5],
                y=[4 - i + 0.5],
                mode='markers+text',
                marker=dict(size=60, color=colors[i][j], opacity=0.8),
                text=str(risk_count) if risk_count > 0 else "",
                textfont=dict(size=20, color='white'),
                hovertext=hover_text,
                hoverinfo='text',
                showlegend=False
            ))
    
    fig.update_layout(
        title="Матрица рисков 5×5",
        xaxis=dict(
            title="Вероятность",
            tickmode='array',
            tickvals=[0.5, 1.5, 2.5, 3.5, 4.5],
            ticktext=['Очень низкая', 'Низкая', 'Средняя', 'Высокая', 'Очень высокая'],
            range=[0, 5]
        ),
        yaxis=dict(
            title="Воздействие",
            tickmode='array',
            tickvals=[0.5, 1.5, 2.5, 3.5, 4.5],
            ticktext=['Незначительное', 'Низкое', 'Среднее', 'Высокое', 'Критическое'],
            range=[0, 5]
        ),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("""
    **Легенда:**
    - 🟢 Низкий риск (1-4)
    - 🟡 Средний риск (5-9)
    - 🟠 Высокий риск (10-16)
    - 🔴 Критический риск (17-25)
    """)