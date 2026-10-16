"""Сборка User Journey Map персоны «Андрей Соколов» (А1) в двух вариантах:
заполненная карта (приложение А) и шаблон для заполнения.

Запуск: python3 build_map.py  ->  map_filled.html, map_template.html
PDF печатается из HTML через Chromium (см. render.js).
"""
from html import escape
from pathlib import Path

OUT = Path(__file__).parent

# ---------------------------------------------------------------- данные
STAGES = [
    ("Осознание проблемы", [1]),
    ("Поиск информации", [2]),
    ("Оценка вариантов", [3, 4, 5]),
    ("Принятие решения", [6]),
    ("Покупка / использование", [7, 8, 9]),
    ("Послепродажный опыт / удаление", [10]),
]

STEPS = [
    dict(
        title="Осознание проблемы",
        time="1–2 дня",
        actions=[
            "Узнаёт, что семья коллеги месяц не могла платить ипотеку",
            "Спрашивает жену, знает ли она пароли от банка и Госуслуг",
            "Пробует записать пароли в заметки телефона",
        ],
        quote="А жена вообще сможет зайти в банк без меня?",
        mood="sad", emo="Тревога, растерянность", mot="Растёт",
        touch=["Коллега", "Жена", "Новости, Дзен", "Заметки в телефоне"],
        pains=[
            "Непонятно, с чего начать",
            "Тема пугает, решение хочется отложить",
            "Пароли в заметках небезопасны",
        ],
        opps=[
            ("P1", "Предложение «Ключа» в онлайн-банке при оформлении страховки"),
            ("P2", "Тест в Дзене «Сможет ли семья обойтись без вас?»"),
        ],
    ),
    dict(
        title="Выбор приложения",
        time="1 вечер, 20–30 минут",
        actions=[
            "Ищет «как передать пароли семье»",
            "Сравнивает «Ключ» с GoodTrust и функциями Google",
            "Читает отзывы и устанавливает приложение",
        ],
        quote="Неужели для этого уже есть приложение?",
        mood="neutral", emo="Тревога, любопытство", mot="Средняя",
        touch=["Поиск Яндекса, Дзен", "Магазин приложений, отзывы", "Смартфон на Android"],
        pains=[
            "Мало материалов на русском языке",
            "Зарубежные сервисы не знают российских банков",
            "Непонятно, кто разработчик",
        ],
        opps=[
            ("P1", "Страница в магазине: «план на всякий случай» и схема защиты на первом экране"),
            ("P2", "Статьи по запросам о наследстве и доступах"),
        ],
    ),
    dict(
        title="Просмотр функций",
        time="5–10 минут",
        moment="Можно ли доверить данные?",
        actions=["Листает экраны знакомства", "Открывает демо-план", "Читает, как работает шифрование"],
        quote="А если их взломают? Кто увидит мои пароли?",
        mood="sad", emo="Сомнение, недоверие", mot="Падает",
        touch=["Экраны знакомства", "Демо-план", "Экран «Как мы защищаем данные»", "Запрос разрешений"],
        pains=[
            "Главный барьер – недоверие к хранению данных",
            "Запрос разрешений сразу при первом входе",
            "Мрачная тема отпугивает",
        ],
        opps=[
            ("P1", "Знакомство и демо-план без регистрации"),
            ("P1", "Простая схема: «даже мы не видим ваши данные»"),
            ("P1", "Разрешение на уведомления – позже, при настройке проверки"),
        ],
    ),
    dict(
        title="Загрузка данных и фото",
        time="Первые 10–15 минут",
        actions=[
            "Добавляет Сбербанк, Госуслуги и облако из шаблонов",
            "Загружает фото документов и семейные фото",
            "Видит «План готов на 20 %»",
        ],
        quote="Шаблоны удобные, но 37 аккаунтов вручную я не внесу",
        mood="neutral", emo="Интерес, лёгкая усталость", mot="Растёт",
        touch=["Шаблоны сервисов", "Камера и галерея", "Индекс готовности"],
        pains=[
            "Долго вносить аккаунты вручную",
            "Страшно загружать фото паспорта",
            "Непонятно, где хранятся загруженные файлы",
        ],
        opps=[
            ("P1", "Шаблоны российских сервисов"),
            ("P1", "Режим «только инструкции, без паролей»"),
            ("P2", "Автопоиск аккаунтов по почте"),
        ],
    ),
    dict(
        title="Настройка инструкций",
        time="1–2 недели по 10–15 минут",
        actions=[
            "Для каждого аккаунта выбирает действие",
            "Пишет инструкцию для банка по шаблону",
            "Записывает видеопослание детям",
        ],
        quote="Не знал, что писать для банка. Хорошо, что есть пример",
        mood="happy", emo="Удовлетворение, иногда грусть", mot="Высокая",
        touch=["Карточка аккаунта", "Шаблоны инструкций", "Камера для послания", "Жена"],
        pains=[
            "Не знает, какие документы нужны банку",
            "Тяжело записывать послания",
            "План пока только на телефоне – страшно его потерять",
        ],
        opps=[
            ("P1", "Шаблоны инструкций для российских банков"),
            ("P1", "Одно действие сразу для группы аккаунтов"),
            ("P2", "Подсказки, с чего начать послание"),
        ],
    ),
    dict(
        title="Регистрация",
        time="2–3 минуты",
        actions=[
            "Нажимает «Пригласить близких»",
            "Входит через Госуслуги",
            "Создаёт мастер-пароль",
            "Выбирает сценарии: болезнь, потеря доступа, смерть",
        ],
        quote="Хорошо, что через Госуслуги, а не ещё один пароль. Но мастер-пароль страшно забыть",
        mood="happy", emo="Решимость, лёгкое волнение", mot="Высокая",
        touch=["Экран регистрации", "Госуслуги", "Экран мастер-пароля"],
        pains=[
            "Страх потерять мастер-пароль",
            "Длинная регистрация отпугнула бы",
            "Страница Госуслуг иногда долго грузится",
        ],
        opps=[
            ("P1", "Регистрация только при приглашении близких, вход через Госуслуги"),
            ("P2", "Восстановление мастер-пароля через доверенных лиц"),
        ],
    ),
    dict(
        title="Назначение доверенных лиц",
        time="1 вечер",
        actions=[
            "Приглашает жену и брата по ссылке",
            "Назначает роли: исполнитель и наследник",
            "Выбирает, кто к каким аккаунтам получит доступ",
        ],
        quote="Жена спросила, зачем ей ещё одно приложение. Хорошо, что можно по ссылке",
        mood="happy", emo="Спокойствие, неловкость при разговоре с семьёй", mot="Высокая",
        touch=["Приглашение по ссылке", "Жена и брат", "Экран ролей"],
        pains=[
            "Неловко обсуждать тему с семьёй",
            "Близким неудобно ставить ещё одно приложение",
            "Непонятна разница между ролями",
        ],
        opps=[
            ("P1", "Приглашение по ссылке без установки"),
            ("P1", "Понятное описание ролей с примерами"),
            ("P2", "Готовый текст приглашения для близких"),
        ],
    ),
    dict(
        title="Настройка проверки «Всё в порядке?»",
        time="5 минут, затем 1 минута в месяц",
        moment="Сработает ли проверка правильно?",
        actions=[
            "Выбирает проверку раз в месяц",
            "Подтверждает «Всё в порядке?» по пушу",
            "Пропускает проверку в командировке и получает звонок",
        ],
        quote="Когда позвонили, испугался: жена уже получила уведомление?",
        mood="happy", emo="Спокойствие; испуг при пропущенной проверке", mot="Средняя",
        touch=["Пуш, SMS, звонок, почта", "Экран периода ожидания", "Доверенные лица"],
        pains=[
            "Страх ложного срабатывания",
            "Частые проверки раздражают",
            "Непонятно, что и когда увидят близкие",
        ],
        opps=[
            ("P1", "Период ожидания 7–30 дней с отменой"),
            ("P1", "Журнал: кто и когда что видел"),
            ("P2", "Гибкая частота и «режим отпуска»"),
        ],
    ),
    dict(
        title="Выбор тарифа подписки",
        time="Через 2–3 недели, 2 минуты",
        moment="Стоит ли платить?",
        actions=[
            "Видит предложение «Ключ Плюс»",
            "Сравнивает личный и семейный тариф, оплату за месяц и за год",
            "Оплачивает год через СБП",
        ],
        quote="99 рублей – меньше, чем кино, а тут спокойствие за семью",
        mood="neutral", emo="Готовность платить, раздражение от лимита", mot="Высокая",
        touch=["Экран тарифов", "Магазин приложений", "ЮKassa, СБП", "Онлайн-банк"],
        pains=["Лимит появляется неожиданно", "Неясно, что будет с планом, если перестать платить"],
        opps=[
            ("P1", "Показывать лимит заранее в индексе готовности"),
            ("P1", "План сохраняется для чтения при отмене подписки"),
            ("P2", "Пробный месяц подписки"),
        ],
    ),
    dict(
        title="Удаление приложения или отказ от сервиса",
        time="1 день",
        actions=["Отменяет подписку", "Ищет, как удалить аккаунт", "Скачивает план в PDF", "Предупреждает жену и брата"],
        quote="Точно ли всё удалится? Не останется ли копия моих паролей?",
        mood="sad", emo="Сомнение, настороженность", mot="Низкая",
        touch=["Настройки приложения", "Магазин приложений", "Письмо с подтверждением", "Доверенные лица"],
        pains=[
            "Удаление приложения не удаляет аккаунт",
            "Неясно, удалены ли данные с сервера",
            "Близкие не знают, что плана больше нет",
        ],
        opps=[
            ("P1", "Удаление аккаунта в 2 шага с выгрузкой плана"),
            ("P1", "Подтверждение удаления данных за 30 дней"),
            ("P1", "Уведомление доверенных лиц"),
            ("P2", "Вопрос о причине ухода"),
        ],
    ),
]

