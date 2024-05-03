import cv2
import numpy as np
import pyautogui as pg
import time
import keyboard
import threading

# Variable to control the click thread
click_thread_running = False

def click_thread():
    print("clicking started")
    global click_thread_running
    while click_thread_running:
        pg.click()

screenshot = pg.screenshot()
screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

try:
    new_border = pg.locateOnScreen('klik.png', confidence=0.9)
    print("Pomeram za klik na [", new_border.left, ",", new_border.top, "]")
    pg.moveTo(new_border.left, new_border.top)
    click_thread_running = True
except:
    pass

# Start the click thread
click_thread = threading.Thread(target=click_thread)
click_thread.daemon = True  # Daemonize the thread so it will exit when the main program exits
click_thread.start()

while True:
    screenshot = pg.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    if keyboard.is_pressed('caps lock'):
        print("======================== Stopiram program ========================")
        click_thread_running = False  # Set the variable to stop the click thread
        break

    try:
        border = pg.locateOnScreen('AktiviranFull.png', confidence=0.9)
        print("Pomeram za upgrade na [", border.left, ",", border.top, "]")
        pg.moveTo(border.left, border.top)
        pg.click()
        time.sleep(0.1)
        try:
            new_border = pg.locateOnScreen('klik.png', confidence=0.9)
            print("Pomeram za klik na [", new_border.left, ",", new_border.top, "]")
            pg.moveTo(new_border.left, new_border.top)
        except:
            pass
    except:
        try:
            golden_border = pg.locateOnScreen('golden_bunny.png',confidence=0.6)
            print("Pomeram za golden na [", golden_border.left, ",", golden_border.top, "]")
            pg.moveTo(golden_border.left, golden_border.top)
            try:
                new_border = pg.locateOnScreen('klik.png', confidence=0.9)
                print("Pomeram za klik na [", new_border.left, ",", new_border.top, "]")
                pg.moveTo(new_border.left, new_border.top)
            except:
                pass
        except:
            print("Nisam nasao Golden Bunnya")

click_thread.join()  # Wait for the click thread to finish execution
