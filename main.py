import logging
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the feedback message handler
def feedback_handler(update: Update, context: CallbackContext) -> None:
    # Get the message text and user ID
    message_text = update.message.text
    user_id = '123456789'   # Replace with the Telegram user ID you want to send feedback to
    
    # Send the feedback message to the target user
    context.bot.send_message(chat_id=user_id, text=f"New feedback received: {message_text}")
    
    # Send a confirmation message to the user who provided the feedback
    context.bot.send_message(chat_id=update.effective_chat.id, text="Thank you for your feedback!")
