from abc import ABC, abstractmethod

def create_car():
    car_model = input("What is name of the car?: ")
    car_battery = input("Please write your battery type: ")
    car_engine = input("What is the engine? :")
    print(car_model)
    print(car_battery)
    print(car_engine)

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass
