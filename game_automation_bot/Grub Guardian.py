import pyautogui
import cv2
import numpy as np
import time

def findImg(img, threshold=0.8):
    #SELECTING WIZARD101 PRIZES
    isDone = False
    while not isDone:
        try:
                # Take a screenshot of the screen
                screenshot = pyautogui.screenshot()
                screen = np.array(screenshot)

                # Convert the screen image to grayscale and match
                screen_gray = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
                result = cv2.matchTemplate(screen_gray, img, cv2.TM_CCOEFF_NORMED)

                # Get the locations of matches
                locations = np.where(result >= threshold)
                
                # If matches exist, return the locations
                if len(locations[0]) > 0:
                    isDone = True
                    return locations
        except OSError as e:
            print("Error taking screenshot, retrying...", e)
            time.sleep(1)  # Wait before retrying
        

def clickImg(locations, img):
        #If matches exist, click the first one
        if (len(locations[0]) > 0):
            # Get the coordinates of the first match
            match_x = locations[1][0]
            match_y = locations[0][0]

            # Calculate the center of the match
            match_center = (match_x + img.shape[1] // 2, match_y + img.shape[0] // 2)

            # Move the mouse to the center of the match and click
            pyautogui.click(match_center)

while True:
    refImg1 = cv2.imread("imgs/reference1.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg1)), refImg1)

    refImg2 = cv2.imread("imgs/reference2.PNG", cv2.IMREAD_GRAYSCALE)
    # clickImg((findImg(refImg2)), refImg2)
    clickImg((findImg(refImg2, 0.5)), refImg2)

    refImg3 = cv2.imread("imgs/reference3.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg3)), refImg3)

    time.sleep(5)

    refImg4 = cv2.imread("imgs/reference4.PNG", cv2.IMREAD_GRAYSCALE)
    locations4 = (findImg(refImg4))
    #Triple-Click to place pet
    clickImg(locations4, refImg4)
    clickImg(locations4, refImg4)
    clickImg(locations4, refImg4)

    time.sleep(0.2)
    refImg5 = cv2.imread("imgs/reference5.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg5)), refImg5)

    speedButton = cv2.imread("imgs/speedButton.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(speedButton)), speedButton)

    #Check for 7 food remaining
    refImg6 = cv2.imread("imgs/reference6.PNG", cv2.IMREAD_GRAYSCALE)
    findImg(refImg6)
    #Pause game if 7 food is remaining
    pauseButton = cv2.imread("imgs/pauseButton.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(pauseButton)), pauseButton)

    #Place towers and upgrade while game is paused
    refImg7 = cv2.imread("imgs/reference7.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg7)), refImg7)

    mythSymbol = cv2.imread("imgs/mythSymbol.PNG", cv2.IMREAD_GRAYSCALE)
    locations8 = (findImg(mythSymbol))
    clickImg(locations8, mythSymbol)
    clickImg(locations8, mythSymbol)

    refImg8 = cv2.imread("imgs/reference8.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg8)), refImg8)

    locations8 = (findImg(mythSymbol))
    clickImg(locations8, mythSymbol)
    clickImg(locations8, mythSymbol)

    refImg9 = cv2.imread("imgs/reference9.PNG", cv2.IMREAD_GRAYSCALE)

    #Upgrade both myth towers to tier 2
    for i in range(2):
        clickImg((findImg(refImg9)), refImg9)
        locations9 = (findImg(mythSymbol))
        clickImg(locations9, mythSymbol)
        clickImg(locations9, mythSymbol)
        time.sleep(0.5)

    #Unpause so minions can advance
    playButton = cv2.imread("imgs/playButton.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(playButton)), playButton)

    refImg10 = cv2.imread("imgs/reference10.PNG", cv2.IMREAD_GRAYSCALE)
    findImg(refImg10)

    #Pause again when myth minions are tier 2
    clickImg((findImg(pauseButton)), pauseButton)

    #Upgrade both myth towers to tier 3
    for i in range(2):
        clickImg((findImg(refImg10)), refImg10)
        locations9 = (findImg(mythSymbol))
        clickImg(locations9, mythSymbol)
        clickImg(locations9, mythSymbol)

    #Unpause so minions can advance
    clickImg((findImg(playButton)), playButton)

    #Check to see if wave 11 has started
    refImg11 = cv2.imread("imgs/reference11.PNG", cv2.IMREAD_GRAYSCALE)
    findImg(refImg11, 0.98)

    clickImg((findImg(pauseButton)), pauseButton)

    #Upgrade right myth tower to tier 4
    refImg12 = cv2.imread("imgs/reference12.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg12)), refImg12)
    locations12 = (findImg(mythSymbol))
    clickImg(locations12, mythSymbol)
    clickImg(locations12, mythSymbol)

    #Upgrade left myth tower to tier 4
    refImg13 = cv2.imread("imgs/reference13.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg13)), refImg13)
    locations13 = (findImg(mythSymbol))
    clickImg(locations13, mythSymbol)
    clickImg(locations13, mythSymbol)

    clickImg((findImg(playButton)), playButton)

    #Upgrade left myth tower to tier 5
    refImg14 = cv2.imread("imgs/reference14.PNG", cv2.IMREAD_GRAYSCALE)
    findImg(refImg14)
    refImg15 = cv2.imread("imgs/reference15.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg15)), refImg15)
    locations15 = (findImg(mythSymbol))
    clickImg(locations15, mythSymbol)
    clickImg(locations15, mythSymbol)

    #Upgrade right myth tower to tier 5
    refImg16 = cv2.imread("imgs/reference16.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg16)), refImg16)
    locations16 = (findImg(mythSymbol))
    clickImg(locations16, mythSymbol)
    clickImg(locations16, mythSymbol)

    #Pause the game when silver reaches 30
    refImg17 = cv2.imread("imgs/reference17.PNG", cv2.IMREAD_GRAYSCALE)
    findImg(refImg17, 0.9)
    clickImg((findImg(pauseButton)), pauseButton)
    clickImg((findImg(refImg6,0.6)), refImg6)

    #Buy star guardian when silver hits 30
    starSymbol = cv2.imread("imgs/starSymbol.PNG", cv2.IMREAD_GRAYSCALE)
    locations17 = (findImg(starSymbol, 0.8))
    time.sleep(1)
    clickImg(locations17, starSymbol)
    #Give the game a buffer of time
    time.sleep(0.1)
    clickImg(locations17, starSymbol)

    #Unpause after placing star guardian
    clickImg((findImg(playButton)), playButton)

    #Upgrade star guardian at the start of wave 8
    refImg18 = cv2.imread("imgs/reference18.PNG", cv2.IMREAD_GRAYSCALE)
    findImg(refImg18, 0.98)
    refImg19 = cv2.imread("imgs/reference19.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg19, 0.7)), refImg19)
    locations19 = (findImg(starSymbol, 0.6))
    clickImg(locations19, starSymbol)
    pyautogui.click()

    refImg20 = cv2.imread("imgs/reference20.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg20, 0.6)), refImg20)
    locations20 = (findImg(starSymbol, 0.6))
    clickImg(locations20, starSymbol)
    pyautogui.click()

    refImg21 = cv2.imread("imgs/reference21.PNG", cv2.IMREAD_GRAYSCALE)
    findImg(refImg21)

    refImg22 = cv2.imread("imgs/reference20.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg22, 0.5)), refImg22)
    locations20 = (findImg(starSymbol, 0.6))
    clickImg(locations20, starSymbol)
    pyautogui.click()

    refImg23 = cv2.imread("imgs/reference23.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg23)), refImg23)

    refImg24 = cv2.imread("imgs/reference24.PNG", cv2.IMREAD_GRAYSCALE)
    clickImg((findImg(refImg24)), refImg24)
