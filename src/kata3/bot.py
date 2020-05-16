import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Activar logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Definimos algunas funciones para los comandos. Estos generalmente toman los dos argumentos update y context
def start(update, context):
    """Envia un mensaje cuando se emita el comando /start."""
    return update.message.reply_text('Hola, Geeks!')

def help(update, context):
    """Envia un mensaje cuando se emita el comando /help."""

    return update.message.reply_text('Ayudame!')

def mayus(update, context):
    resultado = context.args[0].upper()
    resutlado = str(resultado)

    return update.message.reply_text(resultado)

def alreves(update, context):
    """Repite el mensaje del usuario."""
    return update.message.reply_text('hola'[::-1])

def error(update, context):
    """Envia los errores por consola"""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Inicio del Bot"""
    #Colocamos el Token creado por FatherBot
    updater = Updater("1242223840:AAHrD16xebl9EVuyYfncnvrQ3FViGtvUYMI", use_context=True)

    # Es el Registro de Comandos a través del dispartcher
    dp = updater.dispatcher

    # Añadimos a la lista de Registro todos los comandos con su función [start - help - mayus]
    #
    #
    #
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("mayus", mayus))


    # Este comando es un Trigger que se lanza cuando no hay comandos [alreves]
    #
    dp.add_handler(CommandHandler("alreves", alreves))
    # Y este espera al error
    dp.add_error_handler(error)

    # Lanzamos el Bot
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
