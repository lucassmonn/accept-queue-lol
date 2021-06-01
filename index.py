from time import sleep
import pyautogui


def click(x, y):
    pyautogui.click(x, y)


def check_screen():
    button = pyautogui.locateOnScreen('en.png', confidence=0.7)
    buttonPt = pyautogui.locateOnScreen('pt.png', confidence=0.7)
    
    print('Waiting...')

    if button != None:
        click(button.left, button.top)
        return True

    if buttonPt != None:
        click(buttonPt.left, buttonPt.top)
        return True

    return False


def main():
    print('Started.')
    while True:
        if check_screen():
            print('Match accepted.')
            sleep(6)
            break


main()
