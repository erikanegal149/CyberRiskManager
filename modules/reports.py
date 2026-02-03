# modules/reports.py
"""Страница отчётов"""

import streamlit as st
import pandas as pd
from datetime import datetime
from io import BytesIO
from utils import get_risk_level


def create_excel_file(df):
    """Создание Excel файла в памяти"""
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Данные')
    output.seek(0)
    return output


def render():
    """Отрисовка страницы отчётов"""
    st.title("📄 Отчёты")
    st.markdown("---")
    
    st.subheader("Экспорт данных")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.session_state.assets:
            df_assets = pd.DataFrame(st.session_state.assets)
            excel_file = create_excel_file(df_assets)
            st.download_button(
                label="📥 Скачать активы (Excel)",
                data=excel_file,
                file_name=f"assets_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.warning("Нет активов для экспорта")
    
    with col2:
        if st.session_state.risks:
            df_risks = pd.DataFrame(st.session_state.risks)
            excel_file = create_excel_file(df_risks)
            st.download_button(
                label="📥 Скачать риски (Excel)",
                data=excel_file,
                file_name=f"risks_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.warning("Нет рисков для экспорта")
    
    with col3:
        if st.session_state.treatment_plans:
            df_plans = pd.DataFrame(st.session_state.treatment_plans)
            excel_file = create_excel_file(df_plans)
            st.download_button(
                label="📥 Скачать планы (Excel)",
                data=excel_file,
                file_name=f"treatment_plans_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.warning("Нет планов для экспорта")
    
    st.markdown("---")
    
    # Полный отчёт
    st.subheader("Полный отчёт")
    
    if st.session_state.risks:
        # Создаём полный отчёт со всеми данными
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            pd.DataFrame(st.session_state.assets).to_excel(writer, index=False, sheet_name='Активы')
            pd.DataFrame(st.session_state.threats).to_excel(writer, index=False, sheet_name='Угрозы')
            pd.DataFrame(st.session_state.vulnerabilities).to_excel(writer, index=False, sheet_name='Уязвимости')
            pd.DataFrame(st.session_state.risks).to_excel(writer, index=False, sheet_name='Риски')
            pd.DataFrame(st.session_state.treatment_plans).to_excel(writer, index=False, sheet_name='Планы обработки')
        output.seek(0)
        
        st.download_button(
            label="📥 Скачать полный отчёт (Excel)",
            data=output,
            file_name=f"cyber_risk_report_{datetime.now().strftime('%Y%m%d')}.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            type="primary"
        )
    
    st.markdown("---")
    
    # Сводный отчёт
    st.subheader("Сводный отчёт")
    
    report = f"""
## Отчёт по менеджменту киберрисков

**Дата формирования:** {datetime.now().strftime("%Y-%m-%d %H:%M")}

### Статистика
- Всего активов: {len(st.session_state.assets)}
- Всего идентифицированных рисков: {len(st.session_state.risks)}
- Планов обработки: {len(st.session_state.treatment_plans)}

### Распределение рисков по уровням
"""
    
    if st.session_state.risks:
        levels = {"Низкий": 0, "Средний": 0, "Высокий": 0, "Критический": 0}
        for risk in st.session_state.risks:
            level, _ = get_risk_level(risk['probability'], risk['impact'])
            levels[level] += 1
        
        for level, count in levels.items():
            report += f"- {level}: {count}\n"
        
        # Статистика по обработке
        statuses = {"Запланировано": 0, "В процессе": 0, "Выполнено": 0}
        for plan in st.session_state.treatment_plans:
            status = plan.get('status', 'Запланировано')
            if status in statuses:
                statuses[status] += 1
        
        report += f"""
### Статус обработки рисков
- Запланировано: {statuses['Запланировано']}
- В процессе: {statuses['В процессе']}
- Выполнено: {statuses['Выполнено']}
"""
    
    st.markdown(report)