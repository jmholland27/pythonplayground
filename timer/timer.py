# https://www.fesliyanstudios.com/royalty-free-sound-effects-download/alarm-203
import time
from playsound import playsound

# ANSI charcaters that allow you to interact with the terminal
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"



def alarm(secs):
    print(CLEAR)
    for x in range(secs, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600)
        print(f'{CLEAR_AND_RETURN}{hours:02}:{minutes:02}:{seconds:02}')
        time.sleep(1)
    
    print(CLEAR_AND_RETURN, 'Time\'s Up!')
    for i in range(3):
        playsound(r'C:\Users\jmhol\Desktop\alarm.mp3')
    

my_time = int(input('Enter the time in seconds: '))

alarm(my_time)