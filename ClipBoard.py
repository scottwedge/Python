import win32clipboard
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText("Hola")
win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()