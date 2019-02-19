# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import requests

systemDict= {} 
typesDict=  {}
locDict=  {}
systemSec= {} 

SysaSysa={}

with open("mapSolarSystems100.csv", "r") as ins:
    for line in ins:
        my_list = line.split(",")
        #print(my_list[2]+"   " +my_list[3])
        systemDict[my_list[2]] = my_list[3]
        systemSec[my_list[2]] = my_list[4]
        
        

with open("morfik_file.json", "r") as read_file:
    data = json.load(read_file)

for sellitem in data['sell']:
    for buyitem in data['buy']:
        if (sellitem['price']<buyitem['price']):
            
            quantity=buyitem['volume_remain']
            if (sellitem['volume_remain']<buyitem['volume_remain']):
                quantity=sellitem['volume_remain']
            potrata=quantity*sellitem['price']
            dohoda=quantity*buyitem['price']                
            profit=dohoda-potrata


#    distURL="http://everest.kaelspencer.com/jump/"+systemDict.get(str(sellitem['system_id']))+
#     "/"+systemDict.get(str(buyitem['system_id']))+"/"
     
            dist_to_fly=998899
            dist_to_fly=SysaSysa.get(systemDict.get(str(sellitem['system_id']))+systemDict.get(str(buyitem['system_id'])),976976)
            if (dist_to_fly==976976):
                distURL="http://everest.kaelspencer.com/jump/"+systemDict.get(str(sellitem['system_id']))+"/"+systemDict.get(str(buyitem['system_id']))+"/"
                rdis = requests.get(distURL)
                parsed_dist_json = json.loads(rdis.text)
                dist_to_fly=parsed_dist_json["jumps"]            

            SysaSysa[systemDict.get(str(sellitem['system_id']))+systemDict.get(str(buyitem['system_id']))]=dist_to_fly
            SysaSysa[systemDict.get(systemDict.get(str(buyitem['system_id']))+str(sellitem['system_id']))]=dist_to_fly
            
            print("Buy here |"+ 
                  systemDict.get(str(sellitem['system_id']))+"|"+ 
                  #sellitem['station']['name']+" ",
                  str(sellitem['station']['security']),
                  "| and sell here|"+
                  systemDict.get(str(buyitem['system_id']))+"|"+  
                  #buyitem['station']['name']+" ",
                  str(buyitem['station']['security']),"         "+
                  "|quantity|",quantity,"|profit|",profit,
                  "|dist_to_fly|"+str(dist_to_fly)+
                  "|profit per jump|"+str(profit/dist_to_fly))
                 
            
#        print(buyitem['station']['name'],"----",buyitem['station']['security'],"---",
#              buyitem['region']['name'],"--buy--",buyitem['price'],"-----howmuch---",
#              buyitem['volume_remain'])


            
def fussfu1():       
    koraba_w_sys="Jita"     
    distURL="http://everest.kaelspencer.com/jump/"+koraba_w_sys+"/"+systemDict.get(sysa,"figgevoznaet_sysa")+"/"
    #print(distURL)
    rdis = requests.get(distURL, headers=headers)
    #print(rdis.text)
    parsed_dist_json = json.loads(rdis.text)
     #   print("Distance to fly from "+systemDict.get(koraba_w_sys,"figgevoznaet_sysa")+" is "+str(parsed_dist_json["count"]))
    dist_to_fly=parsed_dist_json["jumps"]            
            



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

    