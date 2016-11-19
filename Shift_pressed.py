import win32api, win32con

win32api.keybd_event(win32con.SHIFT_PRESSED,
                     0,
                     win32con.KEYEVENTF_EXTENDEDKEY,
                     0)

win32api.keybd_event(97,
                     0,
                     win32con.KEYEVENTF_EXTENDEDKEY,
                     0)

win32api.keybd_event(97,0,win32con.KEYEVENTF_KEYUP,0)

