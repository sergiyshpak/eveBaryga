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

from SysaSysafile import SysaSysa

with open("mapSolarSystems100.csv", "r") as ins:
    for line in ins:
        my_list = line.split(",")
        #print(my_list[2]+"   " +my_list[3])
        systemDict[my_list[2]] = my_list[3]
        systemSec[my_list[2]] = my_list[4]
        
        
        
typeToSell='5839'           ## IFFA 
lokalSysa='EFA'

response = requests.get("https://api.evemarketer.com/v1/markets/types/"+typeToSell+"?language=en")
data = json.loads(response.text)


#    distURL="http://everest.kaelspencer.com/jump/"+systemDict.get(str(sellitem['system_id']))+
#     "/"+systemDict.get(str(buyitem['system_id']))+"/"


for buyitem in data['buy']:
       
    dist_to_fly=998899
    dist_to_fly=int(SysaSysa.get(lokalSysa+systemDict.get(str(buyitem['system_id'])),976976))
    if (dist_to_fly==976976):
        distURL="http://everest.kaelspencer.com/jump/"+lokalSysa+"/"+systemDict.get(str(buyitem['system_id']))+"/"
        rdis = requests.get(distURL)
        parsed_dist_json = json.loads(rdis.text)
        dist_to_fly=parsed_dist_json["jumps"]            

    SysaSysa[  lokalSysa + systemDict.get(str(buyitem['system_id']))  ]=dist_to_fly
    SysaSysa[  systemDict.get(str(buyitem['system_id']))+lokalSysa]=dist_to_fly

    quantity=str(buyitem['volume_remain'])
    price=str(buyitem['price'])

    print("Buy here |"+ 
                          lokalSysa+"|"+ 
                          "| and sell here|"+
                          systemDict.get(str(buyitem['system_id']))+"|"+  
                          str(buyitem['station']['security']),"         "+
                          "|quantity|",quantity,
                          "|price|",price,
                          "|dist_to_fly|"+str(dist_to_fly))
                         

with open('SysaSysafile.py','w') as file:
    file.write("SysaSysa = { \n")
    for k in SysaSysa.keys():
        file.write("'%s':'%s', \n" % (k, SysaSysa[k]))
    file.write("}")

            
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

    