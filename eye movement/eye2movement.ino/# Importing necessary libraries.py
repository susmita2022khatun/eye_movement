# Importing necessary libraries
import serial
import pyautogui
import webbrowser
import sys

# checking which applications are open
thisPC_opened = False
browser_opened = False
alt_opened = False
connection_success = False

# Initializing serial communication
while not connection_success:
    port = input("Enter port for serial communication: ")
    try:
        ser = serial.Serial(port=port, baudrate='9600', timeout=1)
        connection_success = True

    except:
        print("Invalid port!!")
        connection_success = False


# Receiving serial data
def get_count():
    data = ser.readline().decode()

    if "count:" in data.lower():
        dataList = data.split()
        count = int(dataList[1])
        return count

    else:
        return 0


print(
    ''' 
    This is a script to control your PC with the movement of eyes. The following actions are possible:
    
                [1] : open 'My computer' / 'This PC'
                [2] : open Default web-browser
                [3] : 
                [4] : Exit this program
    
    This script is written and designed by Susmita Khatun''')

# Main program loop
while True:
    count = get_count()
    if count > 0:
        if not thisPC_opened and not browser_opened and not alt_opened:
            if count == 1:
                print("Opening My Computer...")
                pyautogui.hotkey('win', 'e')
                thisPC_opened = True


            elif count == 2:
                print("opening web browser...")
                webbrowser.open('https://www.google.co.in')
                browser_opened = True

            elif count == 3:
                pass


            elif count == 4:
                print("Exiting...")
                sys.exit()


        elif thisPC_opened and not browser_opened:
            if count == 1:
                pyautogui.press('right')

            elif count == 2:
                pyautogui.press('space')

            elif count == 3:
                pyautogui.press('enter')

            elif count == 4:
                pyautogui.hotkey('alt', 'f4')
                thisPC_opened = False


        elif not thisPC_opened and browser_opened:
            if count == 1:
                pyautogui.hotkey('ctrl', 't')

            elif count == 2:
                pyautogui.typewrite('https://www.youtube.com/')
                pyautogui.press('enter')

            elif count == 3:
                pyautogui.typewrite('https://www.google.com/gmail')
                pyautogui.press('enter')

            elif count == 4:
                pyautogui.hotkey('alt', 'f4')
                browser_opened = False