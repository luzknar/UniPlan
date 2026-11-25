from datetime import date


class Schedule:
    def __init__(self, schedule_id, title, subject, deadline, completed=False):
        self.schedule_id = schedule_id
        self.title = title
        self.subject = subject
        self.deadline = date.fromisoformat(deadline).isoformat()
        self.completed = completed

    def get_dday(self):
        days = (date.fromisoformat(self.deadline) - date.today()).days
        if days == 0:
            return 'D-Day'
        return f'D-{days}' if days > 0 else f'D+{-days}'

    def complete(self):
        self.completed = True

    def get_info(self):
        status = '완료' if self.completed else '미완료'
        return f'{self.schedule_id}. {self.title} | {self.subject or "개인"} | {self.deadline} | {self.get_dday()} | {status}'

    def to_dict(self):
        return dict(vars(self), type=self.__class__.__name__)
