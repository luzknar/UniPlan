class Subject:
    def __init__(self, name):
        self.name = name
        self.schedules = []

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def remove_schedule(self, schedule):
        self.schedules.remove(schedule)

    def get_schedules(self):
        return self.schedules.copy()
