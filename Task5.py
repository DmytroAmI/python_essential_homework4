class SportComplex:
    """Describe a sport complex"""

    def __init__(self, sports, coaches, schedule, cost):
        """Initialize the SportComplex attributes"""
        self.sports = sports
        self.coaches = coaches
        self.schedule = schedule
        self.cost = cost

    def add_coach(self, coach):
        """Add a coach to the coaches team"""
        self.coaches.update(
            {coach.last_name: {"sport": coach.sport, "schedule": coach.schedule, "salary": coach.salary}})

    def find_coach(self, last_name):
        """Find a coach by last name"""
        for name, info in self.coaches.items():
            if name == last_name:
                return name, info

    def menu(self):
        """Display the menu on the sport complex"""
        while True:
            print("1. Sports\n2. Coaches team\n3. Find coach\n4. Schedule\n5. Cost of training\n6. Exit")
            choice = input("Enter your choice: ").strip()

            match choice:
                case "1":
                    print("List of sports:")
                    for sport in self.sports:
                        print("\t", sport)
                case "2":
                    print("Trainers:", end="")
                    for name, info in self.coaches.items():
                        print("\n", name, end="")
                        for key, value in info.items():
                            print(f": {key} - '{value}'", end="")
                    print()
                case "3":
                    find = input("Enter coach last name: ").strip().title()
                    try:
                        if find not in self.coaches.keys():
                            raise NoKeyError
                    except NoKeyError:
                        print("There is no coach with this last name")
                        continue

                    result = self.find_coach(find)
                    print(result[0], ":")
                    for key, value in result[1].items():
                        print(f"\t{key} - '{value}'")
                case "4":
                    print("Training schedule:", self.schedule, "\n")
                case "5":
                    print("Training cost:", self.cost, "\n")
                case "6":
                    break
                case _:
                    print("Invalid input, try again")


class Coach:
    """Describe a sport coach"""
    sport_coach = {}

    def __init__(self, last_name, sport, schedule, salary):
        """Initialize the attributes"""
        self.last_name = last_name
        self.sport = sport
        self.schedule = schedule
        self.salary = salary

        Coach.sport_coach.update(
            {self.last_name: {"sport": self.sport, "schedule": self.schedule, "salary": self.salary}})

    def __str__(self):
        """Print the coach attributes"""
        return f"{self.last_name}, sport {self.sport}"


class NoKeyError(Exception):
    pass


if __name__ == "__main__":
    coach1 = Coach("Brown", "Boxing", "some schedule", 1000)
    coach2 = Coach("Sanders", "Football", "some schedule", 800)
    coach3 = Coach("Lebron", "Volleyball", "some schedule", 1100)

    sports_activities = ["Football", "Volleyball", "Tennis", "Boxing", "Basketball"]

    sport_complex = SportComplex(sports_activities, Coach.sport_coach, "some schedule", 200)
    sport_complex.add_coach(Coach("Morrison", "Tennis", "some schedule", 850))

    sport_complex.menu()