INFO = [
    ("Этапы пути", "осознание проблемы → поиск информации → оценка вариантов → принятие решения → "
                   "покупка/использование → послепродажный опыт/удаление"),
    ("Сценарий", "Составление плана цифрового наследства в приложении «Ключ»: от осознания проблемы "
                 "до оплаты подписки и удаления приложения"),
    ("Временные рамки", "Около месяца от осознания проблемы до оплаты подписки, затем регулярное "
                        "использование в течение года"),
    ("Точки входа", "История коллеги, поиск в магазине приложений, статья в Дзене, предложение банка, "
                    "совет знакомых"),
    ("Точки выхода", "План готов и подписка оформлена; отказ при просмотре функций из-за недоверия; "
                     "удаление приложения или отказ от сервиса"),
]

CONCLUSION = (
    "Путь разбит на шесть этапов методики и десять шагов – от осознания проблемы до удаления приложения. "
    "Самые проблемные шаги – просмотр функций, где пользователь не доверяет хранению данных, загрузка данных "
    "и настройка инструкций, где много ручной работы, и удаление приложения, где непонятно, стёрты ли данные. "
    "Моменты истины – решение доверить данные, первая пропущенная проверка и выбор тарифа подписки. "
    "В первую очередь нужны знакомство без регистрации с понятной схемой защиты, шаблоны сервисов и инструкций, "
    "период ожидания с журналом действий и прозрачное удаление аккаунта с выгрузкой плана."
)

