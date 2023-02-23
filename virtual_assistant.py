from datetime import datetime
from os import listdir
from audioplayer import AudioPlayer
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia

# Initialize the user_speech recognizer
recognizer = sr.Recognizer()

# Initialize the speech-to-user_speech engine
engine = pyttsx3.init()

# Define a function to listen for user_speech input turn it into user_speech
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)

        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")


        except sr.RequestError:
            speak("Sorry, the service is not available")

    return said.lower()

# Speaks users user_speech
def speak(user_speech):
    engine.say(user_speech)
    print(user_speech)
    engine.runAndWait()

# Interactions based on user's user_speech
def respond(user_speech):    
    if 'youtube' in user_speech:
        speak("What do you want to search for?")
        keyword = get_audio()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Here is what I have found for {keyword} on youtube")

    elif 'search' in user_speech:
        speak("What do you want to search for?")
        query = get_audio()
        if query !='':
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia, " + result)                        

    elif 'what time' in user_speech:
        strTime = datetime.today().strftime("%H:%M")        
        speak("It is " + strTime + " now")
        
    elif 'play music' in user_speech or 'play song' in user_speech:
        speak("Okay! Playing...")
        music_dir = "C:\\Users\\UserName\\Downloads\\Music\\" #add your music directory here..
        songs = listdir(music_dir)
        #counter = 0        
        audioplayer = AudioPlayer(music_dir + "\\" + songs[0]).play(block=True)

    elif 'stop music' in user_speech:
        speak("Okay. Stopping audio playback.")
        audioplayer.stop()

    elif 'exit' in user_speech:
        speak("See you later!")                
        exit()

# Call the listen_and_respond function in a loop to continuously listen for user_speech input
while True:
    print('Hello! Say something.')
    user_speech = get_audio()
    speak(user_speech)
