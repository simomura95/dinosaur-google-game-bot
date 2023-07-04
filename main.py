from pyautogui import *
import keyboard
import time

# game link: https://elgoog.im/dinosaur-game/

screenWidth, screenHeight = size()
# dino_location = locateCenterOnScreen('dino.png', grayscale=True, region=(0, screenHeight//2, screenWidth//3, screenHeight))
# coordinates of the dinosaur (as from row above) and of a random background pixel in my pc (1920x1080)
dino_location = (147, 738)
bg_location = (dino_location[0], dino_location[1]+200)

# coordinates for collision check: x for distance, y_low for ground level obstacles, y_high for high pterodactyls
x_min = dino_location[0] + 280
x_max = dino_location[0] + 310
y_low = dino_location[1] + 20
y_high = dino_location[1] - 50

# parameters for adapting to game acceleration and duck duration
# tweaking them and x_min/x_max could improve the algorithm, but seems pretty good already
# there's a lot of randomization in the game, so different tries with same parameters can give very different scores
# MY HIGH SCORE with these parameters: 2120
accel_interval = 1  # every N seconds...
accel_value = 5  # ...increase x_max by this
accel_time = time.time() + accel_interval
duck_duration = 0.4

# after running the program, user has 10 seconds to go to the chrome page with the game
print('Start in 10 seconds. Go to the game page in you primary screen')
time.sleep(1)
click(dino_location)  # start
print('Start!')

# bot algorithm
# to stop the bot, press 'q' or go to a screen corner to trigger pyautogui failsafe mechanism (if needed)
while True:
    if keyboard.is_pressed('q'):
        break
    im = screenshot()
    bg_color = im.getpixel(bg_location)  # in the while cycle in order to handle night phases

    # avoid obstacles
    for x in range(x_min, x_max):
        low_color = im.getpixel((x, y_low))
        high_color = im.getpixel((x, y_high))
        if low_color != bg_color:  # jump if a low obstacle is detected
            press('up')
            break
        elif high_color != bg_color:  # duck if a flying obstacle is detected
            keyDown('down')
            time.sleep(duck_duration)
            keyUp('down')
            break

    # acceleration (with parameters defined before)
    if time.time() > accel_time and x_max < screenWidth*4/5:
        x_max += accel_value
        accel_time = time.time() + accel_interval
