import time
from telegram import Bot

# Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather
TOKEN = '6234737963:AAF84w6FMwsSOrKO4aMW1yedqnoe_jAQ3aE'
CHANNEL_ID = 1001910479831  # Replace with your channel's username

def main():
    bot = Bot(token=TOKEN)
    while True:
        new_invite_link = bot.export_chat_invite_link(CHANNEL_ID)
        bot.send_message(chat_id=CHANNEL_ID, text=f"New link: {new_invite_link}")
        time.sleep(300)  # Wait for 5 minutes

if __name__ == '__main__':
    main()
