from PIL import Image
import cv2 as cv
import pyscreenshot as ImageGrab
import pyautogui
import time
from mss import mss
import numpy as np

class params:
    count = 0
    start = 0
    value = 61750

class Coordinates:
    replayBtn = (383, 432)
    dinasaur = (206, 443)
    box = (dinasaur[0] + 65, dinasaur[1] + 5, dinasaur[0] + 90, dinasaur[1] + 15)
    #x = 270
    #y = 465

def restartGame():
    pyautogui.click(Coordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    # time.sleep(0.01)
    # print "Jump"
    pyautogui.keyUp('space')

def grabImage():

    image = ImageGrab.grab(bbox=Coordinates.box)
    imageGray = cv.cvtColor(np.array(image), cv.COLOR_RGB2GRAY)
    return imageGray.sum()

def rate():
    params.count += 1
    if time.time() - params.start > 1:
        print "FPS:", params.count
        params.start = time.time()
        params.count = 0

def main():
    restartGame()
    while True:
        rate()
        val = grabImage()
        if not val == params.value:
            pressSpace()
            # time.sleep(0.01)
            print val
        else:
            pass

main()
