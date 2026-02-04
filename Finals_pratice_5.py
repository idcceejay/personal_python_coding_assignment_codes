class StudySession():
    def __init__(self, course: str, topic: str, duration: float,difficulty: int):
        self.course = course
        self.topic = topic
        self.duration = duration
        self.difficulty = difficulty
    
    def update_duration(self, new_duration: float):
        self.duration = new_duration

    def __str__(self):
        return f"Course: {self.course}, Topic: {self.topic}, Duration: {self.duration:.2f} hours, Difficulty: {self.difficulty}"
    


def print_menu():
    print("[Study Session Tracker]\n 1) Add Study Session \n 2) View all sessions \n 3) View Stats \n 4) Update a session's duration \n 5) Quit")


def convert_difficulty_label(difficulty: int):
    if difficulty == 1 or difficulty == 2:
        return('Easy')
    elif difficulty == 3:
        return("Medium")
    elif difficulty == 4 or difficulty == 5:
        return("Hard")
    else:
        print("Unknown")
        return

def compute_stats(sessions: list[StudySession]):
    if len(sessions) == 0:
        print("No sessions to show statistics for.")
        return
    
    total_hours = 0
    total_difficulty = 0
    hours_by_course = {}

    for s in sessions:
        total_hours += s.duration

        total_difficulty += s.difficulty

        if s.course in hours_by_course:
            hours_by_course[s.course] += s.duration
        else:
            hours_by_course[s.course] = s.duration
        
    avg_difficulty = total_difficulty / len(sessions)

    print(f"Total hours: {total_hours:.2f}")
    print(f"Average difficulty: {avg_difficulty:.2f}")
    print("Hours by course:")

    for courses in hours_by_course:
        print(f'{courses}:{hours_by_course[courses]:.2f}')


def main():
    sessions = []

    while True:
        print_menu()
        option = int(input("Enter Choice: "))

        if option == 1:
            course = input("Enter Course name: ")
            topic = input("Enter Topic: ")
            duration = float(input("Enter duration in hours: "))
            difficulty = int(input("Enter difficulty (1-5):"))
            session = StudySession(course,topic,duration,difficulty)
            sessions.append(session)
            print("Session added")

        elif option == 2:
            if len(sessions) == 0:
                print("No sessions recorded yet.")
            else:
                for s in sessions:
                    print(s)
                    label = convert_difficulty_label(s.difficulty)
                    print("Difficulty level:", label)
                    print()
        elif option == 3:
            compute_stats(sessions)

        elif option == 4:
            if len(sessions) == 0:
                print("No sessions to update.")
            else:
                print("Sessions")
                for i, s in enumerate(sessions, start=1):
                    print(f"{i}) {s}")
                
                choice = int(input("Enter session number to update: "))

                if choice < 1 or choice > len(sessions):
                    print('invalid sessions number')
                else:
                    new_duration = float(input("Enter new duration in hours: "))
                    sessions[choice - 1].update_duration(new_duration)
                    print("Duration Updated")
        elif option == 5:
            print("Good luck with your studing!")
            break
            
        else:
            print("Invalid option try again")
            
if __name__ == "__main__":
    main()        

                




                











    
