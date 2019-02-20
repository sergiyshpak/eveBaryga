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
        
        
#with open("morfik_file.json", "r") as read_file:
#    data = json.load(read_file)

#azu plag 17455
#comp azu plag 28421

response = requests.get("https://api.evemarketer.com/v1/markets/types/17455?language=en")
dataNaProd = json.loads(response.text)

response = requests.get("https://api.evemarketer.com/v1/markets/types/28421?language=en")
dataSkupka = json.loads(response.text)




totProfLimiter=1000000
totProfJumpLimiter=100000


#    distURL="http://everest.kaelspencer.com/jump/"+systemDict.get(str(sellitem['system_id']))+
#     "/"+systemDict.get(str(buyitem['system_id']))+"/"

print ("------------------------ "+dataNaProd['type']['name']+" ------------------------")

for sellitem in dataNaProd['sell']:
    for buyitem in dataSkupka['buy']:
        if (100*sellitem['price']<buyitem['price']):
            
            quantity=buyitem['volume_remain']*100
            if (sellitem['volume_remain']<buyitem['volume_remain']*100):
                quantity=sellitem['volume_remain']
            potrata=quantity*sellitem['price']
            dohoda=quantity/100*buyitem['price']                
            profit=dohoda-potrata

            if (profit>totProfLimiter):
        
                dist_to_fly=998899
                dist_to_fly=int(SysaSysa.get(systemDict.get(str(sellitem['system_id']))+systemDict.get(str(buyitem['system_id'])),976976))
                if (dist_to_fly==976976):
                    distURL="http://everest.kaelspencer.com/jump/"+systemDict.get(str(sellitem['system_id']))+"/"+systemDict.get(str(buyitem['system_id']))+"/"
                    rdis = requests.get(distURL)
                    parsed_dist_json = json.loads(rdis.text)
                    dist_to_fly=parsed_dist_json["jumps"]            
    
                SysaSysa[systemDict.get(str(sellitem['system_id']))+systemDict.get(str(buyitem['system_id']))]=dist_to_fly
                SysaSysa[systemDict.get(systemDict.get(str(buyitem['system_id']))+str(sellitem['system_id']))]=dist_to_fly

                if (profit/dist_to_fly>totProfJumpLimiter):                
                    print("Buy here |"+ 
                          systemDict.get(str(sellitem['system_id']))+"|"+ 
                          str(sellitem['price'])+"|"+
                          #sellitem['station']['name']+" ",
                          str(sellitem['station']['security']),
                          "| and sell here|"+
                          systemDict.get(str(buyitem['system_id']))+"|"+  
                          str(buyitem['price'])+"|"+
                          #buyitem['station']['name']+" ",
                          str(buyitem['station']['security']),"         "+
                          "|quantity|",quantity,"|profit|",profit,
                          "|dist_to_fly|"+str(dist_to_fly)+
                          "|profit per jump|"+str(profit/dist_to_fly))
                         



            
#        print(buyitem['station']['name'],"----",buyitem['station']['security'],"---",
#              buyitem['region']['name'],"--buy--",buyitem['price'],"-----howmuch---",
#              buyitem['volume_remain'])


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

    