from telegram import *
from telegram.ext import *

from config import PORT,TOKEN

def start(update:Update,context:CallbackContext):
	update.message.reply_text("hello")
	
	
	
	
updater = Updater(TOKEN)

ds = updater.dispatcher

ds.add_handler(CommandHandler("start",start))


updater.start_webhook("0,0,0,0",PORT,TOKEN,webhook_url="https://myapptele.herokuapp.com/"+TOKEN)


 
