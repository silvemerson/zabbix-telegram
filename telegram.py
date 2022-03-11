#!/usr/bin/env python3

import sys
import telebot

BOT_TOKEN= "1356580905:AAGfBD5oSjUDgQoYJsxs1if88k_2OVymWeI"
DESTINATION=sys.argv[1]
SUBJECT=sys.argv[2]
MESSAGE=sys.argv[3]

MESSAGE = MESSAGE.replace('/n','\n')
tb = telebot.TeleBot(BOT_TOKEN)
tb.send_message(DESTINATION,SUBJECT + '\n' + MESSAGE)
