"""Карта требований приложения «Ключ» (рисунок 1 отчёта).

Запуск: python3 build_reqmap.py -> reqmap.html; PNG печатает render.js.
"""
from html import escape
from pathlib import Path

COLS = [
    ("Пользовательские требования", "#2E8B57", "#E7F4EC", [
        "ПТ-1. Единый план цифрового наследства",
        "ПТ-2. Доступ близким – только когда это нужно",
        "ПТ-3. Пошаговая инструкция для близких без установки приложения",
        "ПТ-4. Доверие к сервису и полное удаление данных",
    ]),
    ("Функциональные требования", "#2F6DB5", "#E9F0F9", [
        "ФТ-1. Знакомство и демо-план без регистрации, вход через Госуслуги",
        "ФТ-2. Инвентарь активов, шаблоны, документы и фото",
        "ФТ-3. Индекс готовности плана",
        "ФТ-4. Доверенные лица с ролями, приглашение по ссылке",
        "ФТ-5. Проверка «Всё в порядке?» и период ожидания",
        "ФТ-6. Проверка личности и родства наследника",
        "ФТ-7. Режим наследника в браузере",
        "ФТ-8. Шифрование на устройстве",
        "ФТ-9. Тарифы и оплата",
        "ФТ-10. Удаление аккаунта с выгрузкой плана",
    ]),
    ("Нефункциональные требования", "#7B4FB0", "#F1EBF7", [
        "НФТ-1. Безопасность: AES⁠-⁠256, TLS 1.3, серверы в России",
        "НФТ-2. Производительность: запуск ≤ 2 с, отклик ≤ 1 с",
        "НФТ-3. Надёжность: доступность ≥ 99,5 %, резервные копии",
        "НФТ-4. Удобство: первый план ≤ 10 минут, WCAG 2.1 AA",
    ]),
    ("Системные требования", "#C47A1A", "#FBF1E3", [
        "СТ-1. Android 8.0+ и веб-версия от 360 px",
        "СТ-2. Flutter, REST API, PostgreSQL в облаке в России",
        "СТ-3. Интеграции: Госуслуги (ЕСИА), ЮKassa, СБП, SMS, пуш, почта",
        "СТ-4. Смартфон: 2 ГБ ОЗУ, 150 МБ, камера",
    ]),
]

CSS = """
* { box-sizing: border-box; }
body { margin: 0; background: #fff; font-family: Arial, "Liberation Sans", sans-serif; color: #1f2a3c; }
.wrap { width: 1200px; padding: 26px 28px 28px; background: #F4F6FA; border-radius: 18px; }
h1 { margin: 0 0 18px; font-size: 30px; color: #1D3461; }
.cols { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; align-items: stretch; }
.col { border-radius: 14px; overflow: hidden; border: 1.5px solid; }
.bar { height: 10px; }
.t { font-weight: bold; font-size: 20px; line-height: 1.25; padding: 14px 16px 10px; color: #1D3461; }
ul { margin: 0; padding: 0 16px 16px 32px; font-size: 15.5px; line-height: 1.4; }
li { margin-bottom: 7px; }
"""


def build():
    cols = "".join(
        f'<div class="col" style="background:{bg};border-color:{acc}55"><div class="bar" style="background:{acc}"></div>'
        f'<div class="t">{escape(t)}</div><ul>{"".join(f"<li>{escape(x)}</li>" for x in items)}</ul></div>'
        for t, acc, bg, items in COLS)
    return (f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>Карта требований</title>'
            f'<style>{CSS}</style></head><body><div class="wrap" id="map"><h1>Сбор требований</h1>'
            f'<div class="cols">{cols}</div></div></body></html>')


if __name__ == "__main__":
    (Path(__file__).parent / "reqmap.html").write_text(build(), encoding="utf-8")
    print("ok")
