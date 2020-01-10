#py3.7
###############for keys
import win32com.client as comctl
wsh=comctl.Dispatch("WScript.Shell")


###############for mouse
import win32api, win32con
#https://stackoverflow.com/questions/1181464/controlling-mouse-with-python
#https://docs.microsoft.com/en-us/windows/desktop/api/winuser/nf-winuser-mouse_event
def moveTo(x, y):
    win32api.SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTF_MOVE | win32con.MOUSEEVENTF_ABSOLUTE, int(x/SCREEN_WIDTH*65535.0), int(y/SCREEN_HEIGHT*65535.0))

    
def moveRelative(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)
    

def clickRight():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)

def clickLeft():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)

    
import time
#moveTo(250, 45)
#clickLeft()
wsh.AppActivate("Блокнот")
time.sleep(1)
moveRelative(-50, 50)
wsh.SendKeys("a")
time.sleep(0.5)
wsh.SendKeys("a")
time.sleep(0.5)
wsh.SendKeys("a")
#clickRight()
#wsh.SendKeys("{F1}")