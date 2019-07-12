# portfind.py made by Mauro M.


# This code is protected and released to the public under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0) License 
# witch can be viewed on the Creative Commons website (https://creativecommons.org/licenses/by-nc-nd/4.0/).
# Any faliure to comply with the terms stipulated in the license will be met with swift legal action 
# by the Creator.


import glob, os, json # Imports

looking = input("What port do you need to find? ")

# ONLY run inside /srv/daemon/config/servers 

files = glob.glob("*/server.json") # Get all the files directorys as list

for x in files: # For each file
    with open(x, "r") as read_file: # Using itenerable open and preform a set of operations for each file
        data = json.load(read_file) # Load file as JSON
        port = data['build']['default']['port'] # Get the value of build/default/port inside the JSON structure
        if port == looking: 
            uiid = data['uuid'] # Get the uuid
            print("[SUCESS] Found! Folder is /{}/server.json", uiid) 
        else:
            print("[FAIL] Couldn't find any servers with the port {}", port)
