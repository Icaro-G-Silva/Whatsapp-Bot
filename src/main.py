from core import Bot

try:
    print('Starting program...\n')

    #Instantiating object WhatsappBot
    bot = Bot.WhatsappBot("Message", ["Contact Name", "Another Contact"])

    #Schedule time to send the message
    #bot.scheduleTime(minute = 10)

    #Sending the message to contacts listed
    bot.sendMessages()

    #Sending the message with Flood function
    #bot.sendFlood(15)
except Exception as error:
    print(f"Error ocurred -> {error}")
finally:
    print("\nFinishing program...")
