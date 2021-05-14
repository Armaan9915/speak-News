import sys
def speak(str):
    from win32com.client import Dispatch 
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

try:
    if __name__ == '__main__':
        import requests
        import json
        url = ('http://newsapi.org/v2/top-headlines?'
            'country=in&'
            'apiKey=65f097a87edc464e8c92e767cbb7c9db')
        response = requests.get(url)
        text = response.text
        jscomp = json.loads(text)
        print("_______________Indian News________________")
        speak("Some Indian News headlines")
        for i in range(10):
            print("News " + str(i+1)+ " : " + jscomp['articles'][i]['title'])
            speak("News " + str(i+1)+ " : " + jscomp['articles'][i]['title'])

except KeyboardInterrupt:
    sys.exit()







