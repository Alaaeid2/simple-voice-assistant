import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import datetime
import pytz
import time

# Initialize speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

import random

def speak(text):
    print("Assistant:", text)
    time.sleep(random.uniform(0.4, 0.9))  # Pre-response delay
    engine.say(text)
    engine.runAndWait()
    time.sleep(random.uniform(0.3, 0.6))  # Post-response delay

# Listen for voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command.lower()
        except sr.UnknownValueError:
            # Don't say anything, just pass silently
            return ""
        except sr.RequestError:
            speak("Network issue, please check your connection.")
            return ""


# Handle specific commands
def handle_command(command):
    if "facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")

    elif "gmail" in command or "email" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    elif "linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("https://www.linkedin.com")

    elif "github" in command:
        speak("Opening Github")
        webbrowser.open("https://www.github.com")

    elif "time" in command and "cairo" in command:
        cairo_time = datetime.now(pytz.timezone('Africa/Cairo')).strftime('%I:%M %p')
        speak(f"The time in Cairo is {cairo_time}")

    elif "stop" in command or "exit" in command:
        speak("Goodbye! 👋")
        return False

    else:
        speak("I’m not sure how to help with that yet.")
    return True

# Main assistant loop
def main():
    speak("Hey! I'm your voice assistant. How can I help you today?")
    active = True
    while active:
        command = listen()
        if command:
            active = handle_command(command)

if __name__ == "__main__":
    main()
