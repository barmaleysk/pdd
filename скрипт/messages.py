#!/usr/bin/env python
# -*- coding: utf-8 -*-
import settings
start = {'mes':'start',
    'text':'''
Тебя приветсвует Горшочек с золотом!

✔️ Приглашай друзей в "Горшочек с золотом" и получи:
✔️ 15% от заработка рефералов 1 уровня
✔️ 5% от заработка рефералов 2 уровня
✔️ Больше друзей - больше золота!
✔️ Минимальная выплата: 15 рублей на QIWI и Яндекс!

Стоимость раскрутки канала: 50 копеек за одного подписчика. 
Минимальный заказ: 20 подписчиков.

Канал "Горшочек с золотом" https://t.me/pottygold
Смотрящий за ботом @lepriconadmin
По финансовым вопросам и рекламе @palapalaru
    ''',
    'markup':[
    [
        '➕ Горшочек вари'
    ],
    [
        '💎 Золотой пиар канала'
    ],
    [
        '🏠 Личный горшочек','💰 Запасы золота'
    ],
    [
        'Навар','⚠ Рецепт'
    ]
]}
# '💵 Баланс','👥 Рефералы'
admin = {
    'text':'Приветсвую вас в админке бота',
    'markup':[
        ['заявки на вывод'],['сделать рассылку'],['изменить баланс','пополнить баланс'],['⛔️ Отмена']
    ]
}

for_advert={
    'text':'''      *⚠️Как добавить канал⚠️ *
```
ℹ️Чтобы начать продвижение вашего канала вам нужно: 
1️⃣ Добавить нашего бота в администраторы вашего канала.
2️⃣ Переслать любой пост из вашего канала в чат с ботом.
3️⃣ Проследовать дальнейшим указаниям бота

```[ ]({})'''.format(settings.tutorial_url),
    'markup':[['Мои заказы'],['⛔️ Отмена']],
    'success':{
        'text':'''👑 Все сделано правильно!
👥Теперь введите стоимость 1 подписчика на ваш канал в рублях
⛔️Минимальная стоимость: {} рублей.'''.format(settings.min_post_cost),
        'markup':[['⛔️ Отмена']]
    },
    'success_count':{
        'text': '''Теперь введите желаемое количество подписчиков''',
        'markup': [['⛔️ Отмена']]
    },
    'success_apply': {
        'text': '''Стоимость продвижения канала: {} * {} = {}
        Все верно? Подтвердить?''',
        'markup': [['✅ Подтвердить'], ['⛔️ Отмена']]
    },
    'error_not_admin': {
        'text': '''🚫 Ошибка! Бот не обнаружен в администраторах канала. Добавьте бота и нажите кнопку ниже.''',
        'markup': [[{'text':'Проверить','data':'check_admin'},{'text':'❌ Отклонить','data':'cancel_check_admin'}]]
    },
    'error_low_cost': {
        'text': '''🚫 Ошибка!
Минимальная стоимость одного подписчика -  {} руб'''.format(settings.min_post_cost),
        'markup': [['⛔️ Отмена']]
    },
    'success_done':{
        'text': '''Канал добавлен!''',
        'markup': start['markup']
    },
    'error_money':{
        'text': '''🚫 Ошибка! Недостаточно средст на счету''',
        'markup': start['markup']
    },
    'already_in':{
        'text': '''🚫 Ошибка! Канал можно будет добавить заново после вступления добавленного количества подписчиков''',
        'markup': [['Мои заказы'],['⛔️ Отмена']]
    }
}


view_end = {
    'text':'''♦ Держи монетку, вы получили: {} рублей.
💰 Ваш баланс: {} рублей''',
    'markup':start['markup']
}

sub_err= {
    'text':'💰Ты собрал всё золото. Вернись позднее, чтобы горшочек успел пополниться!',
    'markup':start['markup']
}



channel_enter_cost={
    'error':{
        'text':'Ошибка! Введите число',
        'markup':[['⛔️ Отмена']]
    },
    'error_0.10': {
        'text': 'Ошибка! Стоимость 1 просмотра не может быть ниже 0.1 рубля',
        'markup': [['⛔️ Отмена']]
    }

}
channel_enter_count={
    'text':'Введите колличество просмотров',
    'markup':[['⛔️ Отмена']],
    'error':{
        'text':'Ошибка! Введите число',
        'markup':[['⛔️ Отмена']]
    },
    'error_int': {
        'text': 'Ошибка! Введите целое число',
        'markup': [['⛔️ Отмена']]
    }

}


