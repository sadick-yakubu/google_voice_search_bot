import speech_recognition as sr
from selenium import webdriver

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.browser = None

    def start(self):
        print("Voice assistant started. Listening for commands...")
        self.listen_on_mic()

    def listen_on_mic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print("Heard:", command)

                    if "search" in command:
                        search_query = command.split("search ", 1)[-1]
                        self.search_google(search_query)

            except sr.UnknownValueError:
                print("Sorry, I couldn't understand the audio.")
            except sr.RequestError:
                print("Sorry, there was an issue with the speech recognition service.")

    def search_google(self, query):
        try:
            print("Searching Google for:", query)
            if not self.browser:
                self.browser = webdriver.Chrome()
            self.browser.get(f"https://www.google.com/search?q={query}")
        except Exception as e:
            print("An error occurred while searching:", e)

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.start()
