#This is a python project from which you will get to know the covid-19 updates on your windows

import requests
from win10toast import ToastNotifier
import json
import time


def updateCovid():
    r= requests.get("https://coronavirus-19-api.herokuapp.com/all")
    data = r.json()
    text = {'Confirmed Cases : {data["cases"]} \n deaths : {data["deaths"]} \n Recoverd : {data["recovered"]}'}
    while True:
        toast = ToastNotifier()
        toast.show_toast("covid-19 updates",text,duration=20)
        time.sleep(60)

updateCovid();