# ---------------------------------------------------------------- иконки
def svg(body, color="currentColor", size=22, fill="none", sw=2):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="{fill}" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{body}</svg>')

ICON = {
    "pin": '<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.6"/>',
    "cursor": '<path d="M5 5l5.5 14 2-5.8 5.8-2z"/><path d="M13 13l5 5"/><path d="M3 9.5l-1.5-.8M6.5 3l-.6-1.6M3.5 5.5L2 4.5"/>',
    "cloud": '<path d="M7 17a4 4 0 0 1-.6-7.95A5.5 5.5 0 0 1 17 8.5a4.25 4.25 0 0 1 .5 8.5z"/><circle cx="6" cy="20.5" r="1"/>',
    "phone": '<rect x="5" y="2.5" width="10" height="19" rx="2"/><path d="M9 18.5h2"/><path d="M18 9c1 1 1 5 0 6M20.5 7c2 2.5 2 7.5 0 10"/>',
    "warn": '<path d="M12 3.5L2.5 20h19z"/><path d="M12 10v4.5"/><circle cx="12" cy="17.3" r=".4"/>',
    "bulb": '<path d="M9 17.5h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.3 1 2.1v1.5h5V16c0-.8.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/>',
    "flag": '<path d="M5 21V4"/><path d="M5 4h11l-2 4 2 4H5"/>',
}

MOOD = {
    "happy": ("#8BC46A", '<path d="M8.5 14.2c1.9 2 5.1 2 7 0" fill="none"/>'),
    "neutral": ("#F2C94C", '<path d="M8.7 15h6.6" fill="none"/>'),
    "sad": ("#F2994A", '<path d="M8.5 16.3c1.9-2 5.1-2 7 0" fill="none"/>'),
}

