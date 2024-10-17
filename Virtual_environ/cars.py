from fastapi import FastAPI

app = FastAPI()

db = [
    {"id": 1, 'size': 's', 'fuel': 'gasoline', 'doors': 3, 'transmission': 'auto'},
    {"id": 2, 'size': 's', 'fuel': 'electric', 'doors': 3, 'transmission': 'auto'},
    {"id": 3, 'size': 's', 'fuel': 'gasoline', 'doors': 5, 'transmission': 'manual'},
    {"id": 4, 'size': 'm', 'fuel': 'electric', 'doors': 3, 'transmission': 'auto'},
    {"id": 5, 'size': 'm', 'fuel': 'hybrid', 'doors': 5, 'transmission': 'auto'},
    {"id": 6, 'size': 'm', 'fuel': 'gasoline', 'doors': 5, 'transmission': 'manual'},
    {"id": 7, 'size': 'l', 'fuel': 'diesel', 'doors': 5, 'transmission': 'manual'},
    {"id": 8, 'size': 'l', 'fuel': 'electric', 'doors': 5, 'transmission': 'auto'},
    {"id": 9, 'size': 'l', 'fuel': 'hybrid', 'doors': 5, 'transmission': 'auto'},
]
#After the url, input the value ?size=m
#? is inputed after the url link
#size allows us to specify the targeted cars we are looking for with the specified size
#m is the size of the car we are looking for within the list of cars
#To run two statement at the same time in the url ?size=m&transmission=auto
#The & allows us to run two statement at the same time in the URL

@app.get("/api/cars")
def get_cars(size=None): #Allows for an input statement to function, ensures if the url is empty, another statement is run
    if size: #Will return the list of the cars that have the specified size mentioned
        return [car for car in db if car['size'] == size] #A loop that goes through the list of cars for the key size
    else: #Will return the whole list of the cars if the url is empty
        return db


@app.get("/api/cars2")
def get_cars(size=None,transmission=None):
    result = db #Stores the list of cars into the variable result
    if size:
        result = [car for car in result if car["size"] == size]
    if transmission:
        result = [car for car in result if car["transmission"] == transmission]
    return result

@app.get("/api/cars3")
def get_cars(size=None,transmission=None,fuel=None):
    result = db #Stores the list of cars into the variable result
    if size:
        result = [car for car in result if car["size"] == size]
    if transmission:
        result = [car for car in result if car["transmission"] == transmission]
    if fuel:
        result = [car for car in result if car["fuel"] == fuel]
    return result

@app.get("/api/cars4")
def get_cars(size,transmission,fuel,doors:int): #Converts the doors into integer value, even if the the value in the URL is three, this converts it into the number 3
    result = db #Stores the list of cars into the variable result
    if size:
        result = [car for car in result if car["size"] == size]
    if transmission:
        result = [car for car in result if car["transmission"] == transmission]
    if fuel:
        result = [car for car in result if car["fuel"] == fuel]
    if doors:
        result = [car for car in result if car["doors"] == doors]
    return result

@app.get("/api/cars5")
def get_cars(size=None,transmission=None,fuel=None,doors:int|None=None): #Typed optional parameters (|) allows us to apply multiple filters to the same argument
    result = db #Stores the list of cars into the variable result
    if size:
        result = [car for car in result if car["size"] == size]
    if transmission:
        result = [car for car in result if car["transmission"] == transmission]
    if fuel:
        result = [car for car in result if car["fuel"] == fuel]
    if doors:
        result = [car for car in result if car["doors"] == doors]
    return result