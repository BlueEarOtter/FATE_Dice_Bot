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
    return

def roll(bot, update,args):
    """
    /roll function:
        rolls n FATE dice and modified by m.
    syntax:
        /roll ndF ±m
    defaults:
        n = 4, m = 0
    
    Sends dice string and values to the bot
    """
    #initialize variables for output                        
    output = ""
    n=4
    modifier=0
    modstring=""
    
    #read in the arguments
    for arg in args:
        if (arg[0] == "+") and (arg[1::].isdigit()):
            modifier = int(arg[1::])
            modstring = " + " + arg[1::]
        if (arg[0]=="-") and (arg[1::].isdigit()):
            modifier = -int(arg[1::])
            modstring = " - " + arg[1::]
        if (arg[-2::].lower() == "df") and (arg[0:-2].isdigit()):
            n = int(arg[0:-2])
    
    #initialize dice
    dice = [0]*n
    
    #roll the dice n times
    for i in range(0,n):
        #store each roll number and dice face
        dice[i],strdie = fateroll()
        output+= strdie
        del strdie
    
    #write output string
    outText = output+modstring+" = "+str(sum(dice)+modifier)
    #send output to bot
    bot.send_message(chat_id=update.message.chat_id, text=outText)
    return

def help(bot, update, args):
    #help manuals
    helphelp = "Help menu. can list commands using \"/help list\". Can get information about specific functions by calling \"/help <function name>\"\n  ex: /help roll"
    listhelp = "/roll - rolls dice\n/start - launches bot\n/help - help files"
    rollhelp = "/roll function:\nrolls n FATE dice and modified by m.\n\nsyntax:\n    /roll ndF ±m\ndefaults:\n    n = 4, m = 0\n\nSends dice string and values to the bot"
    starthelp="/start fucntion\nMessage that greets users when they first launch the bot.\n  -indicates what the /roll command does"
    #switch statement to chose manual
    if len(args)==0:
        bot.send_message(chat_id=update.message.chat_id, text=helphelp)
    elif args[0].lower() == "list":
        bot.send_message(chat_id=update.message.chat_id, text=listhelp)
    elif args[0].lower() == "roll":
        bot.send_message(chat_id=update.message.chat_id, text=rollhelp)
    elif args[0].lower() == "start":
        bot.send_message(chat_id=update.message.chat_id, text=starthelp)
    else: bot.send_message(chat_id=update.message.chat_id, text=helphelp)
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
    roll_handler = CommandHandler('roll', roll, pass_args=True)
    help_handler = CommandHandler('help', help, pass_args=True)
    
    #Tell the dispatcher where to find the handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(roll_handler)
    dispatcher.add_handler(help_handler)
    
    #Start the bot
    updater.start_polling()
    
    return

####################
#Main Function Call#
####################

if __name__ == "__main__":
    main(authToken)
