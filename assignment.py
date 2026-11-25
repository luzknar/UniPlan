from schedule import Schedule


class Assignment(Schedule):
    def __init__(self, schedule_id, title, subject, deadline, submission_type, priority, completed=False):
        super().__init__(schedule_id, title, subject, deadline, completed)
        self.submission_type = submission_type
        self.priority = priority

    def get_info(self):
        return f'[과제] {super().get_info()} | 제출: {self.submission_type} | 우선순위: {self.priority}'
