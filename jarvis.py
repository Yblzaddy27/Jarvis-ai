import speech_recognition as sr
import pyttsx3
import openai

class Jarvis:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command
            except sr.UnknownValueError:
                print("Sorry, I did not understand that.")
                return None
            except sr.RequestError:
                print("Could not request results from Google Speech Recognition service.")
                return None

    def process_command(self, command):
        openai.api_key = self.openai_api_key
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": command}]
        )
        return response['choices'][0]['message']['content']

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def run(self):
        while True:
            command = self.listen()
            if command:
                response = self.process_command(command)
                self.speak(response)
