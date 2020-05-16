import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    message = 'Hola, Geeks!'
    update.message.reply_text(message)

    return message

def help(update, context):
    message = 'Ayudame!'
    update.message.reply_text(message)

    return message

def mayus(update, context):
        result = [x.upper() for x in context.args]
        result = ''.join(result)
        update.message.reply_text(result)
        
        return result

def alreves(update, context):
    result = update.message.text[::-1]
    update.message.reply_text(result)

    return result

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""

    updater = Updater(
        token=open("./bot_token").read(),
        use_context=True
    )

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('mayus', mayus))

    dp.add_handler(MessageHandler(Filters.text, alreves))
    
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
