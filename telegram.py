
#!/usr/bin/env python

import telebot,sys

BOT_TOKEN='SEU_TOKEN'
DESTINATION=sys.argv[1]
SUBJECT=sys.argv[2]
MESSAGE=sys.argv[3]

MESSAGE = MESSAGE.replace('/n','\n')
tb = telebot.TeleBot(BOT_TOKEN)
tb.send_message(DESTINATION,SUBJECT + '\n' + MESSAGE)
