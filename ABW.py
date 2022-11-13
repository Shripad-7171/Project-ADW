import pyautogui
import time
import datetime
n = datetime.datetime.now()
n = n.strftime("%d%m20%y")
print(n)
friend = {'Meet':7387551883,'Adwait':7666875833,'Saumya':7888183823,'Girishank':8767146190}
def basic():
    pyautogui.press('win')
    time.sleep(2)
    pyautogui.write('Whatapp', interval=0.1)
    pyautogui.press('enter')
    time.sleep(5)

def line():
    pyautogui.write(no, interval=0.1)
    time.sleep(2)
    pyautogui.moveTo(321,272, duration= 2)
    pyautogui.click()
    pyautogui.moveTo(747,978, duration= 2)
    pyautogui.click()
    
if n=="13112022":
    basic()
    no=str(friend.get('Meet'))
    line()
    pyautogui.write("Happy Birthday Meet!!!",interval=0.1)
    pyautogui.press('enter')

# if n=="13112022":
#     basic()
#     no=str(friend.get('Adwait'))
#     line()
#     pyautogui.write("Happy Birthday Adwait!!!",interval=0.1)
#     pyautogui.press('enter')

# if n=="13112022":
#     basic()
#     no=str(friend.get('Saumya'))
#     line()
#     pyautogui.write("Happy Birthday Saumya!!!",interval=0.1)
#     pyautogui.press('enter')

# if n=="13112022":
#     basic()
#     no=str(friend.get('Girishank'))
#     line()
#     pyautogui.write("Happy Birthday Girishank!!!",interval=0.1)
#     pyautogui.press('enter')




    


    




