class Member():
    def __init__(self, name: str, membership_type: str, active: bool = True):
        self.name = name
        self.membership_type = membership_type
        self.active = active

    def cancel(self):
        self.active = False
        
    
    def activate(self):
        self.active = True
        
    
    def __str__(self):
        status = "Yes" if self.active else "No"
        return f"Name: {self.name} | Membership Type: {self.membership_type} | Active(Yes or No) {status}"


class Gym():
    def __init__(self):
        self.members = []
        self.stats = {}

    def add_member(self, member_obj : Member):
        self.members.append(member_obj)
        type = member_obj.membership_type
        if type in self.stats:
            self.stats[type] = self.stats[type] + 1
        else:
            self.stats[type] = 1
        
    
    def remove_member(self, name: str):
        for n in self.members:
            if n.name.lower() == name.lower():
                self.members.remove(n)
                type = n.membership_type
                self.stats[type] = self.stats[type] - 1
                print("Member has been removed")
                return
            
        print("no such member")

    def activate_member(self, name: str):
        for m in self.members:
            if m.name.lower() == name.lower():
                m.activate()
                print("Member has been activated")
                return
        print("Member does not exist")

    def cancel_member(self, name: str):
        for m in self.members:
            if m.name.lower() == name.lower():
                m.cancel()
                print("Membership has been canceled")
                return
        
        print("Member does not exist")

    def list_members(self):
        if len(self.members) == 0:
            print("No members in the gym")
            return
        for m in self.members:
            print(m)
                
    def membership_statistics(self):

        total_members = 0
        total_active = 0
        most_common = None
        highest_count = 0

        if len(self.members) == 0:
            print("There are no members in gym")
            return
        
        for m in self.members:
            if m.active == True:
                total_active += 1
        
        total_members = len(self.members)

        for membership_type, count in self.stats.items():
            if count > highest_count:
                highest_count = count
                most_common = membership_type
                
        print(f"Total members: {total_members}")
        print(f"Active members: {total_active}")
        print(f"Most common membership type: {most_common} ({highest_count})")

    
if __name__ == "__main__":

    gym = Gym()

    while True:

        menu = int(input("1: Add member\n 2: Remove Member\n 3:Activate Membership\n 4: Cancel Membership \n 5:List Members\n 6: Show Statistics\n 7: Quit\n Enter Option(1-7): "))


        if menu == 1:
            name = input("Member Name: ")
            membership_type = input("Membership Type: ")
            member_obj = Member(name,membership_type)
            gym.add_member(member_obj)
            print("Member Added")

        elif menu == 2:
            name = input("Enter Name to remove: ")
            gym.remove_member(name)
            

        elif menu == 3:
            name = input("Member Name:")
            gym.activate_member(name)

        elif menu == 4:
            name = input("Enter Name: ")
            gym.cancel_member(name)
        

        elif menu == 5:
            gym.list_members()
        
        elif menu == 6:
            gym.membership_statistics()

        elif menu == 7:
            print("Good Bye!")
            break

        else:
            print("Invalid Option")
            







        
                



        

    

            
                

                