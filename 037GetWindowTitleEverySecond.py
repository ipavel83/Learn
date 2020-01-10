import win32gui
import time

tempWindowName=win32gui.GetWindowText (win32gui.GetForegroundWindow())
print("first Window Title: ", tempWindowName)

while True:
    if tempWindowName == win32gui.GetWindowText (win32gui.GetForegroundWindow()):
        pass #Window name not changed
    else:
        tempWindowName=win32gui.GetWindowText (win32gui.GetForegroundWindow())
        print(time.time(), tempWindowName) #log changed name
    time.sleep(1.01)