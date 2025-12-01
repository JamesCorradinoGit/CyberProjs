import hashlib
import tkinter as tk

def encodeString(str):
    md5 = hashlib.md5()
    str = str.encode()

    md5.update(str)
    strToReturn = md5.hexdigest()

    return(strToReturn)
root = tk.Tk()
print(encodeString("hi guys"))

root.mainloop()