def mood_icon(m):
    color, mouth = MOOD[m]
    return (f'<svg class="mood" width="34" height="34" viewBox="0 0 24 24">'
            f'<circle cx="12" cy="12" r="11" fill="{color}" stroke="#fff" stroke-width="1.2"/>'
            f'<circle cx="8.8" cy="9.8" r="1.25" fill="#3b3b3b"/><circle cx="15.2" cy="9.8" r="1.25" fill="#3b3b3b"/>'
            f'<g stroke="#3b3b3b" stroke-width="1.5" stroke-linecap="round">{mouth}</g></svg>')

AVATAR = """<svg width="170" height="170" viewBox="0 0 170 170">
<circle cx="85" cy="85" r="85" fill="#DCE6F3"/>
<clipPath id="av"><circle cx="85" cy="85" r="85"/></clipPath>
<g clip-path="url(#av)">
<path d="M28 175c4-34 27-50 57-50s53 16 57 50z" fill="#2F6DB5"/>
<path d="M74 112h22v18c0 6-22 6-22 0z" fill="#EDBE93"/>
<ellipse cx="85" cy="82" rx="32" ry="36" fill="#F4CDA5"/>
<path d="M53 80c-3-26 12-42 32-42s36 13 33 42c-4-12-10-18-14-20-12 4-30 5-45 2-3 4-5 10-6 18z" fill="#5A3A26"/>
<circle cx="74" cy="86" r="3.6" fill="#2b2b2b"/><circle cx="96" cy="86" r="3.6" fill="#2b2b2b"/>
<path d="M75 101c6 5 14 5 20 0" stroke="#C0563B" stroke-width="3" fill="none" stroke-linecap="round"/>
<circle cx="66" cy="96" r="5" fill="#F2A98C" opacity=".45"/><circle cx="104" cy="96" r="5" fill="#F2A98C" opacity=".45"/>
</g></svg>"""

CATS = [
    # ключ, название, иконка, акцент, фон
    ("actions", "Действия пользователя", "cursor", "#2F6DB5", "#E9F0F9"),
    ("thoughts", "Мысли и эмоции", "cloud", "#7B4FB0", "#F1EBF7"),
    ("touch", "Точки контакта", "phone", "#1E8A82", "#E4F3F1"),
    ("pains", "Боли и проблемы", "warn", "#C8404A", "#FBEAEA"),
    ("opps", "Возможности для улучшения", "bulb", "#2E8B57", "#E7F4EC"),
]

