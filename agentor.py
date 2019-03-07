# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:46:53 2019

@author: g705586



parser for

https://www.thonky.com/eve-online-guide/find-nearby-agents?systemOrAll=system&sysname=Jita&jumpmax=79&sortfield=none&ascdesc=asc&page=1
..
..
...
https://www.thonky.com/eve-online-guide/find-nearby-agents?systemOrAll=system&sysname=Jita&jumpmax=79&sortfield=none&ascdesc=asc&page=524


"""





import requests


with open('Agents.csv','w') as file:
    file.write('Name,Level,Type,Corpo,Sys,Security,Station,JumpsFromJita\n')
    
    for i in range(1,524):
        
        response = requests.get("https://www.thonky.com/eve-online-guide/find-nearby-agents?systemOrAll=system&sysname=Jita&jumpmax=79&sortfield=none&ascdesc=asc&page="+str(i))
        stroka=response.text
        blok1=0
        blok1=stroka.find('<div class="col-xs-8">',blok1)
        
        while (blok1!=-1):
            imie2=stroka.find('- <strong>',blok1+1)
            imie=stroka[blok1+24:imie2-1]   
            level=stroka[imie2+27:imie2+28]   
            #####  EBANIDZE.. firefox sorce shows <br>  but real string is  <br /> ???  
            ###  does firefox do fix on the fly?
            atype2=stroka.find('<br',imie2+36+26)
            atype=stroka[imie2+36+27:atype2]   
            corpo1=stroka.find("<strong>Corporation: </strong>",atype2)
            corpo2=stroka.find('- <strong>',corpo1)
            corpo=stroka[corpo1+31:corpo2-1]   
            sysa1=stroka.find("<strong>System:</strong>",corpo2)
            sysa2=stroka.find('- <strong>',sysa1)
            sysa=stroka[sysa1+25:sysa2-1]   
            stan1=stroka.find("<strong>Station: </strong>",sysa2)
            stan2=stroka.find('- <strong>',stan1)
            stan=stroka[stan1+26:stan2-1]       
            seka1=stroka.find("<strong>System Security: </strong>",stan2)
            seka2=stroka.find('<br',seka1)
            seka=stroka[seka1+35:seka2]                   

            jita1=stroka.find("<strong>Jumps: </strong>",seka2)
            jita2=stroka.find('<br',jita1)
            jita=stroka[jita1+25:jita2]                   

            file.write(imie+","+level+','+atype+','+corpo+','+sysa+','+seka+','+stan+','+jita+'\n')

            blok1=stroka.find('<div class="col-xs-8">',blok1+1)
    

