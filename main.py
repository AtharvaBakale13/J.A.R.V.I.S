# Importing Required Modules
import pyttsx3 # type: ignore
import datetime # type: ignore
import speech_recognition as sr # type: ignore
import webbrowser # type: ignore
import os # type: ignore
import random # type: ignore

# Configuring Engine
engine = pyttsx3.init('sapi5') # Using Default Speech API
voices = engine.getProperty('voices') # Getting Available Voices
engine.setProperty('voice', voices[1].id) # Setting Voice to Second Available Voice

# Speak Function
def speak(audio): 
  engine.say(audio) # Queue the Text to be Spoken
  engine.runAndWait() # Process and Play the Speech

# WishMe Function
def wishMe():
  '''
  It wishes the user according to the current time.
  '''

  hour = int(datetime.datetime.now().hour) # Get Current Hour

  if hour >= 0 and hour < 12:
    speak("JARVIS Powering Up. Good Morning Boss! How Can I Help You Today?")
  elif hour >= 12 and hour < 18:
    speak("JARVIS Powering Up. Good Afternoon Boss! How Can I Help You Today?")
  else:
    speak("JARVIS Powering Up. Good Evening Boss! How Can I Help You Today?")

def takeCommand():
  '''
  It takes microphone input from the user and returns string output.
  '''

  recognizer = sr.Recognizer() # Initialize Recognizer

  with sr.Microphone() as source: # Use Microphone as Source
    print("Listening...")
    recognizer.pause_threshold = 1 # Set Pause Threshold
    audio = recognizer.listen(source) # Listen for Audio Input

    try:
      print("Recognizing...")
      query = recognizer.recognize_google(audio, language='en-in') # Recognize Speech using Google
      print(f"User said: {query}\n") # Print Recognized Text

    except Exception as e:
      print("Say That Again Please...") # Prompt User to Repeat For Recognition Failure
      return "None"
  
    return query # Return Recognized Text

# Main Function
if __name__ == "__main__":
  wishMe() # Call WishMe Function

  while True:
    query = takeCommand().lower() # Call takeCommand Function and Convert to Lowercase

    # Logic for Executing Tasks Based on Query

    # Open In Browser
    if "open youtube" in query: # YouTube
      webbrowser.open("youtube.com")

    elif "open google" in query: # Google
      webbrowser.open("google.com")

    elif "open stackoverflow" in query: # Stack Overflow
      webbrowser.open("stackoverflow.com")

    # Playing Music
    elif "play music" in query:
      musicDir = "C:\\Users\\nitin\\OneDrive\\Music" # Path to Music Directory
      songs = os.listdir(musicDir) # List All Songs in Directory
      
      random_index = random.randint(0, len(songs) - 1) # Generate Random Index

      os.startfile(os.path.join(musicDir, songs[random_index])) # Start Playing the Randomly Selected Song

    # Telling Time
    elif "the time" in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S") # Get Current Time
      print (strTime) # Print Current Time
