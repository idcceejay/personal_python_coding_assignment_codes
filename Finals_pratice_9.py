class Car():
    def __init__(self, plate: str, model: str, milege: int = 0):
        self.plate = plate
        self.model = model
        self.milege = milege

    def add_miles(self, amount: int):
        if amount > 0:
            self.milege += amount
        else:
            print("Enter a postive Amount")

    def __str__(self):
        return f"Plate: {self.plate} | Model: {self.model} | Milege: {self.milege}"
    
class Garage():
    def __init__(self):
        self.cars = []

    def park_car(self, car_obj: Car):
        for p in self.cars:
            if p.plate.lower() == car_obj.plate.lower():
                print("The plate already Exist try again")
                return False

        self.cars.append(car_obj)
        print("Car has been added")
        return True

    def remove_car(self, plate: str):
        for p in self.cars:
            if p.plate.lower() == plate.lower():
                self.cars.remove(p)
                print("Car has been Removed")
                return True
            
        print("Plate does not Exist")
        return False
    
    def list_cars(self):
        if len(self.cars) == 0:
            return("No cars in garage")
        
        result  = ""
        for c in self.cars:
            result += str(c) + "\n\n"
            
        return result.strip()

    def count_cars(self):
        return len(self.cars)

    def models_summary(self):
        dict = {}
        for p in self.cars:
            if p.model in dict:
                dict[p.model] = dict[p.model] + 1
            else:
                dict[p.model] = 1

        return dict
    
    def mark_trip_by_model(self, model:str, miles: int):

        for c in self.cars:
            if c.model.lower() == model.lower():
                c.add_miles(miles)
                print(f'Car {c.plate} drove {miles} miles')
                
                found = True
            if found:
                print(f"All {model} cars have been updated.")
            else:
                print("No cars with that model found.")

if __name__ == "__main__":

    garage = Garage()

    while True:

        option = int(input("""[Garage Management System]
                            1. Park car
                            2. Remove car
                            3. List all cars
                            4. Show model summary
                            5. Show car count
                            6. Mark trip by model
                            7. Quit"""))
        
        if option == 1:
            plate = input("Plate: ")
            model = input("Model: ")
            milege = int(input("Milege: "))
            obj = Car(plate,model,milege)
            garage.park_car(obj)
        elif option == 2:
            plate = input("Plate: ")
            garage.remove_car(plate)
        
        elif option == 3:
            print(garage.list_cars())

        elif option == 4:
            summary = garage.models_summary()

            if not summary:
                print("no cars in garage")
            else:
                for model, count in sorted(summary.items()):
                    print(f"{model}: {count}")


        elif option == 5:
            count = garage.count_cars()
            print(f'There are currently {count} cars in the garage.')

        elif option == 6:
            model = input("Enter model to mark trip for: ")
            miles = int(input("Enter miles driven: "))
            garage.mark_trip_by_model(model,miles)

        elif option == 7:
            print("Good Bye")
            break
        else:
            print("Invalid option try again")
            
        


        
