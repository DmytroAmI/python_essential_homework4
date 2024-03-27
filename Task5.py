class SportComplex:
    """Describe a sport complex"""

    def __init__(self, sports, coaches, schedule, cost):
        """Initialize the SportComplex attributes"""
        self.sports = sports
        self.coaches = coaches
        self.schedule = schedule
        self.cost = cost

    def find_coach(self, last_name):
        """Find a coach by last name"""
        for name, info in self.coaches.items():
            if name == last_name:
                return name, info


class NoKeyError(Exception):
    pass


def add_coach(team, last_name, sport, schedule, salary):
    """Add coach"""
    team.update({last_name: {"sport": sport, "schedule": schedule, "salary": salary}})
    return team


def menu(sport_complex):
    """Display the menu on the sport complex"""
    while True:
        print("1. Sports\n2. Coaches team\n3. Find coach\n4. Schedule\n5. Cost of training\n6. Exit")
        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                print("List of sports:")
                for sport in sport_complex.sports:
                    print("\t", sport)
            case "2":
                print("Trainers:", end="")
                for name, info in sport_complex.coaches.items():
                    print("\n", name, end="")
                    for key, value in info.items():
                        print(f": {key} - '{value}'", end="")
                print()
            case "3":
                find = input("Enter coach last name: ").strip().title()
                try:
                    if find not in sport_complex.coaches.keys():
                        raise NoKeyError
                except NoKeyError:
                    print("There is no coach with this last name")
                    continue

                result = sport_complex.find_coach(find)
                print(result[0], ":")
                for key, value in result[1].items():
                    print(f"\t{key} - '{value}'")
            case "4":
                print("Training schedule:", sport_complex.schedule)
            case "5":
                print("Training cost:", sport_complex.cost)
            case "6":
                break
            case _:
                print("Invalid input, try again")


if __name__ == "__main__":
    coach_team = {}
    add_coach(coach_team, "Miller", "Football", "some schedule", 1000)
    add_coach(coach_team, "Gerard", "Tennis", "some schedule", 800)
    add_coach(coach_team, "Bale", "Volleyball", "some schedule", 950)

    sports_activities = ["Football", "Volleyball", "Tennis", "Boxing", "Basketball"]

    sport_complex1 = SportComplex(sports_activities, coach_team, "some schedule", 200)

    menu(sport_complex1)
