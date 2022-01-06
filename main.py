import PySimpleGUI as sg
from gtts import gTTS 
import datetime
import os

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter any japanese text here to get it\'s mp3 format')],
            [sg.Text('Your text here:'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Pragati Voice', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break


    print(datetime.datetime.now())
    date = str(datetime.datetime.now())
    date = date[0:10]
    print(date)

    #Defining a simple text 

    text = values[0]

    #Define the language of text

    language = 'ja'

    #Defining the speech 

    speech = gTTS(text = text, lang = language, slow = False)

    #Saving the speech

    if(len(text)>10):
        file_name = f"{text[0:10]}-{date}.mp3"
    else:
        file_name = f"{text}-{date}.mp3"

    speech.save(file_name)

    #playing the speech 

    os.system(f"start {file_name}")

window.close()