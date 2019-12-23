import speech_recognition as spr
import webbrowser, time, os, random, pyttsx3
from time import ctime

r = spr.Recognizer()

parleur = pyttsx3.init('sapi5')
voices = parleur.getProperty('voices')
parleur.setProperty('voice', voices[1].id)
rate = parleur.getProperty('rate')
parleur.setProperty('rate', 173)

def record_audio(ask=False):
    with spr.Microphone() as source:
        if ask:
            safa_bot(ask)
        audio = r.listen(source)
        votre_parole = ''
        try:
            votre_parole = r.recognize_google(audio)
        except spr.UnknownValueError:
            safa_bot('Sorry, I did not get that')
        except spr.RequestError:
            safa_bot('Sorry, my speech service is down')
        return votre_parole

def safa_bot(audio_string):
    #tts = gTTS(text=audio_string, lang='fr')
    print('Safa Bot : ' + audio_string)
    parleur.say(audio_string)
    parleur.runAndWait()

def respond(votre_parole):
    if 'What is your name' or 'your name' in votre_parole:
        safa_bot('My name is Safa')
    if 'time' or 'what time is it' or 'time now' in votre_parole:
        safa_bot(ctime())
    if 'search' in votre_parole:
        cherche = record_audio(' ?')
        url = 'https://google.com/chercher?q=' + cherche
        webbrowser.get().open(url)
        safa_bot('Here is what I found for' + cherche)
    if 'find location' or 'location' or 'place' in votre_parole:
        lieu = record_audio('What is the location ?')
        url = 'https://google.nl/maps/place/' + lieu + '/&amp;'
        webbrowser.get().open(url)
        safa_bot('Here is the location of '+ lieu)
    if 'exit' in votre_parole:
        exit()

time.sleep(1)
safa_bot('How can i help you!')
while 1:
    votre_parole = record_audio()
    respond(votre_parole)
