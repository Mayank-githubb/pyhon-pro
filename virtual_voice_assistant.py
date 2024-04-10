import speech_recognition as sr
import pyttsx3

def speak(text):
  engine = pyttsx3.init()
  engine.say(text)
  engine.runAndWait()

def get_audio():
  recognizer = sr.Recognizer()
  with sr.Microphone() as source:
    print("Listen...")
    audio = recognizer.listen(source)
  try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
    return text
  except sr.UnknownValueError:
    print("Sorry, I could not understand audio")
    return None
  except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return None

def process_command(command):
  if "open wikipedia" in command.lower():
    speak("Opening Wikipedia...")
    webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")
  elif "play music" in command.lower():
    speak("Playing music...")
    # You'll need additional libraries to play music
  else:
    speak("I can't perform that action yet, but I'm still learning!")

print("Hi! How can I help you?")
while True:
  command = get_audio().lower()
  if command == "quit":
    break
  process_command(command)