# ---------------------------------------------------------------- вёрстка
CSS = """
@page { size: 841mm 594mm; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; background: #fff; }
body { font-family: Arial, "Liberation Sans", Helvetica, sans-serif; color: #1f2a3c; }
.page { width: 841mm; height: 594mm; padding: 30px 74px 0; position: relative; overflow: hidden; }
.pnum { position: absolute; top: 38px; right: 78px; font: 20px "Times New Roman", "Liberation Serif", serif; }
.cap-top { text-align: center; font-size: 21px; line-height: 1.45; margin: 22px 0 16px; }
.cap-bot { text-align: center; font: 21px "Times New Roman", "Liberation Serif", serif; margin-top: 12px; }
.head { display: grid; grid-template-columns: 1.07fr 1fr; gap: 22px; }
.card { background: #F5F7FB; border: 1.5px solid #D9DFEA; border-radius: 14px; }
.persona { display: flex; gap: 22px; align-items: center; padding: 16px 20px; }
.kicker { color: #2F6DB5; font-weight: bold; font-size: 15px; letter-spacing: .3px; }
.name { font-size: 37px; font-weight: bold; color: #1D3461; margin: 2px 0 6px; }
.meta { font-size: 19px; line-height: 1.5; }
.meta i { color: #5b6577; }
.meta b { color: #1D3461; }
.info { padding: 16px 22px; font-size: 18.5px; line-height: 1.75; }
.info b { color: #1D3461; }
.grid { display: grid; grid-template-columns: 300px repeat(10, 1fr); grid-template-rows: auto auto repeat(5, 1fr);
        gap: 8px 7px; margin-top: 16px; height: var(--gh); }
.stage { border-radius: 10px; background: #E3E9F3; border: 1.5px solid #B9C6DC; color: #1D3461;
         font-weight: bold; font-size: 18px; padding: 9px 14px; display: flex; align-items: center; gap: 10px; }
.stage .sn { background: #1D3461; color: #fff; border-radius: 6px; padding: 2px 8px; font-size: 15px; white-space: nowrap; }
.label { border-radius: 12px; display: flex; align-items: center; gap: 14px; padding: 14px 16px; }
.label .ico { width: 46px; height: 46px; border-radius: 50%; background: #fff; display: flex; align-items: center;
              justify-content: center; flex: none; box-shadow: 0 1px 3px rgba(0,0,0,.12); }
.label .t { font-weight: bold; font-size: 23px; line-height: 1.25; color: #1D3461; }
.label .s { font-size: 13.5px; line-height: 1.4; margin-top: 4px; font-weight: normal; }
.lhead { background: #1D3461; color: #fff; }
.lhead .t { color: #fff; }
.lhead .ico { background: rgba(255,255,255,.18); box-shadow: none; }
.step { background: #1D3461; color: #fff; padding: 12px 28px 12px 22px; min-height: 176px;
        clip-path: polygon(0 0, calc(100% - 18px) 0, 100% 50%, calc(100% - 18px) 100%, 0 100%, 10px 50%); }
.step.first { clip-path: polygon(0 0, calc(100% - 18px) 0, 100% 50%, calc(100% - 18px) 100%, 0 100%); }
.step.mot { background: #B5601C; }
.step .n { font-size: 15px; opacity: .85; }
.step .t { font-size: 21.5px; font-weight: bold; line-height: 1.25; margin: 4px 0 6px; }
.step .d { font-size: 16px; line-height: 1.35; display: flex; gap: 6px; }
.step .d svg { flex: none; margin-top: 1px; }
.step .m { color: #FFD9A8; font-weight: bold; font-size: 15.5px; line-height: 1.35; margin-top: 8px; }
.cell { border-radius: 12px; padding: 13px 13px; font-size: 17.5px; line-height: 1.5; overflow: hidden; }
.cell ul { margin: 0; padding-left: 20px; }
.cell li { margin-bottom: 4px; }
.q { display: flex; gap: 8px; align-items: flex-start; }
.q i { color: #5B3A8E; flex: 1; }
.mood { flex: none; }
.emo { margin-top: 8px; font-size: 16px; line-height: 1.45; }
.chip { display: inline-block; border: 1.5px solid #6FB8B0; background: #fff; border-radius: 18px;
        padding: 3px 12px; font-size: 16px; line-height: 1.4; margin: 0 4px 7px 0; }
.opp { margin-bottom: 9px; }
.tag { display: inline-block; color: #fff; font-weight: bold; font-size: 13.5px; border-radius: 5px;
       padding: 1px 6px; margin-right: 6px; vertical-align: 2px; }
.P1 { background: #C8404A; } .P2 { background: #C47A1A; }
.rowline { border-left: 7px solid; }
.concl { margin-top: 14px; background: #FDF6EA; border: 1.5px solid #EDCB8F; border-radius: 12px;
         padding: 14px 26px; font-size: 19.5px; line-height: 1.6; }
.legend { font-size: 16.5px; color: #5b6577; margin-top: 6px; display: flex; gap: 14px; align-items: center; }
.legend .sw { display: inline-block; width: 18px; height: 14px; border-radius: 3px; vertical-align: -2px; margin-right: 6px; }
"""


def li(items):
    return "<ul>" + "".join(f"<li>{escape(x)}</li>" for x in items) + "</ul>"


