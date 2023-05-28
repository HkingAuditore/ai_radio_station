import openai
import pyttsx4


class AIMusicAnalysis:
    @staticmethod
    def init():
        openai.organization = "org-xUHfsra8qWK3EiUfxZ8zy7Wj"
        openai.api_key = "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"

    @staticmethod
    def get_ai_text(msg):
        messages = [{"role": "system", "content": msg}]
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        return chat.choices[0].message.content



class AiTTS:
    engine = pyttsx4.init()

    @staticmethod
    def init():
        engine = pyttsx4.init()

    @staticmethod
    def speak(t):
        file_name = 'tmp.mp3'
        AiTTS.engine.save_to_file(t, file_name)
        AiTTS.engine.runAndWait()
        return file_name
