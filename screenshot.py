import pyscreenshot as ImageGrab
import datetime
import time
time.sleep(3)  # tell me why I used delay here...
im = ImageGrab.grab()
im.save("screenshot-" + str(datetime.datetime.now()) + ".png")
im.show()