from abc import ABC
from typing import Final


class TgConfig(ABC):
    STATE: Final = {}
    BASKETS: Final = {}
    BLACKJACK_STATS: Final = {}
    COINFLIP_STATS: Final = {}
    COINFLIP_ROOMS: Final = {}
    HEADS_GIF: Final = r'C:\\Users\\eriku\\Downloads\\coin-flip-coin-flip-heads.gif'
    TAILS_GIF: Final = r'C:\\Users\\eriku\\Downloads\\coin-flip-coin-flip-tails.gif'
    CHANNEL_URL: Final = 'https://t.me/+iXbi98gT0v5lOTNk'
    HELPER_URL: Final = '@Karunele'
    REVIEWS_URL: Final = 'https://t.me/+-yPLEiJwp-IxYzlk'
    PRICE_LIST_URL: Final = 'https://t.me/+iXbi98gT0v5lOTNk'
    GROUP_ID: Final = -988765433
    REFERRAL_PERCENT = 7
    PAYMENT_TIME: Final = 1800
    RULES: Final = 'insert your rules here'
    START_PHOTO_PATH: Final = r'C:\Users\Administrator\Downloads\photo_2025-08-17_23-09-19.jpg'
    ACHIEVEMENTS: Final = [
        'start',
        'first_purchase',
        'first_topup',
        'first_blackjack',
        'first_coinflip',
        'gift_sent',
        'first_referral',
        'five_purchases',
        'streak_three',
        'ten_referrals',
    ]


    ACHIEVEMENTS: Final = ['start', 'first_purchase']

