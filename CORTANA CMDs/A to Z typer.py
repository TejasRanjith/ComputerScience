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
        k.release(word)
        timer(0.03)

# def func2(*words):
#     for word in words:
#         k.release(word)
#         timer(1)

timer(5)
func1('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
# func2('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')