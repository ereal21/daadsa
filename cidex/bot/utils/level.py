LEVEL_THRESHOLDS = [0, 1, 5, 15, 30, 50]

LEVEL_NAMES = {
    'lt': [
        '😶‍🌫️ Niekšas',
        '👏 Fanas',
        '🎛️ Prodiuseris',
        '🛹 Mobo narys',
        '🧠 Mobo lyderis',
        '🎤 Reperis',
    ],
    'en': [
        '😶‍🌫️ Scoundrel',
        '👏 Fan',
        '🎛️ Producer',
        '🛹 Crew member',
        '🧠 Crew leader',
        '🎤 Rapper',
    ],
    'ru': [
        '😶‍🌫️ Негодяй',
        '👏 Фанат',
        '🎛️ Продюсер',
        '🛹 Участник банды',
        '🧠 Лидер банды',
        '🎤 Рэпер',
    ],
}


def get_level_info(purchases: int, lang: str = 'lt'):
    """Return level details for given purchase count."""
    if purchases < 0:
        purchases = 0
    level_index = 0
    for idx, threshold in enumerate(LEVEL_THRESHOLDS):
        if purchases >= threshold:
            level_index = idx
        else:
            break
    names = LEVEL_NAMES.get(lang, LEVEL_NAMES['lt'])
    level_name = names[level_index]
    discount = round(level_index * 1.2, 1)
    if level_index < len(LEVEL_THRESHOLDS) - 1:
        next_threshold = LEVEL_THRESHOLDS[level_index + 1]
        progress = purchases - LEVEL_THRESHOLDS[level_index]
        needed = next_threshold - LEVEL_THRESHOLDS[level_index]
        bars_filled = (progress * 5) // needed
        progress_bar = '🟩' * bars_filled + '⬜️' * (5 - bars_filled)
        battery = '🪫' if progress * 2 < needed else '🔋'
    else:
        progress_bar = '🟩' * 5
        battery = '🔋'
    return level_name, discount, progress_bar, battery