def build(filled: bool) -> str:
    h = []
    if filled:
        h.append('<div class="pnum">16</div>')
        h.append('<div class="cap-top">Приложение А<br>User Journey Map персоны «Андрей Соколов»</div>')
    else:
        h.append('<div class="cap-top">User Journey Map персоны «Андрей Соколов» – шаблон для заполнения</div>')

    # шапка
    h.append('<div class="head"><div class="card persona">' + AVATAR + '<div>'
             '<div class="kicker">ПЕРСОНА ЯДРА ЦЕЛЕВОЙ АУДИТОРИИ ИЗ ЛАБОРАТОРНОЙ РАБОТЫ № 1</div>'
             '<div class="name">Андрей Соколов, 38 лет</div><div class="meta">'
             'Руководитель отдела продаж · женат, двое детей (7 и 12 лет) · доход 120 000 ₽ · Владивосток · смартфон на Android<br>'
             '<i>Отвечает за семейный бюджет, ипотеку и все счета. Жена не знает, где какие вклады и подписки.</i><br>'
             + svg(ICON["target"], "#1D3461", 18, sw=2.4) +
             ' <b>Цель:</b> Составить план на случай болезни, потери доступа или смерти, чтобы семья не осталась без денег и доступов'
             '</div></div></div>')
    h.append('<div class="card info">' + "<br>".join(f"<b>{k}:</b> {escape(v)}" for k, v in INFO) + '</div></div>')

    h.append('<div class="grid">')
    # строка этапов
    h.append('<div class="label lhead" style="grid-row:1;grid-column:1;padding:9px 16px"><div class="ico" style="width:36px;height:36px">'
             + svg(ICON["flag"], "#fff", 20) + '</div><div class="t" style="font-size:20px">Этап пути</div></div>')
    for i, (name, steps) in enumerate(STAGES, 1):
        a, b = steps[0] + 1, steps[-1] + 2
        h.append(f'<div class="stage" style="grid-row:1;grid-column:{a}/{b}"><span class="sn">Этап {i}</span>{escape(name)}</div>')

    # строка шагов
    h.append('<div class="label lhead" style="grid-row:2"><div class="ico">' + svg(ICON["pin"], "#fff", 26)
             + '</div><div><div class="t">Шаг путешествия</div><div class="s">Ключевые моменты в путешествии</div></div></div>')
    for n, s in enumerate(STEPS, 1):
        cls = "step" + (" first" if n == 1 else "") + (" mot" if filled and s.get("moment") else "")
        m = (f'<div class="m">★ Момент истины: {escape(s["moment"])}</div>' if filled and s.get("moment") else "")
        h.append(f'<div class="{cls}" style="grid-row:2"><div class="n">{n}</div><div class="t">{escape(s["title"])}</div>'
                 f'<div class="d">{svg(ICON["clock"], "#fff", 17)}<span>{escape(s["time"])}</span></div>{m}</div>')

    # категории
    for r, (key, title, ico, acc, bg) in enumerate(CATS, 3):
        sub = ('<div class="s" style="color:#5b6577">Какие меры следует предпринять на этом этапе со стороны разработчика?</div>'
               if key == "opps" and not filled else "")
        h.append(f'<div class="label rowline" style="grid-row:{r};background:{bg};border-color:{acc}">'
                 f'<div class="ico">{svg(ICON[ico], acc, 26)}</div><div><div class="t">{title}</div>{sub}</div></div>')
        for s in STEPS:
            body = ""
            if filled:
                if key == "actions":
                    body = li(s["actions"])
                elif key == "thoughts":
                    body = (f'<div class="q"><i>«{escape(s["quote"])}»</i>{mood_icon(s["mood"])}</div>'
                            f'<div class="emo"><b>Эмоции:</b> {escape(s["emo"])}<br><b>Мотивация:</b> {escape(s["mot"])}</div>')
                elif key == "touch":
                    body = "".join(f'<span class="chip">{escape(t)}</span>' for t in s["touch"])
                elif key == "pains":
                    body = li(s["pains"])
                else:
                    body = "".join(f'<div class="opp"><span class="tag {p}">{p}</span>{escape(t)}</div>' for p, t in s["opps"])
            h.append(f'<div class="cell" style="grid-row:{r};background:{bg}">{body}</div>')
    h.append('</div>')

    if filled:
        h.append('<div class="concl"><b>Выводы.</b> ' + escape(CONCLUSION) +
                 '<div class="legend"><span><span class="sw" style="background:#B5601C"></span>оранжевый шаг – момент истины</span>·'
                 '<span><span class="sw" style="background:#E3E9F3;border:1.5px solid #B9C6DC"></span>этап пути объединяет шаги</span>·'
                 '<span><span class="tag P1">P1</span>первая версия</span>·<span><span class="tag P2">P2</span>развитие продукта</span></div></div>')
        h.append('<div class="cap-bot">Рисунок А.1 – User Journey Map персоны «Андрей Соколов» в приложении «Ключ»</div>')

    title = "User Journey Map – Андрей Соколов" + ("" if filled else " (шаблон)")
    return (f'<!doctype html><html lang="ru"><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{CSS}:root{{--gh:{"1665px" if filled else "1840px"}}}</style></head><body><div class="page">{"".join(h)}</div></body></html>')


if __name__ == "__main__":
    (OUT / "map_filled.html").write_text(build(True), encoding="utf-8")
    (OUT / "map_template.html").write_text(build(False), encoding="utf-8")
    print("ok")
