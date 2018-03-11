from flask import Flask
from dublinbikeminer.dublinbikeminer import dataReturn

while True:
    json = dataReturn()

    app = flask(__name__)

    @app.route("/")
    def printData():
        return json
    
    
if __name__ == "__main__":
    app.run()