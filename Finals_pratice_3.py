class Member():
    def __init__(self, name: str, year: str, major: str, email: str):
        self.name = name
        self.year = year
        self.major = major
        self.email = email
    
    def rename(self, new_name: str):
        self.name = new_name

    def update_email(self, new_email: str): 
        self.email = new_email

    def __str__(self):
        return f"""
    Name: {self.name}
    Year: {self.year}
    Major: {self.major}
    Email: {self.email}
    """

class Club():
    def __init__(self, code: str, name: str, category: str, max_members: int):
        self.code = code #arc club name
        self.name = name # full club name
        self.category = category
        self.max_members = max_members

    def __str__(self):
        return f"[{self.code}] {self.name} Club ({self.category}) - Max members: {self.max_members}"
    
class ClubSystem():
    def __init__(self):
        self.members = []
        self.clubs = []
        self.enrollments = {}
    
    def add_members(self, member: Member):
        for m in self.members:
            if m.email.lower() == member.email.lower():
                print("Member Already exists")
                return False
            
        self.members.append(member)
        print("Member Added")
        return True
    
    def add_club(self, club: Club):
        for c in self.clubs:
            if c.code.lower() == club.code.lower():
                print('The Club already Exists')
                return False
            
        self.clubs.append(club)
        print("Club Added")
        return True

    def enroll(self, member_email: str ,club_code:str):

        member_exist =  None
        for m in self.members:
            if m.email.lower() == member_email.lower():
                member_exist = m
                break
        if member_exist is None:
            print("Member not found")
            return False
            
        club_exist = None
        for c in self.clubs:
                if c.code.lower() == club_code.lower():
                    club_exist = c
                    break
        if club_exist is None:
            print("The Club does not exist")
            return False
                
        code_key = club_exist.code
        current_enrollment = self.enrollments.get(code_key, [])

        
        for email in current_enrollment:

            if email.lower() == member_email.lower():
                print("The Member is already in current Club")
                return False

            if len(current_enrollment) >= club_exist.max_numbers:
                print("The Club is at its Maximum Capacity")
                return False

        current_enrollment.append(member_email)
        self.enrollments[code_key] = current_enrollment
        print("Member Enrolled")


    def drop(self,member_email: str, club_code: str):

        club_exist = False
        
        for c in self.clubs:
            if c.code.lower() == club_code.lower():
                club_exist = True
                club_code = c.code   
                break

        if not club_exist:
            print("The Club does not exist")
            return False
        
        if club_code not in self.enrollments:
            print("No members are enrolled in this club")
            return False
        
        if member_email not in self.enrollments[club_code]:
            print("Member is not enrolled in this club")
            return False
        
        self.enrollments[club_code].remove(member_email)
        print("Member Dropped")
        return True
    
    def list_members(self):
        if len(self.members) == 0:
            print("There are no members in the system.")
        else:
            for m in self.members:
                print(m)
                print()
    
    def list_clubs(self):
        if len(self.clubs) == 0:
            print('There are no Clubs')
        else:
            for c in self.clubs:
                print(c)

    def list_enrollments(self):
        if len(self.enrollments) == 0:
            print("No enrollments yet")
            return
        
        for code in self.enrollments:
            print(f"Club {code}:")
            for email in self.enrollments[code]:
                print(" ", email)


    def club_statistics(self):

        print("---- Club Statistics ----")
        print("Total members in system:", len(self.members))
        print("Total clubs in system:", len(self.clubs))

        if len(self.clubs) == 0:
            print("No clubs to show statistics for.")
            return

        largest_size = -1
        largest_code = None
        total_enrolled = 0
        clubs_with_members = 0

        for c in self.clubs:
            code = c.code

            if code in self.enrollments:
                size = len(self.enrollments[code])
            else:
                size = 0

            print(f"{code}: {size} members")

            if size > 0:
                total_enrolled += size
                clubs_with_members += 1

            if size > largest_size:
                largest_size = size
                largest_code = code

        if clubs_with_members > 0:
            avg = total_enrolled / clubs_with_members
            print(f"Average club size (clubs with members): {avg:.2f}")
        else:
            print("Average club size (clubs with members): 0.00")

        if largest_code is not None:
            print(f"Largest club: {largest_code} ({largest_size} members)")
        else:
            print("Largest club: N/A")


def menu():
    system = ClubSystem()

    while True:
        print("\n===== Campus Club Management =====")
        print("1. Add Member")
        print("2. Add Club")
        print("3. Enroll Member in Club")
        print("4. Drop Member from Club")
        print("5. List Members")
        print("6. List Clubs")
        print("7. List Enrollments")
        print("8. Club Statistics")
        print("9. Quit")

        choice = input("Enter your choice: ")

        # ------------------ ADD MEMBER ------------------
        if choice == "1":
            name = input("Enter member name: ")
            year = input("Enter member year: ")
            major = input("Enter member major: ")
            email = input("Enter member email: ")

            new_member = Member(name, year, major, email)
            system.add_members(new_member)

        # ------------------ ADD CLUB ------------------
        elif choice == "2":
            code = input("Enter club code: ")
            name = input("Enter club name: ")
            category = input("Enter club category: ")
            max_members = int(input("Enter max members: "))

            new_club = Club(code, name, category, max_members)
            system.add_club(new_club)

        # ------------------ ENROLL MEMBER ------------------
        elif choice == "3":
            email = input("Enter member email: ")
            code = input("Enter club code: ")
            system.enroll(email, code)

        # ------------------ DROP MEMBER ------------------
        elif choice == "4":
            email = input("Enter member email: ")
            code = input("Enter club code: ")
            system.drop(email, code)

        # ------------------ LIST MEMBERS ------------------
        elif choice == "5":
            system.list_members()

        # ------------------ LIST CLUBS ------------------
        elif choice == "6":
            system.list_clubs()

        # ------------------ LIST ENROLLMENTS ------------------
        elif choice == "7":
            system.list_enrollments()

        # ------------------ STATISTICS ------------------
        elif choice == "8":
            system.club_statistics()

        # ------------------ QUIT ------------------
        elif choice == "9":
            print("Shutting down system...")
            break

        # ------------------ INVALID ------------------
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    menu()     