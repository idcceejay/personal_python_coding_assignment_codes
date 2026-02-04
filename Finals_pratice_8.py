class Passenger():
    def __init__(self, name: str, ticket_class: str, seat: str, checked_in: bool = False):
        self.name = name
        self.ticket_class = ticket_class
        self.seat = seat
        self.checked_in = checked_in
    
    def check_in(self):
        self.checked_in = True
    
    def uncheck(self):
        self.checked_in = False
    
    def __str__(self):
        check = "Yes" if self.checked_in else "No"
        return  f"Name: {self.name} | Ticket Class: {self.ticket_class} | Seat: {self.seat} | Checked In(Yes or No) : {check}"
    

class Flight():
    def __init__(self):
        self.passengers = []
        self.class_counts = {}

    
    def add_passenger(self, passenger_obj: Passenger):
        self.passengers.append(passenger_obj)
        ctype = passenger_obj.ticket_class
        if ctype in self.class_counts:
            self.class_counts[ctype] = self.class_counts[ctype] + 1
        else:
            self.class_counts[ctype] = 1
        print("Passenger has been added")
    
    def remove_passenger(self, name: str):
        
        for n in self.passengers:
            if n.name.lower() == name.lower():
                ctype = n.ticket_class
                self.passengers.remove(n)
                self.class_counts[ctype] -= 1
                print("Passenger Removed")
                return

        print("Passenger does not Exist")

    def check_in(self,name: str):
        for n in self.passengers:
            if n.name.lower() == name.lower():
                n.check_in
                return
            
        print("Passenger does not Exist")
    
    def uncheck_passenger(self, name: str):
        for n in self.passengers:
            if n.name.lower() == name.lower():
                n.uncheck()
                print("Passenger has unchecked in")
                return
        print("Passenger does not exist")

    def list_passengers(self):
        if len(self.passengers) == 0:
            print("There is no passengers")
            return
        
        for n in self.passengers:
            print(n)

    def flight_statistics(self):

        if len(self.passengers) == 0:
            print("There are no passengers in the list")
            return
        
        total_passengers = len(self.passengers)
        total_checked_in = 0

        most_ticket_class = None #string for most tickets class
        tickets = 0 #int for most tickets class

        for p in self.passengers:
            if p.checked_in:
                total_checked_in += 1
            
        for tclass, count in self.class_counts.items():
            if count > tickets:
                tickets = count
                most_ticket_class = tclass
            
        print(f"Total passengers: {total_passengers}")
        print(f"Checked-in passengers: {total_checked_in}")
        print(f"Most common ticket class: {most_ticket_class} ({tickets})") 
                

if __name__ == "__main__":

    flight = Flight()


    while True:

        option = int(input("""1. Add Passenger
                                2. Remove Passenger
                                3. Check In Passenger
                                4. Undo Check-In
                                5. List Passengers
                                6. Flight Statistics
                                7. Quit
                                Enter Option(1-7):"""))
        
        if option == 1:
            name = input("Name: ")
            ticket = input("Ticket Class: ")
            seat = input('Seat Number: ')
            obj = Passenger(name,ticket,seat)
            flight.add_passenger(obj)

        elif option == 2:
            name = input("Name: ")
            flight.remove_passenger(name)


        elif option == 3:
            name =  input("Name: ")
            flight.check_in(name)

        elif option == 4:
            name = input("Name: ")
            flight.uncheck_passenger(name)

        elif option == 5:
            flight.list_passengers()

        elif option == 6:
            flight.flight_statistics()
        elif option == 7:
            print("Good Bye have a nice day")
            break
        else:
            print("Invalid Option")