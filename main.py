import logging
import asyncio
from telegram import Bot

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = 'YOUR_BOT_TOKEN'
CHANNEL_ID = 'YOUR_CHANNEL_TOKEN'  # Use @username format or numerical ID
DELAY_SECONDS = 3  # Delay between sending each line in seconds

def split_into_lines(message: str) -> list:
    """Split text into separate line"""
    return message.split('\n')

async def test_bot():
    bot = Bot(token=TOKEN)
    message = """ADD TEXT HERE
ADD TEXT HERE
ADD TEXT HERE
ADD TEXT HERE
KEEP GOING IF YOU WANT"""  # Example multi-line message

    lines = split_into_lines(message)

    for line in lines:
        # Send each line to the Telegram channel
        await bot.send_message(chat_id=CHANNEL_ID, text=line)
        logger.info(f"Sent line to channel: {line[:50]}...")  # Log only the start of the line
        await asyncio.sleep(DELAY_SECONDS)  # Delay between messages

    logger.info("All lines sent to channel.")

if __name__ == '__main__':
    asyncio.run(test_bot())
