import telegram
from key import token

bot = telegram.Bot(token=token)
status = bot.send_message(chat_id="@SleepReminder", text="пора спать", parse_mode=telegram.ParseMode.HTML)

print(status)
