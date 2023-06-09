import requests

channelID = 1115923752828555265
headers = {"authorization":"MTExMzY1OTgzNTY4MzE3NjQ5MA.GUsPvK.dagbpHgTuSx3M2m7zWgoAbnKN1ucDH9qo07Kc8"}

file = open("rank.txt", "r")
lines = file.readlines()

for line in lines:
    requests.post(f"https://discord.com/api/v9/channels/{channelID}/messages", headers  = headers, json = {"content": line})