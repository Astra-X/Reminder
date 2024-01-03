# Libraries to be used
from gtts import gTTS
import plyer
import time
from plyer import notification
from playsound import playsound




# Input section

tts = gTTS('Welcome In Reminder App', lang='en', tld="us")
tts.save('hello.mp3')
playsound("hello.mp3")
banner = '''
\033[30;32m
______________________\033[30;31m
        _____
     _.'_____`._
   .'.-'  12 `-.`.
  /,' 11      1 `.\\
 // 10      /   2 \\
;;         /       ::
|| 9  ----O      3 ||
::                 ;;
 \\ 8           4 //
  \`. 7       5 ,'/
   '.`-.__6__.-'.'
    ((-._____.-))
    _))       ((_
   '--'       '--'
\033[30;33m
    Reminder App
       By Saaz
\033[30;32m
______________________
\033[30;33m
Choose The Time Format:
\033[30;32m
::- \033[30;31m Minutes
\033[30;32m
::- \033[30;31m Hour
\033[30;32m
______________________
'''

print(banner)
time_format = str(input("\033[30;32m:- \033[30;31m "))

if time_format == 'minutes':
    print(" ")
    time_minutes = float(input("\033[30;32m Duration: \033[30;31m"))
    body = str(input("\033[30;32m What's the reminder about:- \033[30;31m "))
    time_minutes = time_minutes * 60
    print("\033[30;33m Starting the Timer ..... ")
    time.sleep(time_minutes)
    notification.notify(title = "Reminder", message=(body),timeout = 1)
    body_sound = gTTS(body, lang='en', tld="us")
    body_sound.save('body.mp3')
    playsound("body.mp3")

if time_format == 'hour':
    print(" ")
    time_hour = float(input("\033[30;32m Duration: \033[30;31m"))
    body = str(input("\033[30;32m What's the reminder about:- \033[30;31m "))
    time_hour = time_hour * 60 * 60
    print("\033[30;33m Starting the Timer ..... ")
    time.sleep(time_hour)
    notification.notify(title = "Reminder", message=(body),timeout = 1)
    body_sound = gTTS(body, lang='en', tld="us")
    body_sound.save('body.mp3')
    playsound("body.mp3")


