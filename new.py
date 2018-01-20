from ctypes import windll, Structure, c_long, byref
import time

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt.x, pt.y


i=1
while i<10000:
	pos = queryMousePosition()
	print(pos)
	i=i+1
	time.sleep(.5)