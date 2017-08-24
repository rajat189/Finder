#!/usr/bin/env python3.4

from tkinter import *
from tkinter import ttk
import webbrowser
from pygame import mixer
import speech_recognition as sr
from keys import *

root = Tk()
root.title('Finder')
root.iconbitmap('mic.ico')

photo = PhotoImage(file='microphone.png').subsample(15,15)

lbl = ttk.Label(root, text='Find:')
lbl.grid(row=0, column=0)
Text_field = ttk.Entry(root, width=40)
Text_field.grid(row=0, column=1, columnspan=4)

Button2_Output = StringVar()

def callback():
    
    if Button2_Output.get() == 'google' and Text_field.get() != '':
        webbrowser.open('http://google.com/search?q='+Text_field.get())
        
    elif Button2_Output.get() == 'duck' and Text_field.get() != '':
        webbrowser.open('http://duckduckgo.com/?q='+Text_field.get())

    elif Button2_Output.get() == 'amz' and Text_field.get() != '':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+Text_field.get())

    elif Button2_Output.get() == 'ytb' and Text_field.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+Text_field.get())

    else:
        pass

def get(event):

    if Button2_Output.get() == 'google' and Text_field.get() != '':
        webbrowser.open('http://google.com/search?q='+Text_field.get())
        
    elif Button2_Output.get() == 'duck' and Text_field.get() != '':
        webbrowser.open('http://duckduckgo.com/?q='+Text_field.get())

    elif Button2_Output.get() == 'amz' and Text_field.get() != '':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+Text_field.get())

    elif Button2_Output.get() == 'ytb' and Text_field.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query='+Text_field.get())

    else:
        pass

def buttonClick():

    mixer.init()
    mixer.music.load('Image1.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400

    with sr.Microphone() as source:

        try:

            audio = r.listen(source, timeout=5)
            message = str(r.recognize_google(audio, key=google_api_key))
            mixer.music.load('Image2.mp3')
            mixer.music.play()
            Text_field.focus()
            Text_field.delete(0, END)
            Text_field.insert(0, message)

            if Button2_Output.get() == 'google':
                webbrowser.open('http://google.com/search?q='+message)
        
            elif Button2_Output.get() == 'duck':
                webbrowser.open('http://duckduckgo.com/?q='+message)

            elif Button2_Output.get() == 'amz':
                webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords='+message)

            elif Button2_Output.get() == 'ytb':
                webbrowser.open('https://www.youtube.com/results?search_query='+message)

            else:
                pass

        except sr.UnknownValueError:
            print('Could not understand')

        except sr.RequestError as e:
            print('Did not get the results from Google Spech Recognition')

        else:
            pass    

Text_field.bind('<Return>', get)

Button1 = ttk.Button(root, text='Search', width=10, command=callback)
Button1.grid(row=0, column=6)

Button2 = ttk.Radiobutton(root, text='Google', value='google', variable=Button2_Output)
Button2.grid(row=1, column=1, sticky=W)

Button3 = ttk.Radiobutton(root, text='Duck', value='duck', variable=Button2_Output)
Button3.grid(row=1, column=2, sticky=W)

Button4 = ttk.Radiobutton(root, text='Amz', value='amz', variable=Button2_Output)
Button4.grid(row=1, column=3)

Button5 = ttk.Radiobutton(root, text='Ytb', value='ytb', variable=Button2_Output)
Button5.grid(row=1, column=4, sticky=E)

Button6 = Button(root, image=photo, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
Button6.grid(row=0, column=5)

Text_field.focus()
root.wm_attributes('-topmost', 1)
Button2_Output.set('google')
root.mainloop()