import os,webbrowser,time

def timer(n):
    time.sleep(n)

url1 = "https://web.whatsapp.com/"
url2 = "https://mail.google.com/mail/u/0/?tab=wm&ogbl#inbox"
url3 = "https://mail.google.com/mail/u/1/?tab=wm&ogbl#inbox"
url4 = "https://mail.google.com/mail/u/2/?tab=wm&ogbl#inbox"
url5 = "https://mail.google.com/mail/u/3/?tab=wm&ogbl#inbox"
url6 = "https://mail.google.com/mail/u/4/?tab=wm&ogbl#inbox"

timer(1)
webbrowser.open_new_tab(url1)
timer(1)
webbrowser.open_new_tab(url2)
timer(1)
webbrowser.open_new_tab(url3)
timer(1)
webbrowser.open_new_tab(url4)
timer(1)
webbrowser.open_new_tab(url5)
timer(1)
webbrowser.open_new_tab(url6)
