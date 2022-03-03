# This code to make pranks in your friends
# it will rotate the screen

from rotatescreen import get_primary_display
from time import sleep
degrees = [0, 90, 180, 270, 360]
for i in range(20):
    get_primary_display().rotate_to(degrees[i % 4])
    sleep(2)
