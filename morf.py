# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import requests




def myf3():
    with open("morfik_file.json", "r") as read_file:
        data = json.load(read_file)

for sellitem in data['sell']:
    for buyitem in data['buy']:
        if (sellitem['price']<buyitem['price']):
            
                 
            
#        print(buyitem['station']['name'],"----",buyitem['station']['security'],"---",
#              buyitem['region']['name'],"--buy--",buyitem['price'],"-----howmuch---",
#              buyitem['volume_remain'])





def myf1():
    response = requests.get("https://api.evemarketer.com/v1/markets/types/11399?language=en")
    data = json.loads(response.text)
    with open("morfik_file.json", "w") as write_file:
        json.dump(data, write_file)

def myf2():
    json_string = """
    {
        "researcher": {
            "name": "Ford Prefect",
            "species": "Betelgeusian",
            "relatives": [
                {
                    "name": "Zaphod Beeblebrox",
                    "species": "Betelgeusian"
                }
            ]
        }
    }
    """
    data = json.loads(json_string)
    
    
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)
        
        
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)

    