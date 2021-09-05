from pynput.keyboard import Key, Controller
def timer(n):
    import time
    time.sleep(n)

k = Controller()
timer(6)
count = 0
while count<11:
    count+=1
    timer(1)
    k.press(Key.menu)
    k.release(Key.menu)
    timer(1)
    k.press(Key.down)
    k.release(Key.down)
    timer(1)
    k.press(Key.down)
    k.release(Key.down)
    timer(1)
    k.press(Key.enter)
    k.release(Key.enter)
k.press(Key.alt)
k.press(Key.tab)
k.release(Key.alt)
k.release(Key.tab)
