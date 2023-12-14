import requests
import schedule
import time

def text():
    request = requests.post("https://textbelt.com/text",{
                            "phone" : "+4593956980",
                            "message" : "I like to eat Greek Souvlakia this time!",
                            "key" : "blahblah"})
    print(request.json())

schedule.every().day.at("20:00").do(text)

while True:
    schedule.run_pending()
    time.sleep(1)