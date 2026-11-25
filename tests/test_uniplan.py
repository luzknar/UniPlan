import unittest
from tempfile import TemporaryDirectory
from pathlib import Path
from datetime import date
from assignment import Assignment
from exam import Exam
from personal_schedule import PersonalSchedule
from schedule_manager import ScheduleManager
from file_manager import FileManager


class UniPlanTest(unittest.TestCase):
    def test_workflow(self):
        m = ScheduleManager()
        m.add_subject('빈 과목')
        a = Assignment(1, '과제', 'Python', date.today().isoformat(), 'PDF', '상')
        m.add_schedule(a)
        m.add_schedule(Exam(2, '시험', 'Python', '2030-01-01', '1장', '필기'))
        m.add_schedule(PersonalSchedule(3, '모임', None, '2030-01-02', '학교', '동아리'))
        self.assertEqual(a.get_dday(), 'D-Day')
        self.assertEqual(len(m.search_schedule('Python')), 2)
        self.assertEqual(len(m.filter_schedules('Exam')), 1)
        self.assertEqual(m.sort_schedules()[0], a)
        a.complete()
        self.assertAlmostEqual(m.get_completion_rate(), 100 / 3)
        m.update_schedule(1, '수정', '2030-01-03')
        with self.assertRaises(ValueError):
            m.update_schedule(1, '오류', 'invalid')
        self.assertEqual(a.title, '수정')
        with TemporaryDirectory() as folder:
            f = FileManager(Path(folder) / 'data.json')
            f.save(m)
            loaded = f.load()
            self.assertEqual([s.to_dict() for s in m.schedules], [s.to_dict() for s in loaded.schedules])
            self.assertEqual(len(loaded.subjects), 2)
            loaded.delete_schedule(1)
            self.assertEqual(len(loaded.search_schedule('Python')), 1)
            self.assertEqual(len(loaded.subjects[1].schedules), 1)


if __name__ == '__main__':
    unittest.main()
