from subject import Subject
from datetime import date


class ScheduleManager:
    def __init__(self):
        self.schedules = []
        self.subjects = []

    def add_subject(self, name):
        if not name.strip():
            raise ValueError('과목명을 입력하세요.')
        for subject in self.subjects:
            if subject.name == name:
                return subject
        subject = Subject(name)
        self.subjects.append(subject)
        return subject

    def next_id(self):
        return max([s.schedule_id for s in self.schedules], default=0) + 1

    def find(self, schedule_id):
        for schedule in self.schedules:
            if schedule.schedule_id == schedule_id:
                return schedule
        raise ValueError('해당 일정이 없습니다.')

    def add_schedule(self, schedule):
        if any(s.schedule_id == schedule.schedule_id for s in self.schedules):
            raise ValueError('중복된 일정 번호입니다.')
        if schedule.subject:
            self.add_subject(schedule.subject).add_schedule(schedule)
        self.schedules.append(schedule)

    def delete_schedule(self, schedule_id):
        schedule = self.find(schedule_id)
        for subject in self.subjects:
            if schedule in subject.schedules:
                subject.remove_schedule(schedule)
        self.schedules.remove(schedule)

    def update_schedule(self, schedule_id, title, deadline):
        schedule = self.find(schedule_id)
        new_date = date.fromisoformat(deadline).isoformat()
        if not title.strip():
            raise ValueError('제목을 입력하세요.')
        schedule.title = title
        schedule.deadline = new_date

    def search_schedule(self, keyword):
        return [s for s in self.schedules if keyword.lower() in s.title.lower() or keyword.lower() in (s.subject or '').lower()]

    def sort_schedules(self):
        return sorted(self.schedules, key=lambda s: s.deadline)

    def filter_schedules(self, kind):
        return [s for s in self.schedules if s.__class__.__name__ == kind]

    def get_completion_rate(self):
        if not self.schedules:
            return 0
        return sum(s.completed for s in self.schedules) / len(self.schedules) * 100
