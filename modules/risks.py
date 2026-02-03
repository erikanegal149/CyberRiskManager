# modules/risks.py
"""Страница оценки рисков"""

import streamlit as st
import pandas as pd
from datetime import datetime
from utils import get_risk_level
from data_manager import save_data


def render():
    """Отрисовка страницы оценки рисков"""
    st.title("📋 Оценка киберрисков")
    st.markdown("---")
    
    if not st.session_state.assets:
        st.warning("Сначала добавьте активы в разделе 'Активы'")
        return
    
    # Tabs для разделения функционала
    tab1, tab2, tab3 = st.tabs(["➕ Добавить риск", "✏️ Редактировать риск", "🗑️ Удалить риск"])
    
    with tab1:
        with st.form("add_risk"):
            col1, col2 = st.columns(2)
            
            with col1:
                risk_name = st.text_input("Название риска")
                selected_asset = st.selectbox(
                    "Актив",
                    options=[a['name'] for a in st.session_state.assets],
                    key="add_asset"
                )
                selected_threat = st.selectbox(
                    "Угроза",
                    options=[t['name'] for t in st.session_state.threats],
                    key="add_threat"
                )
                selected_vuln = st.selectbox(
                    "Уязвимость",
                    options=[v['name'] for v in st.session_state.vulnerabilities],
                    key="add_vuln"
                )
            
            with col2:
                st.markdown("**Шкала вероятности:**")
                st.caption("1 - Очень низкая, 2 - Низкая, 3 - Средняя, 4 - Высокая, 5 - Очень высокая")
                probability = st.slider("Вероятность", 1, 5, 3, key="add_prob")
                
                st.markdown("**Шкала воздействия:**")
                st.caption("1 - Незначительное, 2 - Низкое, 3 - Среднее, 4 - Высокое, 5 - Критическое")
                impact = st.slider("Воздействие", 1, 5, 3, key="add_impact")
                
                level, icon = get_risk_level(probability, impact)
                score = probability * impact
                st.markdown(f"**Уровень риска:** {icon} {level} (оценка: {score})")
            
            if st.form_submit_button("Добавить риск"):
                if risk_name:
                    new_risk = {
                        "id": max([r['id'] for r in st.session_state.risks], default=0) + 1,
                        "name": risk_name,
                        "asset": selected_asset,
                        "threat": selected_threat,
                        "vulnerability": selected_vuln,
                        "probability": probability,
                        "impact": impact,
                        "score": probability * impact,
                        "date": datetime.now().strftime("%Y-%m-%d")
                    }
                    st.session_state.risks.append(new_risk)
                    save_data()
                    st.success(f"Риск '{risk_name}' добавлен!")
                    st.rerun()
                else:
                    st.error("Введите название риска")
    
    with tab2:
        if st.session_state.risks:
            # Выбор риска для редактирования
            risk_options = {f"{r['id']}. {r['name']}": r['id'] for r in st.session_state.risks}
            selected_risk_name = st.selectbox(
                "Выберите риск для редактирования",
                options=list(risk_options.keys()),
                key="edit_select"
            )
            
            selected_risk_id = risk_options[selected_risk_name]
            selected_risk = next(r for r in st.session_state.risks if r['id'] == selected_risk_id)
            
            with st.form("edit_risk"):
                col1, col2 = st.columns(2)
                
                with col1:
                    edit_name = st.text_input("Название риска", value=selected_risk['name'])
                    
                    asset_names = [a['name'] for a in st.session_state.assets]
                    asset_index = asset_names.index(selected_risk['asset']) if selected_risk['asset'] in asset_names else 0
                    edit_asset = st.selectbox("Актив", options=asset_names, index=asset_index, key="edit_asset")
                    
                    threat_names = [t['name'] for t in st.session_state.threats]
                    threat_index = threat_names.index(selected_risk['threat']) if selected_risk['threat'] in threat_names else 0
                    edit_threat = st.selectbox("Угроза", options=threat_names, index=threat_index, key="edit_threat")
                    
                    vuln_names = [v['name'] for v in st.session_state.vulnerabilities]
                    vuln_index = vuln_names.index(selected_risk['vulnerability']) if selected_risk['vulnerability'] in vuln_names else 0
                    edit_vuln = st.selectbox("Уязвимость", options=vuln_names, index=vuln_index, key="edit_vuln")
                
                with col2:
                    st.markdown("**Шкала вероятности:**")
                    st.caption("1 - Очень низкая, 2 - Низкая, 3 - Средняя, 4 - Высокая, 5 - Очень высокая")
                    edit_probability = st.slider("Вероятность", 1, 5, selected_risk['probability'], key="edit_prob")
                    
                    st.markdown("**Шкала воздействия:**")
                    st.caption("1 - Незначительное, 2 - Низкое, 3 - Среднее, 4 - Высокое, 5 - Критическое")
                    edit_impact = st.slider("Воздействие", 1, 5, selected_risk['impact'], key="edit_impact")
                    
                    level, icon = get_risk_level(edit_probability, edit_impact)
                    score = edit_probability * edit_impact
                    st.markdown(f"**Уровень риска:** {icon} {level} (оценка: {score})")
                
                if st.form_submit_button("💾 Сохранить изменения"):
                    for risk in st.session_state.risks:
                        if risk['id'] == selected_risk_id:
                            risk['name'] = edit_name
                            risk['asset'] = edit_asset
                            risk['threat'] = edit_threat
                            risk['vulnerability'] = edit_vuln
                            risk['probability'] = edit_probability
                            risk['impact'] = edit_impact
                            risk['score'] = edit_probability * edit_impact
                            break
                    save_data()
                    st.success("Риск обновлён!")
                    st.rerun()
        else:
            st.info("Нет рисков для редактирования")
    
    with tab3:
        if st.session_state.risks:
            risk_options = {f"{r['id']}. {r['name']} (оценка: {r['score']})": r['id'] for r in st.session_state.risks}
            selected_risk_name = st.selectbox(
                "Выберите риск для удаления",
                options=list(risk_options.keys()),
                key="delete_select"
            )
            
            selected_risk_id = risk_options[selected_risk_name]
            selected_risk = next(r for r in st.session_state.risks if r['id'] == selected_risk_id)
            
            # Показываем информацию о риске
            st.warning("⚠️ Вы собираетесь удалить следующий риск:")
            
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Название:** {selected_risk['name']}")
                st.write(f"**Актив:** {selected_risk['asset']}")
                st.write(f"**Угроза:** {selected_risk['threat']}")
            with col2:
                st.write(f"**Вероятность:** {selected_risk['probability']}")
                st.write(f"**Воздействие:** {selected_risk['impact']}")
                level, icon = get_risk_level(selected_risk['probability'], selected_risk['impact'])
                st.write(f"**Уровень:** {icon} {level}")
            
            st.markdown("---")
            
            # Подтверждение удаления
            st.error("🚨 **Внимание!** Это действие необратимо. Восстановить удалённый риск будет невозможно.")
            
            confirm = st.checkbox("Я подтверждаю, что хочу удалить этот риск", key="confirm_delete")
            
            if st.button("🗑️ Удалить риск", type="primary", disabled=not confirm):
                st.session_state.risks = [r for r in st.session_state.risks if r['id'] != selected_risk_id]
                # Также удаляем связанные планы обработки
                st.session_state.treatment_plans = [
                    p for p in st.session_state.treatment_plans if p['risk'] != selected_risk['name']
                ]
                save_data()
                st.success("Риск удалён!")
                st.rerun()
        else:
            st.info("Нет рисков для удаления")
    
    st.markdown("---")
    
    # Таблица рисков
    if st.session_state.risks:
        st.subheader("📋 Реестр рисков")
        
        # Фильтры
        col1, col2, col3 = st.columns(3)
        
        with col1:
            filter_level = st.selectbox(
                "Фильтр по уровню",
                ["Все", "Критический", "Высокий", "Средний", "Низкий"],
                key="filter_level"
            )
        
        with col2:
            assets_list = ["Все"] + list(set(r['asset'] for r in st.session_state.risks))
            filter_asset = st.selectbox("Фильтр по активу", assets_list, key="filter_asset")
        
        with col3:
            sort_option = st.selectbox(
                "Сортировка",
                ["По оценке (убыв.)", "По оценке (возр.)", "По дате (новые)", "По дате (старые)"],
                key="sort_option"
            )
        
        # Применяем фильтры
        filtered_risks = st.session_state.risks.copy()
        
        if filter_level != "Все":
            filtered_risks = [
                r for r in filtered_risks 
                if get_risk_level(r['probability'], r['impact'])[0] == filter_level
            ]
        
        if filter_asset != "Все":
            filtered_risks = [r for r in filtered_risks if r['asset'] == filter_asset]
        
        # Сортировка
        if sort_option == "По оценке (убыв.)":
            filtered_risks.sort(key=lambda x: x['score'], reverse=True)
        elif sort_option == "По оценке (возр.)":
            filtered_risks.sort(key=lambda x: x['score'])
        elif sort_option == "По дате (новые)":
            filtered_risks.sort(key=lambda x: x['date'], reverse=True)
        elif sort_option == "По дате (старые)":
            filtered_risks.sort(key=lambda x: x['date'])
        
        # Отображение
        risks_display = []
        for risk in filtered_risks:
            level, icon = get_risk_level(risk['probability'], risk['impact'])
            risks_display.append({
                "ID": risk['id'],
                "Название": risk['name'],
                "Актив": risk['asset'],
                "Угроза": risk['threat'],
                "Вероятность": risk['probability'],
                "Воздействие": risk['impact'],
                "Оценка": risk['score'],
                "Уровень": f"{icon} {level}",
                "Дата": risk['date']
            })
        
        df_risks = pd.DataFrame(risks_display)
        st.dataframe(df_risks, use_container_width=True, hide_index=True)
        
        st.caption(f"Показано рисков: {len(filtered_risks)} из {len(st.session_state.risks)}")