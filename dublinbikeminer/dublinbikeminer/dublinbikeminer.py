import requests
import json
import time
import datetime

def main():
    
    count = 1
    
    while True:
        
        print("collecting:",count)
        
        file = open("/home/hugh/30670/Project/dublinbikedata.txt", "a")
        
        link = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&&apiKey=4dc48c410fefd7a42d52cdc4a9c6eb7ce0f67ae0"
        
        r = requests.get(link)
        
        data = r.text
        
        title = "period: "+ str(count) + " ----------------------------"
        
        #parsed = json.loads(data)
        
        return json.loads(data)
        
        file.write(title)
        file.write(data)
        
        file.close()
        
        time.sleep(300)
        
        #print(json.dumps(parsed, indent=4))
        
        count+=1
        
    

def dataReturn():
    
    while True:
        
        link = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&&apiKey=4dc48c410fefd7a42d52cdc4a9c6eb7ce0f67ae0"
        
        r = requests.get(link)
        
        data = r.text
        
        #parsed = json.loads(data)
        
        return json.loads(data)
    
        time.sleep(300)