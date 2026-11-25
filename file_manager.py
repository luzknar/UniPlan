import json
from pathlib import Path
from assignment import Assignment
from exam import Exam
from personal_schedule import PersonalSchedule
from schedule_manager import ScheduleManager


class FileManager:
    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def save(self, manager):
        data = {'subjects': [s.name for s in manager.subjects],
                'schedules': [s.to_dict() for s in manager.schedules]}
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.file_path.with_suffix('.tmp')
        temp.write_text(json.dumps(data, ensure_ascii=False, indent=4), encoding='utf-8')
        temp.replace(self.file_path)

    def load(self):
        manager = ScheduleManager()
        if not self.file_path.exists():
            return manager
        data = json.loads(self.file_path.read_text(encoding='utf-8'))
        for name in data['subjects']:
            manager.add_subject(name)
        classes = {'Assignment': Assignment, 'Exam': Exam, 'PersonalSchedule': PersonalSchedule}
        for item in data['schedules']:
            kind = item.pop('type')
            manager.add_schedule(classes[kind](**item))
        return manager
