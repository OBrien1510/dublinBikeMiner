import requests
import json
import time

def main():
    
    count = 1
    
    while True:
        
        print("collecting:",count)
        
        file = open("/hugh/home/30670/Project/dublinbikedata.txt", w)
        
        link = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&&apiKey=4dc48c410fefd7a42d52cdc4a9c6eb7ce0f67ae0"
        
        r = requests.get(link)
        
        data = r.text
        
        parsed = json.loads(data)
        
        file.write(parsed)
        
        time.sleep(300)
        
        #print(json.dumps(parsed, indent=4))
        
        count+=1
        
    

main()