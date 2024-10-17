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

@app.get("/api/cars/{id}") #This will allow the user to access cars by their id number
def car_by_id(id:int):
    result = [car for car in db if car['id'] == id]
    return result[0]

