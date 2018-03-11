import requests
import json
import time
import datetime

# Import MySQl
from mysql.connector import (connection, cursor)
from gevent.libev.corecext import stat

def main():
    
    # Connection to local database
    conex = connection.MySQLConnection(user='root', password='*******', host='127.0.0.1', database='software_engineering')
    
    # MySQL object
    cursor = conex.cursor()
    
    number = 0
    contract_name = None 
    name = None
    address = None
    position_lat = 0.0
    position_lng = 0.0
    banking = None
    bonus = None
    status = None
    bike_stands = 0
    available_bike_stands = 0
    available_bikes = 0
    last_update = 0

    # Execute test
    sqlQuery = "INSERT INTO dublinBikes(Number, Contract_Name, Name, Address, Position_Lat, Position_Lng, Banking, Bonus, Status, Bike_Stands, Available_Bike_Stands, Available_bikes, Last_Update) \
                VALUES('%d', '%s', '%s', '%s', '%f', '%f', '%s', '%s', '%s', '%d', '%d', '%d', '%d')" % \
                (number, contract_name, name, address, position_lat, position_lng, banking, bonus, status, bike_stands, available_bike_stands, available_bikes, last_update)
    
    while True:
        
        link = "https://api.jcdecaux.com/vls/v1/stations?contract=Dublin&&apiKey=4dc48c410fefd7a42d52cdc4a9c6eb7ce0f67ae0"
        
        r = requests.get(link)
        jTxt = json.loads(r.text)
        
        if r.status_code == 200:
            
            try:
                number = jTxt['number']
                name = jTxt['name']
                address = jTxt['address']
                position_lat = jTxt['position']['lat']
                position_lng = jTxt['position']['lng']
                bike_stands = jTxt['bike_stands']
                status = jTxt{'status'}
                available_bike_stands = jTxt['available_bike_stands']
                available_bikes = jTxt['available_bikes']
                last_update = jTxt['last_update']
                
                
                sqlQuery = "INSERT INTO dublinBikes(Number, Name, Address, Position_Lat, Position_Lng, Status, Bike_Stands, Available_Bike_Stands, Available_bikes, Last_Update) \
                VALUES('%d', '%s', '%s', '%f', '%f', '%s', '%d', '%d', '%d', '%d')" % \
                (number, contract_name, name, address, position_lat, position_lng, banking, bonus, status, bike_stands, available_bike_stands, available_bikes, last_update)
            except:
                pass
            
        else:
            # Error occurred 
            pass
        
        return False
    
        time.sleep(300)
        
    conex.close()
     

