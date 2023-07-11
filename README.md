# Bot for google dinosaur game 
Bot for automating google dinosaur game, using PyAutoGUI.
![chrome-dino-game](https://github.com/simomura95/dinosaur-google-game-bot/assets/134875169/87150ec1-d1a7-40a6-9ecf-169936dd530d)

Might need to change dinosaur initial location on different screens, else it will not work.

The bot checks for obstacles in a space that becomes bigger over time (+5 pixels each second), to keep the pace with game acceleration.<br>
Dino jumps if a low obstacle is detected, while it ducks below high obstacles (a jump requires more time and there could not be enough).
