# FATE_Dice_Bot
Telegram Bot that is used to play FATE-based RPGs
-Bot location: @fate_dice_bot
-Bot currently not hosted

This bot uses the python-telegram-bot package to interface with telegram. 

see: https://github.com/python-telegram-bot/python-telegram-bot

Code includes:
- /start command -- Initializes bot
- /roll command -- rolls 4 FATE dice and returns a schematic diagram as well as a number

Intended future edits:
- Character creation sheets from FATE: Accelerated
- Arguments included for adding to rolls and rolling more or less than 4 dice.

Using this code: 
This code is currently written as a python script and intended for use with python 3.6. To use this code, first download and install the python-telegram-bot module for python 3:

$ pip install python-telegram-bot --upgrade

then download this script and edit line 23, inserting the authorization token given to you by Telegram
see: https://core.telegram.org/bots#6-botfather for more info on tokens

run this script from within iPython using the %run "/REPLACE/THIS/WITH/THE/PATH/TO/SCRIPT" command

The bot will begin running. To stop communication with the bot, either use the updater.stop() command or terminate your instance of python.