stat={
    'text':''' *Навар проекта*:
    😎Участников проекта: %all_users%
    🤠Новые участники: %users_today%
    🚀Каналов на продвижении: %posts_count%
    💰Заработано всего: %money_for_views%
    💸Выплачено всего: %money_out%''',
    'markup':start['markup']
}

decline={
    'text':'''Операция отменена''',
    'markup':start['markup']
}



out_pay = {
    'text':'''К выводу доступно %max_money%. Минимальная сумма - {}. Напиши нужную сумму.'''.format(settings.min_out_pay),
    'markup':[['⛔️ Отмена']],
    'ya':{
        'text': '''К выводу доступно %max_money%. Минимальная сумма - {}. Напиши нужную сумму.'''.format(
            settings.min_out_pay),
        'markup': [['⛔️ Отмена']],
    },
    'error_min_pay': {
        'text': 'Ошибка! Нельзя вывести меньше минимальной суммы',
        'markup': [['⛔️ Отмена']]
    },
    'error_max_pay': {
        'text': 'Ошибка! У вас недостаточно средств на счету',
        'markup': [['⛔️ Отмена']]
    },
    'enter_ya': {
        'text': 'Хорошо! Теперь введите номер вашего кошелька',
        'markup': [['⛔️ Отмена']]
    },
    'enter_qiwi': {
        'text': 'Хорошо! Теперь введите номер телефона, который привязан к QIWI',
        'markup': [['Отправить номер вашего телефона'],['⛔️ Отмена']]
    },
    'success': {
        'text': 'Ожидайте перечисления средств с 08-00 по 20-00..',
        'markup': start['markup']
    }
}

balance={
    'code':{
        'text':'''🔥Для автоматического пополнения баланса переведите нужную сумму на этот QIWI кошелек {} со следующим кодом в комментарии к переводу.
⛔️Очень важно оставить код в комментарии, иначе платеж не будет засчитан!

⚡После перевода запасы Вашего золота пополнятся в самое ближайшее время'''.format(settings.number),
        'markup':start['markup']
    },
    'success':{
        'text': 'Ваш счет пополнен на {}',
        'markup': start['markup']
    },
    'ya':{
        'text': '''🔥 Для автоматического пополнения баланса переведите нужную сумму по [ссылке](https://money.yandex.ru/to/{}) со следующим кодом в комментарии к переводу.
⛔️Очень важно оставить код в комментарии, иначе платеж не будет засчитан!

⚡️После перевода запасы Вашего золота пополнятся в самое ближайшее время'''.format(settings.ya_number),
        'markup': start['markup']
    }

}


edit_balance={
    'text': 'Введи имя пользователя с @username или его id',
    'markup':[['⛔️ Отмена']],
    'err_user':{
        'text':'Ошибка, пользователь не найден',
        'markup':[['⛔️ Отмена']]
    },
    'enter_balance':{
        'text': 'Введите новый баланс пользователя, сейчас он %balance%',
        'markup': [['⛔️ Отмена']]
    },
    'success':{
        'text': 'Новый баланс установлен!',
        'markup': admin['markup']
    },
    'err_number':{
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    }

}

pay_balance={
    'text': 'Введи имя пользователя с @username или его id',
    'markup':[['⛔️ Отмена']],
    'err_user':{
        'text':'Ошибка, пользователь не найден',
        'markup':[['⛔️ Отмена']]
    },
    'enter_balance':{
        'text': 'Введите на сколько пополнить, сейчас баланс %balance%',
        'markup': [['⛔️ Отмена']]
    },
    'success':{
        'text': 'Баланс пополнен!',
        'markup': admin['markup']
    },
    'err_number':{
        'text': 'Ошибка! Введите число',
        'markup': [['⛔️ Отмена']]
    }

}

mailer = {
    'text':'Отправь нужное сообщение для рассылки',
    'markup':[['⛔️ Отмена']],
    'confirm':{
        'text': 'Принято! Разослать?',
        'markup': [['⛔️ Отмена'],['✅ Подтвердить']],
    },
    'success':{
        'text': 'Ок!',
        'markup': admin['markup']
    }
}
