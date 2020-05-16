"""
Va a atender a 3 comandos de telegram.
contestará mensajes sencillos

NLTK: procesamiento de lenguaje natural.

Usaremos una librería: python-telegram-bot


"""

from telegram.ext import Updater, CommandHandler #esta clase permite la conexión con telegram y analizar el contenido
def main():
    #inicializamos el updater
    updater= Updater(token="1102785689:AAE34yvxtVJqJCrGf-I72-FqmKqyRSicEVI",use_context=True)
            #updater=Updater(token=open("./bot_token").read(),use_context=True)
            #Lo que hacemos es decirle que lo lea de un archivo
    
    #añadimos manejador al comando /start --> quien atiende a las notificaciones
    updater.dispatcher.add_handler(CommandHandler("start",start)) #se encargan de responder y reaccionar ante comandos/mensajes

    #manejador para comando /repite
    updater.dispatcher.add_handler(CommandHandler("repite", repite))

    #manejador para comando /suma
    updater.dispatcher.add_handler(CommandHandler("suma", suma))

    #empezamos a pedir notificaciones a Telegram
    updater.start_polling()
    
    #capturamos señales de parada
    updater.idle()

#envia 2 parametros: info update y context, el contexto del update
def start(update, context):
    update.message.reply_text("Hola! Soy un bot. Comencemos...")

#responde al mensaje con el texto del propio comando
def repite(update, context):
    update.message.reply_text(update.message.text)

#realiza una suma
def suma(update, context):
    #args = [2,2]
    resultado = int(context.args[0]) + int(context.args[1])
    update.message.reply_text("El resultado es: " + str(resultado))


main()
