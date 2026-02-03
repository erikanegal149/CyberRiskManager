# pages/assets.py
"""Страница управления активами"""

import streamlit as st
import pandas as pd
from config import ASSET_CATEGORIES, ASSET_VALUES
from data_manager import save_data


def render():
    """Отрисовка страницы активов"""
    st.title("💼 Реестр информационных активов")
    st.markdown("---")
    
    # Форма добавления актива
    with st.expander("➕ Добавить новый актив", expanded=False):
        with st.form("add_asset"):
            col1, col2 = st.columns(2)
            with col1:
                asset_name = st.text_input("Название актива")
                asset_category = st.selectbox("Категория", ASSET_CATEGORIES)
            with col2:
                asset_owner = st.text_input("Владелец")
                asset_value = st.selectbox("Ценность", ASSET_VALUES)
            asset_description = st.text_area("Описание")
            
            if st.form_submit_button("Добавить актив"):
                if asset_name:
                    new_asset = {
                        "id": max([a['id'] for a in st.session_state.assets], default=0) + 1,
                        "name": asset_name,
                        "category": asset_category,
                        "owner": asset_owner,
                        "value": asset_value,
                        "description": asset_description
                    }
                    st.session_state.assets.append(new_asset)
                    save_data()
                    st.success(f"Актив '{asset_name}' добавлен!")
                    st.rerun()
                else:
                    st.error("Введите название актива")
    
    # Таблица активов
    if st.session_state.assets:
        st.subheader("Список активов")
        df_assets = pd.DataFrame(st.session_state.assets)
        st.dataframe(df_assets, use_container_width=True, hide_index=True)
        
        # Удаление актива
        asset_options = {f"{a['id']}. {a['name']}": a['id'] for a in st.session_state.assets}
        asset_to_delete = st.selectbox(
            "Выберите актив для удаления",
            options=list(asset_options.keys()),
            key="delete_asset"
        )
        if st.button("🗑️ Удалить выбранный актив"):
            asset_id = asset_options[asset_to_delete]
            st.session_state.assets = [a for a in st.session_state.assets if a['id'] != asset_id]
            save_data()
            st.success("Актив удалён!")
            st.rerun()
    else:
        st.info("Пока нет активов. Добавьте первый актив выше.")