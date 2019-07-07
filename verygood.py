import json
import datetime
import urllib.request
import os
#import pyttsx3

#engine = pyttsx3.init()

def get_json(id, method):
    return json.loads(urllib.request.urlopen("https://api.rust-servers.info/" + method + "/" + str(id)).read())

def get_player(id, name):
    for player in get_json(id, "players"):
        if player["name"] == name:
            return player

def to_file(text):
    with open("templates/log.txt", "a+") as f:
        f.write(text + "\n")

players = ["UltraGold", "douglasjohnnyhit", "verlus", "Brennan3g", "bladezz", "thursday.", "stickyfingaz", "Sir Crank", "idopey"]
online = []

x = 0

while True:
    x += 1
    #print("Starting", x)
    for player in players:
        temp = get_player(1591, player)
        if temp is not None and player not in online:
            online.append(player)
            to_file(player + " online " + str(datetime.datetime.now() - datetime.timedelta(seconds=(temp["play_time_in_seconds"]))))
            print(player + " online " + str(datetime.datetime.now() - datetime.timedelta(seconds=(temp["play_time_in_seconds"]))))
            #engine.say(player + " online!")
            #engine.runAndWait()
        elif temp is None and player in online:
            online.remove(player)
            to_file(player + " offline " + str(datetime.datetime.now()))
            print(player + " offline " + str(datetime.datetime.now()))
            #engine.say(player + " offline!")
            #engine.runAndWait()
    #print("End",x)
