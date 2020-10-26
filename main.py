import speech_recognition as sr # pip install speechrecognition
from time import sleep as slep # sleep functuon
import tweepy # pip install tweepy

import keys # imports the keys file

'''Twitter API keys'''
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

'''Voice recognizer object'''
r = sr.Recognizer()

with sr.Microphone(device_index=1) as source: # microphone may have to be changed
    while True:
        try:
            '''Listens to your voice, prints and tweets it'''
            audio = r.listen(source)
            slep(2)
            voice_text = r.recognize_google(audio)
            print(voice_text)
            final = "Tweet from voice: \n" + voice_text
            api.update_status(str(final))

        except sr.UnknownValueError:
            '''If it doesn't hear what you say'''
            print('Unkown ')