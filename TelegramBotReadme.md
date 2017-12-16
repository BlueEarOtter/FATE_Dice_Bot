# How To use FATE Dice Bot
## Table of Contents
* [Command List](#command-list)
  * [/start](#start---greeting-upon-starting-the-bot)
  * [/roll](##roll---rolls-fate-dice-returns-a-dice-string-and-a-number)
    * [Modified Rolls](#modified-rolls)
    * [Rolling ndF](#rolling-ndf)
  * [/help](#help---returns-manuals-abbreviated-manuals-for-commands)
    * [List](#list)
    * [Function Manuals](#function-manuals)
## Command List
### /start - Greeting upon starting the bot
- Input:
  ```
  /start
  ```
- Output:
  ```
  Welcome Adventurers!
  
  Use /roll to roll 4 FATE dice.
  ```
### /roll - Rolls FATE dice. Returns a dice string and a number
Default roll is 4dF (that is, 4 FATE Dice)
- Input:
  ```
  /roll
  ```
- Output:
  ```
  [ + ][ o ][ + ][ - ] = 1
  ```
#### Modified Rolls
Modifications to roll can be added by including a +m or -m argument
- Example: Modifier = +2
  - Input:
    ```
    /roll +2
    ```
  - Output:
    ```
    [ - ][ - ][ o ][ + ] + 2 = 1
    ```
- Example: Modifier = -1
  - Input:
    ```
    /roll -1
    ```
  - Output:
    ```
    [ - ][ - ][ + ][ + ] - 1 = -1
    ```
#### Rolling ndF
Rolls are not limited to 4dF, using the ndF argument, you can roll n dice
- Example: Rolling 2dF
  - Input:
    ```
    /roll 2dF
    ```
  - Output:
    ```
    [ - ][ - ] = -2
    ```
- Example: Roll 3dF with a +1 modifier
  - Input:
    ```
    /roll 3dF +1
    ```
  - Output:
    ```
    [ o ][ o ][ o ] + 1 = 1
    ```
### /help - Returns manuals abbreviated manuals for commands
Default input:
- Input:
  ```
  /help
  ```
- Output:
  ```
  Help menu. can list commands using "/help list". Can get information about specific functions by calling "/help <function name>"
    ex: /help roll
  ```
#### List
- Input:
```
/help list
```
- Output:
```
/roll - rolls dice
/start - launches bot
/help - help files
```
#### Function Manuals
Example: roll
- Input:
  ```
  /help roll
  ```
- Output:
  ```
  /roll function:
  rolls n FATE dice and modified by m.
  
  syntax:
      /roll ndF ±m
  defaults:
      n = 4, m = 0
  
  Sends dice string and values to the bot
  ```  

