# data_manager.py
"""Управление данными"""

import json
import os
import streamlit as st
from config import DATA_FILE


def save_data():
    """Сохранение данных в файл"""
    data = {
        "assets": st.session_state.assets,
        "threats": st.session_state.threats,
        "vulnerabilities": st.session_state.vulnerabilities,
        "risks": st.session_state.risks,
        "treatment_plans": st.session_state.treatment_plans
    }
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_data():
    """Загрузка данных из файла"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def get_initial_assets():
    """Начальные данные активов"""
    return [
        {"id": 1, "name": "Сервер базы данных", "category": "Аппаратное обеспечение", "owner": "ИТ-отдел", "value": "Критическая", "description": "Основной сервер с базами данных организации"},
        {"id": 2, "name": "CRM-система", "category": "Программное обеспечение", "owner": "Отдел продаж", "value": "Высокая", "description": "Система управления взаимоотношениями с клиентами"},
        {"id": 3, "name": "Персональные данные клиентов", "category": "Информация", "owner": "Юридический отдел", "value": "Критическая", "description": "База персональных данных клиентов"},
        {"id": 4, "name": "Корпоративная почта", "category": "Программное обеспечение", "owner": "ИТ-отдел", "value": "Высокая", "description": "Почтовый сервер организации"},
        {"id": 5, "name": "Локальная сеть", "category": "Сетевая инфраструктура", "owner": "ИТ-отдел", "value": "Высокая", "description": "Внутренняя сеть организации"},
        {"id": 6, "name": "Веб-сайт компании", "category": "Программное обеспечение", "owner": "Отдел маркетинга", "value": "Средняя", "description": "Публичный сайт организации"},
        {"id": 7, "name": "Бухгалтерская система", "category": "Программное обеспечение", "owner": "Бухгалтерия", "value": "Критическая", "description": "Система финансового учёта"},
        {"id": 8, "name": "Рабочие станции сотрудников", "category": "Аппаратное обеспечение", "owner": "ИТ-отдел", "value": "Средняя", "description": "Компьютеры сотрудников"},
        {"id": 9, "name": "ERP-система", "category": "Программное обеспечение", "owner": "Финансовый директор", "value": "Критическая", "description": "Система планирования ресурсов предприятия"},
        {"id": 10, "name": "Файловый сервер", "category": "Аппаратное обеспечение", "owner": "ИТ-отдел", "value": "Высокая", "description": "Хранилище корпоративных документов"},
        {"id": 11, "name": "VPN-шлюз", "category": "Сетевая инфраструктура", "owner": "ИТ-отдел", "value": "Высокая", "description": "Сервер удалённого доступа"},
        {"id": 12, "name": "Система видеонаблюдения", "category": "Физическая инфраструктура", "owner": "Служба безопасности", "value": "Средняя", "description": "Камеры и сервер видеонаблюдения"},
        {"id": 13, "name": "Мобильные устройства сотрудников", "category": "Аппаратное обеспечение", "owner": "ИТ-отдел", "value": "Средняя", "description": "Корпоративные смартфоны и планшеты"},
        {"id": 14, "name": "Система резервного копирования", "category": "Программное обеспечение", "owner": "ИТ-отдел", "value": "Критическая", "description": "Система бэкапов и восстановления"},
        {"id": 15, "name": "Интеллектуальная собственность", "category": "Информация", "owner": "Юридический отдел", "value": "Критическая", "description": "Патенты, торговые марки, ноу-хау"},
    ]


def get_initial_threats():
    """Начальные данные угроз"""
    return [
        {"id": 1, "name": "Вредоносное ПО (вирусы, черви)", "category": "Вредоносное ПО"},
        {"id": 2, "name": "Программы-вымогатели (ransomware)", "category": "Вредоносное ПО"},
        {"id": 3, "name": "Троянские программы", "category": "Вредоносное ПО"},
        {"id": 4, "name": "Шпионское ПО", "category": "Вредоносное ПО"},
        {"id": 5, "name": "Фишинг", "category": "Социальная инженерия"},
        {"id": 6, "name": "Целевой фишинг (spear phishing)", "category": "Социальная инженерия"},
        {"id": 7, "name": "Социальная инженерия", "category": "Социальная инженерия"},
        {"id": 8, "name": "DDoS-атаки", "category": "Сетевые атаки"},
        {"id": 9, "name": "Атаки Man-in-the-Middle", "category": "Сетевые атаки"},
        {"id": 10, "name": "SQL-инъекции", "category": "Сетевые атаки"},
        {"id": 11, "name": "Несанкционированный доступ", "category": "Несанкционированный доступ"},
        {"id": 12, "name": "Подбор паролей (brute force)", "category": "Несанкционированный доступ"},
        {"id": 13, "name": "Кража учётных данных", "category": "Несанкционированный доступ"},
        {"id": 14, "name": "Внутренние угрозы (инсайдеры)", "category": "Внутренние угрозы"},
        {"id": 15, "name": "Ошибки пользователей", "category": "Внутренние угрозы"},
    ]


def get_initial_vulnerabilities():
    """Начальные данные уязвимостей"""
    return [
        {"id": 1, "name": "Устаревшее программное обеспечение", "category": "Технические"},
        {"id": 2, "name": "Отсутствие обновлений безопасности", "category": "Технические"},
        {"id": 3, "name": "Слабые пароли", "category": "Технические"},
        {"id": 4, "name": "Отсутствие многофакторной аутентификации", "category": "Технические"},
        {"id": 5, "name": "Неправильная конфигурация систем", "category": "Технические"},
        {"id": 6, "name": "Отсутствие шифрования данных", "category": "Технические"},
        {"id": 7, "name": "Открытые сетевые порты", "category": "Технические"},
        {"id": 8, "name": "Отсутствие политик безопасности", "category": "Организационные"},
        {"id": 9, "name": "Недостаточная осведомлённость персонала", "category": "Организационные"},
        {"id": 10, "name": "Отсутствие процедур резервного копирования", "category": "Организационные"},
        {"id": 11, "name": "Нечёткое распределение ролей", "category": "Организационные"},
        {"id": 12, "name": "Недостаточный контроль доступа", "category": "Физические"},
        {"id": 13, "name": "Отсутствие видеонаблюдения", "category": "Физические"},
    ]


def get_initial_risks():
    """Начальные данные рисков"""
    return [
        {"id": 1, "name": "Шифрование БД вымогателем", "asset": "Сервер базы данных", "threat": "Программы-вымогатели (ransomware)", "vulnerability": "Устаревшее программное обеспечение", "probability": 4, "impact": 5, "score": 20, "date": "2025-01-15"},
        {"id": 2, "name": "Утечка персональных данных через фишинг", "asset": "Персональные данные клиентов", "threat": "Фишинг", "vulnerability": "Недостаточная осведомлённость персонала", "probability": 4, "impact": 5, "score": 20, "date": "2025-01-18"},
        {"id": 3, "name": "Взлом корпоративной почты", "asset": "Корпоративная почта", "threat": "Подбор паролей (brute force)", "vulnerability": "Слабые пароли", "probability": 4, "impact": 3, "score": 12, "date": "2025-01-20"},
        {"id": 4, "name": "DDoS-атака на сеть", "asset": "Локальная сеть", "threat": "DDoS-атаки", "vulnerability": "Открытые сетевые порты", "probability": 3, "impact": 4, "score": 12, "date": "2025-01-22"},
        {"id": 5, "name": "Несанкционированный доступ к CRM", "asset": "CRM-система", "threat": "Кража учётных данных", "vulnerability": "Отсутствие многофакторной аутентификации", "probability": 3, "impact": 4, "score": 12, "date": "2025-01-25"},
        {"id": 6, "name": "Вирусное заражение рабочих станций", "asset": "Рабочие станции сотрудников", "threat": "Вредоносное ПО (вирусы, черви)", "vulnerability": "Отсутствие обновлений безопасности", "probability": 4, "impact": 2, "score": 8, "date": "2025-01-26"},
        {"id": 7, "name": "Дефейс веб-сайта", "asset": "Веб-сайт компании", "threat": "SQL-инъекции", "vulnerability": "Неправильная конфигурация систем", "probability": 2, "impact": 3, "score": 6, "date": "2025-01-27"},
        {"id": 8, "name": "Мошенничество в бухгалтерии", "asset": "Бухгалтерская система", "threat": "Внутренние угрозы (инсайдеры)", "vulnerability": "Недостаточный контроль доступа", "probability": 2, "impact": 5, "score": 10, "date": "2025-01-28"},
        {"id": 9, "name": "Перехват данных в сети", "asset": "Локальная сеть", "threat": "Атаки Man-in-the-Middle", "vulnerability": "Отсутствие шифрования данных", "probability": 2, "impact": 4, "score": 8, "date": "2025-01-29"},
        {"id": 10, "name": "Социальная атака на сотрудников", "asset": "Персональные данные клиентов", "threat": "Социальная инженерия", "vulnerability": "Недостаточная осведомлённость персонала", "probability": 4, "impact": 4, "score": 16, "date": "2025-01-30"},
        {"id": 11, "name": "Компрометация ERP-системы", "asset": "ERP-система", "threat": "Несанкционированный доступ", "vulnerability": "Слабые пароли", "probability": 3, "impact": 5, "score": 15, "date": "2025-02-01"},
        {"id": 12, "name": "Утечка документов с файлового сервера", "asset": "Файловый сервер", "threat": "Внутренние угрозы (инсайдеры)", "vulnerability": "Недостаточный контроль доступа", "probability": 3, "impact": 4, "score": 12, "date": "2025-02-02"},
        {"id": 13, "name": "Взлом VPN-шлюза", "asset": "VPN-шлюз", "threat": "Кража учётных данных", "vulnerability": "Отсутствие многофакторной аутентификации", "probability": 3, "impact": 5, "score": 15, "date": "2025-02-03"},
        {"id": 14, "name": "Отключение видеонаблюдения", "asset": "Система видеонаблюдения", "threat": "Несанкционированный доступ", "vulnerability": "Неправильная конфигурация систем", "probability": 2, "impact": 3, "score": 6, "date": "2025-02-04"},
        {"id": 15, "name": "Потеря мобильного устройства", "asset": "Мобильные устройства сотрудников", "threat": "Кража учётных данных", "vulnerability": "Отсутствие шифрования данных", "probability": 4, "impact": 3, "score": 12, "date": "2025-02-05"},
        {"id": 16, "name": "Сбой системы резервного копирования", "asset": "Система резервного копирования", "threat": "Ошибки пользователей", "vulnerability": "Отсутствие процедур резервного копирования", "probability": 2, "impact": 5, "score": 10, "date": "2025-02-06"},
        {"id": 17, "name": "Кража интеллектуальной собственности", "asset": "Интеллектуальная собственность", "threat": "Внутренние угрозы (инсайдеры)", "vulnerability": "Недостаточный контроль доступа", "probability": 2, "impact": 5, "score": 10, "date": "2025-02-07"},
        {"id": 18, "name": "Целевая атака на руководство", "asset": "Корпоративная почта", "threat": "Целевой фишинг (spear phishing)", "vulnerability": "Недостаточная осведомлённость персонала", "probability": 3, "impact": 5, "score": 15, "date": "2025-02-08"},
        {"id": 19, "name": "Заражение через USB-носители", "asset": "Рабочие станции сотрудников", "threat": "Троянские программы", "vulnerability": "Отсутствие политик безопасности", "probability": 3, "impact": 3, "score": 9, "date": "2025-02-09"},
        {"id": 20, "name": "Шпионское ПО на мобильных устройствах", "asset": "Мобильные устройства сотрудников", "threat": "Шпионское ПО", "vulnerability": "Отсутствие обновлений безопасности", "probability": 3, "impact": 4, "score": 12, "date": "2025-02-10"},
        {"id": 21, "name": "Случайное удаление файлов", "asset": "Файловый сервер", "threat": "Ошибки пользователей", "vulnerability": "Нечёткое распределение ролей", "probability": 2, "impact": 2, "score": 4, "date": "2025-02-11"},
        {"id": 22, "name": "Сбой принтера", "asset": "Рабочие станции сотрудников", "threat": "Ошибки пользователей", "vulnerability": "Неправильная конфигурация систем", "probability": 2, "impact": 1, "score": 2, "date": "2025-02-12"},
        {"id": 23, "name": "Временная недоступность сайта", "asset": "Веб-сайт компании", "threat": "DDoS-атаки", "vulnerability": "Открытые сетевые порты", "probability": 1, "impact": 2, "score": 2, "date": "2025-02-13"},
        {"id": 24, "name": "Несвоевременное обновление антивируса", "asset": "Рабочие станции сотрудников", "threat": "Вредоносное ПО (вирусы, черви)", "vulnerability": "Отсутствие обновлений безопасности", "probability": 1, "impact": 3, "score": 3, "date": "2025-02-14"},
    ]


def get_initial_treatment_plans():
    """Начальные данные планов обработки"""
    return [
        {"id": 1, "risk": "Шифрование БД вымогателем", "option": "Снижение", "measures": "Обновление ПО, внедрение резервного копирования, установка антивируса", "responsible": "Системный администратор", "deadline": "2025-03-01", "status": "В процессе"},
        {"id": 2, "risk": "Утечка персональных данных через фишинг", "option": "Снижение", "measures": "Проведение тренингов по кибербезопасности, внедрение DLP-системы", "responsible": "Отдел ИБ", "deadline": "2025-03-15", "status": "Запланировано"},
        {"id": 3, "risk": "Взлом корпоративной почты", "option": "Снижение", "measures": "Внедрение политики сложных паролей, включение MFA", "responsible": "ИТ-отдел", "deadline": "2025-02-15", "status": "Выполнено"},
        {"id": 4, "risk": "DDoS-атака на сеть", "option": "Передача", "measures": "Подключение услуги защиты от DDoS у провайдера", "responsible": "ИТ-директор", "deadline": "2025-02-28", "status": "В процессе"},
        {"id": 5, "risk": "Несанкционированный доступ к CRM", "option": "Снижение", "measures": "Внедрение многофакторной аутентификации", "responsible": "ИТ-отдел", "deadline": "2025-02-20", "status": "Выполнено"},
        {"id": 6, "risk": "Вирусное заражение рабочих станций", "option": "Снижение", "measures": "Установка корпоративного антивируса, автоматические обновления", "responsible": "ИТ-отдел", "deadline": "2025-02-10", "status": "Выполнено"},
        {"id": 7, "risk": "Компрометация ERP-системы", "option": "Снижение", "measures": "Аудит доступа, внедрение ролевой модели, MFA", "responsible": "ИТ-директор", "deadline": "2025-03-20", "status": "Запланировано"},
        {"id": 8, "risk": "Взлом VPN-шлюза", "option": "Снижение", "measures": "Внедрение сертификатов, MFA, мониторинг подключений", "responsible": "Сетевой администратор", "deadline": "2025-03-10", "status": "В процессе"},
        {"id": 9, "risk": "Социальная атака на сотрудников", "option": "Снижение", "measures": "Регулярные тренинги, тестовые фишинговые рассылки", "responsible": "Отдел ИБ", "deadline": "2025-04-01", "status": "Запланировано"},
        {"id": 10, "risk": "Потеря мобильного устройства", "option": "Снижение", "measures": "MDM-система, шифрование, удалённое стирание", "responsible": "ИТ-отдел", "deadline": "2025-03-25", "status": "В процессе"},
        {"id": 11, "risk": "Целевая атака на руководство", "option": "Снижение", "measures": "Персональный тренинг для топ-менеджмента, усиленная защита почты", "responsible": "Отдел ИБ", "deadline": "2025-03-05", "status": "Запланировано"},
        {"id": 12, "risk": "Кража интеллектуальной собственности", "option": "Снижение", "measures": "DLP-система, классификация данных, ограничение USB", "responsible": "Отдел ИБ", "deadline": "2025-04-15", "status": "Запланировано"},
    ]

def init_session_state():
    """Инициализация данных в session_state"""
    if 'data_loaded' not in st.session_state:
        st.session_state.data_loaded = True
        saved_data = load_data()
        
        if saved_data:
            st.session_state.assets = saved_data.get("assets", [])
            st.session_state.threats = saved_data.get("threats", [])
            st.session_state.vulnerabilities = saved_data.get("vulnerabilities", [])
            st.session_state.risks = saved_data.get("risks", [])
            st.session_state.treatment_plans = saved_data.get("treatment_plans", [])
        else:
            st.session_state.assets = get_initial_assets()
            st.session_state.threats = get_initial_threats()
            st.session_state.vulnerabilities = get_initial_vulnerabilities()
            st.session_state.risks = get_initial_risks()
            st.session_state.treatment_plans = get_initial_treatment_plans()
            save_data()