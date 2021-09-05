from pynput.keyboard import Key, Controller

def timer(n):
    import time
    time.sleep(n)

k = Controller()

def key(*words):
    for word in words:
        if type(word) == str and len(word) != 1:
            k.type(word)
        else:
            k.press(word)
            k.release(word)
        timer(1)

def func1(*words):
    for word in words:
        k.press(word)

def func2(*words):
    for word in words:
        k.release(word)

timer(1)
func1(Key.ctrl,"a","c")
func2(Key.ctrl,"a","c")
timer(1)
key(Key.cmd,"Windows Terminal",Key.enter)
timer(1)
func1(Key.ctrl,Key.shift,"6")
func2(Key.ctrl,Key.shift,"6")
timer(1)
key("system cls",Key.enter)
# timer(1)
func1(Key.ctrl,"v")
func2(Key.ctrl,"v")