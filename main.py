import speech_recognition as sr
import pyttsx3

class JarvisAI:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            self.listener.adjust_for_ambient_noise(source)
            audio = self.listener.listen(source)
            try:
                command = self.listener.recognize_google(audio)
                return command.lower()
            except sr.UnknownValueError:
                return ""
            except sr.RequestError:
                return ""

    def run(self):
        self.talk("Hello, I am Jarvis, your AI assistant. How can I assist you today?")
        while True:
            command = self.listen()
            if "stop" in command:
                self.talk("Goodbye!")
                break
            elif command:
                self.talk(f"You said: {command}")

if __name__ == '__main__':
    jarvis = JarvisAI()
    jarvis.run()