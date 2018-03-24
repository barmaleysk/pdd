db_url='sqlite:///db.sqlite'

ref_pay_perc_1lvl=0.15 #столько получит от 1 уровная рефералов за оплату
ref_pay_perc_2lvl=0 #столько получит от 2 уровная рефералов за оплату
ref_view_pay_1lvl=0.15 #столько получит от 1 уровная рефералов за подписку
ref_view_pay_2lvl=0.05 #столько получит от 2 уровная рефералов за подписку
user_view_perc=0.40 #столько получит пользователь за вступление(проценты от стоимости установленной заказчиком)
min_out_pay=15 #минимальная сумма для вывода
min_post_cost=0.5 #минимальная стоимость 1 подписчика

number=тут твой номер киви в формате 79872995795
qiwi_token ='тут киви токен'

ya_number=тут твой яндекс кошелек
ya_token=''

telegram_token='569622420:AAGJXvjWHvdVTnfhOS3GcvExt43bdeHgECM'



uah_to_rub=2.16
usd_to_rub=57.85
eur_to_rub=67.73

admins = [сюда вписать ваш id который выдаст бот в вашей статистике для админки]


tutorial_url = 'http://telegra.ph/'



WEBHOOK_HOST = '46.101.75.213'
WEBHOOK_PORT = 88
WEBHOOK_LISTEN = '0.0.0.0'


WEBHOOK_SSL_CERT = './webhook_cert.pem'
WEBHOOK_SSL_PRIV = './webhook_pkey.pem'

WEBHOOK_URL_BASE = "https://{}:{}".format(WEBHOOK_HOST, WEBHOOK_PORT)

WEBHOOK_URL_PATH = "/{}/".format(telegram_token)
