class Patient():
    def __init__(self, name: str, condition: str, admitted: bool = True):
        self.name = name
        self.condition = condition
        self.admitted =  admitted

    def discharged(self):
        self.admitted = False
    
    def admit(self):
        self.admitted = True

    def __str__(self):
        status = "Yes" if self.admitted else "No"
        return f"Name: {self.name} |  Condition: {self.condition} | Admitted(Yes Or No): {status}"
    
class Hospital():
    def __init__(self):
        self.patients = []
        self.condition_counts = {}
    
    def add_patient(self, patient_obj: Patient):
        self.patients.append(patient_obj)
        mtype = patient_obj.condition
        if mtype in self.condition_counts:
            self.condition_counts[mtype] = self.condition_counts[mtype] + 1
        else:
            self.condition_counts[mtype] = 1
        print("Patient has been added")

    def remove_patient(self, name : str):
        for p in self.patients:
            if p.name.lower() == name.lower():
                self.patients.remove(p)
                ptype = p.condition 
                self.condition_counts[ptype] = self.condition_counts[ptype] - 1
                print("Patient has been Removed")
                return
        print("Patient does not exist")

    def admit_patient(self, name: str):
        for p in self.patients:
            if p.name.lower() == name.lower():
                p.admit()
                print("Patient has been admited")
                return
        print("Patient has not been found")
    
    def discharge_patient(self, name : str):
        for p in self.patients:
            if p.name.lower() == name.lower():
                p.discharged()
                print("Patient has been discharged")
                return
        print("Patient has not been found")

    def list_patients(self):
        if len(self.patients) == 0:
            print("There are no Patients")
            return
        for p in self.patients:
            print(p)
    
    def hospital_statistics(self):
        total_patients = 0
        total_admitted = 0
        most_common = None
        highest_count = 0

        if len(self.patients) == 0:
            print("There are no patients in the Hospital")
            return

        for a in self.patients:
            if a.admitted == True:
                total_admitted += 1
        print(f'The total admitted are {total_admitted}')
        
        total_patients = len(self.patients)
        print(f'The total number of patients: {total_patients}')

        for conditions, count in self.condition_counts.items():
            if count > highest_count:
                highest_count = count
                most_common = conditions
            
        print(f"The most common Condition is {highest_count}: {most_common}")

if __name__ == "__main__":
    hospital = Hospital()


    while True:

        
        option = int(input("""
                                1. Add Patient
                                2. Remove Patient
                                3. Admit Patient
                                4. Discharge Patient
                                5. List All Patients
                                6. Hospital Statistics
                                7. Quit
                                Enter Option(1-7):
                                """))


        if option == 1:
            name = input("Name: ")
            condition = input("Condition: ")
            obj = Patient(name,condition)
            hospital.add_patient(obj)
        
        elif option == 2:
            name = input("Name: ")
            hospital.remove_patient(name)

        elif option == 3:
            name = input("Name: ")
            hospital.admit_patient(name)

        elif option == 4:
            name = input("Name: ")
            hospital.discharge_patient(name)

        elif option == 5:
            hospital.list_patients()

        elif option == 6:
            hospital.hospital_statistics()

        elif option == 7:
            print("Good Bye and have a nice day!")
            break
        
        else:
            print("Invalid option ")
            

        

        




        
            
            

