from schedule import Schedule


class PersonalSchedule(Schedule):
    def __init__(self, schedule_id, title, subject, deadline, location, event_type, completed=False):
        super().__init__(schedule_id, title, None, deadline, completed)
        self.location = location
        self.event_type = event_type

    def get_info(self):
        return f'[개인] {super().get_info()} | 장소: {self.location} | 유형: {self.event_type}'
