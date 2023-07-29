import os

class Config:
    TELEGRAM_TOKEN = '5782470033:AAFvagcCui2IGFeB1Utp2UgMTZrzDqZuWsQ'
    TELEGRAM_APP_HASH = '9b5ff18e133fed80f0f6cd7bf30cffdd'
    TELEGRAM_APP_ID = 13715737

    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')

    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
        
