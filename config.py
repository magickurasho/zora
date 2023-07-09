RPCs = {
    'Ethereum': 'https://eth.llamarpc.com',
    'Zora': 'https://rpc.zora.energy',
}

###############################################################################################################

# Время ожидания между выполнением разных акков рандомное в указанном диапазоне
NEXT_ADDRESS_MIN_WAIT_TIME = 1  # В минутах
NEXT_ADDRESS_MAX_WAIT_TIME = 2  # В минутах

# Время ожидания между действиями одного аккаунта
NEXT_TX_MIN_WAIT_TIME = 6   # В секундах
NEXT_TX_MAX_WAIT_TIME = 12  # В секундах

# Максимальное кол-во попыток сделать запрос/транзакцию если они фейлятся
MAX_TRIES = 3

###############################################################################################################

# Токен и chat id бота в тг. Можно оставить пустым.
TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = 0
# При True, скрипт только выдает ваш chat id для отправки сообщений в боте.
GET_TELEGRAM_CHAT_ID = False

###############################################################################################################

# Максимальный газ прайс в Gwei, при котором делать транзакции в Ethereum
MAX_ETH_GAS_PRICE = 20

# Сколько секунд ждать до следующей проверки газ прайса
WAIT_GAS_TIME = 10
# Сколько всего секунд ждать лучшего газ прайса,
# если за это время газ прайс не понизится до нужного значения, будет ошибка
TOTAL_WAIT_GAS_TIME = 3600

###############################################################################################################

# 0 - только бридж
# 1 - только минт
# 2 - и бридж и минт
MODE = 2

# Сколько бриджить эфира в Zora. Выбирается рандомное значение в диапазоне
BRIDGE_AMOUNT = (0.001, 0.0015)

# Сколько максимум ждать бриджа. Баланс проверяется каждые 20 секунд
BRIDGE_WAIT_TIME = 300

# Адрес нфт для минта
NFT_ADDRESS = '0xf41a3e3033d4e878943194b729aec993a4ea2045'
# Стандарт нфт для минта: ERC721 или ERC1155
NFT_STANDARD = 'ERC1155'

# Необходимо для ERC1155 минтов, данные можно взять из любой транзакции минта в сканере
MINTER_ADDRESS = '0x169d9147dFc9409AfA4E558dF2C9ABeebc020182'
TOKEN_ID = 3
