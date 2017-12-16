#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@BlueEarOtter 15 Dec 2017 -- 1513404213

FATE Dice Telegram Bot

Uses python to play FATE Based RPGs

Copy and paste this script to start the bot
or run it using the %run command in iPython
"""

from telegram.ext import Updater
from telegram.ext import CommandHandler
import random as rand
import logging

############
#Parameters#
############
authToken = 'INSERT TOKEN NUMBER HERE' #a token that lets Python communicate with the bot

##############
#Py Functions#
##############

def fateroll():
    die=rand.randint(-1,1)
    if die == -1:
        return die,"[ - ]"
    elif die == 0:
        return die,"[ o ]"
    elif die == 1:
        return die,"[ + ]"

############
#/functions#
############

def start(bot, update):
    """
    /start fucntion
    Message that greets users when they first launch the bot.
        -indicates what the /roll command does
    """
    #Write welcome message
    welcomeText = "Welcome Adventurers!\n\nUse /roll to roll 4 FATE dice."
    #Send welcome message to bot
    bot.send_message(chat_id=update.message.chat_id,text=welcomeText)

def roll(bot, update):
    """
    /roll function
    rolls 4 FATE dice. Sends dice string and values to the bot
    """
    #define variables for output
    dice=[0,0,0,0]                         
    output = ""
    
    #roll the dice 4 times
    for i in range(0,4):
        #store each roll number and dice face
        dice[i],strdie = fateroll()
        output+= strdie
        del strdie
    
    #write output string
    outText = output+" = "+str(sum(dice))
    #send output to bot
    bot.send_message(chat_id=update.message.chat_id, text=outText)
    return

######
#Main#
######

def main(Token):
    #Create an update/dispatch channel to communicate with bot
    updater = Updater(token=Token)
    dispatcher = updater.dispatcher
    
    #Create a log file
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    
    #Define the start and roll handlers
    start_handler = CommandHandler('start', start)
    roll_handler = CommandHandler('roll', roll)
    
    #Tell the dispatcher where to find the handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(roll_handler)
    
    #Start the bot
    updater.start_polling()
    
    return

####################
#Main Function Call#
####################

if __name__ == "__main__":
	main(authToken)
