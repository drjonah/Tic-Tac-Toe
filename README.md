# Tic Tac Toe

## Meet Alex!
Alex is an AI designed to never lose a tic tac toe game!

Alex is able to predict every board possible throughout the game given an index and determine all of the winning, tying, and losing positions. From those three, Alex prioritizes the winnning, then the tying, and finally the losing positions. If there are multiple outcomes in each, Alex will chose randomly which path/position to pursue. 

Alex is able to accomplish this through an algorithm known as **minimax**. This algorithm works by factoring the best way (max) for Alex to win and the best way (min) for you to lose to compute a 1, 0, -1. These represent winning, tying, and losing respectively.

## How to play!

To play, you will want to download the whole *src* folder. To run the game, you will want to run the file **runner.py**. **Settings.json** is where you will edit the settings for your game. (How to use **settings.json** can be found below.) **ai.py** is where all of Alex's logic is found. **ai.py** can be run to test single move outcomes! Costom boards can be stored within **ai.py**'s main function. **Cli.py** and **gui.py** can both be ran by themselves but they run differently outside **runner.py**.

#### cli.py info
This is a board showing each index/position on the board.

`` 0 | 1 | 2 ``

``-- --- --``

`` 3 | 4 | 5``

``-- --- --``

`` 6 | 7 | 8 ``


For example, 0 plays the top left while 7 plays the middle bottom.

#### settings.json info
**Settings.json** is how you control **runner.py**. In **settings.json**, you can edit two parameters: *mode* and *ai difficulty*. 

*Mode*
* "cli" (runs Tic Tac Toe in the terminal)
* "gui" (run Tic Tac Toe in an interactive GUI)

*Ai difficulty*
* "1" = CHILDS PLAY!
* "2" = HARD!
* "3" = IMPOSSIBLE!

## Extra:
If Alex beats you on *difficulty = 3*, let me know! It is not suppose to lose! ;)

## Coming soon!
- [x] Difficulty modes for Alex!
- [x] Interactive playable GUI for Tic Tac Toe.
- [ ] Tic Tac Toe expansion.
- [x] Lose on difficulty level 3