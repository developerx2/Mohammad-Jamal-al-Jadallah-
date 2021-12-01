from winsound import PlaySound, Beep, SND_ALIAS  # winsound library 
from random import randrange # random library

while True:
    Beep(frequency=randrange(5000), duration=randrange(2000)) # here we made every time new sound becuase of that we used randrange from random 
    PlaySound('SystemExit', SND_ALIAS) # PlaySound you can choose the sound
    PlaySound('SystemHand', SND_ALIAS) #  untile the sound work use SND_ALIAS
